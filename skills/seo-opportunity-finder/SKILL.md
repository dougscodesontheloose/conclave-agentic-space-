---
name: seo-opportunity-finder
description: >
  Find quick-win SEO content opportunities by comparing your site's existing content
  against competitor keyword rankings. Chains site-content-catalog and seo-domain-analyzer
  to build a content inventory, then identifies gaps — topics competitors rank for that
  you don't cover yet. Outputs a prioritized list of posts to write or update.
  Use when a seed/Series A team wants to start winning organic traffic without guessing.
tags: [seo]
---

# SEO Opportunity Finder

Identify the highest-leverage content gaps between your site and competitors. Combines a crawl of your existing content with competitor keyword/traffic analysis to surface a prioritized list of posts worth writing.

**Core principle:** Don't start from a blank keyword list. Start by knowing what you have, then find what competitors have that you don't — and pick the gaps most likely to convert.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

- "Find SEO content gaps vs our competitors"
- "What topics should we write about to rank?"
- "We're starting a blog — where should we focus first?"
- "What keywords are [competitor] ranking for that we're missing?"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Phase 0: Intake

1. Your website URL (e.g., `https://yourcompany.com`)
2. 2-3 competitor URLs to compare against
3. Primary ICP — who are you trying to attract? (This filters for commercial intent vs. general traffic)
4. Any topics/keyword themes that are definitely in scope? (Optional — helps prioritize output)

## Phase 1: Catalog Your Existing Content

Build an inventory of the target site's current pages and posts:

1. Fetch sitemap.xml (check `/sitemap.xml`, `/sitemap_index.xml`, `robots.txt` for `Sitemap:` directives)
2. Fall back to RSS feeds (`/feed`, `/blog/feed`) or blog index crawl if no sitemap
3. Extract: all blog post titles and URLs, inferred topics/themes per post, estimated content age

This prevents recommending content you've already written.

## Phase 2: Analyze Competitor SEO Footprint

For each competitor domain, pull SEO metrics:

1. **Domain overview** — authority score, organic traffic estimate, top ranking keywords (via Apify Semrush scraper if `APIFY_API_TOKEN` is set)
2. **Top pages** — highest-traffic pages and their primary keywords
3. **Keyword categories** — which topic clusters they're winning in

If Apify data is limited, supplement with web search probes:
- `site:[competitor]` for indexed page count
- Search target keywords and note which competitors rank where
- SimilarWeb free tier for traffic estimates

## Phase 3: Identify Gaps

Compare your content inventory (Phase 1) against competitor keyword/topic coverage (Phase 2):

### Gap Classification

| Type | Definition | Priority |
|------|------------|----------|
| **Hard gap** | Competitor has a page/post on topic, you have nothing | High |
| **Soft gap** | You have content on topic but it's thin (< 500 words, old, no depth) | Medium |
| **Positioning gap** | Competitor owns a keyword cluster that maps to your ICP's exact problem | High |
| **Informational gap** | High traffic, low commercial intent — good for awareness, not conversion | Low |

### Commercial Intent Filter

For each gap topic, score commercial intent (1-5):
- **5** — Directly maps to your product (e.g., "best AI SDR tools for startups")
- **4** — Problem-aware but not product-specific (e.g., "how to scale outbound SDR")
- **3** — Adjacent pain point (e.g., "cold email open rates benchmark 2026")
- **2** — Educational, tangential (e.g., "what is lead scoring")
- **1** — Generic traffic, low conversion potential

Prioritize gaps with score ≥ 3.

## Phase 4: Synthesize & Output

Produce a prioritized opportunity table + editorial brief starters:

```markdown
# SEO Opportunity Report — [Your Company] vs [Competitors]
Generated: [DATE]

## Your Content Snapshot
- Total indexed pages: [N]
- Blog posts: [N]
- Main topic clusters: [list]

## Competitor Benchmarks
| Domain | DR | Est. Monthly Organic Traffic | Top Keyword Clusters |
|--------|----|-----------------------------|----------------------|
| [comp1] | [X] | [X] | [topics] |
| [comp2] | [X] | [X] | [topics] |

## Top 10 Content Opportunities

### 1. [Topic/Title Suggestion]
- **Keyword target:** [keyword phrase]
- **Why it matters:** [what problem it solves for ICP]
- **Competitor owning it:** [competitor URL]
- **Est. monthly searches:** [range]
- **Commercial intent score:** [1-5]
- **Recommended format:** [listicle / how-to / comparison / landing page]
- **Estimated effort:** [hours or word count target]

### 2. [Topic/Title Suggestion]
...

## Quick Wins (update existing posts)

| Your Post | Issue | What to Add |
|-----------|-------|-------------|
| [URL] | [thin/outdated] | [recommendation] |

## Recommended Content Calendar (Next 90 Days)

| Month | Post | Intent Score | Est. Traffic Potential |
|-------|------|-------------|----------------------|
| Month 1 | [post 1] | [score] | [range] |
| Month 1 | [post 2] | [score] | [range] |
| Month 2 | [post 3] | [score] | [range] |
...
```

Save to the current working directory or wherever the user prefers.

## Cost

| Component | Cost |
|-----------|------|
| Site content catalog | Free (sitemap crawl) |
| SEO domain analyzer (per competitor) | ~$1-3 (Apify Semrush scraper) |
| Traffic analyzer (supplement) | ~$0.10-0.50 (web search probes) |
| **Total per run** | **~$3-10 for 3 competitors** |

## Tools Required

- **Apify API token** — `APIFY_API_TOKEN` env var (for Semrush/Ahrefs data; free web search probes work without it)
- Web search and web fetch capabilities

## Trigger Phrases

- "Find our SEO content gaps"
- "What should we write about to rank?"
- "Compare our content coverage to [competitor]"
- "Run SEO opportunity finder for [client]"

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **API/tool unavailable** | HTTP error, timeout, or command failure | Log the specific error. Attempt retry once. If still failing, skip and note in output |
| **Insufficient input data** | Missing required fields or empty dataset | Prompt user for missing data. Do not proceed with assumptions on critical fields |
| **Unexpected data format** | Parse error or schema mismatch | Log the raw response snippet. Attempt best-effort parsing. Flag `⚠️ Data format unexpected` |
| **Rate limiting** | HTTP 429 or throttle signal | Implement exponential backoff (1s → 2s → 4s). Max 3 retries |
| **Partial results** | Some sources succeed, others fail | Deliver partial results with clear indication of which sources failed and why |

**Principle:** Every execution must produce either a result or a clear, actionable error message. Silent failures are unacceptable.


## Composability

**Receives data from:**
- Skills tagged `seo-domain-analyzer` (e.g., data collection and enrichment)
- Skills tagged `site-content-catalog` (e.g., data collection and enrichment)

**Feeds into:**
- `content-brief-factory`
- `seo-content-engine`
- `topical-authority-mapper`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: seo-opportunity-finder — [finding]` | `[OPERACIONAL]: seo-opportunity-finder — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: seo-opportunity-finder — [param] works better as [value]` | `[OPERACIONAL]: seo-opportunity-finder — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: seo-opportunity-finder — [insight]` | `[ESTRATÉGICO]: seo-opportunity-finder — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Source diversity:** Findings are supported by at least 2 independent sources
- [ ] **Recency check:** Key data points are from the last 12 months (or explicitly flagged as older)
- [ ] **Confidence labeling:** Every finding has a confidence level (high/medium/low)
- [ ] **Actionability:** Report includes at least 1 concrete next step or recommendation
- [ ] **User checkpoint:** Present key findings summary before generating the full report

**If any check fails:** Note the gap explicitly in the output rather than omitting it.

