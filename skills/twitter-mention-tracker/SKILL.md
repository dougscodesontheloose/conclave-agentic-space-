---
name: twitter-mention-tracker
description: >
  Search and scrape Twitter/X posts using Apify. Use when you need to find tweets,
  track brand mentions, monitor competitors on Twitter, or analyze Twitter discussions.
  Uses Twitter native search syntax (since:/until:) for reliable date filtering.
tags: [scraping, monitoring, social-media]
---

# Twitter Mention Tracker

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Search Twitter/X posts using the Apify `apidojo/tweet-scraper` actor.

## Quick Start

Requires `APIFY_API_TOKEN` env var (or `--token` flag).

```bash
# Search with date range (recommended -- uses Twitter native since:/until: operators)
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "YourCompany" --since 2026-02-15 --until 2026-02-23

# Quick summary of recent mentions
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "@yourhandle" --max-tweets 20 --output summary

# Search without date filtering
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "AI content marketing" --max-tweets 50
```

## Date Filtering

**Important:** The `apidojo/tweet-scraper` actor's built-in date parameters are unreliable.
This script embeds `since:YYYY-MM-DD` and `until:YYYY-MM-DD` directly into the search query
string, using Twitter's native advanced search syntax. This ensures date filtering works
correctly server-side.

## How the Script Works

1. Builds a search term with the query quoted and date operators appended
2. Calls the Apify `apidojo/tweet-scraper` actor via REST API
3. Polls until the run completes, then fetches the dataset
4. Deduplicates by tweet ID/URL
5. Applies optional keyword filtering (client-side)
6. Sorts by likes (descending) and outputs JSON or summary

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--query` | *required* | Search query (quoted in Twitter search) |
| `--since` | none | Start date YYYY-MM-DD (inclusive) |
| `--until` | none | End date YYYY-MM-DD (exclusive) |
| `--max-tweets` | 50 | Max tweets to scrape |
| `--keywords` | none | Additional filter keywords (comma-separated, OR logic) |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (prefer `APIFY_API_TOKEN` env var) |
| `--timeout` | 300 | Max seconds to wait for the Apify run |

## Direct API Usage

```json
{
  "searchTerms": ["\"YourCompany\" since:2026-02-15 until:2026-02-22"],
  "maxTweets": 50,
  "searchMode": "live"
}
```

## Output Format

Tweets are returned as JSON array sorted by likes. Each tweet has:

```json
{
  "id": "...",
  "text": "Tweet text...",
  "fullText": "Full tweet text...",
  "likeCount": 42,
  "retweetCount": 5,
  "replyCount": 3,
  "viewCount": 1200,
  "createdAt": "2026-02-18T12:00:00.000Z",
  "author": {"userName": "handle", "name": "Display Name", ...},
  "twitterUrl": "https://twitter.com/..."
}
```

## Common Workflows

### Competitor Monitoring
```bash
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "CompetitorName" --since 2026-02-15 --until 2026-02-23 --output summary
```

### Brand Mention Tracking
```bash
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "@YourHandle OR \"YourBrand\"" --max-tweets 100
```

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **API rate limit / 429** | HTTP 429 or `rate_limit` in response | Wait 60s, retry with exponential backoff (max 3 retries) |
| **API key missing/invalid** | HTTP 401/403 or env var not set | Log `❌ Missing API key: [VAR_NAME]`. Stop and inform user with setup instructions |
| **Target page structure changed** | Zero results from a previously working source | Log `⚠️ 0 results from [source]`. Continue with other sources, flag in output |
| **Network timeout** | No response within configured timeout | Retry once. If still failing, skip source and note in output |
| **Empty dataset returned** | Valid API response but 0 results | Distinguish "no data exists" vs "query too narrow". Suggest query adjustments |

**Principle:** Never fail silently. Every error must produce a visible log line and a note in the final output.


## Composability


**Feeds into:**
- `competitor-intel`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: twitter-mention-tracker — [finding]` | `[OPERACIONAL]: twitter-mention-tracker — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: twitter-mention-tracker — [param] works better as [value]` | `[OPERACIONAL]: twitter-mention-tracker — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: twitter-mention-tracker — [insight]` | `[ESTRATÉGICO]: twitter-mention-tracker — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Data completeness:** At least 1 source returned results. If all sources failed, the output must explain why
- [ ] **No silent failures:** Every source that was attempted has a status (success/partial/failed) in the output
- [ ] **Deduplication applied:** No duplicate entries in the final dataset
- [ ] **Output format valid:** CSV/JSON is well-formed and parseable
- [ ] **User checkpoint:** Present summary to user before proceeding to downstream skills

**If any check fails:** Stop, report the failure, and ask the user how to proceed.



## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Alvo** — Qual a URL ou fonte específica?
2. **Foco** — Que tipo de dados são mais críticos?
3. **Formato** — JSON, CSV ou Markdown?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
