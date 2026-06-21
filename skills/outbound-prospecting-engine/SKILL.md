---
type: playbook
name: outbound-prospecting-engine
description: >
  End-to-end outbound prospecting: detect intent signals, research companies,
  find decision-maker contacts, personalize messaging, launch campaign.
tags: [outreach, lead-generation, orchestration]
---

# Outbound Prospecting Engine

**Core principle:** A verdadeira personalização prova que você fez o dever de casa antes de pedir o tempo do prospect.


Build and run a complete outbound prospecting system: signal detection → company research → contact finding → personalization → campaign launch.

## When to Use

- "Set up outbound prospecting for [client]"
- "Build a lead gen engine targeting [ICP]"
- "Find and reach out to companies that need [solution]"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Prerequisites

- Client context.md with ICP, value props, positioning
- Signal keywords (what to monitor for intent)
- Approved messaging / email sequences (or generate them)


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

## Steps

### 1. Define Signal Sources

Based on the client's ICP and motion, select which signals to monitor:

| Signal Source | Best For | Skill |
|--------------|---------|-------|
| Job postings | Companies with allocated budget | job-posting-intent |
| Funding announcements | Companies with fresh capital | funding-signal-monitor |
| LinkedIn posts/comments | Practitioners discussing the problem | linkedin-post-research + linkedin-commenter-extractor |
| Conference attendees | People actively engaged with the space | luma-event-attendees |
| Competitor customers | Companies already buying similar solutions | competitor-post-engagers |

### 2. Run Signal Detection

Execute selected signal skills with client-specific keywords. Run in parallel.

**Output**: Raw signal list — companies + signal context.

### 3. Qualify & Score

**Skill**: lead-qualification

Filter against ICP criteria. Score each lead:
- Multi-signal leads = highest priority
- Job posting + funding = strongest intent
- Single social mention = lowest (awareness only)

### 4. Find Decision-Maker Contacts

**Skill**: company-contact-finder

For top qualified companies, find the specific decision-makers:
- Target titles from client's ICP
- Get email addresses and LinkedIn URLs

### 5. Deduplicate

**Skill**: contact-cache

Check all leads against the contact cache. Add new leads to cache. Skip any that have been contacted before.

### 6. Personalize Outreach

For each lead, generate personalized email sequence using:
- The signal that surfaced them (the "why now")
- Their company context (what they do, their pain)
- The client's value proposition (how it solves their pain)

### 7. Launch Campaign

**Skill**: cold-email-outreach

Set up the outreach campaign in your chosen tool:
- Create campaign with name and schedule
- Upload lead list
- Configure 2-3 email sequence (personalized per lead or per segment)
- Allocate mailboxes
- Set sending schedule

### 8. Monitor & Iterate

- Track open rates, reply rates, meeting bookings
- A/B test subject lines and messaging
- Re-run signal detection weekly to add new leads
- Update contact cache with outcomes

## Ongoing Cadence

- **Weekly**: Re-run signal detection, qualify new leads, add to campaign
- **Bi-weekly**: Review campaign metrics, adjust messaging
- **Monthly**: Review overall pipeline contribution, adjust signal sources

## Human Checkpoints

- **After Step 3**: Review qualified lead list before finding contacts
- **After Step 6**: Review personalized email copy before launching campaign
- **After Step 8**: Review campaign performance metrics

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
| **Key findings** | `[OPERACIONAL]: outbound-prospecting-engine — [finding]` | `[OPERACIONAL]: outbound-prospecting-engine — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: outbound-prospecting-engine — [param] works better as [value]` | `[OPERACIONAL]: outbound-prospecting-engine — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: outbound-prospecting-engine — [insight]` | `[ESTRATÉGICO]: outbound-prospecting-engine — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

