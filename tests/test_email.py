"""Tests for email rendering helpers."""

from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    row = soup.find("tr")
    header = soup.find("th")
    cell = soup.find("td")

    assert table is not None and "table-layout: fixed" in table["style"]
    assert table is not None and "font-size: 13px" in table["style"]
    assert row is not None and "vertical-align: top" in row["style"]
    assert header is not None and "background: #f6f8fa" in header["style"]
    assert header is not None and "overflow-wrap: anywhere" in header["style"]
    assert cell is not None and "border: 1px solid #d0d7de" in cell["style"]
    assert cell is not None and "word-break: break-word" in cell["style"]
