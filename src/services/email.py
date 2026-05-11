"""Email service for handling subscriptions and sending summaries."""

import email
import html
import imaplib
import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr
from typing import List

try:
    import markdown
except ImportError:
    markdown = None

from bs4 import BeautifulSoup

from ..models import EmailConfig

logger = logging.getLogger(__name__)


class EmailManager:
    """Manages email subscriptions and sending summaries."""

    def __init__(self, config: EmailConfig, console=None):
        self.config = config
        self.pwd = os.getenv(self.config.password_env)
        if console is None:
            try:
                from rich.console import Console
                self.console = Console()
            except ImportError:
                class DummyConsole:
                    def print(self, *args, **kwargs):
                        print(*args, **kwargs)
                self.console = DummyConsole()
        else:
            self.console = console

        if not self.pwd and self.config.enabled:
            logger.warning(
                f"Environment variable {self.config.password_env} not set. Email features may fail."
            )
            self.console.print(f"[yellow]Warning: Environment variable {self.config.password_env} not set. Email features may fail.[/yellow]")

    def check_subscriptions(self, storage_manager):
        """Checks inbox for subscription requests and updates subscriber list."""
        if not self.config.enabled:
            return

        try:
            mail = imaplib.IMAP4_SSL(self.config.imap_server, self.config.imap_port)
            mail.login(self.config.email_address, self.pwd)
            mail.select("INBOX")

            keyword = self.config.subscribe_keyword
            search_crit = f'(UNSEEN SUBJECT "{keyword}")'

            status, messages = mail.search(None, search_crit)

            if status == "OK" and messages[0]:
                email_ids = messages[0].split()
                subscribers = storage_manager.load_subscribers()

                for e_id in email_ids:
                    _, msg_data = mail.fetch(e_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])

                            subject = str(msg.get("Subject") or "").strip()
                            if subject.upper() != keyword.upper():
                                continue

                            sender = msg.get("From")

                            if sender:
                                _, email_addr = parseaddr(sender)
                                if email_addr and "@" in email_addr:
                                    if "noreply" in email_addr.lower() or "no-reply" in email_addr.lower():
                                        continue

                                    if email_addr not in subscribers:
                                        storage_manager.add_subscriber(email_addr)
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_reply(
                                            email_addr,
                                            "Subscribed to Horizon",
                                            "You have been successfully subscribed to Horizon daily summaries.",
                                        )
                                        logger.info(f"Added subscriber: {email_addr}")
                                    else:
                                        logger.info(f"Already subscribed: {email_addr}")

            unsub_keyword = self.config.unsubscribe_keyword
            search_crit_unsub = f'(UNSEEN SUBJECT "{unsub_keyword}")'

            status, messages = mail.search(None, search_crit_unsub)

            if status == "OK" and messages[0]:
                email_ids = messages[0].split()
                subscribers = storage_manager.load_subscribers()

                for e_id in email_ids:
                    _, msg_data = mail.fetch(e_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])

                            subject = str(msg.get("Subject") or "").strip()
                            if subject.upper() != unsub_keyword.upper():
                                continue

                            sender = msg.get("From")

                            if sender:
                                _, email_addr = parseaddr(sender)
                                if email_addr and "@" in email_addr:
                                    if "noreply" in email_addr.lower() or "no-reply" in email_addr.lower():
                                        continue

                                    if email_addr in subscribers:
                                        storage_manager.remove_subscriber(email_addr)
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_reply(
                                            email_addr,
                                            "Unsubscribed from Horizon",
                                            "You have been successfully unsubscribed from Horizon daily summaries.",
                                        )
                                        logger.info(f"Removed subscriber: {email_addr}")
                                    else:
                                        logger.info(f"Not subscribed: {email_addr}")

            mail.close()
            mail.logout()

        except Exception as e:
            logger.error(f"Error checking subscriptions: {e}")

    def send_daily_summary(
        self, summary_md: str, subject: str, subscribers: List[str]
    ):
        """Sends the daily summary to all subscribers."""
        if not self.config.enabled or not subscribers:
            return

        html_content = self._render_markdown_for_email(summary_md)
        html_content = self._apply_email_html_styles(html_content)

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, "Microsoft YaHei", sans-serif; line-height: 1.6; color: #24292f; max-width: 860px; margin: 0 auto; padding: 16px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 100%; max-width: 100%; table-layout: fixed; }}
                th, td {{ border: 1px solid #d0d7de; padding: 6px 8px; word-break: break-word; overflow-wrap: anywhere; vertical-align: top; }}
                th {{ background: #f6f8fa; }}
                p, li {{ word-break: break-word; overflow-wrap: anywhere; }}
                code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
                pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                blockquote {{ border-left: 4px solid #d0d7de; padding-left: 12px; color: #57606a; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #888; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
            </style>
        </head>
        <body>
            {html_content}
            <div class="footer">
                <p>Sent by {self.config.sender_name}</p>
                <p>To unsubscribe, please reply with "{self.config.unsubscribe_keyword}"</p>
            </div>
        </body>
        </html>
        """

        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                for subscriber in subscribers:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = subject
                    msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                    msg["To"] = subscriber

                    text_part = MIMEText(summary_md, "plain", "utf-8")
                    html_part = MIMEText(html_body, "html", "utf-8")

                    msg.attach(text_part)
                    msg.attach(html_part)

                    try:
                        server.send_message(msg)
                        logger.info(f"Sent summary to {subscriber}")
                    except Exception as e:
                        logger.error(f"Failed to send to {subscriber}: {e}")

        except Exception as e:
            logger.error(f"SMTP Error: {e}")

    @staticmethod
    def _merge_inline_styles(existing_style: str | None, style_updates: dict[str, str]) -> str:
        """Merge inline styles and let style_updates override conflicting existing values."""
        style_map = {}
        if existing_style:
            for declaration in existing_style.split(";"):
                if ":" not in declaration:
                    continue
                key, value = declaration.split(":", 1)
                key = key.strip()
                value = value.strip()
                if key and value:
                    style_map[key] = value
        style_map.update(style_updates)
        return "; ".join(f"{key}: {value}" for key, value in style_map.items()) + ";" if style_map else ""

    def _render_markdown_for_email(self, summary_md: str) -> str:
        """Render Markdown into email-safe HTML."""
        if markdown:
            return markdown.markdown(
                summary_md,
                extensions=[
                    "markdown.extensions.tables",
                    "markdown.extensions.fenced_code",
                    "markdown.extensions.sane_lists",
                ],
                output_format="html5",
            )
        return f"<pre>{html.escape(summary_md)}</pre>"

    def _apply_email_html_styles(self, html_content: str) -> str:
        """Apply email-client-safe inline styles to generated HTML."""
        soup = BeautifulSoup(html_content, "html.parser")
        style_map = {
            "table": {
                "border-collapse": "collapse",
                "width": "100%",
                "max-width": "100%",
                "table-layout": "fixed",
                "margin": "12px 0",
                "font-size": "13px",
            },
            "thead": {
                "width": "100%",
            },
            "tbody": {
                "width": "100%",
            },
            "tr": {
                "vertical-align": "top",
            },
            "th": {
                "border": "1px solid #d0d7de",
                "background": "#f6f8fa",
                "padding": "6px 8px",
                "text-align": "left",
                "vertical-align": "top",
                "word-break": "break-word",
                "overflow-wrap": "anywhere",
            },
            "td": {
                "border": "1px solid #d0d7de",
                "padding": "6px 8px",
                "vertical-align": "top",
                "word-break": "break-word",
                "overflow-wrap": "anywhere",
            },
            "p": {
                "word-break": "break-word",
                "overflow-wrap": "anywhere",
            },
            "li": {
                "word-break": "break-word",
                "overflow-wrap": "anywhere",
            },
            "blockquote": {
                "border-left": "4px solid #d0d7de",
                "padding-left": "12px",
                "color": "#57606a",
            },
        }
        for tag_name, styles in style_map.items():
            for element in soup.find_all(tag_name):
                element["style"] = self._merge_inline_styles(element.get("style"), styles)
        return str(soup)

    def _send_reply(self, to_email: str, subject: str, body: str):
        """Helper to send a simple reply."""
        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                msg = MIMEText(body, "plain", "utf-8")
                msg["Subject"] = subject
                msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                msg["To"] = to_email

                server.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to send reply to {to_email}: {e}")
