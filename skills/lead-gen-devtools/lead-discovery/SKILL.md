---
name: lead-discovery
description: Orchestrator that runs first for lead generation requests. Gathers business context via website analysis or questions, identifies competitors, builds ICP, and routes to signal skills with pre-filled inputs.
user-invocable: true
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch
argument-hint: [website-url]
tags: [lead-generation, orchestration, research]
---

# Lead Discovery — Orchestrator

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


This is the entry point for all lead generation requests. Before any signal skill runs, this skill ensures the agent has enough business context to configure every downstream skill correctly.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

- User asks to "find leads", "generate leads", "do outbound", "find prospects", or any variation
- User mentions lead generation without specifying a particular signal source
- User asks to run a specific signal skill but the agent has no business context yet
- **Always run this skill first** — before github-repo-signals, job-signals, community-signals, competitor-signals, or event-signals


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## What This Skill Does

1. Learns about the user's business (via website or questions)
2. Identifies competitors, ICP, and relevant technologies
3. Generates the shared context object that all signal skills need
4. Recommends which signal sources to run and in what order
5. Hands off to individual signal skills with inputs pre-filled

---


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

## Phase 1: Gather Business Context

### If the user provides a website URL

Scrape the website (homepage, pricing page, about page, docs if available) and extract:

1. **Product description** — one-liner of what the product does
2. **Category** — the market category (e.g., observability, API platform, CI/CD, CRM)
3. **Target buyer** — who the product is sold to (developers, DevOps, marketers, etc.)
4. **Key features** — the 3-5 main capabilities
5. **Technology keywords** — the technical terms associated with this product and space
6. **Pricing model** — free tier, usage-based, seat-based, enterprise (helps qualify leads)
7. **Competitors mentioned or implied** — from comparison pages, "alternative to" language, integrations

After extracting, present a summary to the user and ask them to confirm or correct.

### If the user does NOT have a website

Ask these questions one conversational block at a time. Do NOT dump all questions at once.

**Block 1 — The Basics:**
- What does your product do? (one sentence)
- Who is your ideal buyer? (role, company size, industry)
- What problem does it solve?

**Block 2 — The Market (ask after Block 1 is answered):**
- Who are your main competitors? (even indirect ones)
- What technologies or tools does your product integrate with or replace?
- What does your tech stack look like? (helps identify GitHub repos)

**Block 3 — Sales Context (ask after Block 2 is answered):**
- How do you sell today? (inbound, outbound, PLG, partnerships)
- What's your price range? (helps filter lead quality — a $500/yr tool targets different companies than a $50k/yr platform)
- Any specific companies or segments you're already targeting?

---

## Phase 2: Competitor & Ecosystem Research

Once you have the business context, research to fill gaps the user didn't provide:

### Identify Competitors
- Search the web for "[product category] alternatives", "[competitor name] vs", "best [category] tools 2025/2026"
- Build a list of 5-10 direct and indirect competitors
- For each competitor, note:
  - Name and website
  - GitHub repos (if open-source or has public repos)
  - Product Hunt slug (if launched there)
  - Greenhouse/Lever career page slug (for job signals)

### Identify Relevant GitHub Repos
- Search GitHub for repos in the product's technology space
- Include: competitor repos, category-defining repos, popular libraries the ICP uses
- Aim for 3-8 repos that the user's ideal buyers would star, fork, or contribute to

### Identify Community Watering Holes
- Which subreddits discuss this space?
- Are there relevant HN threads or recurring topics?
- Any Slack/Discord communities, forums, or newsletters? (note these even if we can't scrape them — useful context)

### Identify Relevant Events
- What conferences does this ICP attend?
- Any upcoming or recent events in the space?

Present your research findings to the user for confirmation before proceeding.

---

## Phase 3: Build the Shared Context Object

After Phases 1 and 2, you should have all of this:

```
SHARED CONTEXT
==============
Product:          [one-liner description]
Category:         [market category]
Website:          [URL or "none"]

ICP:
  Role:           [e.g., Backend engineers, DevOps leads, Engineering managers]
  Company size:   [e.g., 50-500 employees]
  Industry:       [e.g., SaaS, fintech, healthtech — or "any"]
  Tech stack:     [e.g., Kubernetes, Python, AWS]

Competitors:      [list with GitHub repos, PH slugs, career page slugs where found]
Technology keywords: [list of 10-20 relevant terms]
Problem statements:  [3-5 problems the product solves, as they'd appear in job posts or forum discussions]

GitHub repos to scan:    [3-8 repos]
Subreddits:              [5-10 relevant subreddits]
Job search queries:      [3-5 job title searches]
Greenhouse/Lever slugs:  [company career page slugs]
Product Hunt slugs:      [competitor PH slugs]
Conference/event names:  [if identified]
```

Present this to the user as a formatted summary. Ask them to confirm, add, or remove items.

---

## Phase 4: Recommend Signal Sources & Route

Based on the context, recommend which signal skills to run. Use this priority order:

### Always recommend (free, high signal):
1. **github-repo-signals** — if relevant repos were identified and the ICP is technical/developer-facing
2. **job-signals** (HN + RemoteOK + Greenhouse/Lever only) — free sources, detects hiring intent

### Recommend if relevant:
3. **community-signals** (HN only — free) — if the ICP participates in developer communities
4. **competitor-signals** — if competitors have PH launches, case studies, or recent press
5. **event-signals** — if specific conferences/events were identified

### Recommend with cost note:
6. **community-signals** (add Reddit — ~$5-10) — broader community coverage
7. **job-signals** (add LinkedIn/Google — ~$1-3) — broader job board coverage
8. **SixtyFour enrichment** — after any signal skill produces output (~$0.05-0.20/lead)

Present the recommendation as a numbered plan with costs. Ask the user which sources they want to run — all of them, a subset, or just start with the free ones.

### Handoff

Once the user picks their sources, begin executing them in the recommended order. For each skill:

- Invoke the appropriate skill (e.g., `/github-repo-signals`, `/job-signals`)
- Pre-fill all inputs from the shared context (do NOT re-ask the user for information you already have)
- Only ask skill-specific questions that weren't covered in the shared context (e.g., user limit for github-repo-signals)
- After each skill completes, briefly summarize results and move to the next

---

## Key Rules

1. **Never jump straight to a signal skill** without first understanding the business. Even if the user says "scan this GitHub repo", take 30 seconds to understand what they sell and who they sell to — it makes the output analysis 10x more useful.

2. **Don't ask all questions at once.** Conversational blocks. If the user gives a website, you may not need to ask anything at all.

3. **Research fills gaps.** If the user says "our competitors are X and Y", still research to find Z they may have missed. But present findings for confirmation — don't assume.

4. **Cost transparency.** Always tell the user which sources are free and which cost money before running anything.

5. **Reuse context.** Once the shared context is built, every downstream skill should inherit it. The user should never be asked the same question twice.

6. **Start small, scale up.** Default recommendation: start with free sources, review results, then decide on paid sources. Don't push users to spend money upfront.

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Contact not found** | Empty result from people search | Log `⚠️ No contacts found for [company]`. Skip to next company, note gap in output |
| **Enrichment failed** | API error or missing fields | Use partial data. Mark enrichment_status as `partial` in output |
| **Duplicate contact detected** | Match on LinkedIn URL or email in contact-cache | Skip duplicate, log `ℹ️ Skipped duplicate: [name]` |
| **Template rendering failed** | Missing personalization variables | Fall back to generic template. Flag `⚠️ Low personalization` in output |
| **Outreach tool connection failed** | API error from outreach platform | Export to CSV as fallback. Inform user of manual upload path |

**Principle:** Partial success is better than total failure. Always produce an output, even if degraded.


## Composability

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `cold-email-outreach`
- `contact-cache`
- `content-asset-creator`
- `linkedin-message-writer`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: lead-gen-devtools/lead-discovery — [finding]` | `[OPERACIONAL]: lead-gen-devtools/lead-discovery — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: lead-gen-devtools/lead-discovery — [param] works better as [value]` | `[OPERACIONAL]: lead-gen-devtools/lead-discovery — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: lead-gen-devtools/lead-discovery — [insight]` | `[ESTRATÉGICO]: lead-gen-devtools/lead-discovery — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

