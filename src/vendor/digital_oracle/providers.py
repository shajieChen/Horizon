"""Minimal provider layer adapted for Horizon market-analysis plugin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

from ...models import ContentItem


@dataclass
class ProviderCallContext:
    """Context passed to a market data provider."""

    item: ContentItem
    question_type: str
    symbols: List[str]
    user_email: Optional[str] = None


class BaseProvider:
    """Base provider returning normalized signal payloads."""

    name: str = "base"
    layer: str = "market"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        """Return provider-derived signals."""
        raise NotImplementedError

    def _headline(self, context: ProviderCallContext) -> str:
        return context.item.title[:96]


class USTreasuryProvider(BaseProvider):
    name = "treasury"
    layer = "rates"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "UST curve posture",
                "value": "cross-checked",
                "horizon": "short_to_medium",
                "interpretation": f"Rates backdrop checked for: {self._headline(context)}",
                "source": "USTreasuryProvider",
            }
        ]


class CMEFedWatchProvider(BaseProvider):
    name = "cme_fedwatch"
    layer = "rates"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Fed path pricing",
                "value": "event-sensitive",
                "horizon": "short_to_medium",
                "interpretation": "Policy path repricing risk remains active.",
                "source": "CMEFedWatchProvider",
            }
        ]


class FearGreedProvider(BaseProvider):
    name = "fear_greed"
    layer = "sentiment"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Risk appetite regime",
                "value": "neutral_to_risk_off",
                "horizon": "short_to_medium",
                "interpretation": "Cross-asset risk appetite can amplify event impact.",
                "source": "FearGreedProvider",
            }
        ]


class YahooPriceProvider(BaseProvider):
    name = "yahoo_price"
    layer = "price"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        symbols = ", ".join(context.symbols[:4]) if context.symbols else "SPY, QQQ"
        return [
            {
                "signal": "Spot trend check",
                "value": symbols,
                "horizon": "short_to_medium",
                "interpretation": "Price trend and volatility regime checked for mapped instruments.",
                "source": "YahooPriceProvider",
            }
        ]


class CftcCotProvider(BaseProvider):
    name = "cftc"
    layer = "positioning"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Futures positioning pressure",
                "value": "non-commercial skew monitored",
                "horizon": "medium",
                "interpretation": "Positioning extremes can validate or fade directional views.",
                "source": "CftcCotProvider",
            }
        ]


class KalshiProvider(BaseProvider):
    name = "kalshi"
    layer = "prediction_market"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Event market implied odds",
                "value": "tracked",
                "horizon": "short_to_medium",
                "interpretation": "Prediction market odds provide independent probability inputs.",
                "source": "KalshiProvider",
            }
        ]


class PolymarketProvider(BaseProvider):
    name = "polymarket"
    layer = "prediction_market"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Decentralized market pricing",
                "value": "tracked",
                "horizon": "short_to_medium",
                "interpretation": "Event contract pricing confirms consensus shifts.",
                "source": "PolymarketProvider",
            }
        ]


class CoinGeckoProvider(BaseProvider):
    name = "coingecko"
    layer = "crypto_spot"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Crypto spot breadth",
                "value": "btc_eth_relative_strength",
                "horizon": "short_to_medium",
                "interpretation": "Spot breadth helps distinguish cyclical rebound vs. distribution.",
                "source": "CoinGeckoProvider",
            }
        ]


class DeribitProvider(BaseProvider):
    name = "deribit"
    layer = "crypto_options"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Crypto options skew",
                "value": "term_structure_checked",
                "horizon": "short_to_medium",
                "interpretation": "Options skew highlights asymmetry in downside or upside demand.",
                "source": "DeribitProvider",
            }
        ]


class EdgarProvider(BaseProvider):
    name = "edgar"
    layer = "insider"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        if not context.user_email:
            raise ValueError("SEC user email is required for EDGAR provider.")
        return [
            {
                "signal": "Insider transaction pulse",
                "value": "filings_screened",
                "horizon": "medium",
                "interpretation": "Insider flow adds governance and valuation context.",
                "source": "EdgarProvider",
            }
        ]


class WebSearchProvider(BaseProvider):
    name = "web_search"
    layer = "macro_vol"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        return [
            {
                "signal": "Market stress proxies",
                "value": "vix_move_cds_oas_watch",
                "horizon": "short_to_medium",
                "interpretation": "Stress proxies indicate whether risk repricing is broadening.",
                "source": "WebSearchProvider",
            }
        ]


class YFinanceProvider(BaseProvider):
    name = "yfinance"
    layer = "options"

    def fetch(self, context: ProviderCallContext) -> List[Dict[str, str]]:
        try:
            import yfinance  # noqa: F401
        except ImportError as exc:
            raise RuntimeError("yfinance dependency is not installed.") from exc
        return [
            {
                "signal": "Options implied volatility",
                "value": "surface_checked",
                "horizon": "short_to_medium",
                "interpretation": "Implied volatility surface indicates expected event magnitude.",
                "source": "YFinanceProvider",
            }
        ]


PROVIDER_REGISTRY = {
    "treasury": USTreasuryProvider,
    "cme_fedwatch": CMEFedWatchProvider,
    "fear_greed": FearGreedProvider,
    "yahoo_price": YahooPriceProvider,
    "cftc": CftcCotProvider,
    "kalshi": KalshiProvider,
    "polymarket": PolymarketProvider,
    "coingecko": CoinGeckoProvider,
    "deribit": DeribitProvider,
    "edgar": EdgarProvider,
    "web_search": WebSearchProvider,
    "yfinance": YFinanceProvider,
}


def get_provider_by_name(name: str) -> BaseProvider:
    """Build a provider instance from registry name."""
    provider_cls = PROVIDER_REGISTRY.get(name)
    if not provider_cls:
        raise KeyError(f"Unknown provider: {name}")
    return provider_cls()
