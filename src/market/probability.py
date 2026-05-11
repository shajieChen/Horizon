"""Rule-based directional probability estimator for asset_watchlist trading mode."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .oracle import HorizonProbability, MarketSignal
    from ..models import TradingAssetConfig


def _clamp(value: float, lo: float = 5.0, hi: float = 90.0) -> float:
    return max(lo, min(hi, value))


def _normalize(up: float, down: float, neutral: float) -> tuple[float, float, float]:
    total = up + down + neutral
    if total <= 0:
        return 33.0, 33.0, 34.0
    scale = 100.0 / total
    up_n = round(up * scale, 1)
    down_n = round(down * scale, 1)
    # Adjust neutral to guarantee exact sum of 100.0 despite floating-point rounding
    neutral_n = round(100.0 - up_n - down_n, 1)
    return up_n, down_n, neutral_n


def _extract_signal_value(signals: "List[MarketSignal]", key: str) -> str:
    """Return the first signal value whose signal name contains *key* (case-insensitive)."""
    for s in signals:
        if key.lower() in s.signal.lower():
            return s.value
    return ""


def estimate_horizon_probability(
    asset: "TradingAssetConfig",
    price_signals: "List[MarketSignal]",
    horizon: str,
) -> "HorizonProbability":
    """Estimate directional probability for one time horizon using a simple rule engine.

    The base distribution (up=33, down=33, neutral=34) is adjusted by signals
    extracted from *price_signals*, then clamped to [5, 90] and normalised to 100.
    """
    # Import here to avoid circular imports at module load time
    from .oracle import HorizonProbability  # noqa: PLC0415

    up = 33.0
    down = 33.0
    neutral = 34.0

    basis_items: list[str] = []
    invalidation_items: list[str] = []

    # Extract relevant price signal values
    ret_1d = _extract_signal_value(price_signals, "1d_return")
    ret_5d = _extract_signal_value(price_signals, "5d_return")
    ret_20d = _extract_signal_value(price_signals, "20d_return")
    above_5d_ma = _extract_signal_value(price_signals, "above_5d_ma")
    above_20d_ma = _extract_signal_value(price_signals, "above_20d_ma")
    vol_regime = _extract_signal_value(price_signals, "volatility_regime")

    def _positive(val: str) -> bool:
        try:
            return float(val) > 0
        except (ValueError, TypeError):
            return False

    def _negative(val: str) -> bool:
        try:
            return float(val) < 0
        except (ValueError, TypeError):
            return False

    if horizon == "1d":
        if _positive(ret_1d) and above_5d_ma == "true":
            up += 10
            basis_items.append("1d return positive and price above 5D MA")
        elif _negative(ret_1d) and above_5d_ma == "false":
            down += 10
            basis_items.append("1d return negative and price below 5D MA")
        if vol_regime == "high":
            neutral += 5
            down += 3
            basis_items.append("elevated realized volatility increases uncertainty")
        invalidation_items.append("price reclaims / loses 5D MA intraday")

    elif horizon == "1w":
        if _positive(ret_5d) and above_20d_ma == "true":
            up += 10
            basis_items.append("5d return positive and price above 20D MA")
        elif _negative(ret_5d) and above_20d_ma == "false":
            down += 10
            basis_items.append("5d return negative and price below 20D MA")
        if vol_regime == "high":
            neutral += 5
            basis_items.append("high volatility reduces trend conviction over 1W")
        invalidation_items.append("weekly close outside 20D MA band")

    elif horizon == "1m":
        if _positive(ret_20d) and above_20d_ma == "true":
            up += 15
            basis_items.append("20d return positive with price above 20D MA")
        elif _negative(ret_20d) and above_20d_ma == "false":
            down += 15
            basis_items.append("20d return negative with price below 20D MA")
        # Check macro stress via fear/greed
        fg_val = _extract_signal_value(price_signals, "fear_greed")
        if fg_val == "extreme_fear":
            down += 5
            basis_items.append("extreme fear sentiment adds 1M downside pressure")
        elif fg_val == "extreme_greed":
            up += 5
            basis_items.append("extreme greed sentiment supports 1M upside bias")
        invalidation_items.append("monthly close reversal vs 20D MA trend")

    # Clamp before normalisation
    up = _clamp(up)
    down = _clamp(down)
    neutral = _clamp(neutral)

    up_n, down_n, neutral_n = _normalize(up, down, neutral)

    # Determine bias
    if up_n > down_n and up_n > neutral_n:
        bias = "bullish"
    elif down_n > up_n and down_n > neutral_n:
        bias = "bearish"
    else:
        bias = "neutral"

    # Confidence depends on number of valid price signals
    signal_count = len([s for s in price_signals if s.value not in ("", "N/A")])
    if signal_count >= 5:
        confidence = "medium"
    elif signal_count >= 3:
        confidence = "low"
    else:
        confidence = "low"

    basis = "; ".join(basis_items) if basis_items else "insufficient price data — conservative base distribution used"
    invalidation = "; ".join(invalidation_items) if invalidation_items else "no invalidation criteria identified"

    return HorizonProbability(
        horizon=horizon,
        up_probability=up_n,
        down_probability=down_n,
        neutral_probability=neutral_n,
        expected_bias=bias,
        confidence=confidence,
        basis=basis,
        invalidation=invalidation,
    )
