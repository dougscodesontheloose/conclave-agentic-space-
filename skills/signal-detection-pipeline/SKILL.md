---
type: playbook
name: signal-detection-pipeline
description: Detect buying signals from multiple sources, qualify leads, and generate outreach context
tags: [signals, lead-generation, orchestration]
---

# Signal Detection Pipeline

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


Monitor multiple signal sources to find companies actively in-market for your client's solution. Combine signals for higher-confidence leads.


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

- "Find companies that might need [our product]"
- "Run signal detection for [problem area]"
- "Find buying signals in [industry/topic]"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Signal Sources

Run the sources relevant to the client's ICP. Each is independent — run in parallel.

### Job Posting Signals (Strongest)
**Skill:** job-posting-intent

Companies hiring for roles in the problem area = budget allocated and pain acknowledged.
- Input: Job keywords, ICP criteria
- Output: Qualified companies with outreach angles

### Funding Signals
**Skill:** funding-signal-monitor

Recently funded companies = budget available, growth mandate.
- Input: Industry, funding stage filter
- Output: Funded companies with timing context

### Conference Attendance Signals
**Skill:** luma-event-attendees

People attending events in the problem space = actively engaged.
- Input: Event URLs or topic search
- Output: Person/company list

### Reddit Pain Signals
**Skill:** reddit-post-finder

People complaining about or discussing the problem = experiencing the pain.
- Input: Keywords, relevant subreddits
- Output: Posts with authors, context

### LinkedIn Content Signals
**Skill:** linkedin-post-research + linkedin-commenter-extractor

People posting about or engaging with the problem = thought leaders or practitioners.
- Input: Keywords, time frame
- Output: Posters and commenters with engagement data

## Combining Signals

After running relevant sources:

1. **Deduplicate** companies appearing across multiple signals (multi-signal = strongest leads)
2. **Score** each lead: assign signal strength based on source quality and recency
   - Job posting + funding = highest intent
   - LinkedIn post + Reddit complaint = validated pain
   - Single conference attendance = lowest (awareness only)
3. **Enrich** top leads with web search for company details
4. **Consolidate** into a single Google Sheet: Company, Signal Sources, Signal Strength, Context, Outreach Angle
5. **Prioritize** companies with multiple signal types

## Human Checkpoints

- **After combining signals**: Review consolidated list before outreach

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
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `cold-email-outreach`
- `contact-cache`
- `lead-qualification`
- `linkedin-message-writer`
- `linkedin-outreach`
- `outbound-prospecting-engine`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: signal-detection-pipeline — [finding]` | `[OPERACIONAL]: signal-detection-pipeline — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: signal-detection-pipeline — [param] works better as [value]` | `[OPERACIONAL]: signal-detection-pipeline — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: signal-detection-pipeline — [insight]` | `[ESTRATÉGICO]: signal-detection-pipeline — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

