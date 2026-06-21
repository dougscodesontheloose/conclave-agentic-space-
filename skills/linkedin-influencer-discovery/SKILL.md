---
name: linkedin-influencer-discovery
description: >
  Discover top LinkedIn influencers and voices by topic, industry, follower count,
  and country. Use when you need to find the top 100 voices in a space,
  build influencer lists for outreach, or identify thought leaders on LinkedIn.
tags: [linkedin, research, lead-generation]
---

# LinkedIn Influencer Discovery

**Core principle:** Não procure dados que confirmem sua tese; procure assimetrias que o mercado ignora.


Discover top LinkedIn influencers by topic, country, and follower count using the Apify `powerai/influencer-filter-api-scraper` actor. Queries a database of 3.6M+ influencer profiles filtered to those with LinkedIn presence.

## Quick Start

Requires `APIFY_API_TOKEN` env var (or `--token` flag). Install dependency: `pip install requests`.

```bash
# Find top AI influencers with LinkedIn profiles
python3 skills/linkedin-influencer-discovery/scripts/discover_influencers.py \
  --topic "artificial intelligence" --max-results 50 --output summary

# Find SaaS influencers in the US
python3 skills/linkedin-influencer-discovery/scripts/discover_influencers.py \
  --topic "saas" --country "United States of America" --output summary

# Find marketing influencers with email available
python3 skills/linkedin-influencer-discovery/scripts/discover_influencers.py \
  --topic "marketing" --has-email --max-results 100

# Filter to a specific follower range
python3 skills/linkedin-influencer-discovery/scripts/discover_influencers.py \
  --topic "fintech" --min-followers 10000 --max-followers 500000 --output summary
```

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--topic` | *required* | Topic to search (e.g. "artificial intelligence", "saas", "marketing") |
| `--category` | none | Category filter (e.g. "technology", "business", "lifestyle") |
| `--country` | none | Country (e.g. "United States of America", "United Kingdom") |
| `--language` | English | Language filter |
| `--min-followers` | 0 | Minimum follower count (client-side filter) |
| `--max-followers` | 0 (unlimited) | Maximum follower count (client-side filter) |
| `--has-email` | false | Only return influencers with an email address |
| `--max-results` | 100 | Max influencers to discover (up to 1000) |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (prefer `APIFY_API_TOKEN` env var) |
| `--timeout` | 600 | Max seconds to wait for Apify run |

## Cost

~$0.01 per result. 100 influencers ~ $1.00. The script prints a cost estimate before running.

## Output Fields

Each influencer result includes (when available):
- `full_name` - Display name
- `username` - Social media handle
- `biography` - Bio text
- `follower_count` - Total followers (across platforms)
- `following_count` - Following count
- `main_topic` - Primary topic/niche
- `topics` - List of associated topics
- `category_name` - Category classification
- `linkedin_url` - LinkedIn profile URL
- `has_email` - Whether email is available
- `external_url` - Website URLs
- `country`, `city` - Location
- `is_verified` - Verification status

## Notes

- Results are sorted by follower count (descending) by default
- The actor queries a pre-indexed database, not live LinkedIn search
- Follower counts are across all platforms, not LinkedIn-specific
- The `--min-followers` and `--max-followers` flags filter client-side after results return
- For detailed profile enrichment, use the Apify `harvestapi/linkedin-profile-scraper` actor on the discovered LinkedIn URLs
- For post analysis, use the Apify `harvestapi/linkedin-profile-posts` actor on the discovered LinkedIn URLs


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Entidade alvo** — Empresa, pessoa ou tendência?
2. **Profundidade** — Visão geral (quick) ou análise profunda (deep)?
3. **Objetivo** — O que esta pesquisa deve destravar no seu projeto?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

Use `linkedin-influencer-discovery` when you need to:
- Identify and qualify potential leads
- Build prospect lists from signal sources
- Enrich contact data for outreach

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Lead list / Company target** | Yes | CSV, pasted list, or upstream skill output |
| **ICP criteria** | Recommended | Qualification parameters for filtering |
| **API credentials** | Yes | API key (set via environment variable) |

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
| **Key findings** | `[OPERACIONAL]: linkedin-influencer-discovery — [finding]` | `[OPERACIONAL]: linkedin-influencer-discovery — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: linkedin-influencer-discovery — [param] works better as [value]` | `[OPERACIONAL]: linkedin-influencer-discovery — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: linkedin-influencer-discovery — [insight]` | `[ESTRATÉGICO]: linkedin-influencer-discovery — Competitor X has no case studies page, vulnerability for battlecard` |

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

