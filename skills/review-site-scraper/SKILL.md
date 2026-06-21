---
name: review-site-scraper
description: >
  Scrape product reviews from G2, Capterra, and Trustpilot using Apify.
  Single script with platform dispatch. Use when you need to monitor competitor
  reviews, track product sentiment, or gather customer feedback from review sites.
tags: [scraping, competitive-intel, monitoring]
---

# Review Site Scraper

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Scrape product reviews from G2, Capterra, and Trustpilot using platform-specific Apify actors.

## Quick Start

Requires `APIFY_API_TOKEN` env var (or `--token` flag). No external dependencies needed (uses stdlib `urllib`).

```bash
# Trustpilot reviews
python3 skills/capabilities/review-site-scraper/scripts/scrape_reviews.py \
  --platform trustpilot \
  --url "https://www.trustpilot.com/review/example.com" \
  --max-reviews 10 --output summary

# G2 reviews with keyword filter
python3 skills/capabilities/review-site-scraper/scripts/scrape_reviews.py \
  --platform g2 \
  --url "https://www.g2.com/products/example/reviews" \
  --keywords "pricing,support"

# Capterra reviews (uses company name, not URL)
python3 skills/capabilities/review-site-scraper/scripts/scrape_reviews.py \
  --platform capterra \
  --company-name "HubSpot CRM" \
  --max-reviews 20
```

## Supported Platforms

| Platform | Actor | Input | Cost |
|----------|-------|-------|------|
| G2 | `focused_vanguard/g2-reviews-scraper` | `--url` (G2 product page URL) | Free tier available |
| Capterra | `getdataforme/capterra-reviews-scraper-bulk` | `--company-name` (company name, not a URL) | Pay-per-result |
| Trustpilot | `agents/trustpilot-reviews` | `--url` (Trustpilot review page URL) | ~$0.20/1k reviews |

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--platform` | *required* | `g2`, `capterra`, or `trustpilot` |
| `--url` | none | Product review page URL (required for G2 and Trustpilot) |
| `--company-name` | none | Company name to search (Capterra only) |
| `--max-reviews` | 50 | Max reviews to scrape |
| `--keywords` | none | Keywords to filter (comma-separated, OR logic) |
| `--days` | none | Only include reviews from last N days |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (prefer `APIFY_API_TOKEN` env var) |
| `--timeout` | 300 | Max seconds for Apify run |

## Normalized Output Schema

All platforms are normalized but each has platform-specific fields.

**G2 output fields:**

```json
{
  "platform": "g2",
  "id": "review-id",
  "product_name": "Product Name",
  "title": null,
  "text": "Review body text",
  "rating": 4,
  "author": "Reviewer Name",
  "author_title": "Job Title",
  "author_company": "Company Name",
  "author_company_size": "51-200",
  "author_industry": "Software",
  "date": "2026-02-18",
  "source": "organic",
  "url": "https://..."
}
```

**Capterra output fields:**

```json
{
  "platform": "capterra",
  "title": "Review title",
  "text": "Review body text",
  "overall_rating": 4,
  "ease_of_use": 5,
  "customer_service": 3,
  "features": 4,
  "author": "Reviewer Name",
  "job_title": "Marketing Manager",
  "industry": "Marketing and Advertising",
  "usage_duration": "1-2 years",
  "date": "2026-02-18",
  "url": "https://..."
}
```

**Trustpilot output fields:**

```json
{
  "platform": "trustpilot",
  "id": "review-id",
  "title": "Review title",
  "text": "Review body text",
  "rating": 4,
  "author": "Reviewer Name",
  "date": "2026-02-18T12:00:00.000Z",
  "experienced_date": "2026-02-15T00:00:00.000Z",
  "likes": 2,
  "input_source": "organic",
  "url": "https://..."
}
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

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `campaign-brief-generator`
- `competitor-intel`
- `customer-discovery`
- `industry-scanner`
- `launch-positioning-builder`
- `lead-qualification`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: review-site-scraper — [finding]` | `[OPERACIONAL]: review-site-scraper — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: review-site-scraper — [param] works better as [value]` | `[OPERACIONAL]: review-site-scraper — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: review-site-scraper — [insight]` | `[ESTRATÉGICO]: review-site-scraper — Competitor X has no case studies page, vulnerability for battlecard` |

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
