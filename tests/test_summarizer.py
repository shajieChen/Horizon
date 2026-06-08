"""Unit tests for daily summary rendering."""

from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.models import ContentItem, SourceType


def _make_item(idx: int) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Important Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = f"Summary for item {idx}."
    item.ai_tags = ["AI", "News"]
    return item


def test_generate_webhook_overview_lists_items_without_full_details():
    summarizer = DailySummarizer()
    items = [_make_item(1), _make_item(2)]

    result = summarizer.generate_webhook_overview(
        items,
        date="2026-04-25",
        total_fetched=10,
        language="en",
    )

    assert "Selected 2 important items from 10 fetched items" in result
    assert "1. [Important Item 1](https://example.com/items/1)" in result
    assert "2. [Important Item 2](https://example.com/items/2)" in result
    assert "Summary for item 1." not in result


def test_generate_webhook_item_renders_single_item_detail():
    summarizer = DailySummarizer()

    result = summarizer.generate_webhook_item(
        _make_item(1),
        language="en",
        index=1,
        total=2,
    )

    assert result.startswith("Item 1/2")
    assert "## [Important Item 1](https://example.com/items/1)" in result
    assert "Summary for item 1." in result
    assert "**Tags**: `#AI`, `#News`" in result


def test_generate_webhook_item_renders_forecast_block_when_forecastable():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["forecast"] = {
        "is_forecastable": True,
        "event_type": "policy-signal",
        "actors": [
            {"name": "Actor A", "role": "state", "likely_incentives": ["stability"]},
        ],
        "cause_chain": {
            "immediate_trigger": "Trigger",
            "structural_causes": ["Cause 1"],
            "constraints": ["Constraint 1"],
        },
        "scenarios": [
            {"name": "baseline", "horizon": "7d", "probability": 55, "reasoning": "R1", "trigger_conditions": ["T1"]},
            {"name": "escalation", "horizon": "7d", "probability": 25, "reasoning": "R2", "trigger_conditions": ["T2"]},
            {"name": "deescalation", "horizon": "7d", "probability": 15, "reasoning": "R3", "trigger_conditions": ["T3"]},
            {"name": "wildcard", "horizon": "30d", "probability": 5, "reasoning": "R4", "trigger_conditions": ["T4"]},
        ],
        "near_term_watch": {"24h": ["W1"], "7d": ["W2"], "30d": ["W3"]},
        "confidence": {"level": "medium", "reason": "Reason"},
        "falsifiers": ["F1"],
        "missing_evidence": ["M1"],
        "market_or_policy_implications": ["I1"],
    }

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "**预测分析**" in result
    assert "**未来情景**" in result
    assert "| 基准 | 7d | 55% | R1 | T1 |" in result
    assert "**置信度**：中等。Reason" in result


def test_generate_webhook_item_renders_non_forecastable_reason():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["forecast"] = {
        "is_forecastable": False,
        "reason": "insufficient evidence",
    }

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "**预测分析**：该事件不适合进行独立情景预测。原因：insufficient evidence" in result


def test_generate_webhook_item_asset_watchlist_uses_narrow_tables_and_skips_forecast():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["forecast"] = {
        "is_forecastable": True,
        "event_type": "policy-signal",
    }
    item.metadata["trading_analysis"] = {
        "question_type": "asset_watchlist",
        "asset_views": [
            {
                "name": "QDII Nasdaq 100 Proxy",
                "market": "US",
                "symbols": ["QQQ", "^NDX", "NQ=F"],
                "data_quality": "medium",
                "horizons": [
                    {
                        "horizon": "1d",
                        "up_probability": 33,
                        "down_probability": 33,
                        "neutral_probability": 34,
                        "expected_bias": "neutral",
                        "confidence": "low",
                        "basis": "Short-term breadth improving",
                        "invalidation": "Breadth rolls over sharply",
                    },
                    {
                        "horizon": "1w",
                        "up_probability": 33,
                        "down_probability": 33,
                        "neutral_probability": 34,
                        "expected_bias": "neutral",
                        "confidence": "low",
                        "basis": "Trend remains range-bound",
                        "invalidation": "Index breaks support",
                    },
                    {
                        "horizon": "1m",
                        "up_probability": 33,
                        "down_probability": 33,
                        "neutral_probability": 34,
                        "expected_bias": "neutral",
                        "confidence": "low",
                        "basis": "Macro conditions mixed",
                        "invalidation": "Liquidity tightens materially",
                    },
                ],
            }
        ],
        "data_sources": ["Market data"],
    }

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "**Trading Analysis**" in result
    assert "### 资产概率总览 (Asset Probability Overview)" in result
    assert "#### QDII Nasdaq 100 Proxy" in result
    assert "| 资产 | 市场 | 1日 | 1周 | 1月 | 数据质量 |" in result
    assert "| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |" in result
    assert "| 资产 | 市场 | 1D 偏向 | 1D ↑/↓/~ | 1W 偏向 | 1W ↑/↓/~ | 1M 偏向 | 1M ↑/↓/~ | 数据质量 |" not in result
    assert "**预测分析**" not in result


def test_generate_webhook_item_asset_watchlist_adds_concise_data_unavailable_note():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["trading_analysis"] = {
        "question_type": "asset_watchlist",
        "asset_views": [
            {
                "name": "QDII Nasdaq 100 Proxy",
                "market": "US",
                "symbols": ["QQQ"],
                "data_quality": "low",
                "horizons": [
                    {
                        "horizon": "1d",
                        "up_probability": 33,
                        "down_probability": 33,
                        "neutral_probability": 34,
                        "expected_bias": "neutral",
                        "confidence": "low",
                        "basis": "有效交易信号不足，使用保守基准分布。",
                        "invalidation": "等待更多数据",
                    }
                ],
            }
        ],
        "data_sources": ["Market data"],
    }

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "数据状态：部分市场数据暂不可用，已采用保守基准概率估计。" in result
