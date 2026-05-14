---
name: tam-builder
description: >
  Build and maintain a scored Total Addressable Market (TAM) using Apollo Company Search.
  Discovers companies matching ICP, scores fit (0-100), assigns tiers (1/2/3), and
  auto-builds a persona watchlist for Tier 1-2 companies using Apollo People Search (free).
  Outputs to CSV.
tags: [lead-generation]
---

# TAM Builder

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


Build and maintain a scored Total Addressable Market. Uses Apollo Company Search to discover companies, scores ICP fit (0-100), assigns tiers (1/2/3), and auto-builds a persona watchlist for Tier 1-2 companies using Apollo People Search (free).

**Three modes:**
- **build** — First-time TAM construction from Apollo search
- **refresh** — Update existing TAM: re-score, detect tier changes, deprecate stale companies
- **status** — Read-only report of current TAM state

## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

### Apollo API Key
Add to `.env`:
```
APOLLO_API_KEY=your-api-key-here
```

That's it — one env var.

## Config Format

Create a JSON config per client/segment:

```json
{
  "client_name": "happy-robot",
  "tam_config_name": "voice-ai-midmarket",

  "company_filters": {
    "organization_num_employees_ranges": ["51,200", "201,500", "501,1000"],
    "q_organization_keyword_tags": ["call center", "contact center"],
    "organization_locations": ["United States"]
  },

  "scoring": {
    "weights": {
      "employee_count_fit": 30,
      "industry_fit": 25,
      "funding_stage_fit": 20,
      "geo_fit": 15,
      "keyword_match": 10
    },
    "tier_thresholds": { "tier_1_min_score": 75, "tier_2_min_score": 50 },
    "target_industries": ["Telecommunications", "Customer Service"],
    "target_employee_ranges": [[51, 200], [201, 500], [501, 1000]],
    "target_funding_stages": ["Series A", "Series B", "Series C"],
    "target_geos": ["United States"]
  },

  "watchlist": {
    "enabled": true,
    "personas_per_company": 3,
    "person_filters": {
      "person_titles": ["VP of Operations", "Head of Customer Service"],
      "person_seniority": ["vp", "director", "c_suite"]
    },
    "tiers_to_watch": [1, 2]
  },

  "mode": "standard",
  "max_pages": 50
}
```

## Approval Gate

**CRITICAL: Never export results without explicit user approval.**

**Required flow:**
1. Search Apollo for a small sample first (~100 companies)
2. Score them and present: tier distribution, example Tier 1/2 companies, scoring sanity check
3. **Get explicit user approval** before running the full build
4. Only then run the full search + score + export

## Pipeline: Build Mode

```
Step 0: --preview → total count + cost estimate (no DB writes)
Step 1: --sample --test → search 1 page, score in-memory, show results (no DB writes)
Step 2: User reviews sample → approves, adjusts filters, or caps scope
Step 3: Full build → Apollo Company Search → Export to CSV → Score → Tier → Watchlist
```

Phase details (Step 3 only — after user approval):
```
Phase 1: Apollo Company Search → Upsert raw companies → Score ICP fit → Assign tiers
Phase 2: (skipped in build mode — no prior data to deprecate)
Phase 3: Persona Watchlist — pull 2-3 personas per Tier 1-2 company (free)
```

## Pipeline: Refresh Mode

```
Phase 1: Apollo Company Search → Upsert/update companies → Re-score → Detect tier changes
Phase 2: Deprecation — companies missing 2+ consecutive refreshes get deprecated
Phase 3: Persona Watchlist — pull personas for new/promoted Tier 1-2 companies,
         disqualify personas at deprecated companies
```

## ICP Scoring (0-100)

Pure function, no API calls. Weighted scoring across 5 dimensions from config:
- `employee_count_fit` — headcount in target ranges?
- `industry_fit` — industry matches targets?
- `funding_stage_fit` — funding stage in targets?
- `geo_fit` — HQ location in target geos?
- `keyword_match` — org keywords overlap config keywords?

Score thresholds (configurable): >=75 = Tier 1, >=50 = Tier 2, else Tier 3.

## Deprecation Rules (refresh only)

- First miss (not returned by search): `metadata.refresh_miss_count = 1`, keep active
- Second consecutive miss: `tam_status = 'deprecated'`
- Employee count drops to 0: immediate deprecation
- Companies with `tam_status = 'converted'` are always exempt

## Watchlist — Persona Sync

| Scenario | Behavior |
|----------|----------|
| New Tier 1-2 company | Pull 2-3 personas immediately |
| Company promoted Tier 3→2 | Pull personas during refresh |
| Company deprecated | Disqualify monitoring personas |
| Company demoted Tier 1→3 | Keep existing personas, stop refreshing |

## Mode Caps

| Parameter | Test | Standard | Full |
|-----------|------|----------|------|
| Max pages | 1 | 50 | 200 |
| Max companies | 100 | 5,000 | 20,000 |

## Apollo API Reference

- **Company Search:** `POST https://api.apollo.io/api/v1/mixed_companies/search` — Returns matching companies in the `accounts` array (not `organizations`). Fields: `name`, `primary_domain`, `estimated_num_employees`, `industry`, `keywords`, `city`, `state`, `country`.
- **People Search:** `POST https://api.apollo.io/api/v1/mixed_people/search` — FREE. Returns matching people in the `people` array. Fields: `first_name`, `title`, `organization.name`. Email/LinkedIn obfuscated on free tier.
- **People Match (enrich):** `POST https://api.apollo.io/api/v1/people/match` — 1 credit per match. Reveals email, phone, LinkedIn URL, full name.
- **Auth:** `x-api-key: {APOLLO_API_KEY}` header on all requests
- **Pagination:** `per_page` (max 100), `page` (1-indexed). `pagination.total_entries` gives total count.

## Output

Save results as CSV to the current working directory:
- `tam-companies-{date}.csv` — All discovered companies with ICP score and tier
- `tam-personas-{date}.csv` — Persona watchlist for Tier 1-2 companies (from People Search)

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
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `cold-email-outreach`
- `contact-cache`
- `linkedin-message-writer`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: tam-builder — [finding]` | `[OPERACIONAL]: tam-builder — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: tam-builder — [param] works better as [value]` | `[OPERACIONAL]: tam-builder — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: tam-builder — [insight]` | `[ESTRATÉGICO]: tam-builder — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Lead quality:** All leads have at minimum: name, company, and one contact method (email or LinkedIn URL)
- [ ] **Personalization check:** At least 1 personalized element per message beyond [First Name]
- [ ] **Duplicate check:** Cross-reference against contact-cache to avoid re-contacting
- [ ] **Volume sanity:** If generating >50 contacts, present a sample of 5 for user approval before proceeding
- [ ] **User checkpoint:** Present the lead list and draft messages for review before any outreach execution

**If any check fails:** Flag the specific leads/messages that failed and ask user to review.

