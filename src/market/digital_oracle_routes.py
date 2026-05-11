"""Asset-specific provider routing for digital-oracle watchlist analysis."""

from __future__ import annotations

from dataclasses import dataclass, field

from ..models import TradingAssetConfig


@dataclass(frozen=True)
class ProviderGroupPlan:
    """One provider group in a digital-oracle analysis plan."""

    key: str
    layer: str
    provider: str
    symbols: tuple[str, ...] = ()
    queries: tuple[str, ...] = ()
    series_ticker: str | None = None


def _us_options_symbols(symbols: list[str]) -> tuple[str, ...]:
    picks = []
    for sym in symbols:
        if "." in sym or "=" in sym or sym.startswith("^"):
            continue
        if sym.upper() in {"QQQ", "SPY", "AAPL", "MSFT", "NVDA", "AMZN", "META", "GOOGL", "TSLA"}:
            picks.append(sym.upper())
    return tuple(dict.fromkeys(picks))


def build_asset_provider_plan(asset: TradingAssetConfig) -> list[ProviderGroupPlan]:
    """Return provider plan for one watchlist asset basket."""

    symbols = tuple(asset.symbols)
    options_symbols = _us_options_symbols(asset.symbols)

    if asset.category == "qdii_nasdaq100":
        return [
            ProviderGroupPlan("yahoo_price", "Price Trend", "YahooPriceProvider", symbols=("QQQ", "^NDX", "NQ=F")),
            ProviderGroupPlan("yfinance", "Options / Volatility", "YFinanceProvider", symbols=("QQQ",)),
            ProviderGroupPlan("fear_greed", "Risk Appetite / Macro", "FearGreedProvider"),
            ProviderGroupPlan("treasury", "Risk Appetite / Macro", "USTreasuryProvider"),
            ProviderGroupPlan("cme_fedwatch", "Risk Appetite / Macro", "CMEFedWatchProvider"),
            ProviderGroupPlan(
                "web_search",
                "Risk Appetite / Macro",
                "WebSearchProvider",
                queries=(
                    "VIX current level",
                    "NASDAQ 100 implied volatility current",
                    "MOVE index current level",
                ),
            ),
        ]

    if asset.category == "us_stock":
        return [
            ProviderGroupPlan("yahoo_price", "Price Trend", "YahooPriceProvider", symbols=symbols),
            ProviderGroupPlan(
                "yfinance",
                "Options / Volatility",
                "YFinanceProvider",
                symbols=options_symbols or ("QQQ", "SPY"),
            ),
            ProviderGroupPlan("fear_greed", "Risk Appetite / Macro", "FearGreedProvider"),
            ProviderGroupPlan("treasury", "Risk Appetite / Macro", "USTreasuryProvider"),
            ProviderGroupPlan("edgar", "Risk Appetite / Macro", "EdgarProvider", symbols=options_symbols),
            ProviderGroupPlan(
                "web_search",
                "Risk Appetite / Macro",
                "WebSearchProvider",
                queries=(
                    "VIX current level",
                    "US high yield OAS current",
                    "QQQ implied volatility current",
                ),
            ),
        ]

    if asset.category == "japan_stock":
        return [
            ProviderGroupPlan("yahoo_price", "Price Trend", "YahooPriceProvider", symbols=symbols + ("EWJ",)),
            ProviderGroupPlan("fear_greed", "Risk Appetite / Macro", "FearGreedProvider"),
            ProviderGroupPlan("treasury", "Risk Appetite / Macro", "USTreasuryProvider"),
            ProviderGroupPlan(
                "web_search",
                "Risk Appetite / Macro",
                "WebSearchProvider",
                queries=(
                    "Nikkei 225 volatility current",
                    "JPY USD exchange rate current",
                    "Japan equity risk premium current",
                ),
            ),
        ]

    if asset.category == "hongkong_stock":
        return [
            ProviderGroupPlan("yahoo_price", "Price Trend", "YahooPriceProvider", symbols=symbols + ("EWH", "FXI", "KWEB")),
            ProviderGroupPlan("fear_greed", "Risk Appetite / Macro", "FearGreedProvider"),
            ProviderGroupPlan("treasury", "Risk Appetite / Macro", "USTreasuryProvider"),
            ProviderGroupPlan(
                "web_search",
                "Risk Appetite / Macro",
                "WebSearchProvider",
                queries=(
                    "Hang Seng volatility index current",
                    "USDHKD exchange rate current",
                    "China high yield dollar bond spread current",
                ),
            ),
        ]

    return [
        ProviderGroupPlan("yahoo_price", "Price Trend", "YahooPriceProvider", symbols=symbols),
        ProviderGroupPlan("fear_greed", "Risk Appetite / Macro", "FearGreedProvider"),
        ProviderGroupPlan("treasury", "Risk Appetite / Macro", "USTreasuryProvider"),
        ProviderGroupPlan(
            "web_search",
            "Risk Appetite / Macro",
            "WebSearchProvider",
            queries=(
                "VIX current level",
                "MOVE index current level",
                "US high yield OAS current",
            ),
        ),
    ]
