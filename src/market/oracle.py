"""Trading oracle analyzer for Horizon market plugin."""

from __future__ import annotations

import asyncio
import os
from typing import Dict, List, Optional

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


class TradingOracleAnalyzer:
    """Analyze Horizon content items using market trading data."""

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

        providers = self._select_providers(route.question_type)
        if len(providers) < 3:
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

        for provider_name in providers:
            try:
                provider = get_provider_by_name(provider_name)
                payloads = await asyncio.to_thread(provider.fetch, call_context)
                for payload in payloads:
                    signal = MarketSignal(
                        layer=provider.layer,
                        signal=str(payload.get("signal", "")),
                        value=str(payload.get("value", "")),
                        horizon=str(payload.get("horizon", "short_to_medium")),
                        interpretation=str(payload.get("interpretation", "")),
                        source=str(payload.get("source", provider_name)),
                    )
                    signals.append(signal)
                    data_sources.append(signal.source)
            except Exception as exc:
                errors.append(f"{provider_name}: {exc}")

        signal_count = len(signals)
        confidence = "high" if signal_count >= 5 else ("medium" if signal_count >= 3 else "low")
        resonance = self._extract_resonance(signals)
        divergences = self._extract_divergences(signals)
        if signal_count < 3:
            errors.append("signal coverage is insufficient (<3 independent signals).")

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

    @staticmethod
    def _build_conclusion(question_type: str, confidence: str, signal_count: int) -> str:
        if signal_count < 3:
            return (
                f"{question_type} analysis completed but signal coverage is insufficient; "
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
