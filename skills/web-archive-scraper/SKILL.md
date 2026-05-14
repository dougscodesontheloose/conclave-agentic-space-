---
name: web-archive-scraper
description: >
  Search the Wayback Machine for archived versions of websites. Extract cached pages,
  customer lists, testimonials, and partner directories from sites that have changed or
  gone offline. Uses the free CDX API — no API key needed.
tags: [scraping, research, competitive-intel]
---

# Web Archive Scraper

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Search the Wayback Machine (Internet Archive) for archived snapshots of websites. Fetch cached page content to find customer lists, testimonials, partner directories, and other information from sites that have changed or shut down.

## Quick Start

Only dependency is `requests`. No API key needed.

```bash
# Find all snapshots of a URL
python3 skills/web-archive-scraper/scripts/search_archive.py \
  --url "https://botkeeper.com/customers"

# Search with date range
python3 skills/web-archive-scraper/scripts/search_archive.py \
  --url "https://botkeeper.com" --from 2025-01-01 --to 2026-02-01

# Search all pages under a domain (prefix match)
python3 skills/web-archive-scraper/scripts/search_archive.py \
  --url "https://botkeeper.com" --match prefix --limit 50

# Fetch the actual archived page content
python3 skills/web-archive-scraper/scripts/search_archive.py \
  --url "https://botkeeper.com/customers" --fetch

# Output formats
python3 skills/web-archive-scraper/scripts/search_archive.py --url URL --output json
python3 skills/web-archive-scraper/scripts/search_archive.py --url URL --output csv
python3 skills/web-archive-scraper/scripts/search_archive.py --url URL --output summary
```

## How It Works

1. **CDX API search** — Queries `web.archive.org/cdx/search/cdx` for snapshots matching the URL
2. **Filtering** — Filters by date range, HTTP status code, and MIME type
3. **Dedup** — Collapses to one snapshot per day by default to avoid redundant results
4. **Content fetch** — Optionally fetches the raw archived HTML (using `id_` modifier to skip Wayback toolbar)
5. **Text extraction** — Strips HTML tags for readable text output when fetching content

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | *required* | Target URL to search in the archive |
| `--match` | exact | Match type: `exact`, `prefix`, `host`, `domain` |
| `--from` | none | Start date (YYYY-MM-DD) |
| `--to` | none | End date (YYYY-MM-DD) |
| `--limit` | 25 | Max number of snapshots to return |
| `--fetch` | false | Fetch and display the content of the most recent snapshot |
| `--fetch-all` | false | Fetch content of ALL matched snapshots (use with small --limit) |
| `--status` | 200 | HTTP status filter (set to "any" to include all) |
| `--output` | json | Output format: `json`, `csv`, `summary` |
| `--collapse` | day | Dedup level: `none`, `day`, `month`, `year` |

## Output Schema

```json
{
  "url": "https://botkeeper.com/customers",
  "timestamp": "20250915143022",
  "datetime": "2025-09-15T14:30:22",
  "status_code": "200",
  "mime_type": "text/html",
  "archive_url": "https://web.archive.org/web/20250915143022/https://botkeeper.com/customers",
  "raw_url": "https://web.archive.org/web/20250915143022id_/https://botkeeper.com/customers",
  "content": "..."
}
```

The `content` field is only populated when `--fetch` or `--fetch-all` is used.

## Cost

Free. The Wayback Machine CDX API requires no authentication or API key. Rate limit is ~15 requests/minute.

## Common Use Cases

- **Find customer lists from shut-down companies** (e.g., botkeeper.com)
- **Recover testimonials/case studies** before a site redesign
- **Track how a competitor's messaging changed over time**
- **Find partner directories** that have been removed

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
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `campaign-brief-generator`
- `cold-email-outreach`
- `competitor-intel`
- `content-asset-creator`
- `customer-discovery`
- `industry-scanner`
- `launch-positioning-builder`
- `lead-qualification`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: web-archive-scraper — [finding]` | `[OPERACIONAL]: web-archive-scraper — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: web-archive-scraper — [param] works better as [value]` | `[OPERACIONAL]: web-archive-scraper — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: web-archive-scraper — [insight]` | `[ESTRATÉGICO]: web-archive-scraper — Competitor X has no case studies page, vulnerability for battlecard` |

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
