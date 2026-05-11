# Trading Market Analysis Plugin

## Purpose

The `market_analysis` plugin layer adds market-data-driven analysis to Horizon daily summaries without changing Horizon's core scraping, AI scoring, filtering, deduplication, summary generation, and publishing workflow.

## Enable Trading Analysis

Set `trading.enabled` to `true` in `data/config.json`.

When `trading` is missing or disabled, Horizon behavior remains unchanged.

## Configuration

- `trading.min_ai_score`: Minimum `ContentItem.ai_score` required for analysis.
- `trading.max_items_per_run`: Maximum analyzed items per run.
- `trading.watch_keywords`: Event keywords used by routing.
- `trading.symbols`: Instruments used for provider symbol mapping.
- `trading.enabled_providers`: Allowed provider list.
- `trading.user_email_env`: Environment variable used for SEC EDGAR requests.

## Provider and Optional Dependency Notes

- `YahooPriceProvider` does not require `yfinance`.
- `YFinanceProvider` requires optional dependency:
  - install with `pip install -e '.[trading]'`
- If `yfinance` is not installed, the plugin records an error and continues.

## SEC_USER_EMAIL

Set `SEC_USER_EMAIL` (or your custom env in `user_email_env`) for EDGAR-related provider calls.  
If missing, EDGAR failures are captured in analysis errors and do not stop the run.

## Output Fields

For analyzed items, Horizon writes:

- `item.metadata["trading_analysis"]`: Full structured market analysis
- `item.metadata["forecast"]`: DailySummarizer-compatible forecast structure

Rendered summary includes:

- Event type
- Market question
- Multi-layer signal table
- Resonance signals
- Key divergences
- Probability scenarios
- Trading bias
- Monitor signals
- Falsifiers
- Data sources

## Failure Tolerance Strategy

- Each provider call is isolated with `try/except`.
- Any single provider failure is recorded in `errors`.
- Provider failures never abort summary generation.
- If fewer than 3 independent signals are available, analysis still returns with low-confidence messaging.

## Disclaimer

This module provides market data analysis only and does not constitute investment advice.
