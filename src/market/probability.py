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


def _extract_metadata_value(signals: "List[MarketSignal]", key: str) -> str:
    """Return the first usable metadata value for key across all signals."""
    for signal in signals:
        metadata = getattr(signal, "metadata", {}) or {}
        value = metadata.get(key)
        if value not in (None, "", "N/A", "unknown"):
            return str(value)
    return ""


def _extract_numeric_metadata_values(signals: "List[MarketSignal]", key: str) -> list[float]:
    """Return all usable numeric metadata values for key across all signals."""
    values = []
    for signal in signals:
        metadata = getattr(signal, "metadata", {}) or {}
        raw = metadata.get(key)
        if raw in (None, "", "N/A", "unknown"):
            continue
        try:
            values.append(float(raw))
        except (TypeError, ValueError):
            continue
    return values


def _average_metadata(signals: "List[MarketSignal]", key: str) -> str:
    """Return the average of all usable numeric metadata values for key, or empty string."""
    values = _extract_numeric_metadata_values(signals, key)
    if not values:
        return ""
    return str(sum(values) / len(values))


def _ratio_metadata(signals: "List[MarketSignal]", key: str, expected: str = "true") -> str:
    """Return ratio of signals where metadata[key] == expected, or empty string if no data."""
    total = 0
    matched = 0
    for signal in signals:
        metadata = getattr(signal, "metadata", {}) or {}
        raw = metadata.get(key)
        if raw in (None, "", "N/A", "unknown"):
            continue
        total += 1
        if str(raw).lower() == expected:
            matched += 1
    if total == 0:
        return ""
    return str(matched / total)


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

    # Extract relevant price metric values from metadata (basket-averaged)
    ret_1d = _average_metadata(price_signals, "1d_return")
    ret_5d = _average_metadata(price_signals, "5d_return")
    ret_20d = _average_metadata(price_signals, "20d_return")
    above_5d_ratio = _ratio_metadata(price_signals, "above_5d_ma", "true")
    above_20d_ratio = _ratio_metadata(price_signals, "above_20d_ma", "true")
    vol_regime = _extract_metadata_value(price_signals, "volatility_regime")

    # Determine high-volatility regime: any symbol "high" or >= 30% "high"
    vol_values = [
        (getattr(s, "metadata", {}) or {}).get("volatility_regime", "")
        for s in price_signals
    ]
    vol_values_valid = [v for v in vol_values if v not in ("", None, "N/A", "unknown")]
    high_vol = False
    if vol_values_valid:
        high_count = sum(1 for v in vol_values_valid if v == "high")
        high_vol = high_count >= 1 or (high_count / len(vol_values_valid)) >= 0.3

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

    def _ratio_float(val: str) -> float:
        try:
            return float(val)
        except (ValueError, TypeError):
            return -1.0

    if horizon == "1d":
        r5 = _ratio_float(above_5d_ratio)
        if _positive(ret_1d) and r5 >= 0.5:
            up += 10
            pct = f"{r5:.0%}" if r5 >= 0 else "?"
            basis_items.append(f"1d basket avg return positive and {pct} symbols above 5D MA")
        elif _negative(ret_1d) and 0.0 <= r5 < 0.5:
            down += 10
            pct = f"{r5:.0%}"
            basis_items.append(f"1d basket avg return negative and only {pct} symbols above 5D MA")
        if high_vol:
            neutral += 5
            down += 3
            basis_items.append("elevated realized volatility increases uncertainty")
        invalidation_items.append("price reclaims / loses 5D MA intraday")

    elif horizon == "1w":
        r20 = _ratio_float(above_20d_ratio)
        if _positive(ret_5d) and r20 >= 0.5:
            up += 10
            pct = f"{r20:.0%}" if r20 >= 0 else "?"
            basis_items.append(f"5d basket avg return positive and {pct} symbols above 20D MA")
        elif _negative(ret_5d) and 0.0 <= r20 < 0.5:
            down += 10
            pct = f"{r20:.0%}"
            basis_items.append(f"5d basket avg return negative and only {pct} symbols above 20D MA")
        if high_vol:
            neutral += 5
            basis_items.append("high volatility reduces trend conviction over 1W")
        invalidation_items.append("weekly close outside 20D MA band")

    elif horizon == "1m":
        r20 = _ratio_float(above_20d_ratio)
        if _positive(ret_20d) and r20 >= 0.5:
            up += 15
            pct = f"{r20:.0%}" if r20 >= 0 else "?"
            basis_items.append(f"20d basket avg return positive with {pct} symbols above 20D MA")
        elif _negative(ret_20d) and 0.0 <= r20 < 0.5:
            down += 15
            pct = f"{r20:.0%}"
            basis_items.append(f"20d basket avg return negative with only {pct} symbols above 20D MA")
        # Check macro stress via fear/greed (still via signal name search)
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
