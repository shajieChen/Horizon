---
layout: default
title: Scoring System
---

# Scoring System

After fetching content from all sources, Horizon uses an AI model to score each item on a 0-10 scale. This determines what appears in the daily summary, with the scorer now prioritizing diplomacy, geopolitics, international finance, macro risk, and market-moving events.

## Pipeline

1. **Batch processing** — Items are scored in batches of 10 with a progress bar. Failed items receive a score of 0.
2. **Content preparation** — For each item, the content is truncated (800 chars if comments are present, 1000 otherwise) and engagement metrics are assembled from metadata (HN score, Reddit upvote ratio, etc.).
3. **AI analysis** — The prepared content is sent to the configured AI model (temperature 0.3) with a system prompt defining the scoring criteria.
4. **Response parsing** — The AI response is parsed as JSON (with fallbacks for code-block-wrapped JSON). Each item gets: `ai_score` (float), `ai_reason` (string), `ai_summary` (string), and `ai_tags` (list).
5. **Retry** — Failed AI calls are retried up to 3 times with exponential backoff (2-10 seconds).

## Scoring Scale

| Score | Tier | Description |
|-------|------|-------------|
| 9-10 | Major Risk / High Impact | Major diplomatic shifts, sanctions, trade restrictions, military crises with spillovers, central-bank surprises, systemic market or supply-chain risk |
| 7-8 | High Value | Important meetings, policy signals, macro data, regional instability, or analysis with clear follow-up value for diplomacy or markets |
| 5-6 | Worth Monitoring | Routine but meaningful diplomatic activity, moderate market moves, indirect macro or supply-chain implications |
| 3-4 | Low Priority | Repetitive commentary, weak-signal discussion, limited policy meaning or observable follow-through |
| 0-2 | Noise | Ads, unrelated technical updates, unsupported opinion, clickbait, off-topic items |

## Scoring Factors

The AI evaluates each item based on:

- **State and policy relevance** — involvement of governments, foreign ministries, central banks, finance ministries, regulators, militaries, or multilateral bodies
- **Risk transmission** — potential spillovers into sanctions, trade policy, negotiations, retaliation, capital flows, or market repricing
- **Market sensitivity** — likely effects on FX, rates, bonds, equities, commodities, energy, shipping, or supply chains
- **Source quality and evidence** — official statements, policy documents, macro data, credible investigations, and other factual reporting
- **Community discussion** — only when comments add fact-rich context, counterpoints, or useful sentiment signals

Engagement metadata is source-specific: HN provides score and comment count, Reddit provides upvote ratio and comment count.

## Filtering

After scoring, items are filtered by `filtering.ai_score_threshold` (default: `7.0`) and sorted by score descending. Only items meeting the threshold appear in the daily summary.

```json
{
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24
  }
}
```

Items scoring 9.0 or above are featured in the "Today's Highlights" section of the summary.

The parsed JSON fields remain unchanged: `ai_score`, `ai_reason`, `ai_summary`, and `ai_tags`. The tag set should now favor labels such as `diplomacy`, `geopolitics`, `central-bank`, `macroeconomics`, `trade-policy`, `energy`, `supply-chain`, and `global-markets`.

The new criteria apply when items are scored in future runs. Existing stored outputs remain backward-compatible at the JSON-schema level and are only re-evaluated if they go through the scoring stage again.

## Enrichment

Items that pass the score threshold go through a second AI pass for enrichment (`src/ai/enricher.py`):

1. **Concept extraction** — AI identifies 1-3 concepts in the item that may need explanation.
2. **Web search** — Each concept is searched via DuckDuckGo to gather grounding context.
3. **Structured analysis** — The item content and search results are sent to AI, which produces:
   - `whats_new` — what specifically happened or changed
   - `why_it_matters` — significance and impact
   - `key_details` — notable policy, market, or operational details and caveats
   - `background` — background knowledge for readers without deep domain expertise

These fields are combined into a `detailed_summary` stored in the item's metadata and used in the final daily summary.
