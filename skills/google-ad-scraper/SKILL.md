---
name: google-ad-scraper
description: Scrape competitor ads from Google Ads by domain. Returns ad creatives, formats, and campaign details. Use for competitive ad research and messaging analysis.
tags: [ads, scraping, competitive-intel]
---

# Google Ads Scraper

**Core principle:** Você não compra cliques, você compra a atenção fracionada do seu melhor cliente.


Scrape ads from Google Ads using the Apify `burbn/google-ads-search` actor. Search by domain to get ad creatives, formats, and campaign details.

## Quick Start

Requires `APIFY_API_TOKEN` env var (or `--token` flag).

```bash
# Search by domain (recommended)
python3 skills/google-ad-scraper/scripts/search_google_ads.py \
  --domain "hubspot.com"

# Search by company name (resolves to domain via transparency center)
python3 skills/google-ad-scraper/scripts/search_google_ads.py \
  --company "Nike"

# Limit results
python3 skills/google-ad-scraper/scripts/search_google_ads.py \
  --domain "hubspot.com" --max-ads 30

# Human-readable summary
python3 skills/google-ad-scraper/scripts/search_google_ads.py \
  --domain "stripe.com" --output summary
```

## How It Works

1. **Domain Input**: Pass the target company's domain directly via `--domain`
2. **Company Name Resolution** (optional): If only `--company` is provided, the script searches Google Ads Transparency Center using Apify's web-scraper (Puppeteer) to resolve the company name to advertiser info
3. **Ad Scraping**: Calls the Apify `burbn/google-ads-search` actor with `{"domain": "...", "maxItems": N}`
4. **Output**: Returns ads as JSON or human-readable summary

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--domain` | none | Company domain (e.g. hubspot.com) — recommended |
| `--company` | none | Company name (resolved to domain via transparency center) |
| `--max-ads` | 50 | Maximum number of ads to return |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (prefer `APIFY_API_TOKEN` env var) |
| `--timeout` | 300 | Max seconds to wait for Apify run |

At least one of `--company` or `--domain` is required.

## Output Fields

Each ad in the output contains:

```json
{
  "advertiserId": "AR13129532367502835713",
  "advertiserName": "Nike, Inc.",
  "creativeId": "CR12345678901234567890",
  "originalUrl": "https://www.nike.com/",
  "imageUrl": "https://...",
  "variantFormat": "TEXT",
  "variantContent": "Shop the latest Nike shoes...",
  "variants": [...],
  "variantCount": 3,
  "startDate": "2026-01-15"
}
```

**Output fields:**

| Field | Description |
|-------|-------------|
| `advertiserId` | Google Ads advertiser ID |
| `advertiserName` | Company/advertiser display name |
| `creativeId` | Unique ID for the ad creative |
| `originalUrl` | Destination URL the ad links to |
| `imageUrl` | URL of the ad image (if applicable) |
| `variantFormat` | Ad format (TEXT, IMAGE, VIDEO, etc.) |
| `variantContent` | Ad copy/text content |
| `variants` | Array of ad variants |
| `variantCount` | Number of variants for this creative |
| `startDate` | Date the ad first appeared |

## Cost

- Ad scraping: Varies by actor pricing, typically a few cents per domain
- Company name resolution (optional): ~$0.05 (one web-scraper page)

## Common Workflows

### 1. Competitor Ad Research

```bash
python3 skills/google-ad-scraper/scripts/search_google_ads.py \
  --domain "competitor.com" --max-ads 100 --output summary
```

### 2. Compare Multiple Competitors

```bash
# Run for each competitor domain
for domain in "competitor1.com" "competitor2.com" "competitor3.com"; do
  python3 skills/google-ad-scraper/scripts/search_google_ads.py \
    --domain "$domain" --max-ads 50
done
```

## Limitations

- **Company name resolution** uses Puppeteer-based web scraping of Google's SPA. It may occasionally fail — use `--domain` for best results.
- **Ad coverage**: Google only shows ads from verified advertisers. Some smaller advertisers may not appear.
- **Historical data**: Primarily shows recently active ads.

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

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: google-ad-scraper — [finding]` | `[OPERACIONAL]: google-ad-scraper — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: google-ad-scraper — [param] works better as [value]` | `[OPERACIONAL]: google-ad-scraper — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: google-ad-scraper — [insight]` | `[ESTRATÉGICO]: google-ad-scraper — Competitor X has no case studies page, vulnerability for battlecard` |

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

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
