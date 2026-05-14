---
name: landing-page-intel
description: >
  Extract competitor and customer intelligence from any company's landing page HTML.
  Discovers tech stack, analytics tools, ad pixels, customer logos, SEO metadata,
  CTAs, hidden elements, and more. No API keys required.
tags: [competitive-intel, scraping, research]
description_pt-BR: >
  Analisa qualquer URL de landing page: posicionamento, estrutura de copy, estratégia de conversão e padrões de persuasão. Útil para benchmarking competitivo e melhoria de copy própria.
type: playbook
---

# Landing Page Intel

**Core principle:** Landing pages revelam o gap entre o que a marca diz e o que converte.

Extract GTM-relevant intelligence from any company's landing page by scraping its HTML source.

## Quick Start

Only dependency is `pip install requests`. No API key needed.

```bash
# Basic scan of a single URL
python3 skills/landing-page-intel/scripts/scrape_landing_page.py \
  --url "https://example.com"

# Scan multiple pages of the same site
python3 skills/landing-page-intel/scripts/scrape_landing_page.py \
  --url "https://example.com" --pages "/,/pricing,/about"

# Output as summary table instead of JSON
python3 skills/landing-page-intel/scripts/scrape_landing_page.py \
  --url "https://example.com" --output summary

# Save full report to file
python3 skills/landing-page-intel/scripts/scrape_landing_page.py \
  --url "https://example.com" --output json > report.json
```

## What It Extracts

| Category | Details |
|----------|---------|
| **Tech Stack** | Analytics (GA4, Mixpanel, Amplitude, PostHog, Heap), marketing automation (HubSpot, Marketo, Pardot), chat widgets (Intercom, Drift, Crisp, Zendesk), A/B testing (Optimizely, VWO, LaunchDarkly), session recording (Hotjar, FullStory, LogRocket), CDPs (Segment, Clearbit, 6sense) |
| **Ad Pixels** | Meta Pixel, Google Ads, LinkedIn Insight Tag, TikTok pixel, Twitter pixel |
| **Customer Logos** | Image URLs from "trusted by" / logo carousel sections, grouped by directory |
| **SEO Metadata** | Title, meta description, Open Graph tags, Twitter Cards, canonical URL, structured data (JSON-LD), hreflang tags |
| **CTAs & Sales Motion** | All CTA button text and links — reveals PLG vs sales-led motion |
| **Social Proof** | Testimonials, customer counts, case study links, badge images |
| **Integrations** | Links to integration/partner pages, embedded third-party widgets |
| **Hidden Elements** | Content in `display:none`, `hidden`, or HTML comments that may reveal upcoming features |
| **Infrastructure** | CMS platform (Webflow, WordPress, Next.js, etc.), detected from HTML signatures |

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | *required* | Target website URL |
| `--pages` | `/` | Comma-separated paths to scan (e.g., `/,/pricing,/about`) |
| `--output` | `json` | Output format: `json` or `summary` |
| `--timeout` | `15` | Request timeout in seconds |

## GTM Use Cases

- **Competitive intel**: See what tools competitors use, how they position, who their customers are
- **Prospect research**: Before a sales call, scan a prospect's site to understand their stack and maturity
- **Market mapping**: Scan multiple competitors to compare positioning, customer segments, and GTM motions
- **Customer discovery**: Extract competitor customer logos as potential prospects for your own product

## Cost

Free. No API keys required. Uses only HTTP requests to fetch public HTML.

## When to Use

Use `landing-page-intel` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Prerequisites

### Environment Variables

```env
# Nenhuma variável obrigatória
```

### Dependencies

`WebFetch` + scripts em `scripts/` (ver pasta). Rodar com Python 3.11+.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Target URL(s)** | Yes | URL(s) to scrape |
| **Keywords/Query** | Varies | Search terms or filters |
| **API credentials** | Yes | API key (set via environment variable) |
| **Output format** | No | `json` (default) or `csv` |


## Phase 0: Intake

1. **URL alvo** — Landing page específica (não site inteiro).
2. **Contexto comparativo** — Auditar isolada, ou comparar com 2-3 concorrentes?
3. **Objetivo** — Diagnóstico de conversão, replicação de padrões, ou battlecard contra essa LP?
4. **Profundidade** — `quick` (above-the-fold) ou `deep` (jornada completa)?

## Output Format

| Output | Format | Location |
|---|---|---|
| **Raw data** | JSON or CSV | Current working directory or specified path |
| **Summary** | Markdown table | Displayed to user in terminal |
| **Error log** | Inline notes | Included in output when sources fail |

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
| **Key findings** | `[OPERACIONAL]: landing-page-intel — [finding]` | `[OPERACIONAL]: landing-page-intel — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: landing-page-intel — [param] works better as [value]` | `[OPERACIONAL]: landing-page-intel — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: landing-page-intel — [insight]` | `[ESTRATÉGICO]: landing-page-intel — Competitor X has no case studies page, vulnerability for battlecard` |

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

---

## Conclave Output Convention

Quando rodado dentro de um squad Conclave, o output canônico segue:

Write to `squads/{code}/output/lp-intel-{slug}.md`.

Report:
```
Landing Page Intel — output:
— URL analisada: {url}
— Seções mapeadas: {N}
— CTAs encontrados: {N}
— Estratégia: {conversion strategy type}
— Arquivo: output/lp-intel-{slug}.md
```
