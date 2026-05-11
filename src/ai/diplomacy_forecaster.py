"""Structured diplomacy forecasting for important items."""

from typing import List

from .client import AIClient
from .prompts import DIPLOMACY_FORECAST_SYSTEM, DIPLOMACY_FORECAST_USER
from .utils import parse_json_response
from ..models import ContentItem


class DiplomacyForecaster:
    """Generates structured forecasts for high-scoring content items."""

    def __init__(self, ai_client: AIClient, min_score: float = 6.0, max_items: int = 8):
        self.client = ai_client
        self.min_score = min_score
        self.max_items = max_items

    async def forecast_batch(self, items: List[ContentItem]) -> int:
        """Forecast eligible items and store results in metadata."""
        eligible = [
            item for item in items
            if item.ai_score is not None and item.ai_score >= self.min_score
        ][: self.max_items]

        success_count = 0
        for item in eligible:
            try:
                if await self._forecast_item(item):
                    success_count += 1
            except Exception as e:
                # Keep the pipeline running if a single item fails.
                print(f"Warning: forecast failed for {item.id}: {e}")

        return success_count

    async def _forecast_item(self, item: ContentItem) -> bool:
        """Forecast a single item and write structured output to metadata."""
        meta = item.metadata
        summary = (
            meta.get("detailed_summary_en")
            or meta.get("detailed_summary")
            or item.ai_summary
            or item.title
        )

        tags = ", ".join(item.ai_tags) if item.ai_tags else ""
        published_at = item.published_at.isoformat() if item.published_at else ""
        content = (item.content or "")[:4000]

        context_parts = []
        for key in (
            "title_en",
            "title_zh",
            "background_en",
            "background_zh",
            "community_discussion_en",
            "community_discussion_zh",
        ):
            value = meta.get(key)
            if value:
                context_parts.append(f"{key}: {value}")
        enriched_context = "\n".join(context_parts) if context_parts else "None"

        user_prompt = DIPLOMACY_FORECAST_USER.format(
            title=item.title,
            url=str(item.url),
            source=item.source_type.value,
            published_at=published_at,
            score=item.ai_score or 0,
            reason=item.ai_reason or "",
            tags=tags,
            summary=summary,
            content=content,
            enriched_context=enriched_context,
        )

        response = await self.client.complete(
            system=DIPLOMACY_FORECAST_SYSTEM,
            user=user_prompt,
        )
        result = parse_json_response(response)
        if result is None:
            # Parsing errors are non-fatal for the full batch.
            print(f"Warning: could not parse forecast response for {item.id}, skipping forecast")
            return False

        item.metadata["forecast"] = result
        return True
