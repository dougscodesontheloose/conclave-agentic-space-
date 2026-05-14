---
type: playbook
name: competitor-monitoring-system
description: >
  Set up and run ongoing competitive intelligence monitoring for a client.
  Tracks competitor content, ads, reviews, social, and product moves.
tags: [competitive-intel, monitoring, orchestration]
---

# Competitor Monitoring System

**Core principle:** Movimentos do concorrente são sinais; sua resposta é estratégia.


Set up ongoing competitive intelligence for a client. Monitor competitor content, ads, reviews, social presence, and product moves. Produce regular intelligence reports.

## When to Use

- "Set up competitor monitoring for [client]"
- "Track what [competitors] are doing"
- "Monitor [competitor] content and ads"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Prerequisites

- List of competitors to track (typically 3-7)
- Client context with competitive positioning
- Competitor founder/executive LinkedIn profiles (for social monitoring)


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Entidade alvo** — Empresa, pessoa ou tendência?
2. **Profundidade** — Visão geral (quick) ou análise profunda (deep)?
3. **Objetivo** — O que esta pesquisa deve destravar no seu projeto?

## Setup Steps

### 1. Define Competitor Watchlist

Create a competitor tracking file: `clients/<client-name>/intelligence/competitor-watchlist.md`

For each competitor, document:
- Company name and URL
- Key products/features
- Founder/exec LinkedIn profiles
- Known content channels (blog URL, YouTube, podcast)
- Review profiles (G2, Capterra URLs)
- Ad library pages (Meta, Google)

### 2. Initial Competitive Baseline

Run the full competitor-intel composite for each competitor to establish a baseline:

**Skill**: competitor-intel (chains reddit + twitter + linkedin + blog + review scrapers)

Plus:
- **Skill**: google-ad-scraper — Scrape their current Google ads
- **Method**: Use `web_search` against Meta Ad Library (facebook.com/ads/library) for Meta ad research
- **Skill**: review-site-scraper — Pull latest G2/Capterra/Trustpilot reviews

**Output**: `clients/<client-name>/intelligence/competitor-baseline.md`

### 3. Configure Monitoring Cadence

| What to Monitor | Frequency | Skill | What to Look For |
|----------------|-----------|-------|-----------------|
| Blog/content output | Weekly | blog-feed-monitor | New posts, topic shifts, SEO attacks |
| Social media posts | Weekly | linkedin-profile-post-scraper + twitter-mention-tracker | Messaging changes, product announcements, engagement patterns |
| Reddit/HN mentions | Weekly | reddit-post-finder + hacker-news-scraper | User sentiment, complaints, praise, feature requests |
| Ad creative changes | Bi-weekly | google-ad-scraper + web_search (Meta Ad Library) | New campaigns, messaging shifts, spend changes |
| Review sentiment | Monthly | review-site-scraper | New reviews, rating trends, common complaints |

### 4. Run Monitoring

Each monitoring cycle:

1. Run the relevant scrapers for the cycle type
2. Compare new data against the baseline/previous cycle
3. Flag significant changes:
   - New product features or pricing changes
   - New content targeting our client's keywords
   - Negative review trends (poaching opportunity)
   - New ad campaigns (messaging intelligence)
   - Founder/exec public statements about strategy

### 5. Produce Intelligence Report

After each cycle, produce a brief intelligence summary:

```
# Competitor Intelligence — [Client] — Week of [Date]

## Key Changes
- [Competitor A] published 3 new blog posts targeting "[keyword]"
- [Competitor B] launched new Meta ad campaign focused on [theme]
- [Competitor C] received 5 negative G2 reviews about [issue]

## Recommended Actions
- Publish response content for [Competitor A]'s keyword attack
- Create comparison page addressing [Competitor B]'s new messaging
- Target [Competitor C]'s unhappy customers with migration content

## Detailed Findings
[Per-competitor breakdown]
```

**Output**: `clients/<client-name>/intelligence/competitor-reports/[date].md`

## Ongoing Cadence

- **Weekly**: Content + social monitoring, brief report
- **Bi-weekly**: Ad monitoring
- **Monthly**: Full review scrape + comprehensive report
- **Quarterly**: Re-run full competitor-intel baseline, update watchlist

## Human Checkpoints

- **After setup**: Review competitor watchlist and monitoring plan
- **After each report**: Review recommended actions before executing

## Output Format

| Output | Format | Location |
|---|---|---|
| **Intelligence briefing** | Markdown | `{name}-scan-{YYYY-MM-DD}.md` |
| **Signal alerts** | Structured list | Included in briefing |
| **Scan statistics** | Summary table | End of briefing |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

## Composability

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `campaign-brief-generator`
- `competitor-intel`
- `industry-scanner`
- `launch-positioning-builder`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: competitor-monitoring-system — [finding]` | `[OPERACIONAL]: competitor-monitoring-system — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: competitor-monitoring-system — [param] works better as [value]` | `[OPERACIONAL]: competitor-monitoring-system — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: competitor-monitoring-system — [insight]` | `[ESTRATÉGICO]: competitor-monitoring-system — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

