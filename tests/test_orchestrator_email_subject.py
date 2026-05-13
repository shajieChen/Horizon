import asyncio
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from src.models import (
    AIConfig,
    AIProvider,
    Config,
    ContentItem,
    EmailConfig,
    FilteringConfig,
    SourceType,
    SourcesConfig,
    TradingConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def _make_config() -> Config:
    return Config(
        ai=AIConfig(
            provider=AIProvider.OPENAI,
            model="gpt-4",
            api_key_env="OPENAI_API_KEY",
            languages=["zh"],
        ),
        sources=SourcesConfig(),
        filtering=FilteringConfig(ai_score_threshold=7.0, time_window_hours=24),
        trading=TradingConfig(enabled=False),
        email=EmailConfig(
            imap_server="imap.example.com",
            smtp_server="smtp.example.com",
            email_address="horizon@example.com",
            enabled=True,
        ),
    )


def _make_item() -> ContentItem:
    item = ContentItem(
        id="rss:item",
        source_type=SourceType.RSS,
        title="Important item",
        url="https://example.com/item",
        content="Important item",
        published_at=datetime(2026, 5, 12, 3, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = "Important item"
    return item


def test_build_email_subject_uses_required_china_time_format() -> None:
    subject = HorizonOrchestrator._build_email_subject(
        datetime(2026, 5, 13, 6, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
    )

    assert subject == "Infomation Summary - 2026-05-13 06:00 CST"
    assert "Horizon Summary" not in subject
    assert "(ZH)" not in subject
    assert "(EN)" not in subject


def test_run_keeps_date_only_filenames_and_uses_timestamped_email_subject(
    tmp_path,
    monkeypatch,
) -> None:
    import src.orchestrator as orchestrator_module

    fixed_now = datetime(2026, 5, 12, 22, 0, tzinfo=timezone.utc)

    class FixedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            if tz is None:
                return fixed_now.replace(tzinfo=None)
            return fixed_now.astimezone(tz)

    class FakeSummarizer:
        async def generate_summary(self, items, today, all_items_count, language="en"):
            return f"# Summary\n{today} {language} {all_items_count} {len(items)}"

    class FakeEmailManager:
        def __init__(self):
            self.sent_subjects = []

        def check_subscriptions(self, storage):
            pass

        def send_daily_summary(self, summary, subject, subscribers):
            self.sent_subjects.append(subject)

    async def no_op_async(*args, **kwargs):
        return None

    item = _make_item()
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("EMAIL_PASSWORD", "test-password")
    monkeypatch.setattr(orchestrator_module, "datetime", FixedDatetime)
    monkeypatch.setattr(orchestrator_module, "DailySummarizer", FakeSummarizer)

    storage = StorageManager(data_dir=str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(_make_config(), storage)
    fake_email_manager = FakeEmailManager()
    orchestrator.email_manager = fake_email_manager

    monkeypatch.setattr(orchestrator, "fetch_all_sources", no_op_async)
    monkeypatch.setattr(orchestrator, "_analyze_content", no_op_async)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", no_op_async)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", no_op_async)
    monkeypatch.setattr(orchestrator, "_forecast_important_items", no_op_async)

    async def fetch_all_sources(since):
        return [item]

    async def analyze_content(items):
        return items

    async def merge_topic_duplicates(items):
        return items

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)

    asyncio.run(orchestrator.run(force_hours=168))

    assert fake_email_manager.sent_subjects == [
        "Infomation Summary - 2026-05-13 06:00 CST"
    ]
    assert (tmp_path / "data" / "summaries" / "horizon-2026-05-13-zh.md").exists()
    assert (tmp_path / "docs" / "_posts" / "2026-05-13-summary-zh.md").exists()
    assert not (tmp_path / "data" / "summaries" / "horizon-2026-05-13-06:00-zh.md").exists()


def test_orchestrator_uses_asia_shanghai_for_report_date() -> None:
    import inspect

    source = inspect.getsource(HorizonOrchestrator._now_china)
    run_source = inspect.getsource(HorizonOrchestrator.run)

    assert 'ZoneInfo("Asia/Shanghai")' in source or "CHINA_TZ" in source
    assert "now_utc" not in run_source
    assert "_build_email_subject(now_china)" in run_source
