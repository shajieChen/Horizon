"""Trading question routing for market analysis plugin."""

from __future__ import annotations

from typing import Optional, List, Tuple

from pydantic import BaseModel, Field

from ..models import ContentItem, TradingConfig


class TradingRoute(BaseModel):
    """Market analysis route for one content item."""

    enabled: bool
    question_type: Optional[str] = None
    reason: Optional[str] = None
    symbols: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    horizon: str = "short_to_medium"


class TradingQuestionRouter:
    """Route Horizon content items to market-analysis question types."""

    _QUESTION_KEYWORDS = [
        ("macro_rates", ["fed", "rates", "rate cut", "inflation", "cpi", "treasury", "yield curve"]),
        ("recession_risk", ["recession", "slowdown", "unemployment", "credit spread"]),
        ("geopolitical_risk", ["war", "invasion", "taiwan", "russia", "ukraine", "israel", "iran", "oil shock"]),
        ("crypto_cycle", ["bitcoin", "ethereum", "crypto", "btc", "eth", "deribit"]),
        ("equity_options", ["nvda", "options", "spy", "qqq", "earnings", "ai bubble"]),
        ("commodity_risk", ["gold", "oil", "copper", "wheat", "natural gas"]),
        ("ai_bubble", ["ai bubble", "gpu", "semiconductor", "datacenter", "nvda"]),
    ]

    _SYMBOL_HINTS = [
        "spy",
        "qqq",
        "nvda",
        "gc=f",
        "cl=f",
        "hg=f",
        "si=f",
        "ita",
        "btc",
        "eth",
        "btc-usd",
        "eth-usd",
        "smh",
        "soxx",
    ]

    def __init__(self, config: TradingConfig):
        self.config = config

    def route(self, item: ContentItem) -> TradingRoute:
        """Return market-analysis route for a content item."""
        ai_score = item.ai_score or 0.0
        if ai_score < self.config.min_ai_score:
            return TradingRoute(enabled=False, reason="ai_score_below_threshold")

        text_parts = [
            item.title or "",
            item.ai_summary or "",
            " ".join(item.ai_tags or []),
        ]
        text = " ".join(text_parts).lower()
        watch_hits = self._collect_hits(self.config.watch_keywords, text)
        category, category_hits = self._match_question_type(text)

        if not watch_hits and not category:
            return TradingRoute(enabled=False, reason="no_trading_keywords")

        symbols = self._collect_symbols(text)
        merged_hits = sorted(set(watch_hits + category_hits))
        question_type = category or "generic_market_event"
        reason = "keyword_match" if category_hits else "watch_keyword_match"
        return TradingRoute(
            enabled=True,
            question_type=question_type,
            reason=reason,
            symbols=symbols,
            keywords=merged_hits,
        )

    @staticmethod
    def _collect_hits(keywords: List[str], text: str) -> List[str]:
        hits: List[str] = []
        for keyword in keywords:
            token = (keyword or "").strip().lower()
            if token and token in text:
                hits.append(keyword)
        return hits

    def _match_question_type(self, text: str) -> Tuple[Optional[str], List[str]]:
        for question_type, keywords in self._QUESTION_KEYWORDS:
            hits = self._collect_hits(keywords, text)
            if hits:
                return question_type, hits
        return None, []

    def _collect_symbols(self, text: str) -> List[str]:
        configured = [s for s in self.config.symbols if s and s.lower() in text]
        hinted = [s.upper() for s in self._SYMBOL_HINTS if s in text]
        return sorted(set(configured + hinted))
