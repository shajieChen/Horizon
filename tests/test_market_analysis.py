"""Tests for market analysis plugin integration."""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

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
            assert abs(total - 100.0) < 1.5, (
                f"{av.name} {hp.horizon}: probabilities sum to {total} (expected ~100)"
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

