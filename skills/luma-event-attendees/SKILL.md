---
name: luma-event-attendees
version: 1.0.0
description: Find speakers, hosts, and guest profiles at conferences and events on Luma. Two modes - free direct scrape for hosts, or Apify-powered search for full guest profiles with LinkedIn/Twitter/bio.
tags: [lead-generation]
---

# luma-event-attendees

**Core principle:** Qualificar cedo custa pouco; desqualificar tarde custa o deal.


Find and extract speakers, hosts, and registered guest profiles from Luma events for outreach prospecting.

## Two Modes

### 1. Direct Scrape (free)

Scrapes Luma event pages directly. Gets event metadata + hosts. Guest profiles only if publicly embedded in the page.

```bash
python3 scripts/scrape_event.py https://lu.ma/abc123
```

### 2. Apify Search (paid, recommended for guest lists)

Uses the `lexis-solutions/lu-ma-scraper` Apify actor to search Luma and return full event data including **featured guest profiles** (name, bio, LinkedIn, Twitter, Instagram, website).

```bash
python3 scripts/scrape_event.py --search "AI San Francisco"
```

**Cost:** $29/month flat subscription on Apify.
**Rent:** https://console.apify.com/actors/r5gMxLV2rOF3J1fxu

## Setup

### 1. Apify API Token (required for --search mode)

1. Create account: https://apify.com/
2. Get API token: https://console.apify.com/account/integrations
3. Rent the Luma scraper: https://console.apify.com/actors/r5gMxLV2rOF3J1fxu ($29/mo, 24h free trial)
4. Set token:

```bash
export APIFY_API_TOKEN="apify_api_YOUR_TOKEN_HERE"
# Or create .env file in skill directory
```

### 2. Install Dependencies

```bash
pip3 install requests
```

## Usage

### Direct Scrape (free, hosts only)

```bash
# Single event
python3 scripts/scrape_event.py https://lu.ma/pwciozw0

# Multiple events
python3 scripts/scrape_event.py https://lu.ma/abc https://lu.ma/def

# Export to CSV
python3 scripts/scrape_event.py https://lu.ma/abc --output hosts.csv
```

### Apify Search (guest profiles)

```bash
# Search for AI events in SF
python3 scripts/scrape_event.py --search "AI San Francisco"

# Just list events (don't extract people)
python3 scripts/scrape_event.py --search "SaaS NYC" --events-only

# Export all guests to CSV
python3 scripts/scrape_event.py --search "AI San Francisco" --output guests.csv

# Export as JSON
python3 scripts/scrape_event.py --search "AI SF" --output guests.json --json
```

### Caching

Results cached for 24 hours by default:

```bash
# Force fresh fetch
python3 scripts/scrape_event.py --search "AI SF" --no-cache

# Custom cache duration
python3 scripts/scrape_event.py --search "AI SF" --cache-hours 12
```

### Options Reference

```
Positional:
  urls                    Event URLs to scrape directly (free)

Search:
  --search, -s            Search Luma via Apify (e.g., 'AI San Francisco')
  --events-only           Only list events, don't extract people

Output:
  --output, -o            Output file path (.csv or .json)
  --json                  Output JSON format (default: CSV)

Cache:
  --no-cache              Skip cache, always fetch fresh
  --cache-hours           Cache max age in hours (default: 24)
```

## Output Format

### CSV Columns

| name | event_role | bio | title | company | linkedin_url | twitter_url | instagram_url | website_url | username | event_name | event_date | event_url |
|------|-----------|-----|-------|---------|-------------|-------------|---------------|-------------|----------|------------|------------|-----------|

### What You Get Per Person

- **name** - Full name
- **event_role** - Host, Guest, or Speaker
- **bio** - Luma profile bio
- **linkedin_url** - LinkedIn profile URL
- **twitter_url** - Twitter/X profile URL
- **instagram_url** - Instagram handle
- **website_url** - Personal website
- **username** - Luma username
- **event_name** - Which event they're associated with
- **event_date** - Event date (ISO format)
- **event_url** - Link to the event

## AI Agent Workflow

This skill is designed to be called by an AI agent as part of a prospecting workflow:

### Step 1: Find Events

> "Search Luma for AI and SaaS events in San Francisco"

```bash
python3 scripts/scrape_event.py --search "AI San Francisco" --events-only
```

### Step 2: Extract Guest Profiles

> "Get all guest profiles from those events"

```bash
python3 scripts/scrape_event.py --search "AI San Francisco" --output guests.csv
```

### Step 3: Qualify Against ICP

Ask the agent to filter the CSV:

> "From these guests, find founders/VPs at B2B SaaS companies, 20-200 employees"

### Step 4: Enrich

For qualified leads:
- Look up LinkedIn profiles for role/company details
- Research their companies
- Check for overlapping signals (hiring? recently funded?)

### Step 5: Generate Outreach

> "Draft connection requests for qualified guests. I'll be at [event]. We sell [product] at [price]. Keep it casual."

## Data Access Realities

| Data | Direct Scrape (free) | Apify Search (paid) |
|------|---------------------|---------------------|
| Event metadata | Yes | Yes |
| Hosts/organizers | Yes | Yes |
| Featured guests (public RSVPs) | Sometimes | Yes |
| Full attendee list | No (requires auth) | Partial (public profiles only) |
| Guest LinkedIn/Twitter | Yes (if in page) | Yes |
| Guest bio | Yes (if in page) | Yes |
| Guest email | No | No |

**Note:** Luma events have a `show_guest_list` setting. When disabled, guest profiles aren't publicly accessible. The Apify scraper can still get `featured_guests` for events that have them.

## Example Prompts

**Quick search:**
> "Find AI events in SF this month and get me guest profiles"

**Targeted:**
> "Search Luma for 'SaaS growth' events. Export all guest profiles to CSV. Then qualify against our ICP: VP+ at B2B SaaS, 50-500 employees."

**Full workflow:**
> "Search Luma for AI and developer events in SF. Get all guest profiles. For each person with a LinkedIn, check if they match our ICP (founders/VPs at B2B SaaS, 20-200 employees, Series A-C). Draft pre-event connection requests for the ones I'll see at [event name]. We sell GTM engineering at $10K/month. Output qualified leads to CSV."

## Troubleshooting

### "APIFY_API_TOKEN not set"

```bash
export APIFY_API_TOKEN="your_token_here"
```

### "Apify actor not rented"

Rent the Luma scraper at: https://console.apify.com/actors/r5gMxLV2rOF3J1fxu

### No guests found for an event

- The event may have `show_guest_list` disabled
- Try the --search mode which can access featured_guests
- Some events simply don't have public guest profiles

### "ModuleNotFoundError: requests"

```bash
pip3 install requests
```

## Metadata

```yaml
metadata:
  clawdbot:
    emoji: "🎤"
    requires:
      env: ["APIFY_API_TOKEN"]
      bins: ["python3"]
      packages: ["requests"]
```

---

Built by Goose - Powered by Apify (lexis-solutions/lu-ma-scraper)

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
| **Key findings** | `[OPERACIONAL]: luma-event-attendees — [finding]` | `[OPERACIONAL]: luma-event-attendees — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: luma-event-attendees — [param] works better as [value]` | `[OPERACIONAL]: luma-event-attendees — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: luma-event-attendees — [insight]` | `[ESTRATÉGICO]: luma-event-attendees — Competitor X has no case studies page, vulnerability for battlecard` |

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

1. **ICP** — Qual o perfil ideal exato que estamos buscando?
2. **Contexto** — Qual a dor que nossa abordagem resolve?
3. **Volume** — Limite de leads/mensagens por lote?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
