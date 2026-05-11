"""Asset universe helpers for asset_watchlist trading mode."""

from __future__ import annotations

from typing import List

from ..models import TradingAssetConfig, TradingConfig

_SUPPORTED_CATEGORIES = frozenset(
    [
        "qdii_nasdaq100",
        "overseas_stock",
        "us_stock",
        "japan_stock",
        "hongkong_stock",
    ]
)


def get_enabled_assets(config: TradingConfig) -> List[TradingAssetConfig]:
    """Return enabled assets within configured asset scope."""
    scope = set(config.asset_scope)
    return [
        asset
        for asset in config.watch_assets
        if asset.enabled and asset.category in scope and asset.symbols
    ]


def is_supported_asset_category(category: str) -> bool:
    """Return whether category is supported by asset watchlist mode."""
    return category in _SUPPORTED_CATEGORIES
