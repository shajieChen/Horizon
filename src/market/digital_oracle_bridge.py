"""Bridge between Horizon watchlist and full digital-oracle providers."""

from __future__ import annotations

import asyncio
import importlib
import math
import re
import statistics
import sys
from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel, Field

from ..models import TradingAssetConfig, TradingConfig
from .digital_oracle_probability import estimate_digital_oracle_probabilities
from .digital_oracle_routes import ProviderGroupPlan, build_asset_provider_plan
from .oracle import HorizonProbability, TradingScenario


class DigitalOracleSignal(BaseModel):
    """One normalized signal from digital-oracle provider."""

    layer: str
    provider: str
    signal: str
    data: str
    interpretation: str
    horizon: str
    confidence: str = "medium"
    raw: Dict[str, Any] = Field(default_factory=dict)


class DigitalOracleAssetResult(BaseModel):
    """Digital-oracle result for one asset basket."""

    name: str
    category: str
    market: str
    symbols: list[str]
    signals: list[DigitalOracleSignal]
    resonance: list[str]
    divergences: list[str]
    horizon_views: list[HorizonProbability]
    probability_scenarios: list[TradingScenario]
    conclusion: str
    missing_evidence: list[str] = Field(default_factory=list)
    data_sources: list[str] = Field(default_factory=list)


class DigitalOracleWatchlistResult(BaseModel):
    """Digital-oracle watchlist analysis result."""

    asset_results: list[DigitalOracleAssetResult]
    global_signals: list[DigitalOracleSignal]
    global_resonance: list[str]
    global_divergences: list[str]
    missing_evidence: list[str]
    data_sources: list[str]


class DigitalOracleBridge:
    """Bridge between Horizon asset watchlist and digital-oracle providers."""

    def __init__(self, config: TradingConfig):
        self.config = config
        self.module: Any | None = None
        self.module_file: str | None = None
        self.unavailable_reason: str | None = None
        self.available = self._detect_digital_oracle()

    def _detect_digital_oracle(self) -> bool:
        """Return whether full digital-oracle package is importable."""

        try:
            self.module = importlib.import_module("digital_oracle")
            self.module_file = getattr(self.module, "__file__", None)
            self.unavailable_reason = None
            return True
        except Exception:
            pass

        vendor_root = Path(__file__).resolve().parents[1] / "vendor" / "digital_oracle_full"
        if vendor_root.exists():
            if str(vendor_root) not in sys.path:
                sys.path.insert(0, str(vendor_root))
            try:
                self.module = importlib.import_module("digital_oracle")
                self.module_file = getattr(self.module, "__file__", None)
                self.unavailable_reason = None
                return True
            except Exception as exc:
                self.unavailable_reason = str(exc)
                return False

        self.unavailable_reason = "digital_oracle package not importable"
        return False

    def describe_runtime(self) -> dict[str, str | bool | None]:
        """Return diagnostic information for the digital-oracle runtime."""
        return {
            "available": self.available,
            "module_file": self.module_file,
            "unavailable_reason": self.unavailable_reason,
        }

    async def analyze_asset(self, asset: TradingAssetConfig) -> DigitalOracleAssetResult:
        """Analyze one configured asset using digital-oracle methodology."""

        if not self.available or self.module is None:
            return DigitalOracleAssetResult(
                name=asset.name,
                category=asset.category,
                market=asset.market,
                symbols=asset.symbols,
                signals=[],
                resonance=[],
                divergences=[],
                horizon_views=[],
                probability_scenarios=[],
                conclusion="digital-oracle full provider package unavailable.",
                missing_evidence=[
                    "digital-oracle full provider package unavailable; using minimal Horizon fallback provider."
                ],
                data_sources=[],
            )

        plan = build_asset_provider_plan(asset)
        print(f"🔎 Analyzing {asset.name} with {len(plan)} provider groups")

        module = self.module
        gather = getattr(module, "gather")

        providers = self._build_provider_instances(module, plan)
        tasks, task_meta, skipped = self._build_tasks(module, asset, plan, providers)

        missing_evidence: list[str] = list(skipped)
        signals: list[DigitalOracleSignal] = []

        if tasks:
            gathered = await asyncio.to_thread(gather, tasks)
            for key, err in gathered.errors.items():
                meta = task_meta[key]
                missing_evidence.append(f"{meta['provider']}: {meta['label']} unavailable ({err})")

            for key, payload in gathered.results.items():
                meta = task_meta[key]
                try:
                    adapted = self._adapt_payload(asset, meta, payload)
                    signals.extend(adapted)
                except Exception as exc:
                    missing_evidence.append(f"{meta['provider']}: adapter failed for {meta['label']} ({exc})")

        self._emit_group_logs(plan, signals, missing_evidence)

        unique_layers = sorted({s.layer for s in signals})
        if len(unique_layers) < 3:
            missing_evidence.append("insufficient independent market signal layers (<3).")

        resonance = self._build_resonance(signals)
        divergences = self._build_divergences(signals)
        horizon_views = estimate_digital_oracle_probabilities(asset, signals)
        scenarios = self._build_scenarios(horizon_views)
        conclusion = self._build_conclusion(asset.name, horizon_views, unique_layers)

        data_sources = sorted({s.provider for s in signals})
        return DigitalOracleAssetResult(
            name=asset.name,
            category=asset.category,
            market=asset.market,
            symbols=asset.symbols,
            signals=signals,
            resonance=resonance,
            divergences=divergences,
            horizon_views=horizon_views,
            probability_scenarios=scenarios,
            conclusion=conclusion,
            missing_evidence=sorted(set(missing_evidence)),
            data_sources=data_sources,
        )

    async def analyze_assets(self, assets: list[TradingAssetConfig]) -> DigitalOracleWatchlistResult:
        """Analyze all configured assets concurrently."""

        results = await asyncio.gather(*(self.analyze_asset(asset) for asset in assets))
        all_signals = [sig for result in results for sig in result.signals]
        missing_evidence = sorted({e for result in results for e in result.missing_evidence})
        data_sources = sorted({s.provider for s in all_signals})

        global_resonance = [
            "多资产价格层与风险偏好层存在交叉验证。"
            if len({s.layer for s in all_signals}) >= 3
            else "全局信号层覆盖不足，需补充更多独立交易数据。"
        ]
        global_divergences = self._build_divergences(all_signals)

        return DigitalOracleWatchlistResult(
            asset_results=results,
            global_signals=all_signals[:12],
            global_resonance=global_resonance,
            global_divergences=global_divergences,
            missing_evidence=missing_evidence,
            data_sources=data_sources,
        )

    def _build_provider_instances(self, module: Any, plan: list[ProviderGroupPlan]) -> dict[str, Any]:
        providers: dict[str, Any] = {}
        sec_env = self.config.user_email_env or "SEC_USER_EMAIL"
        sec_user = __import__("os").getenv(sec_env)

        for group in plan:
            try:
                cls = getattr(module, group.provider)
                if group.key == "edgar":
                    providers[group.key] = cls(user_email=sec_user)
                else:
                    providers[group.key] = cls()
            except Exception:
                continue
        return providers

    def _build_tasks(self, module: Any, asset: TradingAssetConfig, plan: list[ProviderGroupPlan], providers: dict[str, Any]):
        tasks: dict[str, Any] = {}
        meta: dict[str, dict[str, str]] = {}
        skipped: list[str] = []

        for group in plan:
            provider = providers.get(group.key)
            if provider is None:
                skipped.append(f"{group.provider}: unavailable")
                continue

            try:
                if group.key == "yahoo_price":
                    query_cls = getattr(module, "PriceHistoryQuery")
                    for symbol in group.symbols:
                        key = f"{group.key}:{symbol}"
                        tasks[key] = lambda s=symbol, p=provider, qc=query_cls: p.get_history(qc(symbol=s, limit=30))
                        meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "price", "label": symbol}

                elif group.key == "yfinance":
                    query_cls = getattr(module, "OptionsChainQuery")
                    for symbol in group.symbols:
                        key = f"{group.key}:{symbol}"
                        tasks[key] = lambda s=symbol, p=provider, qc=query_cls: p.get_chain(qc(ticker=s))
                        meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "options", "label": symbol}

                elif group.key == "fear_greed":
                    key = f"{group.key}:index"
                    tasks[key] = lambda p=provider: p.get_index()
                    meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "fear_greed", "label": "index"}

                elif group.key == "treasury":
                    key = f"{group.key}:curve"
                    tasks[key] = lambda p=provider: p.latest_yield_curve()
                    meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "treasury", "label": "latest_yield_curve"}

                elif group.key == "cme_fedwatch":
                    key = f"{group.key}:probabilities"
                    tasks[key] = lambda p=provider: p.get_probabilities()
                    meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "fedwatch", "label": "probabilities"}

                elif group.key == "kalshi":
                    query_cls = getattr(module, "KalshiMarketQuery")
                    series = group.series_ticker or "KXINX"
                    key = f"{group.key}:{series}"
                    tasks[key] = lambda s=series, p=provider, qc=query_cls: p.list_markets(qc(series_ticker=s, limit=5))
                    meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "kalshi", "label": series}

                elif group.key == "web_search":
                    for query in group.queries:
                        key = f"{group.key}:{query}"
                        tasks[key] = lambda q=query, p=provider: p.search(q)
                        meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "web", "label": query}

                elif group.key == "edgar":
                    query_cls = getattr(module, "EdgarInsiderQuery")
                    for symbol in group.symbols[:3]:
                        key = f"{group.key}:{symbol}"
                        tasks[key] = lambda s=symbol, p=provider, qc=query_cls: p.get_insider_transactions(qc(ticker=s, limit=10))
                        meta[key] = {"provider": group.provider, "layer": group.layer, "kind": "edgar", "label": symbol}
            except Exception as exc:
                skipped.append(f"{group.provider}: task wiring failed ({exc})")

        return tasks, meta, skipped

    def _adapt_payload(self, asset: TradingAssetConfig, meta: dict[str, str], payload: Any) -> list[DigitalOracleSignal]:
        kind = meta["kind"]
        if kind == "price":
            return [self._adapt_price_signal(meta, payload)]
        if kind == "options":
            return [self._adapt_options_signal(meta, payload)]
        if kind == "fear_greed":
            return [self._adapt_fear_greed_signal(meta, payload)]
        if kind == "treasury":
            return [self._adapt_treasury_signal(meta, payload)]
        if kind == "fedwatch":
            return [self._adapt_fedwatch_signal(meta, payload)]
        if kind == "kalshi":
            return [self._adapt_kalshi_signal(meta, payload)]
        if kind == "web":
            return [self._adapt_web_signal(meta, payload)]
        if kind == "edgar":
            return [self._adapt_edgar_signal(meta, payload)]
        return []

    def _adapt_price_signal(self, meta: dict[str, str], history: Any) -> DigitalOracleSignal:
        bars = list(getattr(history, "bars", ()) or ())
        closes = [float(getattr(bar, "close", 0.0)) for bar in bars if getattr(bar, "close", None) is not None]
        symbol = getattr(history, "symbol", meta["label"])
        if len(closes) < 2:
            raise ValueError("insufficient bars")

        latest = closes[-1]
        ret_1d = (closes[-1] - closes[-2]) / closes[-2] if len(closes) >= 2 else 0.0
        ret_5d = (closes[-1] - closes[-6]) / closes[-6] if len(closes) >= 6 else ret_1d
        ret_20d = (closes[-1] - closes[-21]) / closes[-21] if len(closes) >= 21 else ret_5d

        ma5 = statistics.mean(closes[-5:]) if len(closes) >= 5 else latest
        ma20 = statistics.mean(closes[-20:]) if len(closes) >= 20 else latest

        rets = [((closes[i] - closes[i - 1]) / closes[i - 1]) for i in range(1, len(closes)) if closes[i - 1] != 0]
        vol_5d = statistics.pstdev(rets[-5:]) * math.sqrt(252) if len(rets) >= 5 else 0.0

        raw = {
            "symbol": symbol,
            "latest": latest,
            "ret_1d": ret_1d,
            "ret_5d": ret_5d,
            "ret_20d": ret_20d,
            "ma5": ma5,
            "ma20": ma20,
            "above_5d_ratio": 1.0 if latest > ma5 else 0.0,
            "above_20d_ratio": 1.0 if latest > ma20 else 0.0,
            "vol_5d": vol_5d,
        }
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal=f"{symbol} price trend",
            data=f"close={latest:.2f}; 1d={ret_1d:+.2%}; 5d={ret_5d:+.2%}; 20d={ret_20d:+.2%}",
            interpretation="价格趋势与均线位置用于判断短中期方向概率。",
            horizon="1d/1w/1m",
            confidence="high",
            raw=raw,
        )

    def _adapt_options_signal(self, meta: dict[str, str], chain: Any) -> DigitalOracleSignal:
        ticker = getattr(chain, "ticker", meta["label"])
        atm_iv = getattr(chain, "atm_iv", None)
        implied_move = chain.implied_move() if hasattr(chain, "implied_move") else None
        pcr_oi = getattr(chain, "put_call_oi_ratio", None)
        max_pain = chain.max_pain() if hasattr(chain, "max_pain") else None
        raw = {
            "symbol": ticker,
            "atm_iv": float(atm_iv) if isinstance(atm_iv, (int, float)) else None,
            "implied_move": float(implied_move) if isinstance(implied_move, (int, float)) else None,
            "put_call_oi_ratio": float(pcr_oi) if isinstance(pcr_oi, (int, float)) else None,
            "max_pain": float(max_pain) if isinstance(max_pain, (int, float)) else None,
        }
        iv_txt = f"{atm_iv:.1%}" if isinstance(atm_iv, (int, float)) else "N/A"
        move_txt = f"{implied_move:.1%}" if isinstance(implied_move, (int, float)) else "N/A"
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal=f"{ticker} options surface",
            data=f"ATM IV={iv_txt}; implied_move={move_txt}; put/call OI={pcr_oi if pcr_oi is not None else 'N/A'}",
            interpretation="期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。",
            horizon="1d/1w",
            confidence="medium",
            raw=raw,
        )

    def _adapt_fear_greed_signal(self, meta: dict[str, str], snapshot: Any) -> DigitalOracleSignal:
        score = float(getattr(snapshot, "score", 0.0))
        rating = str(getattr(snapshot, "rating", "Unknown"))
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal="CNN Fear & Greed",
            data=f"score={score:.1f}; rating={rating}",
            interpretation="风险偏好指数用于识别情绪顺风或逆风。",
            horizon="1d/1w",
            raw={"fear_greed_score": score, "fear_greed_rating": rating},
        )

    def _adapt_treasury_signal(self, meta: dict[str, str], curve: Any) -> DigitalOracleSignal:
        y10 = curve.yield_for("10Y") if curve else None
        y2 = curve.yield_for("2Y") if curve else None
        spread = curve.spread("10Y", "2Y") if curve else None
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal="US Treasury curve",
            data=f"10Y={y10 if y10 is not None else 'N/A'}; 2Y={y2 if y2 is not None else 'N/A'}; 10Y-2Y={spread if spread is not None else 'N/A'}",
            interpretation="利率曲线决定权益估值贴现与风险偏好上限。",
            horizon="1w/1m",
            raw={"yield_10y": y10, "yield_2y": y2, "curve_10y_2y": spread},
        )

    def _adapt_fedwatch_signal(self, meta: dict[str, str], meetings: Any) -> DigitalOracleSignal:
        meeting_list = list(meetings or [])
        if not meeting_list:
            raise ValueError("empty FedWatch meetings")
        first = meeting_list[0]
        probs = list(getattr(first, "probabilities", ()) or ())
        top = max(probs, key=lambda p: getattr(p, "probability", 0.0)) if probs else None
        top_text = "N/A"
        if top is not None:
            top_text = f"{top.target_low:.2f}-{top.target_high:.2f}: {top.probability:.1%}"
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal="CME FedWatch path",
            data=f"next={getattr(first, 'meeting_date', 'N/A')}; top_prob={top_text}",
            interpretation="联邦基金利率期货隐含路径反映宏观贴现率预期。",
            horizon="1w/1m",
            raw={"fedwatch_top_probability": getattr(top, "probability", None) if top else None},
        )

    def _adapt_kalshi_signal(self, meta: dict[str, str], markets: Any) -> DigitalOracleSignal:
        rows = list(markets or [])
        if not rows:
            raise ValueError("empty kalshi markets")
        first = rows[0]
        yes_prob = getattr(first, "yes_probability", None)
        title = getattr(first, "title", "Kalshi market")
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal=f"Kalshi {meta['label']}",
            data=f"{title}; yes_prob={yes_prob if yes_prob is not None else 'N/A'}",
            interpretation="事件市场概率提供独立的交易定价参考。",
            horizon="1w/1m",
            raw={"kalshi_yes_probability": yes_prob},
        )

    def _adapt_web_signal(self, meta: dict[str, str], result: Any) -> DigitalOracleSignal:
        text = result.text() if hasattr(result, "text") else str(result)
        value = _extract_first_number(text)
        raw: dict[str, Any] = {"query": meta["label"], "raw_text": text[:300]}
        lowered = meta["label"].lower()
        if "vix" in lowered:
            raw["vix"] = value
        elif "move" in lowered:
            raw["move"] = value
        elif "high yield" in lowered or "oas" in lowered:
            raw["hy_oas"] = value
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal=f"Web metric: {meta['label']}",
            data=f"{meta['label']} => {value if value is not None else 'N/A'}",
            interpretation="补充性交易数据用于校验波动与信用风险状态。",
            horizon="1d/1w",
            confidence="low",
            raw=raw,
        )

    def _adapt_edgar_signal(self, meta: dict[str, str], summary: Any) -> DigitalOracleSignal:
        count = getattr(summary, "total_form4_count", None)
        ticker = getattr(summary, "ticker", meta["label"])
        return DigitalOracleSignal(
            layer=meta["layer"],
            provider=meta["provider"],
            signal=f"{ticker} insider filings",
            data=f"recent Form4 count={count if count is not None else 'N/A'}",
            interpretation="内部人交易节奏可作为估值温度辅助校验信号。",
            horizon="1m",
            confidence="low",
            raw={"insider_form4_count": count},
        )

    @staticmethod
    def _build_resonance(signals: list[DigitalOracleSignal]) -> list[str]:
        if not signals:
            return ["暂无有效信号。"]
        layers = sorted({signal.layer for signal in signals})
        return [f"已覆盖信号层：{', '.join(layers)}。", "价格趋势层与风险偏好层形成交叉验证。"]

    @staticmethod
    def _build_divergences(signals: list[DigitalOracleSignal]) -> list[str]:
        has_price = any(s.layer == "Price Trend" for s in signals)
        has_options = any(s.layer == "Options / Volatility" for s in signals)
        if has_price and has_options:
            return ["价格方向与期权隐含波动可能出现背离，需跟踪IV变化。"]
        return ["跨层分歧信息有限，后续需补充更多波动与事件市场数据。"]

    @staticmethod
    def _build_scenarios(horizons: list[HorizonProbability]) -> list[TradingScenario]:
        if not horizons:
            return []
        h1m = next((h for h in horizons if h.horizon == "1m"), horizons[-1])
        up = round(h1m.up_probability, 1)
        down = round(h1m.down_probability, 1)
        neutral = round(h1m.neutral_probability, 1)
        return [
            TradingScenario(name="upside", probability=up, basis=h1m.basis, trading_bias="risk-on tilt"),
            TradingScenario(name="downside", probability=down, basis=h1m.basis, trading_bias="defensive"),
            TradingScenario(name="range", probability=neutral, basis=h1m.basis, trading_bias="neutral"),
        ]

    @staticmethod
    def _build_conclusion(asset_name: str, horizons: list[HorizonProbability], layers: list[str]) -> str:
        if not horizons:
            return f"{asset_name}: 有效信号不足，暂无法形成稳定概率结论。"
        h1d = next((h for h in horizons if h.horizon == "1d"), horizons[0])
        h1w = next((h for h in horizons if h.horizon == "1w"), horizons[0])
        h1m = next((h for h in horizons if h.horizon == "1m"), horizons[-1])
        return (
            f"{asset_name}: 1日/1周/1月偏向分别为 {h1d.expected_bias}/{h1w.expected_bias}/{h1m.expected_bias}，"
            f"基于 {len(layers)} 个独立信号层的多信号综合判断。"
        )

    @staticmethod
    def _emit_group_logs(plan: list[ProviderGroupPlan], signals: list[DigitalOracleSignal], missing_evidence: list[str]) -> None:
        for group in plan:
            group_signals = [s for s in signals if s.provider == group.provider]
            if group_signals:
                detail = f"{len(group_signals)} signal(s)"
                if group.key == "yfinance":
                    detail = f"{len(group_signals)} options chain signal(s)"
                print(f"   ✓ {group.key}: {detail}")
                continue
            group_errors = [e for e in missing_evidence if group.provider in e]
            if group_errors:
                print(f"   ⚠ {group.key}: {group_errors[0]}")


def _extract_first_number(text: str) -> float | None:
    match = re.search(r"(-?\d+(?:\.\d+)?)", text)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None
