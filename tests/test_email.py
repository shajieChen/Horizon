"""Tests for email rendering helpers."""

from src.models import EmailConfig
from src.services.email import EmailManager


def _make_email_manager() -> EmailManager:
    return EmailManager(
        EmailConfig(
            imap_server="imap.example.com",
            smtp_server="smtp.example.com",
            email_address="bot@example.com",
            enabled=False,
        )
    )


def test_render_markdown_for_email_converts_tables():
    manager = _make_email_manager()

    html = manager._render_markdown_for_email(
        "| A | B |\n|---|---|\n| 1 | 2 |\n"
    )

    assert "<table>" in html
    assert "<td>1</td>" in html


def test_apply_email_html_styles_inlines_table_styles():
    manager = _make_email_manager()

    html = manager._apply_email_html_styles("<table><tr><th>A</th><td>1</td></tr></table>")

    assert 'style="border-collapse: collapse; width: 100%; max-width: 100%; table-layout: fixed; margin: 12px 0; font-size: 13px"' in html
    assert 'style="vertical-align: top"' in html
    assert 'style="border: 1px solid #d0d7de; background: #f6f8fa; padding: 6px 8px; text-align: left; vertical-align: top; word-break: break-word; overflow-wrap: anywhere"' in html
    assert 'style="border: 1px solid #d0d7de; padding: 6px 8px; vertical-align: top; word-break: break-word; overflow-wrap: anywhere"' in html
