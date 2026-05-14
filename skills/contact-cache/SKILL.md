---
name: contact-cache
description: >
  Track all identified/contacted people across strategies. CSV-backed contact
  database with dedup by LinkedIn URL or email. Prevents duplicate outreach
  when running strategies on a recurring cadence.
tags: [lead-generation]
---

# Contact Cache

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


Track all identified/contacted people across strategies. CSV-backed contact database with dedup by LinkedIn URL or email. Prevents duplicate outreach when running strategies on a recurring cadence.

## Usage

```bash
# Check if contacts are already cached
python3 skills/contact-cache/scripts/cache.py check --linkedin-urls "https://linkedin.com/in/person1,https://linkedin.com/in/person2"
python3 skills/contact-cache/scripts/cache.py check --emails "john@example.com,jane@example.com"

# Add a single contact
python3 skills/contact-cache/scripts/cache.py add --name "John Smith" --linkedin-url "https://linkedin.com/in/johnsmith" --email "john@example.com" --company "Acme Corp" --title "VP Finance" --strategy "2A-hiring-signal"

# Bulk import from CSV
python3 skills/contact-cache/scripts/cache.py add --csv /path/to/leads.csv --strategy "2A-hiring-signal"

# Update a contact's status
python3 skills/contact-cache/scripts/cache.py update --linkedin-url "https://linkedin.com/in/johnsmith" --status contacted --notes "Sent intro email 2026-02-24"

# Export the full cache
python3 skills/contact-cache/scripts/cache.py export --format csv
python3 skills/contact-cache/scripts/cache.py export --format json
python3 skills/contact-cache/scripts/cache.py export --status contacted
python3 skills/contact-cache/scripts/cache.py export --strategy "2A-hiring-signal"

# Print summary statistics
python3 skills/contact-cache/scripts/cache.py stats
```

## Data

Contacts are stored in `skills/contact-cache/data/contacts.csv`. The file is auto-created on first use.

Dedup is by LinkedIn URL (preferred) or email. Both are normalized and hashed (SHA256, first 16 chars) to produce a stable `contact_id`.

## Valid Statuses

`new`, `qualified`, `contacted`, `replied`, `meeting_booked`, `converted`, `not_interested`


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

Use `contact-cache` when you need to:
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


## Output Format

| Output | Format | Location |
|---|---|---|
| **Lead list** | CSV | `{name}-{YYYY-MM-DD}.csv` |
| **Summary report** | Markdown | Displayed to user |
| **Qualification verdicts** | Inline | Included per lead in CSV |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

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
- `linkedin-message-writer`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: contact-cache — [finding]` | `[OPERACIONAL]: contact-cache — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: contact-cache — [param] works better as [value]` | `[OPERACIONAL]: contact-cache — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: contact-cache — [insight]` | `[ESTRATÉGICO]: contact-cache — Competitor X has no case studies page, vulnerability for battlecard` |

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

