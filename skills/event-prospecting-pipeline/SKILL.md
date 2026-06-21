---
type: playbook
name: event-prospecting-pipeline
description: Find attendees at conferences/events, research their companies, qualify against ICP, and launch outreach
tags: [lead-generation, outreach, events]
---

# Event Prospecting Pipeline

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


End-to-end workflow: find event attendees → research → qualify against ICP → deduplicate → outreach.


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

Nenhuma. Pure reasoning skill.

## When to Use

- "Find leads from [event name/URL]"
- "Who's speaking at [conference]? Get me their contact info"
- "Find AI events in SF and get me decision-maker contacts"
- "Find leads from upcoming conferences and launch outreach"

> **For Luma-only qualified lead gen** with built-in Google Sheets + Slack alerting, use [[skills/composites/get-qualified-leads-from-luma/SKILL.md]] instead. This playbook is the full pipeline including outreach.


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Steps

### 1. Find Attendees / Speakers
**Skills:** luma-event-attendees OR conference-speaker-scraper

- If user provides a Luma event URL or topic → use `luma-event-attendees`
- If user provides a conference website → use `conference-speaker-scraper`
- If user provides a topic/location → use `luma-event-attendees` Apify search mode to find events first

**Output:** Person list with names, bios, LinkedIn/Twitter URLs, companies.

### 2. Research & Enrich
**Capability:** Web search

For each person/company:
- Company funding stage, size, product
- Person's current role and seniority
- Recent news or activity

Skip if user just wants a raw attendee list.

### 3. Qualify Against ICP
**Skill:** lead-qualification

Filter the enriched list against the client's ICP criteria. Score each lead.

### 4. Find Decision-Maker Contacts
**Skill:** company-contact-finder

For qualified companies, find the specific decision-makers with email addresses.

### 5. Deduplicate
**Skill:** contact-cache

Check all leads against the contact cache to prevent duplicate outreach across strategies.

### 6. Output Results
**Capability:** Google Sheets or CSV export

Export qualified, deduplicated leads with columns: Name, Title, Company, LinkedIn URL, Email, Signal, Score.

### 7. Launch Outreach (optional)
**Skill:** cold-email-outreach

If approved, set up personalized outreach via your chosen outreach tool or direct email via AgentMail API (agentmail.dev).

## Human Checkpoints

- **After Step 3**: Review qualified lead list before finding contacts
- **After Step 6**: Review final list and email copy before launching outreach

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
- Skills tagged `lead-generation` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `cold-email-outreach`
- `contact-cache`
- `linkedin-message-writer`
- `linkedin-outreach`
- `pipeline-review`
- `sequence-performance`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: event-prospecting-pipeline — [finding]` | `[OPERACIONAL]: event-prospecting-pipeline — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: event-prospecting-pipeline — [param] works better as [value]` | `[OPERACIONAL]: event-prospecting-pipeline — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: event-prospecting-pipeline — [insight]` | `[ESTRATÉGICO]: event-prospecting-pipeline — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

