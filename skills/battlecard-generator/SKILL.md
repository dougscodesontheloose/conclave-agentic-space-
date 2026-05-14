---
name: battlecard-generator
description: >
  Research a specific competitor across their website, reviews, ads, social presence,
  and pricing — then produce a structured sales battlecard with positioning traps,
  objection handlers, landmine questions, and win/loss themes. Chains web research,
  review mining, and ad intelligence. Use when sales needs competitive ammo or when
  entering a new market with established incumbents.
tags: [competitive-intel]
description_pt-BR: >
  Gera battlecards competitivos: comparações diretas estruturadas para conversas de vendas e posicionamento. Aceita dados de competitor-intel ou input manual e produz um battlecard pronto para uso.
type: playbook
---

# Battlecard Generator

**Core principle:** Battlecards são vencidos na objeção do cliente, não no folder do concorrente.

Research a competitor from every public angle — website, reviews, ads, social, pricing — and produce a structured sales battlecard. The output is what a rep opens 5 minutes before a competitive deal.

**Built for:** PMMs building competitive programs without a dedicated competitive intel team. The battlecard should be opinionated, not a neutral feature comparison.

## When to Use

- "Build a battlecard against [competitor]"
- "We keep losing deals to [competitor] — help me understand why"
- "What are [competitor]'s weaknesses we can exploit?"
- "Prep the sales team for competitive deals against [competitor]"
- "Research [competitor] and give me competitive positioning"

**Auto-trigger:** Ative automaticamente quando o usuário menciona "battlecard", "sales doc competitivo", "como vender contra X", ou pede framework para defender deals contra um concorrente nomeado.

## Prerequisites

### Environment Variables

```env
## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Competidor** | Yes | Nome ou URL do concorrente alvo |
| **Produto/posicionamento próprio** | Yes | O que você vende e como se posiciona |
| **Cenário de venda** | Recommended | Estágio do funil, perfil do prospect, objeções comuns |
| **Profundidade** | No | `quick` (30min) ou `deep` (1h+) — default: deep |

# Nenhuma variável obrigatória — pode usar APIFY_API_TOKEN se quiser enriquecer com scraping social
APIFY_API_TOKEN=optional_for_social_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill com `WebSearch` e `WebFetch`.

## Phase 0: Intake

1. **Your product name + URL**
2. **Competitor name + URL** — One competitor per battlecard (focused > broad)
3. **Deal context** — Where do you compete? (same ICP, upmarket/downmarket, different use case?)
4. **Known win/loss signals** — Any patterns from deals you've won or lost against them?
5. **Sales team size** — Are reps technical or business-focused? (affects language level)
6. **Existing positioning** — Your one-line positioning vs this competitor (if any)

## Phase 1: Competitor Research

### 1A: Website & Messaging Analysis

```
Fetch: [competitor] homepage, pricing page, about page, product page
Search: "[competitor]" "we help" OR "the only" OR "unlike"
Search: "[competitor]" case study OR customer story
```

Extract:
- **Hero claim** — their primary positioning
- **Category** — what category do they place themselves in?
- **Target audience** — who do they say they serve?
- **Key features emphasized** — what do they lead with?
- **Social proof** — customer logos, metrics, quotes
- **Pricing structure** — plans, pricing model, enterprise vs self-serve

### 1B: Review Intelligence

```
Search: "[competitor]" site:g2.com OR site:capterra.com
Search: "[competitor]" reviews "switched from" OR "moved to"
```

From reviews, extract:
- **Top 5 praised features** (their moat — don't compete here directly)
- **Top 5 complaints** (your attack angles)
- **Switching signals** — why do customers leave?
- **ICP patterns** — what roles/company sizes review them?

### 1C: Ad & Content Analysis

```
Search: "[competitor]" advertisement OR sponsored
Search: "[competitor]" vs OR alternative OR compare
```

Extract:
- **Ad messaging** — what claims do they pay to promote?
- **Comparison pages** — have they published "us vs X" pages?
- **Content themes** — what topics do they create content around?

### 1D: Social & Community Signals

```
Search: "[competitor]" site:reddit.com OR site:twitter.com complaints OR issues
Search: "[competitor]" "looking for alternative" OR "anyone use"
```

Extract:
- **Common frustrations** discussed publicly
- **Feature requests** their users are vocal about
- **Sentiment patterns** — do users love or tolerate them?

### 1E: Pricing Deep Dive

```
Fetch: [competitor] pricing page
Search: "[competitor]" pricing OR cost OR "how much"
```

Map their pricing:
- **Model:** Per seat / usage-based / flat rate / hybrid
- **Tiers:** What's in each tier?
- **Free tier:** What's included? What's gated?
- **Enterprise:** Custom pricing? What triggers enterprise sales?
- **Hidden costs:** Implementation, overages, add-ons?

## Phase 2: Competitive Analysis

### Strengths & Weaknesses Matrix

| Dimension | Them | Us | Net |
|-----------|------|-----|-----|
| [Feature area 1] | [Rating + context] | [Rating + context] | Win/Lose/Tie |
| [Feature area 2] | ... | ... | ... |
| Pricing | ... | ... | ... |
| Ease of use | ... | ... | ... |
| Support | ... | ... | ... |
| Integrations | ... | ... | ... |

### Where We Win (lead with these)
1. [Strength] — [Evidence from research]
2. [Strength] — [Evidence]
3. [Strength] — [Evidence]

### Where We Lose (don't engage here)
1. [Weakness] — [Mitigation strategy]
2. [Weakness] — [How to reframe]

### Where It's Close (differentiate on narrative)
1. [Area] — [How to position the tie as a win]

## Phase 3: Output — Battlecard

```markdown
# Battlecard: [Your Product] vs [Competitor]
Last updated: [DATE] | Confidence: [High/Medium — based on data freshness]

---

## Quick Reference (The 30-Second Version)

**They say:** "[Their positioning headline]"
**We say:** "[Our counter-positioning]"
**We win when:** [Deal profile where we have advantage]
**We lose when:** [Deal profile where they have advantage]
**Best opening move:** "[Question or statement to frame the deal]"

---

## Competitor Overview

| | [Competitor] |
|---|---|
| **Founded** | [Year] |
| **Funding** | [Amount / stage] |
| **Headcount** | [Estimate] |
| **Target market** | [Who they serve] |
| **Pricing** | [Model + range] |
| **Category** | [How they position] |

---

## Positioning Traps

Questions to ask early in the deal that frame the evaluation in your favor:

1. **"[Question that highlights your strength]"**
   → If they say [X], you win because [reason]
   → If they say [Y], pivot to [angle]

2. **"[Question that exposes competitor weakness]"**
   → Their answer will likely be [X], which reveals [limitation]

3. **"[Question about a capability they lack]"**
   → They can't do this. When the prospect asks them, it plants doubt.

---

## Landmine Questions

Drop these casually — they'll come up when the prospect evaluates the competitor:

- "Have you asked [competitor] about [specific limitation]?"
- "When you evaluate [competitor], make sure to test [area where they're weak]."
- "One thing worth checking: [competitor] pricing can get expensive once you [usage trigger]."

---

## Objection Handling

### "Why shouldn't we just go with [Competitor]?"
> "[Direct response — acknowledge their strength, pivot to your differentiation]"

### "[Competitor] has more features / is more established"
> "[Response — focus on what matters for this buyer's use case, not feature count]"

### "[Competitor] is cheaper"
> "[Response — reframe on total cost, hidden costs, or value per dollar]"

### "[Competitor] has [big customer logo]"
> "[Response — your relevant social proof + why logo != fit]"

### "We're already using [Competitor]"
> "[Response — switching cost vs cost of staying, what's changed]"

---

## Feature Comparison (Honest Assessment)

| Capability | Us | [Competitor] | Verdict |
|-----------|-----|-------------|---------|
| [Feature 1] | [Status + context] | [Status + context] | [Who wins + why] |
| [Feature 2] | ... | ... | ... |
| [Feature 3] | ... | ... | ... |
| Pricing transparency | ... | ... | ... |
| Onboarding speed | ... | ... | ... |
| Support quality | ... | ... | ... |

---

## Their Customers Say (From Reviews)

### What they love (don't fight these):
- "[Quote from review]" — [Platform, Role]
- "[Quote]" — ...

### What they hate (exploit these):
- "[Quote from negative review]" — [Platform, Role]
- "[Quote]" — ...
- "[Quote]" — ...

---

## Pricing Comparison

| | Us | [Competitor] |
|---|---|---|
| **Entry price** | [$/mo] | [$/mo] |
| **Mid-tier** | [$/mo] | [$/mo] |
| **Enterprise** | [Custom / $X] | [Custom / $X] |
| **Free tier** | [What's included] | [What's included] |
| **Hidden costs** | [None / list] | [Implementation, overages, etc.] |

**Pricing attack angle:** [How to frame pricing comparison favorably]

---

## Win Themes (What Wins Deals)

Based on competitive patterns:
1. **[Theme]** — "[Proof point or quote]"
2. **[Theme]** — ...
3. **[Theme]** — ...

## Loss Themes (What Loses Deals)

Be aware — we tend to lose when:
1. **[Pattern]** — Mitigation: [strategy]
2. **[Pattern]** — Mitigation: [strategy]

---

## Quick Responses for Email/Chat

**When prospect mentions [competitor]:**
> "[2-sentence response for email or Slack]"

**When asked for a comparison:**
> "[3-sentence elevator pitch vs competitor]"
```

Save to `clients/<client-name>/product-marketing/battlecards/vs-[competitor-slug]-[YYYY-MM-DD].md`.

## Cost

| Component | Cost |
|-----------|------|
| Web research | Free |
| Review mining (optional, via review-site-scraper) | ~$0.50-1.00 |
| Ad analysis (optional, via ad scrapers) | ~$0.50-1.00 |
| All analysis and battlecard generation | Free (LLM reasoning) |
| **Total** | **Free — $2** |

## Tools Required

- **web_search** — for competitor research
- **fetch_webpage** — for site analysis
- **Optional:** `review-site-scraper` for G2/Capterra mining
- **Optional:** `google-ad-scraper` for ad intelligence, `web_search` against Meta Ad Library for Meta ads

## Trigger Phrases

- "Build a battlecard against [competitor]"
- "Competitive intel on [competitor]"
- "Run the battlecard generator for [competitor]"
- "Help me win deals against [competitor]"

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **Concorrente sem presença web** | 0 fontes válidas após 3 buscas | Pedir ao usuário materiais privados (deck do prospect, screenshots) |
| **Dados conflitantes entre fontes** | Preço/feature divergente em 2+ fontes | Reportar ambas com timestamps e marcar `low-confidence` |
| **Concorrente recém-pivotou** | Site reflete posicionamento novo, mas reviews/cases ainda do antigo | Separar seção "Posicionamento atual" vs "Reputação histórica" |

**Principle:** Cite fontes. Quando incerto, declare incerteza explícita em vez de apresentar low-confidence como fato.

## Composability

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `campaign-brief-generator`
- `launch-positioning-builder`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: battlecard-generator — [finding]` | `[OPERACIONAL]: battlecard-generator — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: battlecard-generator — [param] works better as [value]` | `[OPERACIONAL]: battlecard-generator — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: battlecard-generator — [insight]` | `[ESTRATÉGICO]: battlecard-generator — Competitor X has no case studies page, vulnerability for battlecard` |

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

---

## Conclave Output Convention

Quando rodado dentro de um squad Conclave, o output canônico segue:

Write to `squads/{code}/output/battlecard-{slug}.md`.

Report:
```
Battlecard Generator — output:
— Confronto: {Your Company} vs {Competitor}
— Dimensões comparadas: {N}
— Objeções endereçadas: {N}
— Arquivo: output/battlecard-{slug}.md
```
