---
name: site-content-catalog
description: >
  Crawl a website's sitemap and blog index to build a complete content inventory.
  Lists every page with URL, title, publish date, content type, and topic cluster.
  Groups content by category and topic. Optionally deep-reads top N pages for
  quality analysis and funnel stage tagging. Use before SEO audits, content gap
  analysis, or brand voice extraction.
tags: [content, seo]
---

# Site Content Catalog

**Core principle:** Atenção não se aluga com volume, se conquista com densidade.


Crawl a website's sitemap and blog to build a complete content inventory — every page cataloged with URL, title, date, content type, and topic cluster. Groups content by category, identifies publishing patterns, and optionally deep-analyzes top pages.

## Quick Start

```bash
# Basic content inventory
python3 scripts/catalog_content.py --domain "example.com"

# With deep analysis of top 20 pages
python3 scripts/catalog_content.py --domain "example.com" --deep-analyze 20

# Output to specific file
python3 scripts/catalog_content.py --domain "example.com" --output content-inventory.json
```


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Audiência** — Para quem estamos escrevendo/criando?
2. **Tom de Voz** — Qual a diretriz de marca a ser usada?
3. **Canal** — Onde isso será publicado?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## Inputs

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| domain | Yes | — | Domain to catalog (e.g., "example.com") |
| deep-analyze | No | 0 | Number of top pages to deep-read for content analysis |
| output | No | stdout | Path to save JSON output |
| include-non-blog | No | true | Also catalog landing pages, docs, etc. (not just blog) |

## Cost

- **Sitemap/RSS crawling:** Free (direct HTTP requests)
- **Apify sitemap extractor (fallback):** ~$0.50 per site
- **Deep analysis:** Free (WebFetch on individual pages)

## Process

### Phase 1: Discover All Pages

The script attempts multiple methods to find all pages on a site, in order:

#### A) Sitemap.xml
1. Fetch `https://[domain]/sitemap.xml`
2. If it's a sitemap index, recursively fetch all child sitemaps
3. Common alternate locations: `/sitemap_index.xml`, `/sitemap-index.xml`, `/wp-sitemap.xml`
4. Check `robots.txt` for `Sitemap:` directives

#### B) RSS/Atom Feeds
1. Check `/feed`, `/rss`, `/atom.xml`, `/blog/feed`, etc.
2. Extract posts with titles, dates, and URLs
3. RSS typically only surfaces recent content (last 10-50 posts)

#### C) Blog Index Crawl
1. Fetch `/blog`, `/resources`, `/insights`, `/news`, `/articles`
2. Extract links from the page
3. Follow pagination if present (`/blog/page/2`, `?page=2`, etc.)

#### D) Site: Search (fallback)
1. WebSearch: `site:[domain]` to estimate total indexed pages
2. WebSearch: `site:[domain]/blog` to find blog content
3. WebSearch: `site:[domain] intitle:` to discover page title patterns

#### E) Apify Sitemap Extractor (fallback for JS-heavy sites)
- Actor: `onescales/sitemap-url-extractor`
- Use when sitemap.xml is missing and the site is JS-rendered

### Phase 2: Classify Each Page

For each discovered URL, classify by:

#### Content Type
Classify based on URL patterns and page titles:

| Type | URL Patterns | Examples |
|------|-------------|----------|
| `blog-post` | `/blog/`, `/posts/`, `/articles/` | How-to guides, opinion pieces |
| `case-study` | `/case-study/`, `/customers/`, `/success-stories/` | Customer stories |
| `comparison` | `/vs/`, `/compare/`, `/alternative/` | X vs Y pages |
| `landing-page` | `/solutions/`, `/use-cases/`, `/for-/` | Product marketing pages |
| `docs` | `/docs/`, `/help/`, `/documentation/`, `/api/` | Technical documentation |
| `changelog` | `/changelog/`, `/releases/`, `/whats-new/` | Product updates |
| `pricing` | `/pricing/` | Pricing page |
| `about` | `/about/`, `/team/`, `/careers/` | Company pages |
| `legal` | `/privacy/`, `/terms/`, `/security/` | Legal/compliance |
| `resource` | `/resources/`, `/guides/`, `/ebooks/`, `/webinars/` | Gated/downloadable content |
| `glossary` | `/glossary/`, `/dictionary/`, `/terms/` | SEO glossary pages |
| `integration` | `/integrations/`, `/apps/`, `/marketplace/` | Integration pages |
| `other` | — | Anything else |

#### Topic Cluster
Group by extracting topic signals from URL slugs and titles:
- Extract keywords from URL path segments
- Group similar keywords into clusters (e.g., "aws-cost", "cloud-spending", "finops" → "Cloud Cost Management")
- Use simple keyword co-occurrence for clustering

### Phase 3: Analyze Publishing Patterns

From the dated content (primarily blog posts):
- **Total content pieces** by type
- **Publishing frequency:** Posts per month over last 12 months
- **Trend:** Increasing, decreasing, or stable output
- **Recency:** Date of most recent publish
- **Author diversity:** Unique authors (if extractable from RSS)

### Phase 4: Deep Analysis (Optional)

If `--deep-analyze N` is specified, fetch the top N pages (prioritizing blog posts) and extract:
- **Word count** (approximate)
- **Target keyword** (inferred from title + H1 + URL)
- **Funnel stage:** TOFU (awareness), MOFU (consideration), BOFU (decision)
- **Content depth:** Shallow (<500 words), Medium (500-1500), Deep (1500+)
- **Has images/video:** Boolean
- **Has CTA:** Boolean (detected by common CTA patterns)
- **Internal links count**

### Phase 5: Output

#### JSON Output (default)
```json
{
  "domain": "example.com",
  "crawl_date": "2026-02-25",
  "total_pages": 347,
  "discovery_methods": ["sitemap.xml", "rss"],
  "pages": [
    {
      "url": "https://example.com/blog/reduce-aws-costs",
      "title": "How to Reduce Your AWS Bill by 40%",
      "date": "2025-11-15",
      "type": "blog-post",
      "topic_cluster": "Cloud Cost Optimization",
      "deep_analysis": {
        "word_count": 2100,
        "target_keyword": "reduce aws costs",
        "funnel_stage": "TOFU",
        "content_depth": "deep",
        "has_images": true,
        "has_cta": true
      }
    }
  ],
  "summary": {
    "by_type": {"blog-post": 89, "landing-page": 23, "case-study": 12, ...},
    "by_topic": {"Cloud Cost Optimization": 34, "FinOps": 18, ...},
    "publishing_cadence": {
      "posts_per_month_avg": 4.2,
      "trend": "increasing",
      "most_recent": "2026-02-20"
    }
  }
}
```

#### Markdown Summary (also generated)
```markdown
# Content Inventory: example.com
**Crawled:** 2026-02-25 | **Total pages:** 347

## Content by Type
| Type | Count | % |
|------|-------|---|
| Blog Posts | 89 | 25.6% |
| Landing Pages | 23 | 6.6% |
| ...

## Content by Topic Cluster
| Topic | Posts | Most Recent |
|-------|-------|-------------|
| Cloud Cost Optimization | 34 | 2026-02-20 |
| ...

## Publishing Cadence
- Average: 4.2 posts/month
- Trend: Increasing (3.1 → 5.4 over last 6 months)
- Most recent: 2026-02-20

## Full Catalog
| # | Date | Type | Topic | Title | URL |
|---|------|------|-------|-------|-----|
| 1 | 2026-02-20 | blog-post | Cloud Cost | How to Reduce... | https://... |
```

## Tips

- **Sitemap.xml is the best source.** Most well-maintained sites have one. If missing, it's itself an SEO signal (negative).
- **RSS only shows recent content.** If you need the full catalog, sitemap is essential. RSS is supplementary.
- **Deep analysis is optional but valuable.** Use it when feeding into brand-voice-extractor or when you need funnel stage mapping.
- **JS-rendered sites** may need the Apify fallback. Signs: sitemap.xml returns HTML, or blog page returns mostly JavaScript.
- **Combine with seo-domain-analyzer** to overlay traffic data on the content inventory — see which content actually performs.

## Dependencies

- Python 3.8+
- `requests` library (`pip install requests`)
- `APIFY_API_TOKEN` env var (only for Apify fallback mode)

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **External API unavailable** (Gamma, v0) | HTTP error or timeout | Fall back to self-hosted HTML generation. Log `ℹ️ Using HTML fallback` |
| **Font loading failed** | Timeout on font CDN | Use system font stack as fallback. Note in output |
| **Screenshot generation failed** | Playwright/browser error | Provide HTML files and manual screenshot instructions |
| **Content exceeds format limits** | Text overflow or slide count exceeded | Split into multiple units. Warn user about content volume |
| **Brand config missing** | No brand JSON found | Use neutral default palette. Ask user for brand details |

**Principle:** Always produce a deliverable, even if lower fidelity than ideal.


## Composability

**Receives data from:**
- Skills tagged `brand` (e.g., data collection and enrichment)
- Skills tagged `competitive-intel` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `seo-domain-analyzer` (e.g., data collection and enrichment)

**Feeds into:**
- `content-brief-factory`
- `create-html-carousel`
- `create-html-slides`
- `linkedin-outreach`
- `seo-content-engine`
- `topical-authority-mapper`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: site-content-catalog — [finding]` | `[OPERACIONAL]: site-content-catalog — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: site-content-catalog — [param] works better as [value]` | `[OPERACIONAL]: site-content-catalog — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: site-content-catalog — [insight]` | `[ESTRATÉGICO]: site-content-catalog — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Brand consistency:** Colors, fonts, and tone match the brand config (or defaults)
- [ ] **Format compliance:** Output meets platform specs (e.g., 1080×1080 for LinkedIn carousel)
- [ ] **Content density:** No slide/section exceeds readability limits
- [ ] **Link integrity:** All URLs in the output are valid and accessible
- [ ] **User checkpoint:** Present preview to user for approval before final export

**If any check fails:** Generate a corrected version and present both options to the user.

