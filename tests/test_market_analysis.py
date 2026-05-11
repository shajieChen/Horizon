"""Tests for market analysis plugin integration."""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

from src.market.oracle import TradingOracleAnalyzer
from src.market.router import TradingQuestionRouter
from src.market.report import trading_result_to_forecast
from src.models import (
    AIConfig,
    AIProvider,
    Config,
    ContentItem,
    FilteringConfig,
    SourceType,
    SourcesConfig,
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
        trading=trading,
    )


def test_config_without_trading_field_is_still_valid():
    config = Config(
        ai=AIConfig(provider=AIProvider.OPENAI, model="gpt-4", api_key_env="OPENAI_API_KEY"),
        sources=SourcesConfig(),
        filtering=FilteringConfig(),
    )
    assert config.trading is None


def test_router_recognizes_multiple_question_types():
    trading = TradingConfig(enabled=True, watch_keywords=["fed", "bitcoin", "nvda", "taiwan"])
    router = TradingQuestionRouter(trading)

    assert router.route(_make_item("Fed signals inflation and Treasury yield curve")).question_type == "macro_rates"
    assert router.route(_make_item("Bitcoin and Ethereum options surge on Deribit")).question_type == "crypto_cycle"
    assert router.route(_make_item("NVDA options activity rises before earnings")).question_type == "equity_options"
    assert router.route(_make_item("War risk around Taiwan raises oil shock fears")).question_type == "geopolitical_risk"


def test_orchestrator_skips_market_analysis_when_disabled(tmp_path: Path):
    config = _make_config(TradingConfig(enabled=False, watch_keywords=["fed"]))
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    item = _make_item("Fed rate cut signal")

    asyncio.run(orchestrator._forecast_important_items([item]))
    assert "trading_analysis" not in item.metadata
    assert "forecast" not in item.metadata


def test_orchestrator_skips_items_below_min_ai_score(tmp_path: Path):
    config = _make_config(TradingConfig(enabled=True, min_ai_score=8.5, watch_keywords=["fed"]))
    orchestrator = HorizonOrchestrator(config, StorageManager(data_dir=str(tmp_path / "data")))
    item = _make_item("Fed rate cut signal", score=8.0)

    asyncio.run(orchestrator._forecast_important_items([item]))
    assert "trading_analysis" not in item.metadata
    assert "forecast" not in item.metadata


def test_analyzer_tolerates_provider_failures_without_raise():
    config = TradingConfig(
        enabled=True,
        watch_keywords=["nvda", "earnings", "options"],
        enabled_providers=["yfinance", "edgar", "fear_greed", "yahoo_price"],
    )
    analyzer = TradingOracleAnalyzer(config)
    item = _make_item("NVDA options and earnings setup")

    result = asyncio.run(analyzer.analyze(item))
    assert result is not None
    assert result.question_type == "equity_options"
    assert result.errors


def test_orchestrator_writes_trading_analysis_and_forecast(tmp_path: Path):
    trading = TradingConfig(enabled=True, min_ai_score=7.0, watch_keywords=["fed", "inflation"])
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
    config = TradingConfig(enabled=True, watch_keywords=["bitcoin"])
    analyzer = TradingOracleAnalyzer(config)
    item = _make_item("Bitcoin cycle risk check", score=9.0)

    result = asyncio.run(analyzer.analyze(item))
    assert result is not None
    forecast = trading_result_to_forecast(result)

    assert forecast["is_forecastable"] is True
    assert "cause_chain" in forecast
    assert "scenarios" in forecast
    assert "confidence" in forecast
