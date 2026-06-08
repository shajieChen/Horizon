"""Render market analysis into forecast metadata for DailySummarizer."""

from __future__ import annotations

from typing import Dict

from .constants import DEFAULT_FALSIFIER
from .oracle import TradingAnalysisResult

_CONSERVATIVE_BASIS_MARKERS = (
    "有效交易信号不足",
    "保守基准分布",
    "价格数据不足",
    "conservative base distribution",
)


def _confidence_level(result: TradingAnalysisResult) -> str:
    signal_count = len(result.signals)
    if signal_count >= 5:
        return "high"
    if signal_count >= 3:
        return "medium"
    return "low"


def _has_conservative_basis(result: TradingAnalysisResult) -> bool:
    for scenario in result.scenarios:
        basis = str(getattr(scenario, "basis", "") or "")
        if any(marker in basis for marker in _CONSERVATIVE_BASIS_MARKERS):
            return True
    for asset_view in result.asset_views:
        for horizon in asset_view.horizons:
            basis = str(getattr(horizon, "basis", "") or "")
            if any(marker in basis for marker in _CONSERVATIVE_BASIS_MARKERS):
                return True
    return False


def trading_result_to_forecast(result: TradingAnalysisResult) -> Dict:
    """Convert trading analysis result into Horizon forecast metadata."""
    scenarios = []
    for scenario in result.scenarios:
        scenarios.append(
            {
                "name": scenario.name,
                "horizon": "short_to_medium",
                "probability": scenario.probability,
                "reasoning": scenario.basis,
                "trigger_conditions": [scenario.trading_bias],
            }
        )

    confidence_level = _confidence_level(result)
    missing_evidence = list(result.missing_evidence or result.errors)
    if len(result.signals) < 3 and "signal coverage is insufficient." not in missing_evidence:
        missing_evidence.append("signal coverage is insufficient.")
    if _has_conservative_basis(result):
        concise_note = "部分市场数据暂不可用，已采用保守基准概率估计。"
        if concise_note not in missing_evidence:
            missing_evidence.append(concise_note)

    # Build asset_views summary for near_term_watch when available
    near_term_watch: Dict[str, list] = {
        "24h": [],
        "7d": [],
        "30d": [],
    }
    if result.asset_views:
        for av in result.asset_views:
            for hp in av.horizons:
                entry = (
                    f"{av.name} {hp.horizon}: {hp.expected_bias} "
                    f"(↑{hp.up_probability:.0f}%/↓{hp.down_probability:.0f}%/~{hp.neutral_probability:.0f}%)"
                )
                if hp.horizon == "1d":
                    near_term_watch["24h"].append(entry)
                elif hp.horizon == "1w":
                    near_term_watch["7d"].append(entry)
                elif hp.horizon == "1m":
                    near_term_watch["30d"].append(entry)
    else:
        near_term_watch = {
            "24h": [m.get("signal", "") for m in result.monitor_signals[:2] if m.get("signal")],
            "7d": [m.get("signal", "") for m in result.monitor_signals[2:4] if m.get("signal")],
            "30d": [m.get("signal", "") for m in result.monitor_signals[4:] if m.get("signal")],
        }

    return {
        "is_forecastable": result.is_forecastable,
        "event_type": result.question_type,
        "analysis_method": result.analysis_method,
        "cause_chain": {
            "immediate_trigger": result.market_question,
            "structural_causes": result.resonance,
            "constraints": result.divergences,
        },
        "actors": [],
        "scenarios": scenarios,
        "near_term_watch": near_term_watch,
        "confidence": {
            "level": confidence_level,
            "reason": f"Based on {len(result.signals)} independent market signals.",
        },
        "falsifiers": result.divergences or [DEFAULT_FALSIFIER],
        "missing_evidence": missing_evidence,
        "market_or_policy_implications": [result.conclusion],
    }
