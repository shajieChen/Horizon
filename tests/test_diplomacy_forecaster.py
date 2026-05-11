"""Unit tests for diplomacy forecast generation."""

import asyncio
from datetime import datetime, timezone

from src.ai.client import AIClient
from src.ai.diplomacy_forecaster import DiplomacyForecaster
from src.models import ContentItem, SourceType


class _FakeAIClient(AIClient):
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = 0

    async def complete(self, system: str, user: str, temperature=None, max_tokens=None) -> str:
        self.calls += 1
        return self._responses.pop(0)


def _make_item(idx: int, score: float) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="Some content",
        author="tester",
        published_at=datetime(2026, 5, 1, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = score
    item.ai_reason = "Important development"
    item.ai_summary = "Key summary"
    item.ai_tags = ["diplomacy", "markets"]
    return item


def test_forecast_batch_applies_limits_and_tolerates_parse_failure():
    client = _FakeAIClient(
        [
            '{"is_forecastable": true, "event_type": "meeting", "scenarios": [{"probability": 55}, {"probability": 45}]}',
            "not json",
        ]
    )
    forecaster = DiplomacyForecaster(client, min_score=6.0, max_items=2)

    items = [
        _make_item(1, 9.0),
        _make_item(2, 7.5),
        _make_item(3, 5.0),
    ]
    count = asyncio.run(forecaster.forecast_batch(items))

    assert count == 1
    assert client.calls == 2
    assert items[0].metadata["forecast"]["is_forecastable"] is True
    assert "forecast" not in items[1].metadata
    assert "forecast" not in items[2].metadata
