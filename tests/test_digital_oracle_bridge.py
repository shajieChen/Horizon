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
    TradingReference,
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


def _fake_reference(
    url: str = "https://example.com/vix",
    query: str = "VIX current level",
    asset: str = "QDII Nasdaq 100 Proxy",
) -> TradingReference:
    return TradingReference(
        title="VIX current level",
        url=url,
        snippet="VIX latest market data",
        provider="WebSearchProvider",
        query=query,
        asset=asset,
        layer="Risk Appetite / Macro",
        fetched_at="2026-05-12T00:00:00+00:00",
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


def test_trading_reference_serializes():
    ref = _fake_reference()
    dumped = ref.model_dump()

    assert dumped["title"] == "VIX current level"
    assert dumped["url"] == "https://example.com/vix"
    assert dumped["provider"] == "WebSearchProvider"


def test_adapt_web_signal_extracts_references_from_snippets():
    bridge = DigitalOracleBridge(TradingConfig())
    asset = TradingAssetConfig(
        name="QDII Nasdaq 100 Proxy",
        category="qdii_nasdaq100",
        symbols=["QQQ"],
        market="US",
    )
    result = SimpleNamespace(
        query="VIX current level",
        fetched_at="2026-05-12T00:00:00+00:00",
        snippets=(
            SimpleNamespace(title="VIX Index Current Level", url="https://example.com/vix", snippet="VIX is 18.5."),
            SimpleNamespace(title="", url="", snippet="skip me"),
        ),
        text=lambda: "VIX is 18.5",
    )
    signal = bridge._adapt_web_signal(
        asset,
        {"provider": "WebSearchProvider", "layer": "Risk Appetite / Macro", "kind": "web", "label": "VIX current level"},
        result,
    )

    assert signal.references
    assert signal.references[0].title == "VIX Index Current Level"
    assert signal.references[0].url == "https://example.com/vix"
    assert signal.references[0].query == "VIX current level"
    assert signal.references[0].asset == "QDII Nasdaq 100 Proxy"
    assert signal.raw["vix"] == 18.5


def test_analyze_asset_aggregates_signal_references():
    bridge = DigitalOracleBridge(TradingConfig())
    bridge.available = True
    ref = _fake_reference()
    asset = TradingAssetConfig(name="QDII Nasdaq 100 Proxy", category="qdii_nasdaq100", symbols=["QQQ"], market="US")
    signal = DigitalOracleSignal(
        layer="Risk Appetite / Macro",
        provider="WebSearchProvider",
        signal="Web metric: VIX current level",
        data="VIX current level => 18.5",
        interpretation="market data",
        horizon="1d/1w",
        references=[ref],
    )

    with patch.object(bridge, "_build_provider_instances", return_value={"web_search": object()}), patch.object(
        bridge,
        "_build_tasks",
        return_value=(
            {"web_search:VIX current level": lambda: None},
            {
                "web_search:VIX current level": {
                    "provider": "WebSearchProvider",
                    "layer": "Risk Appetite / Macro",
                    "kind": "web",
                    "label": "VIX current level",
                }
            },
            [],
        ),
    ), patch.object(bridge, "_adapt_payload", return_value=[signal]):
        bridge.module = SimpleNamespace(gather=lambda tasks: SimpleNamespace(results={"web_search:VIX current level": object()}, errors={}))
        result = asyncio.run(bridge.analyze_asset(asset))

    assert result.references == [ref]


def test_analyze_assets_aggregates_and_dedupes_references():
    bridge = DigitalOracleBridge(TradingConfig())
    ref = _fake_reference(url="https://example.com/vix")
    duplicate = _fake_reference(url="https://example.com/vix")
    asset_a = _fake_asset_result("Asset A")
    asset_b = _fake_asset_result("Asset B")
    asset_a.references = [ref]
    asset_b.references = [duplicate, _fake_reference(url="https://example.com/move", query="MOVE index current level", asset="Asset B")]
    configs = [
        TradingAssetConfig(name="Asset A", category="us_stock", symbols=["AAPL"], market="US"),
        TradingAssetConfig(name="Asset B", category="us_stock", symbols=["MSFT"], market="US"),
    ]

    async def fake_analyze_asset(asset):
        return asset_a if asset.name == "Asset A" else asset_b

    with patch.object(bridge, "analyze_asset", side_effect=fake_analyze_asset):
        result = asyncio.run(bridge.analyze_assets(configs))

    assert [ref.url for ref in result.references] == ["https://example.com/vix", "https://example.com/move"]


def test_dedupe_references_skips_empty_url_and_duplicates():
    bridge = DigitalOracleBridge(TradingConfig())
    refs = [
        _fake_reference(url=""),
        _fake_reference(url="https://example.com/vix"),
        _fake_reference(url="https://example.com/vix"),
    ]

    deduped = bridge._dedupe_references(refs)

    assert len(deduped) == 1
    assert deduped[0].url == "https://example.com/vix"


def test_convert_digital_oracle_result_includes_references():
    analyzer = TradingOracleAnalyzer(TradingConfig(mode="asset_watchlist"))
    asset = _fake_asset_result()
    asset.references = [_fake_reference()]
    watch = DigitalOracleWatchlistResult(
        asset_results=[asset],
        global_signals=[],
        global_resonance=["gr"],
        global_divergences=["gd"],
        missing_evidence=[],
        data_sources=["YahooPriceProvider", "WebSearchProvider"],
        references=[_fake_reference()],
    )

    converted = analyzer._convert_digital_oracle_result(watch)

    assert converted.references[0]["url"] == "https://example.com/vix"
    assert converted.digital_oracle_layers[asset.name]["references"][0]["url"] == "https://example.com/vix"


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
        references=[_fake_reference().model_dump()],
    )
    block = summarizer._format_asset_watchlist_block(trade_result.model_dump())

    assert "digital-oracle multi-signal synthesis" in block
    assert "Layer 1: Price Trend" in block
    assert "Layer 2: Options / Volatility" in block
    assert "Layer 3: Risk Appetite / Macro" in block
    assert "Resonance signals" in block
    assert "Key divergences" in block
    assert "Probability Estimates" in block
    assert "可追溯性：结构化 provider 数据 + WebSearch 市场数据引用" in block
    assert "### Trading 分析参考文章" in block
    assert "- [VIX current level](https://example.com/vix)" in block

    for line in block.splitlines():
        if line.strip().startswith("|"):
            cols = [c for c in line.split("|") if c.strip()]
            assert len(cols) <= 7


def test_summarizer_trading_references_skip_empty_url_and_use_bullets():
    summarizer = DailySummarizer()
    rendered = summarizer._format_trading_references(
        [
            {"title": "No URL", "url": "", "snippet": "skip"},
            _fake_reference().model_dump(),
        ]
    )

    assert "No URL" not in rendered
    assert "- [VIX current level](https://example.com/vix)" in rendered
    assert "| Title |" not in rendered


def test_summarizer_empty_trading_references_does_not_raise():
    summarizer = DailySummarizer()
    rendered = summarizer._format_trading_references([])

    assert "暂无可追溯 Web 引用" in rendered
