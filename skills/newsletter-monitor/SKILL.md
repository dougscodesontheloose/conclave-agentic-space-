---
name: newsletter-monitor
description: >
  Scan an AgentMail inbox for newsletter signals using configurable keyword
  campaigns. Extracts matched keywords, context snippets, and company mentions
  from incoming emails. Use for monitoring accounting industry newsletters for buying signals.
tags: [monitoring, signals, lead-generation]
---

# Newsletter Monitor

**Core principle:** Sinais só têm valor se a janela de oportunidade ainda estiver aberta.


Scan an AgentMail inbox for newsletter signals using configurable keyword campaigns. Designed for monitoring accounting industry newsletters for buying signals like acquisitions, Sage Intacct migrations, staffing challenges, and technology adoption.

## Quick Start

```bash
# Set your API key
export AGENTMAIL_API_KEY="your_key_here"

# Scan inbox with all campaigns (summary view)
python3 skills/newsletter-monitor/scripts/scan_newsletters.py --output summary

# Scan specific campaign, last 7 days
python3 skills/newsletter-monitor/scripts/scan_newsletters.py --campaign acquisitions --days 7 --output summary

# JSON output for downstream processing
python3 skills/newsletter-monitor/scripts/scan_newsletters.py --output json --limit 50
```

## Dependencies

```
pip3 install agentmail python-dotenv
```

## Configuration

Keyword campaigns are defined in `config/campaigns.json`. Each campaign has a description and a list of keywords for case-insensitive substring matching.

Built-in campaigns:
- **acquisitions** - CPA firm M&A activity
- **sage_intacct** - Sage Intacct migration and implementation signals
- **staffing** - Accounting talent and staffing challenges
- **technology** - Accounting technology adoption

## CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--campaign NAME` | Run only a specific campaign | All campaigns |
| `--days N` | Only scan emails from last N days | No limit |
| `--keywords "a,b,c"` | Custom keywords (overrides campaigns) | Use campaigns.json |
| `--output json\|summary` | Output format | `json` |
| `--inbox ADDRESS` | Override inbox address | `AGENTMAIL_INBOX` env or `supergoose@agentmail.to` |
| `--limit N` | Max messages to fetch | `100` |

## Output

### JSON mode (default)

Returns an array of matched messages with:
- `message_id`, `from`, `subject`, `date`
- `matched_campaigns` - which campaigns triggered
- `matched_keywords` - specific keywords found
- `context_snippets` - 200-char window around each match
- `companies_mentioned` - capitalized multi-word phrases near matches

### Summary mode

Human-readable report showing matched emails grouped by campaign with snippets and detected companies.

## Downstream Skills

When newsletter signals are found, chain to:
- **company-contact-finder** - look up contacts at mentioned companies
- **accounting-news-monitor** - combine with direct news monitoring for fuller signal coverage

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Contact not found** | Empty result from people search | Log `⚠️ No contacts found for [company]`. Skip to next company, note gap in output |
| **Enrichment failed** | API error or missing fields | Use partial data. Mark enrichment_status as `partial` in output |
| **Duplicate contact detected** | Match on LinkedIn URL or email in contact-cache | Skip duplicate, log `ℹ️ Skipped duplicate: [name]` |
| **Template rendering failed** | Missing personalization variables | Fall back to generic template. Flag `⚠️ Low personalization` in output |
| **Outreach tool connection failed** | API error from outreach platform | Export to CSV as fallback. Inform user of manual upload path |

**Principle:** Partial success is better than total failure. Always produce an output, even if degraded.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: newsletter-monitor — [finding]` | `[OPERACIONAL]: newsletter-monitor — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: newsletter-monitor — [param] works better as [value]` | `[OPERACIONAL]: newsletter-monitor — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: newsletter-monitor — [insight]` | `[ESTRATÉGICO]: newsletter-monitor — Competitor X has no case studies page, vulnerability for battlecard` |

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



## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
