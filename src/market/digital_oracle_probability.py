"""Probability synthesis for digital-oracle asset-watchlist signals."""

from __future__ import annotations

from typing import Iterable

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
    neutral_n = round(100.0 - up_n - down_n, 1)
    return up_n, down_n, neutral_n


def _avg(values: Iterable[float]) -> float | None:
    vals = list(values)
    if not vals:
        return None
    return sum(vals) / len(vals)


def _signal_raw_value(signals: list, layer: str, key: str) -> list[float]:
    out: list[float] = []
    for signal in signals:
        if getattr(signal, "layer", "") != layer:
            continue
        raw = getattr(signal, "raw", {}) or {}
        value = raw.get(key)
        if isinstance(value, (int, float)):
            out.append(float(value))
    return out


def _signal_raw_str(signals: list, layer: str, key: str) -> list[str]:
    out: list[str] = []
    for signal in signals:
        if getattr(signal, "layer", "") != layer:
            continue
        raw = getattr(signal, "raw", {}) or {}
        value = raw.get(key)
        if isinstance(value, str) and value.strip():
            out.append(value.strip())
    return out


def _build_probability(asset: TradingAssetConfig, signals: list, horizon: str):
    from .oracle import HorizonProbability

    up, down, neutral = 33.0, 33.0, 34.0
    basis: list[str] = []
    invalidation: list[str] = []

    ret_1d = _avg(_signal_raw_value(signals, "Price Trend", "ret_1d"))
    ret_5d = _avg(_signal_raw_value(signals, "Price Trend", "ret_5d"))
    ret_20d = _avg(_signal_raw_value(signals, "Price Trend", "ret_20d"))
    above_5d = _avg(_signal_raw_value(signals, "Price Trend", "above_5d_ratio"))
    above_20d = _avg(_signal_raw_value(signals, "Price Trend", "above_20d_ratio"))

    atm_iv = _avg(_signal_raw_value(signals, "Options / Volatility", "atm_iv"))
    implied_move = _avg(_signal_raw_value(signals, "Options / Volatility", "implied_move"))

    fg_rating = next(iter(_signal_raw_str(signals, "Risk Appetite / Macro", "fear_greed_rating")), "")
    fg_score = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "fear_greed_score"))

    y10 = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "yield_10y"))
    curve_10_2 = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "curve_10y_2y"))

    vix = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "vix"))
    move = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "move"))
    hy_oas = _avg(_signal_raw_value(signals, "Risk Appetite / Macro", "hy_oas"))

    iv_high = (atm_iv is not None and atm_iv >= 0.35) or (implied_move is not None and implied_move >= 0.03)
    stress_high = (vix is not None and vix >= 25) or (move is not None and move >= 120) or (hy_oas is not None and hy_oas >= 450)

    if horizon == "1d":
        if ret_1d is not None and ret_1d > 0 and (above_5d or 0) >= 0.5:
            up += 8
            basis.append("1日篮子收益与5日均线结构偏强")
        if iv_high:
            down += 4
            neutral += 4
            basis.append("短线隐含波动偏高，回撤与震荡风险上升")
        if fg_rating.lower() == "extreme greed":
            up += 3
            basis.append("恐贪处于极度贪婪，短线仍有顺势上行惯性")
        if fg_rating.lower() == "extreme fear":
            down += 5
            basis.append("恐贪处于极度恐惧，短线风险溢价抬升")
        if stress_high:
            down += 4
            basis.append("VIX/MOVE/HY OAS 指向风险偏好回落")
        invalidation.append("若多数成分股跌破5日均线且波动率继续抬升，短线偏多失效")

    elif horizon == "1w":
        if ret_5d is not None and ret_5d > 0 and (above_20d or 0) >= 0.5:
            up += 8
            basis.append("5日收益与20日均线结构支持1周偏多")
        if iv_high:
            neutral += 5
            basis.append("期权隐含波动较高，1周方向分歧增加")
        if curve_10_2 is not None and curve_10_2 < 0:
            down += 4
            basis.append("收益率曲线倒挂仍在，增长资产面临估值压力")
        if hy_oas is not None and hy_oas >= 400:
            down += 5
            basis.append("高收益利差走阔，信用风险偏好下降")
        invalidation.append("若1周内20日均线失守且信用利差继续走阔，偏多失效")

    else:  # 1m
        if ret_20d is not None and ret_20d > 0 and (above_20d or 0) >= 0.5:
            up += 10
            basis.append("20日趋势维持上行，1月窗口偏多")
        if y10 is not None and y10 >= 4.6 and asset.market in {"US", "JP", "HK"}:
            down += 5
            basis.append("长端美债收益率偏高，对成长风格估值形成压制")
        if iv_high:
            down += 5
            basis.append("期权市场仍在计入较高下行尾部风险")
        if (fg_score is not None and fg_score >= 55) and not stress_high:
            up += 5
            basis.append("风险偏好仍可控且波动未失控，中期上行概率提高")
        invalidation.append("若月内趋势反转并伴随波动与信用利差恶化，偏多失效")

    up, down, neutral = _clamp(up), _clamp(down), _clamp(neutral)
    up_n, down_n, neutral_n = _normalize(up, down, neutral)

    if up_n > down_n and up_n > neutral_n:
        bias = "bullish"
    elif down_n > up_n and down_n > neutral_n:
        bias = "bearish"
    else:
        bias = "neutral"

    layer_count = len({getattr(s, "layer", "") for s in signals})
    conflict = iv_high and ret_1d is not None and ret_1d > 0 and stress_high
    confidence = "high" if layer_count >= 3 else "medium"
    if conflict:
        confidence = "low"

    return HorizonProbability(
        horizon=horizon,
        up_probability=up_n,
        down_probability=down_n,
        neutral_probability=neutral_n,
        expected_bias=bias,
        confidence=confidence,
        basis="；".join(basis) if basis else "有效交易信号不足，使用保守基准分布。",
        invalidation="；".join(invalidation) if invalidation else "信号不足，等待更多市场数据确认。",
    )


def estimate_digital_oracle_probabilities(asset: TradingAssetConfig, signals: list):
    """Return 1D/1W/1M probabilities from digital-oracle normalized signals."""

    return [
        _build_probability(asset, signals, "1d"),
        _build_probability(asset, signals, "1w"),
        _build_probability(asset, signals, "1m"),
    ]
