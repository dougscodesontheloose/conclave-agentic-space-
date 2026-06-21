---
name: champion-tracker
description: >
  Track product champions for job changes and qualify their new companies against ICP.
  Takes a CSV of known champions (with LinkedIn URLs), creates a baseline snapshot via
  Apify enrichment, then detects when champions move to new companies. Scores new
  companies on a 0-4 ICP fit scale. Outputs a downloadable CSV of movers with
  qualification verdicts.
tags: [lead-generation]
---

# Champion Tracker

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


Detect when product champions change jobs and qualify their new companies against ICP.

## When to Use

- You have a list of known product users/champions (from reviews, LinkedIn posts, CRM exports)
- You want to detect when they change companies (high-intent re-sell signal)
- You want each job change scored against ICP before reaching out


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Two Phases

### Phase A: Discover Champions (agent-driven, one-time)

Build the initial champion list from public sources. This is done by the agent, not the script.

1. **Scrape reviews** — Use `review-site-scraper` skill to pull G2/Trustpilot reviews. Extract reviewer names + companies.
2. **Search LinkedIn posts** — Use Crustdata MCP to find people who posted about the product.
3. **Resolve LinkedIn URLs** — Use Crustdata MCP to search by name + company → get profile URLs.
4. **Compile CSV** — Merge all sources into `champions.csv` with required columns.

### Phase B: Track Job Changes (script-driven, repeatable)

Use `champion_tracker.py` for ongoing tracking.

## Script Usage

### Prerequisites

- `APIFY_API_TOKEN` in `.env` (for LinkedIn profile enrichment)
- Champion CSV with columns: `name`, `linkedin_url` (required); `original_company`, `original_title`, `email`, `source`, `notes` (optional)


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

### Commands

**Initialize baseline** (first run):
```bash
# Dry run — see cost estimate
python3 skills/champion-tracker/scripts/champion_tracker.py init -i champions.csv --dry-run

# Create baseline
python3 skills/champion-tracker/scripts/champion_tracker.py init -i champions.csv
```

**Check for job changes** (subsequent runs):
```bash
# Dry run
python3 skills/champion-tracker/scripts/champion_tracker.py check --dry-run

# Detect changes and output CSV
python3 skills/champion-tracker/scripts/champion_tracker.py check -o changes.csv
```

**View status**:
```bash
python3 skills/champion-tracker/scripts/champion_tracker.py status
```

## Output CSV Columns

| Column | Description |
|--------|-------------|
| champion_name | Full name |
| linkedin_url | LinkedIn profile URL |
| previous_company | Company at baseline |
| previous_title | Title at baseline |
| new_company | Current company (changed) |
| new_title | Current title |
| change_detected_date | Date this check was run |
| position_start_date | When they started the new role |
| days_since_change | Days since new position started |
| icp_score | 0-4 ICP qualification score |
| icp_verdict | Strong Fit / Good Fit / Possible Fit / Weak Fit |
| icp_notes | Scoring breakdown |
| email | Email if available |
| notes | Original notes from champion CSV |

## ICP Scoring (0-4)

| Signal | Points | What it checks |
|--------|--------|----------------|
| B2B signal | 1.0 | Title contains sales/SDR/revenue/growth keywords |
| Outbound motion | 1.0 | Sales leadership title (VP Sales, Head of Growth, etc.) |
| Company size | 1.0 / 0.5 | SMB/mid-market = 1.0; unknown = 0.5 benefit-of-doubt |
| Seniority | 1.0 | VP, Director, Head of, C-level, Founder |

**Verdicts**: Strong Fit (>=3) / Good Fit (>=2) / Possible Fit (>=1.5) / Weak Fit (<1.5)

## Cost

- ~$3 per 1,000 LinkedIn profiles enriched
- 50-80 champions ≈ $0.15-0.25 per run
- `--dry-run` always shows cost before any API calls

## File Structure

```
skills/champion-tracker/
  SKILL.md                    # This file
  scripts/
    champion_tracker.py       # Main CLI script
  input/
    champions_template.csv    # Template for manual additions
  snapshots/                  # Created at runtime
    baseline.json             # Latest full snapshot
    archive/                  # Timestamped copies
  output/                     # Created at runtime
    changes-YYYY-MM-DD.csv    # Generated output
```

## Dependencies

- Reuses `LinkedInEnricher` from `skills/lead-qualification/scripts/enrich_leads.py`
- Falls back to inline implementation if import fails
- Requires: `requests` (Python package), `APIFY_API_TOKEN` (env var)

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
| **Key findings** | `[OPERACIONAL]: champion-tracker — [finding]` | `[OPERACIONAL]: champion-tracker — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: champion-tracker — [param] works better as [value]` | `[OPERACIONAL]: champion-tracker — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: champion-tracker — [insight]` | `[ESTRATÉGICO]: champion-tracker — Competitor X has no case studies page, vulnerability for battlecard` |

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

