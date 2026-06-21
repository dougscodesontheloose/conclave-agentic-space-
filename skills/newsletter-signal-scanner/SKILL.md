---
name: newsletter-signal-scanner
description: >
  Subscribe to and scan industry newsletters for buying signals, competitor mentions,
  ICP pain-point language, and market shifts. Parses incoming newsletter emails via
  AgentMail, matches against keyword campaigns, and delivers a weekly digest of
  actionable signals. Use when a marketing team wants to turn newsletter subscriptions
  into an ongoing intelligence feed without manual reading.
tags: [monitoring]
---

# Newsletter Signal Scanner

**Core principle:** Sinais só têm valor se a janela de oportunidade ainda estiver aberta.


Turn your newsletter subscriptions into a structured intelligence feed. Monitors an AgentMail inbox for incoming newsletters, extracts signal-relevant content by keyword campaign, and delivers a weekly digest of what matters — competitor mentions, ICP pain language, market shifts, and emerging topics.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

- "Monitor industry newsletters for competitor mentions"
- "Alert me when newsletters mention [topic] or [company]"
- "What are newsletters writing about this week in our space?"
- "Set up newsletter monitoring for [client]"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Phase 0: Intake

### Newsletters to Monitor
1. Which newsletters should be subscribed to and monitored? (List names or URLs)
   - If unknown, ask: "What 3-5 newsletters does your ICP read?" — then use `sponsored-newsletter-finder` to discover others.
2. Which AgentMail inbox should receive them? (Or should we create a new one?)

### Keyword Campaigns
3. Competitor names to track (e.g., "Clay", "Apollo", "Outreach")
4. ICP pain-language terms to track (e.g., "outbound struggling", "pipeline dried up", "SDR ramp")
5. Market shift terms (e.g., "AI SDR", "agent-led growth", "GTM engineer")
6. Your brand name (to catch mentions)

### Output
7. Digest delivery: Slack channel, email, or markdown file? (default: markdown file)
8. Frequency: daily or weekly? (default: weekly)

Save campaign config to the current working directory as `newsletter-signals.json` (or user-specified path).

```json
{
  "inbox_id": "<agentmail_inbox_id>",
  "keyword_campaigns": {
    "competitors": ["Clay", "Apollo", "Outreach", "Salesloft"],
    "pain_language": ["pipeline is down", "outbound isn't working", "SDR ramp"],
    "market_shifts": ["AI SDR", "GTM engineer", "agent-led"],
    "brand_mentions": ["YourCompany", "yourcompany.com"]
  },
  "newsletters": [
    {"name": "Exit Five", "from_domain": "exitfive.com"},
    {"name": "The GTM Newsletter", "from_domain": "gtmnewsletter.com"}
  ],
  "output": {
    "format": "markdown",
    "path": "newsletter-signals-[DATE].md"
  }
}
```

## Phase 1: Scan Inbox

Use the AgentMail API (agentmail.dev) to fetch new emails from the monitored inbox:

```
Fetch emails from inbox <inbox_id> since <last_scan_date>
Filter to: known newsletter senders (match against newsletters config)
```

For each email:
- Extract subject, sender, date, full body text
- Strip HTML → plain text for analysis

## Phase 2: Apply Keyword Campaigns

For each newsletter email, scan for keyword matches:

```python
for email in emails:
    matches = {}
    for campaign, keywords in keyword_campaigns.items():
        found = []
        for keyword in keywords:
            if keyword.lower() in email.body.lower():
                # Extract context: 50 chars before + keyword + 50 chars after
                context = extract_context(email.body, keyword)
                found.append({"keyword": keyword, "context": context})
        if found:
            matches[campaign] = found
    email.signal_matches = matches
```

Only include emails with at least one keyword match in the digest.

## Phase 3: Extract Signal Snippets

For each matched email, extract clean signal snippets:

**Competitor mention example:**
> Newsletter: The GTM Newsletter | Date: 2026-03-05
> Campaign: competitors
> Keyword: "Clay"
> Context: "...teams that use **Clay** for enrichment are seeing 3x better personalization rates compared to..."

**Pain language example:**
> Newsletter: Exit Five | Date: 2026-03-04
> Campaign: pain_language
> Keyword: "outbound isn't working"
> Context: "...a lot of founders telling me **outbound isn't working** the way it used to. The reply rates I'm seeing..."

## Phase 4: Output Format

```markdown
# Newsletter Signal Digest — Week of [DATE]

## Summary
- Newsletters scanned: [N]
- Emails with signals: [N]
- Top trending topic: [topic]

---

## Competitor Mentions

### Clay
- **[Newsletter Name]** — [Date]
  > "[Context snippet]"
  Source: [email subject] | [URL if available]

### [Other Competitor]
...

---

## ICP Pain Language

Signals suggesting your ICP is feeling pain your product solves:

- **[Newsletter Name]** — [Date]
  > "[Context snippet]"
  — Relevance: [why this matters]

---

## Market Shift Signals

Emerging topics gaining newsletter coverage:

- **"[Topic]"** — mentioned in [N] newsletters this week
  > "[Context snippet]"

---

## Your Brand Mentions
[Any mentions of your company or product]

---

## Recommended Actions
1. [Specific action based on signals — e.g., "Exit Five is covering AI SDR fatigue — good moment to publish our take"]
2. [Competitive response if needed]
```

Save to the current working directory as `newsletter-signals-[YYYY-MM-DD].md` (or user-specified path).

## Phase 5: Setup — Subscribe to Newsletters

For first-time setup, subscribe the AgentMail address to target newsletters:

1. Get the AgentMail inbox address (via AgentMail API at agentmail.dev)
2. For each newsletter, visit subscription page and submit the AgentMail address
3. Confirm subscriptions (check inbox for confirmation emails)
4. Allow 1-2 weeks of accumulation before first full digest

## Scheduling

Run weekly (Monday morning recommended):

```bash
# Every Monday at 7am — before the team's standup
0 7 * * 1 python3 run_skill.py newsletter-signal-scanner --client <client-name>
```

## Cost

| Component | Cost |
|-----------|------|
| AgentMail inbox | Depends on AgentMail pricing |
| Email parsing + keyword matching | Free (local logic) |
| **Total** | **Near-zero ongoing cost** |

## Tools Required

- **AgentMail API** (agentmail.dev) — for inbox access. Requires `AGENTMAIL_API_KEY` environment variable and the `agentmail` pip package (`pip3 install agentmail`).

## Trigger Phrases

- "Scan newsletters for this week's signals"
- "What are industry newsletters saying about [topic]?"
- "Run newsletter signal scanner for [client]"
- "Set up newsletter monitoring"

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Source temporarily unavailable** | HTTP error or timeout on monitored source | Skip source for this scan cycle. Note in output `⚠️ [source] unavailable` |
| **No new signals detected** | Valid scan but 0 new items | Report clean scan explicitly: "No new signals detected (sources: X scanned)". Don't fail silently |
| **Keyword config outdated** | Consistently 0 matches across multiple scans | Suggest keyword review. Log `ℹ️ Consider updating keywords — 0 matches in last N scans` |
| **API credits exhausted** | Credit limit or quota error | Switch to free alternatives where available. Log remaining credit status |
| **Duplicate signals from prior scan** | Match against previous scan results | Deduplicate. Only surface genuinely new items |

**Principle:** Monitoring skills must clearly distinguish "nothing happened" from "scan failed". Both are valid but mean different things.


## Composability


**Feeds into:**
- `competitor-intel`
- `industry-scanner`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: newsletter-signal-scanner — [finding]` | `[OPERACIONAL]: newsletter-signal-scanner — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: newsletter-signal-scanner — [param] works better as [value]` | `[OPERACIONAL]: newsletter-signal-scanner — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: newsletter-signal-scanner — [insight]` | `[ESTRATÉGICO]: newsletter-signal-scanner — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Data completeness:** At least 1 source returned results. If all sources failed, the output must explain why
- [ ] **No silent failures:** Every source that was attempted has a status (success/partial/failed) in the output
- [ ] **Deduplication applied:** No duplicate entries in the final dataset
- [ ] **Output format valid:** CSV/JSON is well-formed and parseable
- [ ] **User checkpoint:** Present summary to user before proceeding to downstream skills

**If any check fails:** Stop, report the failure, and ask the user how to proceed.

