"""Render market analysis into forecast metadata for DailySummarizer."""

from __future__ import annotations

from typing import Dict

from .oracle import TradingAnalysisResult


def _confidence_level(result: TradingAnalysisResult) -> str:
    signal_count = len(result.signals)
    if signal_count >= 5:
        return "high"
    if signal_count >= 3:
        return "medium"
    return "low"


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
    missing_evidence = list(result.errors)
    if len(result.signals) < 3 and "signal coverage is insufficient." not in missing_evidence:
        missing_evidence.append("signal coverage is insufficient.")

    return {
        "is_forecastable": result.is_forecastable,
        "event_type": result.question_type,
        "cause_chain": {
            "immediate_trigger": result.market_question,
            "structural_causes": result.resonance,
            "constraints": result.divergences,
        },
        "actors": [],
        "scenarios": scenarios,
        "near_term_watch": {
            "24h": [m.get("signal", "") for m in result.monitor_signals[:2] if m.get("signal")],
            "7d": [m.get("signal", "") for m in result.monitor_signals[2:4] if m.get("signal")],
            "30d": [m.get("signal", "") for m in result.monitor_signals[4:] if m.get("signal")],
        },
        "confidence": {
            "level": confidence_level,
            "reason": f"Based on {len(result.signals)} independent market signals.",
        },
        "falsifiers": result.divergences or ["Signal alignment fails across layers."],
        "missing_evidence": missing_evidence,
        "market_or_policy_implications": [result.conclusion],
    }
