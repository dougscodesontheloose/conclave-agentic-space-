---
name: competitive-pricing-intel
description: >
  Monitor competitor pricing pages via live web scrape and Web Archive snapshots.
  Track plan changes, tier restructuring, new pricing models, and feature gating shifts.
  Produces a pricing comparison matrix and flags when a competitor changes packaging.
  Use when a product marketing team needs to stay current on competitive pricing or when
  preparing for a pricing change of their own.
tags: [competitive-intel]
---

# Competitive Pricing Intel

Track competitor pricing pages over time. Detect when they change plans, shift feature gating, adjust pricing models, or introduce new tiers. The output is a living pricing comparison matrix plus alerts when something changes.

**Core principle:** Pricing is the most under-monitored competitive signal. Most teams only check competitor pricing when they're about to change their own. This skill makes it continuous.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

- "What are our competitors charging?"
- "Has [competitor] changed their pricing recently?"
- "Build a pricing comparison matrix"
- "Monitor competitor pricing for changes"
- "We're rethinking our pricing — show me the competitive landscape"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Phase 0: Intake

1. **Your product name + pricing page URL**
2. **Competitors to track** — Names + pricing page URLs (2-5 recommended)
3. **Your pricing model** — How do you charge? (per seat, usage, flat, freemium, etc.)
4. **Key comparison dimensions** — What matters to your buyer? (price per seat, included features, limits, support tiers)
5. **First run or recurring?**
   - **First run:** Full baseline capture + historical analysis
   - **Recurring:** Compare against last snapshot

## Phase 1: Current Pricing Capture

### 1A: Live Scrape

For each competitor's pricing page:

```
Fetch: [competitor pricing URL]
```

Extract:
- **Plan names and prices** — Every tier with monthly and annual pricing
- **Feature matrix** — What's included in each tier?
- **Limits** — Usage caps, seat limits, storage, API calls
- **Add-ons** — What costs extra beyond base plans?
- **Enterprise tier** — "Contact us" or listed price? What's gated behind sales?
- **Free tier / trial** — What's available without paying?
- **Pricing model** — Per seat / per user / usage-based / flat / hybrid

### 1B: Web Archive Historical Check

Search for past versions of their pricing page:

```
Search: "web.archive.org" "[competitor pricing URL]"
Fetch: web.archive.org/web/*/[competitor pricing URL]
```

Look for the last 2-3 snapshots to detect:
- **Price increases/decreases**
- **Plan restructuring** (new tiers added, tiers removed)
- **Feature gating changes** (features moved between tiers)
- **Model shifts** (e.g., moved from per-seat to usage-based)
- **Free tier changes** (expanded or restricted)

### 1C: Pricing Announcement Research

```
Search: "[competitor]" pricing change OR "new pricing" OR "updated plans"
Search: "[competitor]" blog pricing OR announcement plans
Search: "[competitor]" site:reddit.com pricing OR "price increase"
```

Capture any public announcements or community reactions to pricing changes.

## Phase 2: Pricing Analysis

### 2A: Competitive Pricing Matrix

Build a normalized comparison across all competitors:

| Dimension | Your Product | Competitor A | Competitor B | Competitor C |
|-----------|-------------|-------------|-------------|-------------|
| **Starter price** | $X/mo | $X/mo | $X/mo | $X/mo |
| **Mid-tier price** | $X/mo | $X/mo | $X/mo | $X/mo |
| **Enterprise** | $X/mo or Custom | ... | ... | ... |
| **Pricing model** | [Model] | [Model] | [Model] | [Model] |
| **Free tier** | [Yes/No + limits] | ... | ... | ... |
| **Annual discount** | [X%] | ... | ... | ... |
| **Key limit (starter)** | [e.g., 5 seats] | ... | ... | ... |
| **Key limit (mid)** | [e.g., 20 seats] | ... | ... | ... |
| **Overage cost** | [$/unit or blocked] | ... | ... | ... |
| **Support included** | [Email/chat/phone] | ... | ... | ... |

### 2B: Price-to-Value Ratio

For the ICP's typical use case, calculate effective cost:

```
Scenario: [Typical ICP — e.g., "10-person growth team, 5,000 contacts, 1,000 emails/month"]

Your Product: $[X]/mo for this scenario
Competitor A: $[X]/mo for this scenario
Competitor B: $[X]/mo for this scenario
```

This reveals true competitive pricing position, not just list price.

### 2C: Packaging Strategy Analysis

For each competitor, identify their packaging strategy:

| Strategy | Description | Who Uses It |
|----------|-------------|-------------|
| **Good-Better-Best** | 3 tiers, clear upgrade path | Most SaaS |
| **Usage-based** | Pay for what you use | API/infrastructure |
| **Per-seat** | Price scales with team | Collaboration tools |
| **Freemium** | Free forever, premium features | PLG products |
| **Reverse trial** | Full features free, then downgrade | Conversion-optimized |
| **Platform + add-ons** | Base platform + modular features | Enterprise |

### 2D: Change Detection (Recurring Runs)

Compare current snapshot against previous:

| Change Type | Severity | Example |
|------------|----------|---------|
| **Price increase** | High | Starter: $29 → $39/mo |
| **Price decrease** | High | Aggressive competitive move |
| **New tier added** | Medium | "Growth" plan between Starter and Pro |
| **Tier removed** | Medium | Simplified from 4 to 3 plans |
| **Feature ungated** | Medium | Feature moved from Pro to Starter |
| **Feature gated** | Medium | Feature moved from Starter to Pro |
| **Model change** | Critical | Shifted from per-seat to usage-based |
| **Free tier change** | High | Free plan limits reduced/expanded |

## Phase 3: Output Format

```markdown
# Competitive Pricing Intel — [DATE]
Products tracked: [your product], [competitors]
Previous snapshot: [date or "first run"]

---

## Pricing Change Alerts

### [Competitor Name]
- **Change detected:** [Description of what changed]
- **Previous:** [Old pricing/plan structure]
- **Current:** [New pricing/plan structure]
- **Implication for us:** [What this means for your positioning/pricing]

*(Repeat for each competitor with changes. If no changes: "No pricing changes detected since [last run date].")*

---

## Competitive Pricing Matrix

| | [You] | [Comp A] | [Comp B] | [Comp C] |
|---|---|---|---|---|
| **Starter** | $[X]/mo | $[X]/mo | $[X]/mo | $[X]/mo |
| **Mid-tier** | $[X]/mo | $[X]/mo | $[X]/mo | $[X]/mo |
| **Enterprise** | [Price] | [Price] | [Price] | [Price] |
| **Model** | [Type] | [Type] | [Type] | [Type] |
| **Free tier** | [Details] | [Details] | [Details] | [Details] |
| **Annual discount** | [X%] | [X%] | [X%] | [X%] |

---

## ICP Scenario Pricing

For: [Typical buyer scenario]

| Product | Monthly Cost | Annual Cost | Notes |
|---------|-------------|-------------|-------|
| [You] | $[X] | $[X] | [Context] |
| [Comp A] | $[X] | $[X] | [Context — e.g., "requires add-on for [feature]"] |
| [Comp B] | $[X] | $[X] | [Context] |

**Your position:** [Cheapest / Mid-range / Premium] for this scenario

---

## Feature Gating Comparison

Features that matter most to ICP — where are they gated?

| Feature | [You] | [Comp A] | [Comp B] |
|---------|-------|----------|----------|
| [Feature 1] | [Tier] | [Tier] | [Tier] |
| [Feature 2] | [Tier] | [Tier] | [Tier] |
| [Feature 3] | [Tier] | [Tier] | [Tier] |

---

## Packaging Strategy Summary

| Competitor | Strategy | Target Motion | Notes |
|-----------|----------|--------------|-------|
| [Comp A] | [Strategy type] | [PLG/Sales-led/Hybrid] | [Key observation] |
| [Comp B] | [Strategy type] | [Motion] | [Observation] |

---

## Pricing Recommendations

Based on competitive analysis:

### If holding current pricing:
- **Strength:** [Where your pricing wins]
- **Vulnerability:** [Where a competitor undercuts you]
- **Messaging guidance:** [How to position price on sales calls]

### If considering a change:
- **Opportunity:** [Gap in market you could fill — e.g., "no one offers usage-based in this category"]
- **Risk:** [What to watch out for — e.g., "Competitor B is already cheaper at scale"]
```

Save to `pricing-comparison-[YYYY-MM-DD].md` in the current working directory.

## Scheduling

Run monthly (pricing changes are infrequent but impactful):

```bash
0 8 1 * * python3 run_skill.py competitive-pricing-intel --client <client-name>
```

## Cost

| Component | Cost |
|-----------|------|
| Web scraping (pricing pages) | Free |
| Web Archive lookups | Free |
| Web search (announcements) | Free |
| Analysis and comparison | Free (LLM reasoning) |
| **Total** | **Free** |

## Tools Required

- **web_search** — for pricing announcements and community reactions
- **fetch_webpage** — for scraping current pricing pages
- No API keys required

## Trigger Phrases

- "What are competitors charging?"
- "Has [competitor] changed their pricing?"
- "Build a pricing comparison matrix"
- "Run competitive pricing intel for [client]"
- "Monitor competitor pricing pages"

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Primary source unavailable** | HTTP error or empty response | Fall back to WebSearch as secondary source. Note `⚠️ Primary source unavailable` |
| **Insufficient data for analysis** | Fewer than minimum data points required | Lower confidence level of findings. Mark as `low-confidence` in output |
| **Conflicting data across sources** | Contradictory information found | Report both versions with sources. Let user resolve the conflict |
| **Rate limiting on research queries** | Throttled responses | Space queries with 2-3s delays. Reduce parallel requests |
| **Stale data detected** | Dates older than threshold (varies by use case) | Flag `⚠️ Data may be stale (from [date])`. Suggest re-running with fresh sources |

**Principle:** Always cite sources. When data is uncertain, say so explicitly rather than presenting low-confidence findings as facts.


## Composability

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `campaign-brief-generator`
- `launch-positioning-builder`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: competitive-pricing-intel — [finding]` | `[OPERACIONAL]: competitive-pricing-intel — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: competitive-pricing-intel — [param] works better as [value]` | `[OPERACIONAL]: competitive-pricing-intel — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: competitive-pricing-intel — [insight]` | `[ESTRATÉGICO]: competitive-pricing-intel — Competitor X has no case studies page, vulnerability for battlecard` |

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

