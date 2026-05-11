"""Tests for market analysis plugin integration."""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.market.oracle import TradingOracleAnalyzer
from src.market.router import TradingQuestionRouter
from src.market.report import trading_result_to_forecast
from src.market.universe import get_enabled_assets, is_supported_asset_category
from src.models import (
    AIConfig,
    AIProvider,
    Config,
    ContentItem,
    FilteringConfig,
    SourceType,
    SourcesConfig,
    TradingAssetConfig,
    TradingConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def _make_item(title: str, score: float = 8.0) -> ContentItem:
    item = ContentItem(
        id=f"rss:{title}",
        source_type=SourceType.RSS,
        title=title,
        url="https://example.com/item",
        content=title,
        published_at=datetime(2026, 5, 11, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = score
    item.ai_summary = title
    return item


def _make_config(trading: TradingConfig | None = None) -> Config:
    return Config(
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="OPENAI_API_KEY"),
        sources=SourcesConfig(),
        filtering=FilteringConfig(ai_score_threshold=7.0, time_window_hours=24),
        trading=trading or TradingConfig(),
    )


# ─── Model defaults ────────────────────────────────────────────────────────────

def test_trading_config_default_enabled():
    """TradingConfig.enabled defaults to True."""
    config = TradingConfig()
    assert config.enabled is True


def test_trading_config_default_mode_is_asset_watchlist():
    config = TradingConfig()
    assert config.mode == "asset_watchlist"


def test_config_auto_creates_default_trading_config():
    """Config auto-creates a TradingConfig even when the trading field is omitted."""
    config = Config(
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="OPENAI_API_KEY"),
        sources=SourcesConfig(),
        filtering=FilteringConfig(),
    )
    assert config.trading is not None
    assert config.trading.enabled is True


def test_trading_config_has_default_watch_assets():
    config = TradingConfig()
    assert len(config.watch_assets) >= 3
    categories = {a.category for a in config.watch_assets}
    assert "qdii_nasdaq100" in categories
    assert "us_stock" in categories


# ─── Universe helpers ──────────────────────────────────────────────────────────

def test_get_enabled_assets_filters_scope():
    config = TradingConfig(
        asset_scope=["us_stock"],
        watch_assets=[
            TradingAssetConfig(name="US", category="us_stock", symbols=["AAPL"]),
            TradingAssetConfig(name="JP", category="japan_stock", symbols=["7203.T"]),
        ],
    )
    assets = get_enabled_assets(config)
    assert len(assets) == 1
    assert assets[0].name == "US"


def test_get_enabled_assets_skips_empty_symbols():
    config = TradingConfig(
        watch_assets=[
            TradingAssetConfig(name="Empty", category="us_stock", symbols=[]),
        ]
    )
    assets = get_enabled_assets(config)
    assert not any(a.name == "Empty" for a in assets)


def test_is_supported_asset_category():
    assert is_supported_asset_category("qdii_nasdaq100") is True
    assert is_supported_asset_category("us_stock") is True
    assert is_supported_asset_category("crypto") is False
    assert is_supported_asset_category("commodity_risk") is False


# ─── Router ────────────────────────────────────────────────────────────────────

def test_route_asset_watchlist_returns_correct_question_type():
    trading = TradingConfig(mode="asset_watchlist")
    router = TradingQuestionRouter(trading)
    route = router.route(_make_item("anything"))
    assert route.question_type == "asset_watchlist"
    assert route.enabled is True
    assert route.horizon == "1d_1w_1m"


def test_route_asset_watchlist_collects_all_symbols():
    trading = TradingConfig(
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(name="US", category="us_stock", symbols=["AAPL", "MSFT"]),
            TradingAssetConfig(name="HK", category="hongkong_stock", symbols=["0700.HK"]),
        ],
    )
    router = TradingQuestionRouter(trading)
    route = router.route_asset_watchlist()
    assert "AAPL" in route.symbols
    assert "0700.HK" in route.symbols


def test_router_recognizes_multiple_question_types():
    trading = TradingConfig(
        enabled=True,
        mode="event_driven",
        min_ai_score=0.0,
        watch_keywords=["fed", "bitcoin", "nvda", "taiwan"],
    )
    router = TradingQuestionRouter(trading)

    assert router.route(_make_item("Fed signals inflation and Treasury yield curve")).question_type == "macro_rates"
    assert router.route(_make_item("Bitcoin and Ethereum options surge on Deribit")).question_type == "crypto_cycle"
    assert router.route(_make_item("NVDA options activity rises before earnings")).question_type == "equity_options"
    assert router.route(_make_item("War risk around Taiwan raises oil shock fears")).question_type == "geopolitical_risk"


# ─── Orchestrator ─────────────────────────────────────────────────────────────

def test_orchestrator_skips_market_analysis_when_disabled(tmp_path: Path):
    config = _make_config(TradingConfig(enabled=False, watch_keywords=["fed"]))
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    item = _make_item("Fed rate cut signal")

    asyncio.run(orchestrator._forecast_important_items([item]))
    assert "trading_analysis" not in item.metadata
    assert "forecast" not in item.metadata


def test_orchestrator_asset_watchlist_generates_synthetic_item_even_when_items_empty(tmp_path: Path):
    """In asset_watchlist mode, a synthetic trading item is generated even when items is empty."""
    config = _make_config(TradingConfig(enabled=True, mode="asset_watchlist"))
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    items: list = []

    asyncio.run(orchestrator._forecast_important_items(items))
    # The synthetic item should have been inserted at position 0
    assert len(items) == 1
    assert "trading_analysis" in items[0].metadata
    assert items[0].metadata["trading_analysis"]["question_type"] == "asset_watchlist"


def test_orchestrator_skips_items_below_min_ai_score(tmp_path: Path):
    config = _make_config(
        TradingConfig(enabled=True, mode="event_driven", min_ai_score=8.5, watch_keywords=["fed"])
    )
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    item = _make_item("Fed rate cut signal", score=8.0)

    asyncio.run(orchestrator._forecast_important_items([item]))
    assert "trading_analysis" not in item.metadata
    assert "forecast" not in item.metadata


# ─── Oracle ───────────────────────────────────────────────────────────────────

def test_analyze_asset_watchlist_outputs_all_three_horizons():
    config = TradingConfig(enabled=True, mode="asset_watchlist")
    analyzer = TradingOracleAnalyzer(config)

    result = asyncio.run(analyzer.analyze_asset_watchlist())
    assert result is not None
    assert result.question_type == "asset_watchlist"
    assert len(result.asset_views) > 0

    for av in result.asset_views:
        horizons = {h.horizon for h in av.horizons}
        assert "1d" in horizons
        assert "1w" in horizons
        assert "1m" in horizons


def test_horizon_probabilities_sum_to_100():
    config = TradingConfig(enabled=True, mode="asset_watchlist")
    analyzer = TradingOracleAnalyzer(config)

    result = asyncio.run(analyzer.analyze_asset_watchlist())
    assert result is not None
    for av in result.asset_views:
        for hp in av.horizons:
            total = hp.up_probability + hp.down_probability + hp.neutral_probability
            assert abs(total - 100.0) < 0.2, (
                f"{av.name} {hp.horizon}: probabilities sum to {total} (expected 100.0)"
            )


def test_analyzer_tolerates_provider_failures_without_raise():
    config = TradingConfig(
        enabled=True,
        mode="event_driven",
        min_ai_score=0.0,
        watch_keywords=["nvda", "earnings", "options"],
        enabled_providers=["yfinance", "edgar", "fear_greed", "yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)
    item = _make_item("NVDA options and earnings setup")

    result = asyncio.run(analyzer.analyze(item))
    assert result is not None
    assert result.question_type == "equity_options"
    assert result.errors


def test_yfinance_not_installed_does_not_raise():
    """YFinanceProvider must not crash when yfinance is not installed (simulated)."""
    from src.vendor.digital_oracle.providers import YFinanceProvider, ProviderCallContext

    item = _make_item("test")
    ctx = ProviderCallContext(item=item, question_type="asset_watchlist", symbols=["AAPL"])

    # Patch sys.modules to simulate missing yfinance
    import sys
    original = sys.modules.get("yfinance", None)
    sys.modules["yfinance"] = None  # type: ignore[assignment]
    try:
        provider = YFinanceProvider()
        results = provider.fetch(ctx)
        # Should return a fallback signal, not raise
        assert isinstance(results, list)
        assert len(results) > 0
    finally:
        if original is None:
            sys.modules.pop("yfinance", None)
        else:
            sys.modules["yfinance"] = original


def test_asset_watchlist_tolerates_individual_symbol_failure(tmp_path: Path):
    """A bad symbol should not abort the entire watchlist analysis."""
    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(
                name="Invalid Symbol Test",
                category="us_stock",
                symbols=["INVALID_SYMBOL_XYZ"],
            ),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)
    result = asyncio.run(analyzer.analyze_asset_watchlist())
    assert result is not None
    assert len(result.asset_views) == 1


def test_orchestrator_writes_trading_analysis_and_forecast(tmp_path: Path):
    trading = TradingConfig(
        enabled=True,
        mode="event_driven",
        min_ai_score=0.0,
        watch_keywords=["fed", "inflation"],
    )
    config = _make_config(trading)
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    item = _make_item("Fed inflation and Treasury path repricing", score=9.0)

    asyncio.run(orchestrator._forecast_important_items([item]))

    assert "trading_analysis" in item.metadata
    assert "forecast" in item.metadata
    forecast = item.metadata["forecast"]
    assert forecast["is_forecastable"] is True
    assert "event_type" in forecast


def test_trading_report_conversion_has_required_fields():
    config = TradingConfig(
        enabled=True,
        mode="event_driven",
        min_ai_score=0.0,
        watch_keywords=["bitcoin"],
    )
    analyzer = TradingOracleAnalyzer(config)
    item = _make_item("Bitcoin cycle risk check", score=9.0)

    result = asyncio.run(analyzer.analyze(item))
    assert result is not None
    forecast = trading_result_to_forecast(result)

    assert forecast["is_forecastable"] is True
    assert "cause_chain" in forecast
    assert "scenarios" in forecast
    assert "confidence" in forecast


# ─── Summarizer ───────────────────────────────────────────────────────────────

def test_summarizer_renders_asset_views():
    from src.ai.summarizer import DailySummarizer

    summarizer = DailySummarizer()

    trading_analysis = {
        "question_type": "asset_watchlist",
        "asset_views": [
            {
                "name": "QDII Nasdaq 100 Proxy",
                "category": "qdii_nasdaq100",
                "market": "US",
                "symbols": ["QQQ", "^NDX"],
                "analysis_proxy": True,
                "note": "Proxy for QDII.",
                "horizons": [
                    {
                        "horizon": "1d",
                        "up_probability": 40.0,
                        "down_probability": 35.0,
                        "neutral_probability": 25.0,
                        "expected_bias": "bullish",
                        "confidence": "low",
                        "basis": "price above 5D MA",
                        "invalidation": "loses 5D MA",
                    }
                ],
                "key_signals": [],
                "conclusion": "Slight bullish bias.",
                "data_quality": "low",
            }
        ],
        "errors": [],
        "data_sources": ["YahooPriceProvider"],
    }

    block = summarizer._format_trading_analysis_block(trading_analysis)
    assert "QDII Nasdaq 100 Proxy" in block
    assert "免责声明" in block
    assert "1日" in block
    assert "bullish" in block


def test_summarizer_event_driven_block_still_works():
    """Legacy event_driven trading analysis still renders without errors."""
    from src.ai.summarizer import DailySummarizer

    summarizer = DailySummarizer()
    trading_analysis = {
        "question_type": "macro_rates",
        "market_question": "How will markets react to Fed?",
        "signals": [],
        "resonance": ["rates and equity aligned"],
        "divergences": ["credit spread divergence"],
        "scenarios": [
            {"name": "baseline", "probability": 50, "trading_bias": "hold"},
        ],
        "monitor_signals": [],
        "errors": [],
        "data_sources": ["FearGreedProvider"],
    }
    block = summarizer._format_trading_analysis_block(trading_analysis)
    assert "macro_rates" in block
    assert "Market Question" in block or "市场问题" in block


# ─── New metadata / basket tests ──────────────────────────────────────────────

def test_market_signal_stores_metadata():
    """MarketSignal must accept and store arbitrary metadata fields."""
    from src.market.oracle import MarketSignal

    sig = MarketSignal(
        layer="price",
        signal="QQQ price",
        value="450.00",
        horizon="1d",
        interpretation="test",
        source="YahooPriceProvider",
        metadata={"1d_return": "0.012", "5d_return": "-0.005", "above_5d_ma": "true"},
    )
    assert sig.metadata["1d_return"] == "0.012"
    assert sig.metadata["above_5d_ma"] == "true"


def test_oracle_preserves_price_metadata_in_analyze_asset_watchlist():
    """analyze_asset_watchlist must propagate 1d_return etc. into MarketSignal.metadata."""
    from src.market.oracle import TradingOracleAnalyzer
    from src.models import TradingConfig, TradingAssetConfig
    from unittest.mock import patch, MagicMock

    fake_payload = {
        "signal": "QQQ price",
        "value": "450.00",
        "horizon": "1d",
        "interpretation": "test",
        "source": "YahooPriceProvider",
        "1d_return": "0.0120",
        "5d_return": "0.0250",
        "20d_return": "0.0500",
        "above_5d_ma": "true",
        "above_20d_ma": "true",
        "volatility_regime": "low",
    }

    mock_provider = MagicMock()
    mock_provider.layer = "price"
    mock_provider.fetch.return_value = [fake_payload]

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(name="Test Basket", category="us_stock", symbols=["QQQ"]),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.oracle.get_provider_by_name", return_value=mock_provider), patch(
        "src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle",
        return_value=False,
    ):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    price_signals = [s for s in result.signals if s.layer == "price"]
    assert len(price_signals) > 0
    sig = price_signals[0]
    assert sig.metadata.get("1d_return") == "0.0120"
    assert sig.metadata.get("above_5d_ma") == "true"


def test_probability_reads_metadata_values():
    """estimate_horizon_probability must read price metrics from metadata, not signal name."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    sig = MarketSignal(
        layer="price",
        signal="QQQ price",
        value="450.00",
        horizon="1d",
        interpretation="test",
        source="YahooPriceProvider",
        metadata={
            "1d_return": "0.012",
            "5d_return": "0.025",
            "20d_return": "0.050",
            "above_5d_ma": "true",
            "above_20d_ma": "true",
            "volatility_regime": "low",
        },
    )
    asset = TradingAssetConfig(name="Test", category="us_stock", symbols=["QQQ"])

    hp_1d = estimate_horizon_probability(asset, [sig], "1d")
    assert "insufficient price data" not in hp_1d.basis
    assert "篮子" in hp_1d.basis or "均线" in hp_1d.basis

    hp_1w = estimate_horizon_probability(asset, [sig], "1w")
    assert "insufficient price data" not in hp_1w.basis

    hp_1m = estimate_horizon_probability(asset, [sig], "1m")
    assert "insufficient price data" not in hp_1m.basis


def test_basket_aggregation_averages_returns():
    """Multi-symbol basket return and MA ratio should be averaged across symbols."""
    from src.market.oracle import MarketSignal
    from src.market.probability import _average_metadata, _ratio_metadata

    signals = [
        MarketSignal(
            layer="price", signal="AAPL price", value="180.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={"1d_return": "0.02", "above_5d_ma": "true"},
        ),
        MarketSignal(
            layer="price", signal="MSFT price", value="380.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={"1d_return": "-0.01", "above_5d_ma": "false"},
        ),
        MarketSignal(
            layer="price", signal="NVDA price", value="800.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={"1d_return": "0.03", "above_5d_ma": "true"},
        ),
    ]

    avg_ret = float(_average_metadata(signals, "1d_return"))
    assert abs(avg_ret - (0.02 - 0.01 + 0.03) / 3) < 1e-9

    ratio = float(_ratio_metadata(signals, "above_5d_ma", "true"))
    assert abs(ratio - 2 / 3) < 1e-9


def test_basis_not_conservative_when_price_data_present():
    """When valid price data is available, basis must not say 'insufficient price data'."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    signals = [
        MarketSignal(
            layer="price", signal="QQQ price", value="450.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={
                "1d_return": "0.015",
                "5d_return": "0.030",
                "20d_return": "0.060",
                "above_5d_ma": "true",
                "above_20d_ma": "true",
                "volatility_regime": "low",
            },
        ),
    ]
    asset = TradingAssetConfig(name="QQQ", category="qdii_nasdaq100", symbols=["QQQ"])

    for hz in ("1d", "1w", "1m"):
        hp = estimate_horizon_probability(asset, signals, hz)
        assert "insufficient price data" not in hp.basis, (
            f"horizon={hz}: got conservative basis: {hp.basis!r}"
        )


def test_conservative_basis_only_when_all_data_missing():
    """When all price data is N/A/unknown, conservative base distribution with bilingual message is used."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    signals = [
        MarketSignal(
            layer="price", signal="QQQ price", value="N/A", horizon="1d",
            interpretation="Price unavailable", source="YahooPriceProvider",
            metadata={
                "1d_return": "N/A",
                "5d_return": "N/A",
                "20d_return": "N/A",
                "above_5d_ma": "unknown",
                "above_20d_ma": "unknown",
                "volatility_regime": "unknown",
            },
        ),
    ]
    asset = TradingAssetConfig(name="QQQ", category="qdii_nasdaq100", symbols=["QQQ"])

    for hz in ("1d", "1w", "1m"):
        hp = estimate_horizon_probability(asset, signals, hz)
        assert "conservative base distribution" in hp.basis
        assert "价格数据不足" in hp.basis


def test_yahoo_price_provider_fallback_uses_na_not_zero():
    """YahooPriceProvider exception fallback must use N/A, not 0, for returns."""
    from src.vendor.digital_oracle.providers import YahooPriceProvider

    with patch_yfinance_to_fail():
        result = YahooPriceProvider._fetch_symbol_price("FAIL_SYM")
    assert result["1d_return"] == "N/A"
    assert result["5d_return"] == "N/A"
    assert result["20d_return"] == "N/A"


def test_yfinance_unavailable_does_not_crash_watchlist():
    """When yfinance is not importable, analysis still runs without raising."""
    from src.market.oracle import TradingOracleAnalyzer
    from src.models import TradingConfig, TradingAssetConfig

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(name="Test", category="us_stock", symbols=["AAPL"]),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch_yfinance_to_fail():
        result = asyncio.run(analyzer.analyze_asset_watchlist())
    assert result is not None
    assert len(result.asset_views) >= 1


# Helper context manager for the fallback test
class patch_yfinance_to_fail:
    def __enter__(self):
        import sys
        self._orig = sys.modules.get("yfinance", None)
        sys.modules["yfinance"] = None  # type: ignore[assignment]
        return self

    def __exit__(self, *args):
        import sys
        if self._orig is None:
            sys.modules.pop("yfinance", None)
        else:
            sys.modules["yfinance"] = self._orig


# ─── New tests for yfinance fix and data quality ──────────────────────────────

def test_workflow_installs_trading_extra():
    """daily-summary.yml must use 'uv sync --extra trading' to install yfinance."""
    import re
    from pathlib import Path

    wf = Path(__file__).parent.parent / ".github" / "workflows" / "daily-summary.yml"
    content = wf.read_text()
    assert "uv sync --extra trading" in content, (
        "Workflow must install yfinance via 'uv sync --extra trading'"
    )


def test_only_na_price_signals_gives_low_data_quality():
    """data_quality must be 'low' when all price signals have value=N/A."""
    from src.market.oracle import TradingOracleAnalyzer
    from src.models import TradingConfig, TradingAssetConfig
    from unittest.mock import patch, MagicMock

    na_payload = {
        "signal": "QQQ price",
        "value": "N/A",
        "horizon": "1d",
        "interpretation": "Price data unavailable for QQQ: import error",
        "source": "YahooPriceProvider",
        "1d_return": "N/A",
        "5d_return": "N/A",
        "20d_return": "N/A",
        "above_5d_ma": "unknown",
        "above_20d_ma": "unknown",
        "volatility_regime": "unknown",
    }

    mock_provider = MagicMock()
    mock_provider.layer = "price"
    mock_provider.fetch.return_value = [na_payload]

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(name="Test Basket", category="us_stock", symbols=["QQQ"]),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.oracle.get_provider_by_name", return_value=mock_provider), patch(
        "src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle",
        return_value=False,
    ):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    av = result.asset_views[0]
    assert av.data_quality == "low"

    # probability basis must include the bilingual fallback text
    for hp in av.horizons:
        assert "价格数据不足" in hp.basis, f"Expected 价格数据不足 in basis, got: {hp.basis!r}"

    # conclusion must mention no valid price data
    assert "No valid price data" in av.conclusion, (
        f"Expected 'No valid price data' in conclusion, got: {av.conclusion!r}"
    )

    # errors must include the missing price data message
    price_errors = [e for e in result.errors if "no valid yfinance price signals" in e]
    assert price_errors, "Expected a missing-price-data error in result.errors"


def test_valid_price_signal_raises_data_quality_to_at_least_medium():
    """data_quality must be at least 'medium' when a valid price signal with 1d_return exists."""
    from src.market.oracle import TradingOracleAnalyzer
    from src.models import TradingConfig, TradingAssetConfig
    from unittest.mock import patch, MagicMock

    valid_payload = {
        "signal": "QQQ price",
        "value": "450.00",
        "horizon": "1d",
        "interpretation": "1d=+1.20% above_5D_MA=true",
        "source": "YahooPriceProvider",
        "1d_return": "0.0120",
        "5d_return": "0.0250",
        "20d_return": "0.0500",
        "above_5d_ma": "true",
        "above_20d_ma": "true",
        "volatility_regime": "low",
    }

    mock_provider = MagicMock()
    mock_provider.layer = "price"
    mock_provider.fetch.return_value = [valid_payload]

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(name="Test Basket", category="us_stock", symbols=["QQQ"]),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.oracle.get_provider_by_name", return_value=mock_provider), patch(
        "src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle",
        return_value=False,
    ):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    av = result.asset_views[0]
    assert av.data_quality in ("medium", "high"), (
        f"Expected 'medium' or 'high' data_quality, got: {av.data_quality!r}"
    )
    # basis must not be the conservative fallback
    for hp in av.horizons:
        assert "价格数据不足" not in hp.basis, (
            f"Expected real basis when valid data present, got: {hp.basis!r}"
        )


def test_three_valid_price_signals_give_high_data_quality():
    """data_quality must be 'high' when 3+ valid price signals with 1d_return exist."""
    from src.market.oracle import TradingOracleAnalyzer
    from src.models import TradingConfig, TradingAssetConfig
    from unittest.mock import patch, MagicMock

    def make_payload(sym: str, ret: str) -> dict:
        return {
            "signal": f"{sym} price",
            "value": "100.00",
            "horizon": "1d",
            "interpretation": "test",
            "source": "YahooPriceProvider",
            "1d_return": ret,
            "5d_return": ret,
            "20d_return": ret,
            "above_5d_ma": "true",
            "above_20d_ma": "true",
            "volatility_regime": "low",
        }

    mock_provider = MagicMock()
    mock_provider.layer = "price"
    mock_provider.fetch.return_value = [
        make_payload("QQQ", "0.01"),
        make_payload("SPY", "0.02"),
        make_payload("AAPL", "0.03"),
    ]

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        watch_assets=[
            TradingAssetConfig(
                name="Test Basket", category="us_stock", symbols=["QQQ", "SPY", "AAPL"]
            ),
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.oracle.get_provider_by_name", return_value=mock_provider), patch(
        "src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle",
        return_value=False,
    ):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    av = result.asset_views[0]
    assert av.data_quality == "high", (
        f"Expected 'high' data_quality with 3 valid price signals, got: {av.data_quality!r}"
    )


def test_conclusion_shows_price_signal_counts():
    """_build_asset_conclusion must show 'Price signals: X/Y symbols' when data is valid."""
    from src.market.oracle import TradingOracleAnalyzer, MarketSignal, HorizonProbability
    from src.models import TradingAssetConfig

    signals = [
        MarketSignal(
            layer="price", signal="QQQ price", value="450.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={"1d_return": "0.01", "above_5d_ma": "true"},
        ),
        MarketSignal(
            layer="price", signal="SPY price", value="N/A", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={"1d_return": "N/A"},
        ),
    ]
    horizons = [
        HorizonProbability(
            horizon="1d", up_probability=40.0, down_probability=30.0, neutral_probability=30.0,
            expected_bias="bullish", confidence="low", basis="test", invalidation="test",
        ),
        HorizonProbability(
            horizon="1w", up_probability=35.0, down_probability=35.0, neutral_probability=30.0,
            expected_bias="neutral", confidence="low", basis="test", invalidation="test",
        ),
        HorizonProbability(
            horizon="1m", up_probability=38.0, down_probability=32.0, neutral_probability=30.0,
            expected_bias="bullish", confidence="low", basis="test", invalidation="test",
        ),
    ]

    conclusion = TradingOracleAnalyzer._build_asset_conclusion("Test", signals, horizons)
    assert "Price signals: 1/2 symbols" in conclusion, (
        f"Expected 'Price signals: 1/2 symbols' in conclusion, got: {conclusion!r}"
    )
    assert "No valid price data" not in conclusion
    # Bias string must be present (bullish/neutral/bullish from the horizons above)
    assert "bullish/neutral/bullish" in conclusion, (
        f"Expected bias string in conclusion, got: {conclusion!r}"
    )


# ─── New tests: provider payload fields, no truncation, Chinese basis ──────────

def test_yahoo_price_provider_success_payload_has_new_fields():
    """YahooPriceProvider success payload must include symbol, latest_close, ma5, ma20, vol_5d, vol_20d."""
    pd = pytest.importorskip("pandas")
    np = pytest.importorskip("numpy")
    from unittest.mock import patch, MagicMock
    from src.vendor.digital_oracle.providers import YahooPriceProvider

    dates = pd.date_range("2026-01-01", periods=25, freq="B")
    closes = pd.Series(np.linspace(100.0, 110.0, 25), index=dates, name="Close")
    hist = pd.DataFrame({"Close": closes})

    mock_ticker = MagicMock()
    mock_ticker.history.return_value = hist

    with patch("yfinance.Ticker", return_value=mock_ticker):
        result = YahooPriceProvider._fetch_symbol_price("QQQ")

    assert result["symbol"] == "QQQ"
    assert "latest_close" in result
    assert "ma5" in result
    assert "ma20" in result
    assert "vol_5d" in result
    assert "vol_20d" in result
    assert result["value"] != "N/A"
    # Values should be formatted as 4-decimal strings with expected magnitudes
    assert abs(float(result["latest_close"]) - 110.0) < 0.1
    assert 99.0 < float(result["ma5"]) <= 110.0
    assert 100.0 < float(result["ma20"]) <= 110.0
    assert float(result["vol_5d"]) >= 0.0
    assert float(result["vol_20d"]) >= 0.0


def test_yahoo_price_provider_failure_payload_has_symbol():
    """YahooPriceProvider failure payload must include symbol field."""
    from src.vendor.digital_oracle.providers import YahooPriceProvider

    with patch_yfinance_to_fail():
        result = YahooPriceProvider._fetch_symbol_price("FAIL_SYM")
    assert result["symbol"] == "FAIL_SYM"


def test_yahoo_price_provider_does_not_truncate_symbols():
    """YahooPriceProvider must fetch all symbols in context, not just the first 6."""
    from unittest.mock import patch
    from src.vendor.digital_oracle.providers import YahooPriceProvider, ProviderCallContext

    test_symbols = ["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN", "TSLA"]  # 7 symbols
    item = _make_item("test")
    ctx = ProviderCallContext(item=item, question_type="asset_watchlist", symbols=test_symbols)

    called_symbols: list = []

    def mock_fetch_price(symbol):
        called_symbols.append(symbol)
        return {
            "signal": f"{symbol} price", "value": "100.00", "horizon": "1d",
            "interpretation": "test", "source": "YahooPriceProvider", "symbol": symbol,
            "latest_close": "100.0000", "1d_return": "0.0100", "5d_return": "0.0200",
            "20d_return": "0.0300", "ma5": "99.0000", "ma20": "98.0000",
            "above_5d_ma": "true", "above_20d_ma": "true",
            "vol_5d": "0.1500", "vol_20d": "0.1200", "volatility_regime": "medium",
        }

    with patch.object(YahooPriceProvider, "_fetch_symbol_price", staticmethod(mock_fetch_price)):
        results = YahooPriceProvider().fetch(ctx)

    assert called_symbols == test_symbols, f"Expected all 7 symbols fetched, got: {called_symbols}"
    assert len(results) == 7


def test_basis_contains_chinese_text_and_real_percentages():
    """When valid price data exists, basis must contain Chinese text and percentage values."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    sig = MarketSignal(
        layer="price", signal="QQQ price", value="450.00", horizon="1d",
        interpretation="", source="YahooPriceProvider",
        metadata={
            "symbol": "QQQ",
            "1d_return": "0.0072",
            "5d_return": "0.0240",
            "20d_return": "0.0580",
            "above_5d_ma": "true",
            "above_20d_ma": "true",
            "volatility_regime": "low",
        },
    )
    asset = TradingAssetConfig(name="QQQ", category="qdii_nasdaq100", symbols=["QQQ"])

    hp_1d = estimate_horizon_probability(asset, [sig], "1d")
    assert "篮子" in hp_1d.basis
    assert "5日均线" in hp_1d.basis
    assert "%" in hp_1d.basis
    assert "1/1" in hp_1d.basis

    hp_1w = estimate_horizon_probability(asset, [sig], "1w")
    assert "篮子" in hp_1w.basis
    assert "20日均线" in hp_1w.basis
    assert "%" in hp_1w.basis

    hp_1m = estimate_horizon_probability(asset, [sig], "1m")
    assert "篮子" in hp_1m.basis
    assert "20日均线" in hp_1m.basis
    assert "%" in hp_1m.basis


def test_basis_shows_matched_over_total():
    """Basis must show matched/total count for symbols above MA."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    def _sig(sym, above_5d, above_20d, ret):
        return MarketSignal(
            layer="price", signal=f"{sym} price", value="100.00", horizon="1d",
            interpretation="", source="YahooPriceProvider",
            metadata={
                "symbol": sym, "1d_return": ret, "5d_return": ret, "20d_return": ret,
                "above_5d_ma": above_5d, "above_20d_ma": above_20d,
                "volatility_regime": "low",
            },
        )

    signals = [
        _sig("AAPL", "true", "true", "0.02"),
        _sig("MSFT", "true", "true", "0.01"),
        _sig("NVDA", "true", "false", "0.03"),
    ]
    asset = TradingAssetConfig(name="Test", category="us_stock", symbols=["AAPL", "MSFT", "NVDA"])

    # 1d: all 3 above 5D MA → 3/3
    hp_1d = estimate_horizon_probability(asset, signals, "1d")
    assert "3/3" in hp_1d.basis, f"Expected '3/3' in 1d basis, got: {hp_1d.basis!r}"

    # 1w: 2 out of 3 above 20D MA → 2/3
    hp_1w = estimate_horizon_probability(asset, signals, "1w")
    assert "2/3" in hp_1w.basis, f"Expected '2/3' in 1w basis, got: {hp_1w.basis!r}"


def test_basis_shows_symbol_return_samples():
    """Basis must include sample symbol return values."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    sig = MarketSignal(
        layer="price", signal="QQQ price", value="450.00", horizon="1d",
        interpretation="", source="YahooPriceProvider",
        metadata={
            "symbol": "QQQ", "1d_return": "0.0065",
            "5d_return": "0.0240", "20d_return": "0.0580",
            "above_5d_ma": "true", "above_20d_ma": "true",
            "volatility_regime": "low",
        },
    )
    asset = TradingAssetConfig(name="QDII", category="qdii_nasdaq100", symbols=["QQQ"])

    hp_1d = estimate_horizon_probability(asset, [sig], "1d")
    assert "QQQ" in hp_1d.basis, f"Expected 'QQQ' in basis, got: {hp_1d.basis!r}"
    assert "%" in hp_1d.basis


def test_basis_not_only_english_template():
    """Basis must not be the old English template strings when valid data is present."""
    from src.market.oracle import MarketSignal
    from src.market.probability import estimate_horizon_probability
    from src.models import TradingAssetConfig

    sig = MarketSignal(
        layer="price", signal="QQQ price", value="450.00", horizon="1d",
        interpretation="", source="YahooPriceProvider",
        metadata={
            "1d_return": "0.010", "5d_return": "0.020", "20d_return": "0.040",
            "above_5d_ma": "true", "above_20d_ma": "true", "volatility_regime": "low",
        },
    )
    asset = TradingAssetConfig(name="Test", category="us_stock", symbols=["QQQ"])

    for hz in ("1d", "1w", "1m"):
        hp = estimate_horizon_probability(asset, [sig], hz)
        assert "1d basket avg return positive" not in hp.basis, (
            f"horizon={hz}: old English template still present: {hp.basis!r}"
        )
        assert "100% symbols above" not in hp.basis, (
            f"horizon={hz}: old '100%' template still present: {hp.basis!r}"
        )


def test_trading_config_has_max_symbols_per_asset():
    """TradingConfig must expose max_symbols_per_asset with default value 10."""
    config = TradingConfig()
    assert hasattr(config, "max_symbols_per_asset")
    assert config.max_symbols_per_asset == 10


def test_oracle_respects_max_symbols_per_asset():
    """Oracle must slice asset symbols to max_symbols_per_asset when building provider context."""
    from unittest.mock import patch, MagicMock

    fetched_symbols: list = []

    def mock_fetch_price(symbol):
        fetched_symbols.append(symbol)
        return {
            "signal": f"{symbol} price", "value": "100.00", "horizon": "1d",
            "interpretation": "test", "source": "YahooPriceProvider", "symbol": symbol,
            "latest_close": "100.0000", "1d_return": "0.01", "5d_return": "0.02",
            "20d_return": "0.03", "ma5": "99.0000", "ma20": "98.0000",
            "above_5d_ma": "true", "above_20d_ma": "true",
            "vol_5d": "0.15", "vol_20d": "0.12", "volatility_regime": "low",
        }

    from src.vendor.digital_oracle.providers import YahooPriceProvider

    mock_provider = MagicMock(spec=YahooPriceProvider)
    mock_provider.layer = "price"

    # Capture the call to see what symbols are passed
    captured_contexts = []

    def mock_fetch(ctx):
        captured_contexts.append(list(ctx.symbols))
        return [mock_fetch_price(s) for s in ctx.symbols]

    mock_provider.fetch.side_effect = mock_fetch

    config = TradingConfig(
        enabled=True,
        mode="asset_watchlist",
        max_symbols_per_asset=3,
        watch_assets=[
            TradingAssetConfig(
                name="US Mega Cap", category="us_stock",
                symbols=["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN", "TSLA"],
            )
        ],
        enabled_providers=["yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)

    with patch("src.market.oracle.get_provider_by_name", return_value=mock_provider), patch(
        "src.market.digital_oracle_bridge.DigitalOracleBridge._detect_digital_oracle",
        return_value=False,
    ):
        result = asyncio.run(analyzer.analyze_asset_watchlist())

    assert result is not None
    # Should have fetched only the first 3 symbols
    assert len(captured_contexts) == 1
    assert captured_contexts[0] == ["AAPL", "MSFT", "NVDA"], (
        f"Expected first 3 symbols, got: {captured_contexts[0]}"
    )
