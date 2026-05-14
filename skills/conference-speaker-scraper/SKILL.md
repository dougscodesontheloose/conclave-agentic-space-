---
name: conference-speaker-scraper
description: >
  Extract speaker names, titles, companies, and bios from conference websites.
  Supports direct HTML scraping and Apify web scraper fallback for JS-heavy sites.
  Use for pre-event research and outreach targeting.
tags: [scraping, lead-generation, events]
---

# Conference Speaker Scraper

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Extract speaker names, titles, companies, and bios from conference website /speakers pages. Supports direct HTML scraping with multiple extraction strategies, plus Apify fallback for JS-heavy sites.

## Quick Start

No API key needed for direct scraping mode.

```bash
# Scrape speakers from a conference page
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py \
  --url "https://example.com/speakers"

# Use Apify for JS-heavy sites
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py \
  --url "https://example.com/speakers" --mode apify

# Custom conference name (otherwise inferred from URL)
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py \
  --url "https://example.com/speakers" --conference "Sage Future 2026"

# Output formats
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py --url URL --output json     # default
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py --url URL --output csv
python3 skills/conference-speaker-scraper/scripts/scrape_speakers.py --url URL --output summary
```

## How It Works

### Direct Mode (default)

Fetches the page HTML and tries multiple extraction strategies in order, using whichever returns the most results:

1. **Strategy A -- CSS class hints:** Looks for speaker cards with class names containing "speaker", "presenter", "faculty", "panelist", "team-member"
2. **Strategy B -- Heading + paragraph patterns:** Looks for repeated `<h2>`/`<h3>` + `<p>` structures
3. **Strategy C -- JSON-LD structured data:** Checks for `<script type="application/ld+json">` with speaker data
4. **Strategy D -- Platform embeds:** Detects Sched.com/Sessionize patterns used by many conferences

### Apify Mode

Uses `apify/cheerio-scraper` actor with a custom page function that targets common speaker card selectors. Standard POST/poll/GET dataset pattern.

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | *required* | Conference speakers page URL |
| `--conference` | inferred | Conference name (otherwise inferred from URL domain) |
| `--mode` | direct | `direct` (HTML scraping) or `apify` (Apify cheerio scraper) |
| `--output` | json | Output format: `json`, `csv`, or `summary` |
| `--token` | env var | Apify token (only needed for apify mode) |
| `--timeout` | 300 | Max seconds for Apify run |

## Output Schema

```json
{
  "name": "Jane Smith",
  "title": "VP of Finance",
  "company": "Acme Corp",
  "bio": "Jane leads the finance transformation at...",
  "linkedin_url": "https://linkedin.com/in/janesmith",
  "image_url": "https://...",
  "conference": "Sage Future 2026",
  "source_url": "https://sagefuture2026.com/speakers"
}
```

## Cost

- **Direct mode:** Free (no API, no tokens)
- **Apify mode:** Uses `apify/cheerio-scraper` -- minimal Apify credits

## Testing Notes

HTML scraping is inherently fragile across conference sites. The multi-strategy approach maximizes coverage, but JS-heavy sites will require Apify mode. When direct scraping returns 0 results, try `--mode apify`.


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

Use `conference-speaker-scraper` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Target URL(s)** | Yes | URL(s) to scrape |
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
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `cold-email-outreach`
- `competitor-intel`
- `contact-cache`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`
- `linkedin-message-writer`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: conference-speaker-scraper — [finding]` | `[OPERACIONAL]: conference-speaker-scraper — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: conference-speaker-scraper — [param] works better as [value]` | `[OPERACIONAL]: conference-speaker-scraper — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: conference-speaker-scraper — [insight]` | `[ESTRATÉGICO]: conference-speaker-scraper — Competitor X has no case studies page, vulnerability for battlecard` |

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

