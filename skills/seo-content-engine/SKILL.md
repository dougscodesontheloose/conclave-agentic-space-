---
type: playbook
name: seo-content-engine
description: >
  Build and run an SEO content engine: audit current state, identify gaps,
  build keyword architecture, generate content calendar, draft content.
tags: [seo, content, strategy]
---

# SEO Content Engine

**Core principle:** A intenção do usuário dita a arquitetura; o algoritmo apenas lê o mapa.


Build a compounding SEO content engine for a client: audit → gap analysis → keyword architecture → content calendar → content drafting → publishing pipeline.

## When to Use

- "Build an SEO content strategy for [client]"
- "Create a content engine for [company]"
- "What content should [company] be publishing?"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Prerequisites

- Client website URL
- Client context.md with ICP, value props, positioning
- Top competitors identified (from intelligence package or manually)


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

## Steps

### 1. Audit Current State

**Skill**: seo-content-audit (orchestrates site-content-catalog + seo-domain-analyzer + brand-voice-extractor)

Run the full SEO audit to understand:
- Current content inventory (what exists, by type and topic)
- Domain authority, organic traffic, keyword rankings
- Competitive gap matrix (what competitors rank for that the client doesn't)
- Brand voice profile (writing style to match)

**Skill**: aeo-visibility

Test AI answer engine visibility for key queries.

**Output**: Complete picture of where the client stands in search.

### 2. Identify Content Gaps

From the audit, identify:

**Competitive gaps**: Keywords competitors rank for that the client doesn't
**Funnel gaps**: Missing content at TOFU, MOFU, or BOFU stages
**Topic gaps**: Industry/vertical content that doesn't exist
**Comparison gaps**: Missing "vs" pages and "alternatives" pages

Prioritize by: search volume x commercial intent x competitive difficulty.

### 3. Build Keyword Architecture

Organize target keywords by funnel stage:

- **TOFU** (awareness): "what is [category]", "[category] use cases", "how to [solve problem]"
- **MOFU** (evaluation): "[category] comparison", "how to choose [solution]", "[compliance/technical] requirements"
- **BOFU** (decision): "[Company] vs [Competitor]", "[Competitor] alternatives", pricing guides, migration guides

Map each keyword cluster to a content type (blog post, landing page, guide, comparison page).

### 4. Create Content Calendar

Build a prioritized content calendar:

1. **Week 1-2**: Highest-urgency BOFU pages (comparison pages, especially if competitors are publishing attack content)
2. **Week 2-4**: Core MOFU guides and evaluation content
3. **Week 4-8**: TOFU awareness content and programmatic SEO templates
4. **Ongoing**: 2-3 editorial pieces per week

### 5. Draft Content

**Skill**: content-asset-creator (for landing pages, reports, one-pagers)
**Method**: AI-assisted drafting with brand voice matching (from brand-voice-extractor output)

For each content piece:
- Match the client's brand voice and style
- Include target keywords naturally
- Build internal linking to related content
- Include clear CTAs
- Add structured data / schema markup recommendations

### 6. Build Internal Linking Architecture

Design the linking structure:
- TOFU pages link to related MOFU pages
- MOFU pages link to BOFU pages (comparison, pricing)
- BOFU pages link to product/signup
- All pages link to relevant pillar content

### 7. Publish & Monitor

- Publish on client's blog/site (or provide drafts for client to publish)
- Track: organic traffic by page/cluster, rankings by keyword, content-to-signup conversion
- Monthly: Review which content is ranking, which needs updates

## Ongoing Cadence

- **Weekly**: Publish 2-3 pieces, monitor rankings
- **Monthly**: Review content performance, update calendar, refresh underperforming pages
- **Quarterly**: Re-run seo-content-audit to measure progress and identify new gaps

## Human Checkpoints

- **After Step 2**: Review gap analysis and priority recommendations
- **After Step 4**: Review content calendar before drafting
- **After Step 5**: Review content drafts before publishing

## Output Format

| Output | Format | Location |
|---|---|---|
| **Content asset** | HTML / PNG / Markdown | Current working directory |
| **Preview** | Browser or inline | Presented for user approval |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

## Composability

**Receives data from:**
- Skills tagged `brand` (e.g., data collection and enrichment)
- Skills tagged `competitive-intel` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `seo-domain-analyzer` (e.g., data collection and enrichment)
- Skills tagged `site-content-catalog` (e.g., data collection and enrichment)

**Feeds into:**
- `content-brief-factory`
- `create-html-carousel`
- `create-html-slides`
- `linkedin-outreach`
- `topical-authority-mapper`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: seo-content-engine — [finding]` | `[OPERACIONAL]: seo-content-engine — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: seo-content-engine — [param] works better as [value]` | `[OPERACIONAL]: seo-content-engine — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: seo-content-engine — [insight]` | `[ESTRATÉGICO]: seo-content-engine — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

