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


def _extract_numeric_metadata_values(signals: "List[MarketSignal]", key: str) -> List[float]:
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


def _format_ratio(ratio: float) -> str:
    """Format a ratio as a percentage string, or '?' if ratio is negative (unknown)."""
    return f"{ratio:.0%}" if ratio >= 0 else "?"


def _format_pct(value: "str | float") -> str:
    """Format a decimal return value as a signed percentage string."""
    try:
        return f"{float(value) * 100:+.2f}%"
    except (TypeError, ValueError):
        return "N/A"


def _valid_price_signals(signals: "List[MarketSignal]") -> "List[MarketSignal]":
    """Return price signals that have a numeric value and a usable 1d_return metadata."""
    return [
        s for s in signals
        if s.layer == "price"
        and s.value not in ("", "N/A")
        and (getattr(s, "metadata", {}) or {}).get("1d_return") not in (None, "", "N/A", "unknown")
    ]


def _symbol_return_summary(signals: "List[MarketSignal]", key: str, limit: int = 5) -> str:
    """Return a semicolon-joined list of 'SYMBOL +X.XX%' strings for up to *limit* symbols."""
    rows = []
    for s in _valid_price_signals(signals):
        meta = getattr(s, "metadata", {}) or {}
        symbol = meta.get("symbol") or s.signal.replace(" price", "")
        raw = meta.get(key)
        if raw in (None, "", "N/A", "unknown"):
            continue
        rows.append(f"{symbol} {_format_pct(raw)}")
    return "；".join(rows[:limit])


def _ratio_count(
    signals: "List[MarketSignal]", key: str, expected: str = "true"
) -> "tuple[int, int, float]":
    """Return (matched, total, ratio) for *key* among valid price signals."""
    total = 0
    matched = 0
    for s in _valid_price_signals(signals):
        meta = getattr(s, "metadata", {}) or {}
        raw = meta.get(key)
        if raw in (None, "", "N/A", "unknown"):
            continue
        total += 1
        if str(raw).lower() == expected:
            matched += 1
    ratio = matched / total if total else 0.0
    return matched, total, ratio


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

    # Determine high-volatility regime: true if any single symbol is "high",
    # or if 30% or more of symbols are "high".
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

    if horizon == "1d":
        matched_5, total_5, r5 = _ratio_count(price_signals, "above_5d_ma")
        avg_1d = _average_metadata(price_signals, "1d_return")
        summary = _symbol_return_summary(price_signals, "1d_return")
        suffix = f"样本：{summary}。" if summary else ""
        if _positive(avg_1d) and r5 >= 0.5:
            up += 10
            basis_items.append(
                f"1日篮子平均涨幅 {_format_pct(avg_1d)}，"
                f"{matched_5}/{total_5} 个品种位于 5日均线上方，短线动量偏多。{suffix}"
            )
        elif _negative(avg_1d) and 0.0 <= r5 < 0.5:
            down += 10
            basis_items.append(
                f"1日篮子平均跌幅 {_format_pct(avg_1d)}，"
                f"仅 {matched_5}/{total_5} 个品种位于 5日均线上方，短线动量偏弱。{suffix}"
            )
        if high_vol:
            neutral += 5
            down += 3
            basis_items.append("elevated realized volatility increases uncertainty")
        invalidation_items.append("price reclaims / loses 5D MA intraday")

    elif horizon == "1w":
        matched_20, total_20, r20 = _ratio_count(price_signals, "above_20d_ma")
        avg_5d = _average_metadata(price_signals, "5d_return")
        summary = _symbol_return_summary(price_signals, "5d_return")
        suffix = f"样本：{summary}。" if summary else ""
        if _positive(avg_5d) and r20 >= 0.5:
            up += 10
            basis_items.append(
                f"1周篮子平均涨幅 {_format_pct(avg_5d)}，"
                f"{matched_20}/{total_20} 个品种位于 20日均线上方，中短期趋势偏多。{suffix}"
            )
        elif _negative(avg_5d) and 0.0 <= r20 < 0.5:
            down += 10
            basis_items.append(
                f"1周篮子平均跌幅 {_format_pct(avg_5d)}，"
                f"仅 {matched_20}/{total_20} 个品种位于 20日均线上方，中短期趋势偏弱。{suffix}"
            )
        if high_vol:
            neutral += 5
            basis_items.append("high volatility reduces trend conviction over 1W")
        invalidation_items.append("weekly close outside 20D MA band")

    elif horizon == "1m":
        matched_20, total_20, r20 = _ratio_count(price_signals, "above_20d_ma")
        avg_20d = _average_metadata(price_signals, "20d_return")
        summary = _symbol_return_summary(price_signals, "20d_return")
        suffix = f"样本：{summary}。" if summary else ""
        if _positive(avg_20d) and r20 >= 0.5:
            up += 15
            basis_items.append(
                f"1月篮子平均涨幅 {_format_pct(avg_20d)}，"
                f"{matched_20}/{total_20} 个品种位于 20日均线上方，中期趋势偏多。{suffix}"
            )
        elif _negative(avg_20d) and 0.0 <= r20 < 0.5:
            down += 15
            basis_items.append(
                f"1月篮子平均跌幅 {_format_pct(avg_20d)}，"
                f"仅 {matched_20}/{total_20} 个品种位于 20日均线上方，中期趋势偏弱。{suffix}"
            )
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

    basis = "; ".join(basis_items) if basis_items else "价格数据不足：未获取到有效 yfinance 价格历史，使用保守基准分布。（insufficient price data — conservative base distribution used）"
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
