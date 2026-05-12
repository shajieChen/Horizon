"""Trading oracle analyzer for Horizon market plugin."""

from __future__ import annotations

import asyncio
import os
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..models import ContentItem, TradingConfig
from ..vendor.digital_oracle import ProviderCallContext, get_provider_by_name
from .router import TradingQuestionRouter


class MarketSignal(BaseModel):
    """One market-derived signal."""

    layer: str
    signal: str
    value: str
    horizon: str
    interpretation: str
    confidence: str = "medium"
    source: str
    metadata: Dict[str, str] = Field(default_factory=dict)


class HorizonProbability(BaseModel):
    """Probability view for one time horizon."""

    horizon: str
    up_probability: float
    down_probability: float
    neutral_probability: float
    expected_bias: str
    confidence: str
    basis: str
    invalidation: str


class AssetTradingView(BaseModel):
    """Trading view for one configured asset or basket."""

    name: str
    category: str
    market: str
    symbols: List[str]
    analysis_proxy: bool = False
    horizons: List[HorizonProbability]
    key_signals: List[MarketSignal]
    conclusion: str
    data_quality: str = "medium"


class TradingScenario(BaseModel):
    """One probability scenario."""

    name: str
    probability: float
    basis: str
    trading_bias: str


class TradingAnalysisResult(BaseModel):
    """Structured trading analysis result."""

    is_forecastable: bool
    question_type: str
    market_question: str
    summary: str
    signals: List[MarketSignal]
    resonance: List[str]
    divergences: List[str]
    scenarios: List[TradingScenario]
    conclusion: str
    monitor_signals: List[Dict[str, str]]
    data_sources: List[str]
    errors: List[str] = Field(default_factory=list)
    asset_views: List[AssetTradingView] = Field(default_factory=list)
    analysis_method: str = "unknown"
    digital_oracle_layers: Dict[str, Any] = Field(default_factory=dict)
    missing_evidence: List[str] = Field(default_factory=list)
    references: List[Dict[str, Any]] = Field(default_factory=list)


class TradingOracleAnalyzer:
    """Analyze Horizon content items using market trading data."""

    _MIN_SIGNALS = 3
    _INSUFFICIENT_COVERAGE_REASON = "insufficient independent market signals"

    _PROVIDER_PLAN = {
        "macro_rates": ["treasury", "cme_fedwatch", "fear_greed", "yahoo_price", "cftc", "kalshi"],
        "recession_risk": ["treasury", "cme_fedwatch", "fear_greed", "yahoo_price", "cftc", "kalshi"],
        "geopolitical_risk": ["polymarket", "kalshi", "yahoo_price", "cftc", "fear_greed", "web_search"],
        "crypto_cycle": ["coingecko", "deribit", "fear_greed", "yahoo_price", "polymarket"],
        "equity_options": ["yfinance", "yahoo_price", "fear_greed", "cftc", "edgar", "kalshi"],
        "commodity_risk": ["yahoo_price", "cftc", "treasury", "fear_greed", "polymarket"],
        "ai_bubble": ["yahoo_price", "yfinance", "edgar", "treasury", "fear_greed", "web_search"],
        "generic_market_event": ["fear_greed", "yahoo_price", "treasury"],
    }

    def __init__(self, config: TradingConfig):
        self.config = config
        self.router = TradingQuestionRouter(config)

    def is_trading_relevant(self, item: ContentItem) -> bool:
        """Return whether item should receive trading analysis."""
        return self.router.route(item).enabled

    async def analyze(self, item: ContentItem) -> Optional[TradingAnalysisResult]:
        """Generate trading analysis for one item."""
        route = self.router.route(item)
        if not route.enabled or not route.question_type:
            return None

        if route.question_type == "asset_watchlist":
            return await self.analyze_asset_watchlist(item)

        providers = self._select_providers(route.question_type)
        if len(providers) < self._MIN_SIGNALS:
            providers = list(dict.fromkeys(providers + ["fear_greed", "yahoo_price", "treasury"]))

        errors: List[str] = []
        signals: List[MarketSignal] = []
        data_sources: List[str] = []
        sec_env = self.config.user_email_env or "SEC_USER_EMAIL"
        user_email = os.getenv(sec_env)
        call_context = ProviderCallContext(
            item=item,
            question_type=route.question_type,
            symbols=route.symbols,
            user_email=user_email,
        )

        _known_keys = {"signal", "value", "horizon", "interpretation", "source"}

        for provider_name in providers:
            try:
                provider = get_provider_by_name(provider_name)
                payloads = await asyncio.to_thread(provider.fetch, call_context)
                for payload in payloads:
                    metadata = {
                        str(k): str(v)
                        for k, v in payload.items()
                        if k not in _known_keys and v is not None
                    }
                    signal = MarketSignal(
                        layer=provider.layer,
                        signal=str(payload.get("signal", "")),
                        value=str(payload.get("value", "")),
                        horizon=str(payload.get("horizon", "short_to_medium")),
                        interpretation=str(payload.get("interpretation", "")),
                        source=str(payload.get("source", provider_name)),
                        metadata=metadata,
                    )
                    signals.append(signal)
                    data_sources.append(signal.source)
            except Exception as exc:
                errors.append(f"{provider_name}: {exc}")

        signal_count = len(signals)
        confidence = "high" if signal_count >= 5 else ("medium" if signal_count >= self._MIN_SIGNALS else "low")
        resonance = self._extract_resonance(signals)
        divergences = self._extract_divergences(signals)
        if signal_count < self._MIN_SIGNALS:
            errors.append(f"{self._INSUFFICIENT_COVERAGE_REASON} (<{self._MIN_SIGNALS} signals).")

        scenarios = self._build_scenarios(route.question_type, confidence)
        conclusion = self._build_conclusion(route.question_type, confidence, signal_count)
        monitor_signals = self._build_monitor_signals(signals)
        question = self._build_market_question(item, route.question_type)

        return TradingAnalysisResult(
            is_forecastable=True,
            question_type=route.question_type,
            market_question=question,
            summary=f"Generated from {signal_count} market signals across {len(set(data_sources))} sources.",
            signals=signals,
            resonance=resonance,
            divergences=divergences,
            scenarios=scenarios,
            conclusion=conclusion,
            monitor_signals=monitor_signals,
            data_sources=sorted(set(data_sources)),
            errors=errors,
        )

    def _select_providers(self, question_type: str) -> List[str]:
        enabled = set(self.config.enabled_providers)
        planned = self._PROVIDER_PLAN.get(question_type, self._PROVIDER_PLAN["generic_market_event"])
        return [name for name in planned if name in enabled]

    @staticmethod
    def _build_market_question(item: ContentItem, question_type: str) -> str:
        return f"{question_type}: how could markets reprice after '{item.title}'?"

    @staticmethod
    def _extract_resonance(signals: List[MarketSignal]) -> List[str]:
        layers = [s.layer for s in signals]
        if not layers:
            return []
        unique_layers = sorted(set(layers))
        return [f"Multi-layer alignment observed in: {', '.join(unique_layers[:4])}."]

    @staticmethod
    def _extract_divergences(signals: List[MarketSignal]) -> List[str]:
        if len(signals) < 2:
            return ["Not enough cross-layer signals to assess divergence."]
        return ["Cross-asset confirmation remains partial; monitor breakdown risk."]

    @staticmethod
    def _build_scenarios(question_type: str, confidence: str) -> List[TradingScenario]:
        if confidence == "low":
            return [
                TradingScenario(name="baseline", probability=40, basis="Limited signal coverage.", trading_bias="Reduce risk and wait for confirmation."),
                TradingScenario(name="bullish_risk_on", probability=30, basis="Growth-sensitive assets stabilize.", trading_bias="Selective long beta exposure."),
                TradingScenario(name="downside_shock", probability=30, basis="Tail risk repricing resumes.", trading_bias="Favor hedges and defensive assets."),
            ]
        if question_type in {"crypto_cycle", "equity_options", "ai_bubble"}:
            return [
                TradingScenario(name="baseline", probability=45, basis="Trend persistence with moderate volatility.", trading_bias="Directional with risk controls."),
                TradingScenario(name="bullish_risk_on", probability=35, basis="Positioning squeeze supports upside.", trading_bias="Long growth / beta."),
                TradingScenario(name="downside_shock", probability=20, basis="Volatility spike invalidates trend.", trading_bias="Hedge with convex protection."),
            ]
        return [
            TradingScenario(name="baseline", probability=50, basis="Current macro regime persists.", trading_bias="Balanced and defensive tilt."),
            TradingScenario(name="bullish_risk_on", probability=25, basis="Policy and risk premia ease.", trading_bias="Rotate into cyclicals."),
            TradingScenario(name="downside_shock", probability=25, basis="Growth or geopolitical shock expands.", trading_bias="Long duration and safe havens."),
        ]

    @classmethod
    def _build_conclusion(cls, question_type: str, confidence: str, signal_count: int) -> str:
        if signal_count < cls._MIN_SIGNALS:
            return (
                f"{question_type} analysis completed with {cls._INSUFFICIENT_COVERAGE_REASON}; "
                "treat directional bias as tentative."
            )
        return f"{question_type} analysis indicates a {confidence} confidence tactical setup."

    @staticmethod
    def _build_monitor_signals(signals: List[MarketSignal]) -> List[Dict[str, str]]:
        monitors: List[Dict[str, str]] = []
        for signal in signals[:5]:
            monitors.append(
                {
                    "signal": signal.signal,
                    "threshold": "regime shift",
                    "meaning": signal.interpretation,
                }
            )
        return monitors

    async def analyze_asset_watchlist(
        self, item: Optional[ContentItem] = None
    ) -> Optional[TradingAnalysisResult]:
        """Generate fixed asset watchlist trading analysis."""
        from .digital_oracle_bridge import DigitalOracleBridge
        from .universe import get_enabled_assets
        print("📈 Running market analysis...")
        enabled_assets = get_enabled_assets(self.config)
        if not enabled_assets:
            return None

        bridge = DigitalOracleBridge(self.config)
        if bridge.available:
            print("🔮 digital-oracle bridge: available")
            print(f"🔮 digital-oracle module: {bridge.module_file}")
            oracle_result = await bridge.analyze_assets(enabled_assets)
            return self._convert_digital_oracle_result(oracle_result)

        print("⚠ digital-oracle full package unavailable; using Horizon minimal fallback providers.")
        return await self._analyze_asset_watchlist_fallback(
            item,
            fallback_reason=(
                "digital-oracle full provider package unavailable; using minimal Horizon fallback provider."
            ),
        )

    async def _analyze_asset_watchlist_fallback(
        self,
        item: Optional[ContentItem] = None,
        fallback_reason: Optional[str] = None,
    ) -> Optional[TradingAnalysisResult]:
        """Fallback watchlist analysis using local minimal providers."""
        from .probability import estimate_horizon_probability
        from .universe import get_enabled_assets

        enabled_assets = get_enabled_assets(self.config)
        if not enabled_assets:
            return None

        errors: List[str] = []
        all_signals: List[MarketSignal] = []
        data_sources: List[str] = []
        asset_views: List[AssetTradingView] = []

        sec_env = self.config.user_email_env or "SEC_USER_EMAIL"
        user_email = os.getenv(sec_env)

        if item is None:
            from datetime import datetime, timezone
            from ..models import SourceType
            item = ContentItem(
                id="trading:asset_watchlist:synthetic",
                source_type=SourceType.RSS,
                title="Daily Asset Watchlist Analysis",
                url="https://github.com/shajieChen/Horizon",
                published_at=datetime.now(timezone.utc),
            )

        watchlist_providers = [
            p for p in self.config.enabled_providers
            if p in {"yahoo_price", "yfinance", "fear_greed", "treasury"}
        ]
        if not watchlist_providers:
            watchlist_providers = ["fear_greed", "yahoo_price", "treasury"]

        _known_keys = {"signal", "value", "horizon", "interpretation", "source"}

        for asset in enabled_assets:
            asset_signals: List[MarketSignal] = []
            call_context = ProviderCallContext(
                item=item,
                question_type="asset_watchlist",
                symbols=asset.symbols[:self.config.max_symbols_per_asset],
                user_email=user_email,
            )
            for provider_name in watchlist_providers:
                try:
                    provider = get_provider_by_name(provider_name)
                    payloads = await asyncio.to_thread(provider.fetch, call_context)
                    for payload in payloads:
                        metadata = {
                            str(k): str(v)
                            for k, v in payload.items()
                            if k not in _known_keys and v is not None
                        }
                        signal = MarketSignal(
                            layer=provider.layer,
                            signal=str(payload.get("signal", "")),
                            value=str(payload.get("value", "")),
                            horizon=str(payload.get("horizon", "short_to_medium")),
                            interpretation=str(payload.get("interpretation", "")),
                            source=str(payload.get("source", provider_name)),
                            metadata=metadata,
                        )
                        asset_signals.append(signal)
                        all_signals.append(signal)
                        data_sources.append(signal.source)
                except Exception as exc:
                    msg = f"{asset.name}/{provider_name}: {exc}"
                    errors.append(msg)

            horizons_list: List[HorizonProbability] = []
            for hz in self.config.default_horizons:
                horizons_list.append(
                    estimate_horizon_probability(asset, asset_signals, hz)
                )

            valid_count, _ = self._count_valid_price_signals(asset_signals)
            if valid_count >= 3:
                data_quality = "high"
            elif valid_count >= 1:
                data_quality = "medium"
            else:
                data_quality = "low"
                errors.append(
                    f"Missing price data for {asset.name}: no valid yfinance price signals. "
                    "Check yfinance installation, network access, and Yahoo symbol support."
                )

            conclusion = self._build_asset_conclusion(asset.name, asset_signals, horizons_list)
            asset_views.append(
                AssetTradingView(
                    name=asset.name,
                    category=asset.category,
                    market=asset.market,
                    symbols=asset.symbols,
                    analysis_proxy=asset.analysis_proxy,
                    horizons=horizons_list,
                    key_signals=asset_signals[:5],
                    conclusion=conclusion,
                    data_quality=data_quality,
                )
            )

        if fallback_reason:
            errors.append(fallback_reason)

        signal_count = len(all_signals)
        confidence = "medium" if signal_count >= 4 else "low"
        resonance = self._extract_resonance(all_signals)
        divergences = self._extract_divergences(all_signals)
        scenarios = self._build_scenarios("asset_watchlist", confidence)
        monitor_signals = self._build_monitor_signals(all_signals)
        conclusion = (
            f"Asset watchlist analysis for {len(asset_views)} basket(s) completed "
            f"with {signal_count} signals. Data quality: {confidence}."
        )
        if errors:
            conclusion += f" {len(errors)} provider error(s) recorded."

        return TradingAnalysisResult(
            is_forecastable=True,
            question_type="asset_watchlist",
            market_question=(
                "asset_watchlist: 1D/1W/1M directional probability for "
                "QDII Nasdaq 100 / US / Japan / Hong Kong baskets"
            ),
            summary=(
                f"Generated from {signal_count} market signals across "
                f"{len(set(data_sources))} sources for {len(asset_views)} asset basket(s)."
            ),
            signals=all_signals,
            resonance=resonance,
            divergences=divergences,
            scenarios=scenarios,
            conclusion=conclusion,
            monitor_signals=monitor_signals,
            data_sources=sorted(set(data_sources)),
            errors=errors,
            asset_views=asset_views,
            analysis_method="horizon_minimal_fallback",
            digital_oracle_layers={},
            missing_evidence=errors,
        )

    @staticmethod
    def _convert_digital_oracle_result(oracle_result: Any) -> TradingAnalysisResult:
        """Convert bridge watchlist result into TradingAnalysisResult."""
        asset_views: List[AssetTradingView] = []
        all_signals: List[MarketSignal] = []
        all_sources: List[str] = []
        digital_layers: Dict[str, Any] = {}

        for asset in oracle_result.asset_results:
            asset_market_signals: List[MarketSignal] = []
            for signal in asset.signals:
                metadata = {
                    str(k): str(v)
                    for k, v in (signal.raw or {}).items()
                    if v is not None and not isinstance(v, (dict, list))
                }
                ms = MarketSignal(
                    layer=signal.layer,
                    signal=signal.signal,
                    value=signal.data,
                    horizon=signal.horizon,
                    interpretation=signal.interpretation,
                    source=signal.provider,
                    metadata=metadata,
                )
                all_signals.append(ms)
                asset_market_signals.append(ms)
                all_sources.append(signal.provider)

            quality = "high" if len({s.layer for s in asset.signals}) >= 3 else "medium"
            asset_views.append(
                AssetTradingView(
                    name=asset.name,
                    category=asset.category,
                    market=asset.market,
                    symbols=asset.symbols,
                    analysis_proxy=asset.category == "qdii_nasdaq100",
                    horizons=asset.horizon_views,
                    key_signals=asset_market_signals[:5],
                    conclusion=asset.conclusion,
                    data_quality=quality,
                )
            )
            digital_layers[asset.name] = {
                "signals": [s.model_dump() for s in asset.signals],
                "resonance": asset.resonance,
                "divergences": asset.divergences,
                "probability_scenarios": [s.model_dump() for s in asset.probability_scenarios],
                "references": [
                    ref.model_dump() if hasattr(ref, "model_dump") else dict(ref)
                    for ref in getattr(asset, "references", [])
                ],
            }

        if not all_signals:
            scenarios = []
            monitor_signals = []
        else:
            scenarios = [
                TradingScenario(name="baseline", probability=50.0, basis="multi-asset synthesis", trading_bias="balanced"),
                TradingScenario(name="upside", probability=30.0, basis="risk appetite stabilizes", trading_bias="risk-on"),
                TradingScenario(name="downside", probability=20.0, basis="volatility/rates shock", trading_bias="defensive"),
            ]
            monitor_signals = TradingOracleAnalyzer._build_monitor_signals(all_signals)

        conclusion = (
            f"Digital-oracle watchlist analysis completed for {len(asset_views)} basket(s) "
            f"with {len(all_signals)} normalized signals."
        )
        if oracle_result.missing_evidence:
            conclusion += f" Missing evidence items: {len(oracle_result.missing_evidence)}."

        return TradingAnalysisResult(
            is_forecastable=True,
            question_type="asset_watchlist",
            market_question=(
                "asset_watchlist: 1D/1W/1M directional probability for "
                "QDII Nasdaq 100 / US / Japan / Hong Kong baskets"
            ),
            summary=(
                f"Generated from {len(all_signals)} market signals across "
                f"{len(set(all_sources))} sources for {len(asset_views)} asset basket(s)."
            ),
            signals=all_signals,
            resonance=list(oracle_result.global_resonance),
            divergences=list(oracle_result.global_divergences),
            scenarios=scenarios,
            conclusion=conclusion,
            monitor_signals=monitor_signals,
            data_sources=sorted(set(all_sources)),
            errors=list(oracle_result.missing_evidence),
            asset_views=asset_views,
            analysis_method="digital_oracle",
            digital_oracle_layers=digital_layers,
            missing_evidence=list(oracle_result.missing_evidence),
            references=[
                ref.model_dump() if hasattr(ref, "model_dump") else dict(ref)
                for ref in getattr(oracle_result, "references", [])
            ],
        )

    @staticmethod
    def _count_valid_price_signals(signals: List[MarketSignal]) -> tuple[int, int]:
        """Return (valid_count, total_price_count) for price signals.

        A price signal is *valid* when its value is not empty/N/A and it carries
        a usable ``1d_return`` metadata entry.
        """
        total = sum(1 for s in signals if s.layer == "price")
        valid = sum(
            1 for s in signals
            if s.layer == "price"
            and s.value not in ("", "N/A")
            and (s.metadata or {}).get("1d_return") not in (None, "", "N/A", "unknown")
        )
        return valid, total

    @staticmethod
    def _build_asset_conclusion(
        name: str,
        signals: List[MarketSignal],
        horizons: List[HorizonProbability],
    ) -> str:
        """Build a one-line conclusion summarising bias direction and signal coverage."""
        if not horizons:
            return f"{name}: no horizon data available."
        biases = [h.expected_bias for h in horizons]
        bias_str = "/".join(biases)

        valid_price, total_price = TradingOracleAnalyzer._count_valid_price_signals(signals)

        if valid_price == 0:
            return (
                f"{name}: {bias_str} bias across 1D/1W/1M. "
                "No valid price data. Conservative probability distribution used."
            )
        return (
            f"{name}: {bias_str} bias across 1D/1W/1M. "
            f"Price signals: {valid_price}/{total_price} symbols. Treat as probability estimate only."
        )
