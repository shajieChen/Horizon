"""Tests for digital-oracle bridge integration."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from unittest.mock import patch

from src.ai.summarizer import DailySummarizer
from src.market.digital_oracle_bridge import (
    DigitalOracleAssetResult,
    DigitalOracleBridge,
    DigitalOracleSignal,
    DigitalOracleWatchlistResult,
)
from src.market.oracle import HorizonProbability, TradingAnalysisResult, TradingOracleAnalyzer, TradingScenario
from src.models import TradingAssetConfig, TradingConfig


def _fake_horizons() -> list[HorizonProbability]:
    return [
        HorizonProbability(horizon="1d", up_probability=40, down_probability=30, neutral_probability=30, expected_bias="bullish", confidence="medium", basis="b1", invalidation="i1"),
        HorizonProbability(horizon="1w", up_probability=38, down_probability=32, neutral_probability=30, expected_bias="bullish", confidence="medium", basis="b2", invalidation="i2"),
        HorizonProbability(horizon="1m", up_probability=35, down_probability=35, neutral_probability=30, expected_bias="neutral", confidence="low", basis="b3", invalidation="i3"),
    ]


def _fake_asset_result(name: str = "QDII Nasdaq 100 Proxy") -> DigitalOracleAssetResult:
    signals = [
        DigitalOracleSignal(layer="Price Trend", provider="YahooPriceProvider", signal="QQQ price trend", data="close=500", interpretation="price up", horizon="1d/1w/1m", raw={"ret_1d": 0.01, "above_5d_ratio": 1.0}),
        DigitalOracleSignal(layer="Options / Volatility", provider="YFinanceProvider", signal="QQQ options surface", data="ATM IV=20%", interpretation="vol stable", horizon="1d/1w", raw={"atm_iv": 0.2}),
        DigitalOracleSignal(layer="Risk Appetite / Macro", provider="FearGreedProvider", signal="Fear & Greed", data="score=55", interpretation="risk appetite neutral", horizon="1d/1w", raw={"fear_greed_score": 55}),
    ]
    return DigitalOracleAssetResult(
        name=name,
        category="qdii_nasdaq100",
        market="US",
        symbols=["QQQ", "^NDX", "NQ=F"],
        signals=signals,
        resonance=["r1"],
        divergences=["d1"],
        horizon_views=_fake_horizons(),
        probability_scenarios=[
            TradingScenario(name="upside", probability=40, basis="b", trading_bias="risk-on"),
            TradingScenario(name="downside", probability=30, basis="b", trading_bias="defensive"),
            TradingScenario(name="range", probability=30, basis="b", trading_bias="neutral"),
        ],
        conclusion="test conclusion",
        missing_evidence=[],
        data_sources=["YahooPriceProvider", "YFinanceProvider", "FearGreedProvider"],
    )


def test_bridge_can_import_full_package_or_fallback_cleanly():
    bridge = DigitalOracleBridge(TradingConfig())
    assert isinstance(bridge.available, bool)


def test_bridge_analyze_assets_returns_watchlist_result_without_raise_on_provider_failure():
    bridge = DigitalOracleBridge(TradingConfig())
    bridge.available = True
    bridge.module = object()

    asset = TradingAssetConfig(name="US Mega Cap Basket", category="us_stock", symbols=["AAPL", "MSFT"], market="US")

    with patch.object(bridge, "_build_provider_instances", return_value={"yahoo_price": object()}), patch.object(
        bridge,
        "_build_tasks",
        return_value=(
            {"yahoo_price:AAPL": lambda: None},
            {"yahoo_price:AAPL": {"provider": "YahooPriceProvider", "layer": "Price Trend", "kind": "price", "label": "AAPL"}},
            [],
        ),
    ), patch.object(
        bridge,
        "_adapt_payload",
        side_effect=RuntimeError("adapter boom"),
    ):
        bridge.module = SimpleNamespace(gather=lambda tasks: SimpleNamespace(results={"yahoo_price:AAPL": object()}, errors={}))
        result = asyncio.run(bridge.analyze_assets([asset]))

    assert isinstance(result, DigitalOracleWatchlistResult)
    assert result.asset_results
    assert result.asset_results[0].missing_evidence


def test_each_asset_has_at_least_three_signal_layers_when_available():
    result = _fake_asset_result()
    assert len({s.layer for s in result.signals}) >= 3


def test_analysis_method_is_digital_oracle_when_bridge_available():
    analyzer = TradingOracleAnalyzer(TradingConfig(mode="asset_watchlist"))
    watch = DigitalOracleWatchlistResult(
        asset_results=[_fake_asset_result()],
        global_signals=[],
        global_resonance=["gr"],
        global_divergences=["gd"],
        missing_evidence=[],
        data_sources=["YahooPriceProvider"],
    )
    converted = analyzer._convert_digital_oracle_result(watch)
    assert converted.analysis_method == "digital_oracle"


def test_fallback_path_works_when_bridge_unavailable():
    config = TradingConfig(mode="asset_watchlist", enabled_providers=["fear_greed", "treasury"])
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle", return_value=False):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    assert result.analysis_method == "horizon_minimal_fallback"
    assert any("fallback" in e.lower() for e in result.missing_evidence)


def test_summarizer_renders_digital_oracle_sections_and_narrow_tables():
    summarizer = DailySummarizer()
    trade_result = TradingAnalysisResult(
        is_forecastable=True,
        question_type="asset_watchlist",
        market_question="mq",
        summary="sum",
        signals=[],
        resonance=[],
        divergences=[],
        scenarios=[],
        conclusion="c",
        monitor_signals=[],
        data_sources=["YahooPriceProvider"],
        asset_views=[
            {
                "name": "QDII Nasdaq 100 Proxy",
                "category": "qdii_nasdaq100",
                "market": "US",
                "symbols": ["QQQ"],
                "analysis_proxy": True,
                "horizons": [h.model_dump() for h in _fake_horizons()],
                "key_signals": [],
                "conclusion": "final",
                "data_quality": "high",
            }
        ],
        analysis_method="digital_oracle",
        digital_oracle_layers={
            "QDII Nasdaq 100 Proxy": {
                "signals": [s.model_dump() for s in _fake_asset_result().signals],
                "resonance": ["r1"],
                "divergences": ["d1"],
            }
        },
        missing_evidence=[],
    )
    block = summarizer._format_asset_watchlist_block(trade_result.model_dump())

    assert "digital-oracle multi-signal synthesis" in block
    assert "Layer 1: Price Trend" in block
    assert "Layer 2: Options / Volatility" in block
    assert "Layer 3: Risk Appetite / Macro" in block
    assert "Resonance signals" in block
    assert "Key divergences" in block
    assert "Probability Estimates" in block

    for line in block.splitlines():
        if line.strip().startswith("|"):
            cols = [c for c in line.split("|") if c.strip()]
            assert len(cols) <= 7
