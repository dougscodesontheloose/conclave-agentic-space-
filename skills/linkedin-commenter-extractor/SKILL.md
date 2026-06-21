---
name: linkedin-commenter-extractor
description: >
  Extract commenters from LinkedIn posts via Apify. Returns commenter names, titles,
  LinkedIn profile URLs, and comment text. Use to find warm leads engaging with
  relevant discussions. No LinkedIn cookies required.
tags: [scraping, linkedin, lead-generation]
---

# LinkedIn Commenter Extractor

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Extract names, titles, companies, LinkedIn URLs, and comment text from people who commented on specific LinkedIn posts. Uses Apify — no LinkedIn cookies required.

## Quick Start

Requires `requests` and `APIFY_API_TOKEN` environment variable.

```bash
# Extract commenters from a single post
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py \
  --post-url "https://www.linkedin.com/posts/someone_topic-activity-123456789"

# Multiple posts
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py \
  --post-url URL1 --post-url URL2

# Limit comments per post
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py \
  --post-url URL --max-comments 50

# Output formats
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py --post-url URL --output json
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py --post-url URL --output csv
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py --post-url URL --output summary

# Deduplicate across multiple posts
python3 skills/linkedin-commenter-extractor/scripts/extract_commenters.py \
  --post-url URL1 --post-url URL2 --dedup
```

## How It Works

1. Takes one or more LinkedIn post URLs
2. Calls the `harvestapi~linkedin-post-comments` Apify actor (no cookies needed)
3. Extracts commenter name, headline (title + company), LinkedIn profile URL, and comment text
4. Parses headline into separate title and company fields where possible
5. Optionally deduplicates across multiple posts by LinkedIn profile URL

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--post-url` | *required* | LinkedIn post URL (can be repeated for multiple posts) |
| `--max-comments` | 100 | Max comments to extract per post |
| `--output` | json | Output format: `json`, `csv`, `summary` |
| `--dedup` | false | Deduplicate commenters across multiple posts |
| `--token` | env var | Apify API token (overrides APIFY_API_TOKEN env var) |
| `--timeout` | 120 | Max seconds to wait for Apify run |

## Output Schema

```json
{
  "name": "Jane Smith",
  "headline": "VP of Finance at Acme Corp",
  "title": "VP of Finance",
  "company": "Acme Corp",
  "linkedin_url": "https://www.linkedin.com/in/janesmith",
  "comment_text": "Great insights on AI in accounting...",
  "post_url": "https://www.linkedin.com/posts/...",
  "profile_image_url": "https://..."
}
```

## Cost

Uses `harvestapi~linkedin-post-comments` Apify actor — ~$2 per 1,000 comments. No LinkedIn cookies or login required.


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

Use `linkedin-commenter-extractor` when you need to:
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
| **Key findings** | `[OPERACIONAL]: linkedin-commenter-extractor — [finding]` | `[OPERACIONAL]: linkedin-commenter-extractor — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: linkedin-commenter-extractor — [param] works better as [value]` | `[OPERACIONAL]: linkedin-commenter-extractor — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: linkedin-commenter-extractor — [insight]` | `[ESTRATÉGICO]: linkedin-commenter-extractor — Competitor X has no case studies page, vulnerability for battlecard` |

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

