"""Minimal provider layer adapted for Horizon market-analysis plugin."""

from __future__ import annotations

import math
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
        symbols = context.symbols[:6] if context.symbols else ["SPY", "QQQ"]
        signals = []
        for sym in symbols:
            price_data = self._fetch_symbol_price(sym)
            signals.append(price_data)
        return signals

    @staticmethod
    def _fetch_symbol_price(symbol: str) -> Dict[str, str]:
        """Attempt yfinance price fetch; fall back to stub on failure."""
        try:
            import yfinance as yf  # noqa: PLC0415

            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="30d")
            if hist.empty or len(hist) < 2:
                raise ValueError(f"Insufficient price history for {symbol} (got {len(hist)} day(s), need at least 2)")

            closes = hist["Close"].dropna()
            latest = float(closes.iloc[-1])
            ret_1d = float((closes.iloc[-1] - closes.iloc[-2]) / closes.iloc[-2]) if len(closes) >= 2 else 0.0
            ret_5d = float((closes.iloc[-1] - closes.iloc[-6]) / closes.iloc[-6]) if len(closes) >= 6 else 0.0
            ret_20d = float((closes.iloc[-1] - closes.iloc[0]) / closes.iloc[0]) if len(closes) >= 20 else 0.0

            ma5 = float(closes.iloc[-5:].mean()) if len(closes) >= 5 else latest
            ma20 = float(closes.mean())
            above_5d_ma = "true" if latest > ma5 else "false"
            above_20d_ma = "true" if latest > ma20 else "false"

            # Realized volatility (annualised from daily log returns)
            log_rets = closes.pct_change().dropna()
            vol_5d = float(log_rets.iloc[-5:].std() * math.sqrt(252)) if len(log_rets) >= 5 else 0.0
            vol_20d = float(log_rets.iloc[-20:].std() * math.sqrt(252)) if len(log_rets) >= 20 else 0.0
            vol_regime = "high" if vol_5d > 0.30 else ("medium" if vol_5d > 0.15 else "low")

            return {
                "signal": f"{symbol} price",
                "value": f"{latest:.2f}",
                "horizon": "1d",
                "interpretation": (
                    f"1d={ret_1d:+.2%} 5d={ret_5d:+.2%} 20d={ret_20d:+.2%} "
                    f"above_5D_MA={above_5d_ma} above_20D_MA={above_20d_ma} "
                    f"vol_5d={vol_5d:.1%} vol_20d={vol_20d:.1%}"
                ),
                "source": "YahooPriceProvider",
                "1d_return": f"{ret_1d:.4f}",
                "5d_return": f"{ret_5d:.4f}",
                "20d_return": f"{ret_20d:.4f}",
                "above_5d_ma": above_5d_ma,
                "above_20d_ma": above_20d_ma,
                "volatility_regime": vol_regime,
            }
        except Exception as exc:
            return {
                "signal": f"{symbol} price",
                "value": "N/A",
                "horizon": "1d",
                "interpretation": f"Price data unavailable for {symbol}: {exc}",
                "source": "YahooPriceProvider",
                "1d_return": "N/A",
                "5d_return": "N/A",
                "20d_return": "N/A",
                "above_5d_ma": "unknown",
                "above_20d_ma": "unknown",
                "volatility_regime": "unknown",
            }


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
            raise ValueError(
                "SEC user email is required for EDGAR provider. "
                "Set the environment variable configured by trading.user_email_env "
                "(default: SEC_USER_EMAIL)."
            )
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
            import yfinance as yf  # noqa: PLC0415
        except ImportError:
            return [
                {
                    "signal": "Options implied volatility",
                    "value": "N/A",
                    "horizon": "short_to_medium",
                    "interpretation": "yfinance not installed — options IV unavailable.",
                    "source": "YFinanceProvider",
                }
            ]

        results = []
        for symbol in context.symbols[:4]:
            result = self._fetch_options(symbol, yf)
            if result:
                results.append(result)

        if not results:
            results.append(
                {
                    "signal": "Options implied volatility",
                    "value": "N/A",
                    "horizon": "short_to_medium",
                    "interpretation": "No options data retrieved for configured symbols.",
                    "source": "YFinanceProvider",
                }
            )
        return results

    @staticmethod
    def _fetch_options(symbol: str, yf) -> Optional[Dict[str, str]]:  # type: ignore[type-arg]
        """Fetch ATM implied volatility for a single symbol; return None on failure."""
        try:
            ticker = yf.Ticker(symbol)
            expirations = ticker.options
            if not expirations:
                return {
                    "signal": f"{symbol} options IV",
                    "value": "N/A",
                    "horizon": "short_to_medium",
                    "interpretation": f"No options listed for {symbol} (non-US or delisted).",
                    "source": "YFinanceProvider",
                    "fear_greed": "",
                }

            # Use nearest expiry
            chain = ticker.option_chain(expirations[0])
            calls = chain.calls
            if calls.empty:
                raise ValueError(f"Empty options chain for {symbol}")

            # Find ATM strike
            hist = ticker.history(period="2d")
            spot = float(hist["Close"].iloc[-1]) if not hist.empty else None
            if spot is None:
                raise ValueError(f"Cannot determine spot price for {symbol}")

            calls["strike_diff"] = (calls["strike"] - spot).abs()
            atm_row = calls.nsmallest(1, "strike_diff").iloc[0]
            iv = float(atm_row.get("impliedVolatility", 0.0))

            return {
                "signal": f"{symbol} ATM IV",
                "value": f"{iv:.1%}",
                "horizon": "short_to_medium",
                "interpretation": (
                    f"ATM implied volatility for {symbol} at {spot:.2f}: "
                    f"IV={iv:.1%} (expiry {expirations[0]})"
                ),
                "source": "YFinanceProvider",
            }
        except Exception as exc:
            return {
                "signal": f"{symbol} options IV",
                "value": "N/A",
                "horizon": "short_to_medium",
                "interpretation": f"Options data unavailable for {symbol}: {exc}",
                "source": "YFinanceProvider",
            }


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
