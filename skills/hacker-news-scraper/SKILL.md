---
name: hacker-news-scraper
description: >
  Search Hacker News stories and comments using the free Algolia API.
  No Apify token needed. Use when you need to find HN discussions, track mentions,
  discover Show HN launches, or monitor tech community sentiment.
tags: [scraping, monitoring, research]
---

# Hacker News Scraper

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Search Hacker News using the free [Algolia HN Search API](https://hn.algolia.com/api). No Apify token or API key needed.

## Quick Start

Only dependency: `pip install requests`.

```bash
# Stories about AI content marketing in last week
python3 skills/hacker-news-scraper/scripts/search_hn.py \
  --query "AI content marketing" --days 7

# Show HN posts in last month (summary view)
python3 skills/hacker-news-scraper/scripts/search_hn.py \
  --query "" --tags show_hn --days 30 --output summary

# Comments mentioning a specific tool
python3 skills/hacker-news-scraper/scripts/search_hn.py \
  --query "LangChain" --tags comment --days 14 --max-results 20
```

## How the Script Works

1. Queries the Algolia HN Search API (`search_by_date` endpoint)
2. Uses `numericFilters=created_at_i>{unix_timestamp}` for server-side date filtering
3. Paginates until max-results reached
4. Normalizes results to a consistent schema
5. Applies optional keyword filtering (client-side)
6. Sorts by points (descending) and outputs JSON or summary

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--query` | *required* | Search query |
| `--days` | 7 | How many days back to search |
| `--tags` | story | Item type: `story`, `comment`, `ask_hn`, `show_hn` |
| `--max-results` | 50 | Max results to return |
| `--keywords` | none | Additional filter keywords (comma-separated, OR logic) |
| `--output` | json | Output format: `json` or `summary` |

## Output Format

```json
{
  "id": "12345678",
  "title": "Show HN: My new tool",
  "url": "https://example.com",
  "author": "username",
  "points": 42,
  "num_comments": 15,
  "created_at": "2026-02-18T12:00:00.000Z",
  "hn_url": "https://news.ycombinator.com/item?id=12345678",
  "text": ""
}
```

## Cost

**Free.** No API key, no rate limits (within reason), no Apify credits.


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

## When to Use

Use `hacker-news-scraper` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Keywords/Query** | Varies | Search terms or filters |
| **API credentials** | Yes | API key (set via environment variable) |
| **Output format** | No | `json` (default) or `csv` |

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

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `cold-email-outreach`
- `competitor-intel`
- `content-asset-creator`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`
- `linkedin-outreach`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: hacker-news-scraper — [finding]` | `[OPERACIONAL]: hacker-news-scraper — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: hacker-news-scraper — [param] works better as [value]` | `[OPERACIONAL]: hacker-news-scraper — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: hacker-news-scraper — [insight]` | `[ESTRATÉGICO]: hacker-news-scraper — Competitor X has no case studies page, vulnerability for battlecard` |

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

