---
name: pain-language-engagers
description: >
  Find warm leads by searching LinkedIn for pain-language posts — the frustrations, complaints,
  and operational struggles your ICP talks about publicly. Asks clarifying questions to understand
  your product, ICP, and their pain points, then generates pain-language search keywords,
  scrapes LinkedIn for posts and engagers, enriches profiles, and ICP-filters the results.
  Use when someone wants to "find leads who are complaining about X" or "find people
  discussing problems we solve" or "LinkedIn pain-based prospecting."
tags: [lead-generation]
---

# Pain-Language Engagers

Find warm leads by scraping LinkedIn for pain-language posts and their engagers. People who write about, react to, or comment on posts expressing operational frustrations are signaling they live with a problem your product solves. This skill turns those signals into a qualified lead list.

**Core principle:** Search for **pain-language**, not solution-language. Solution keywords ("AI automation", "workflow optimization") attract builders and VCs. Pain keywords ("can't find drivers", "check calls are killing us") attract operators living with the problem.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## Phase 0: Intake

Before generating keywords or running anything, ask the user these questions. Present them as a numbered list and tell the user to answer what's relevant and skip what's not.

### Product & Pain Context

1. What does your product/service do in one sentence?
2. What specific problem does it solve? Who feels this pain most acutely?
3. What does your ICP's day-to-day look like WITHOUT your product? (The frustrations, workarounds, manual processes)
4. What phrases would someone use when **complaining** about this problem on LinkedIn? (e.g., "check calls are killing us", "can't find drivers", "spending hours on manual data entry")

### ICP Definition

5. What industries/verticals are your target buyers in?
6. What job titles or roles are your ideal buyers? (e.g., "VP Operations", "Broker owner", "Head of Logistics")
7. What titles should be EXCLUDED? (e.g., "Software Engineer", "AI researcher")
8. Any specific competitors whose employees should be filtered out?
9. Geographic focus? (e.g., "United States only", "global")

### LinkedIn Signal Sources

10. Any LinkedIn company pages where your ICP is likely to engage? (Industry publications, communities, competitor pages)
11. Any specific LinkedIn posts or content creators your ICP follows?

## Phase 1: Generate Pain-Language Keywords

Based on the intake answers, generate ~15-25 pain-language keywords in LinkedIn boolean search syntax. Organize into categories:

- **Staffing/Resource Pain** — hiring difficulties, turnover, burnout
- **Operational Friction** — manual processes, missed SLAs, communication breakdowns
- **Margin/Growth Pain** — cost pressure, scaling challenges
- **Process Complaints** — specific workflow frustrations

**Key principle:** Every keyword should be something a frustrated operator would actually type or say, not marketing language or solution framing.

Also generate:
- **ICP keyword list** — industry terms for ICP classification (from answer #5)
- **Tech vendor exclusion list** — competitor names + generic tech titles (from answers #7, #8)
- **Pain-pattern regexes** — for filtering company page posts (derived from the keywords)
- **Broad topic patterns** — industry terms for known industry page filtering
- **Hardcoded company pages** — from answer #10, plus any the agent suggests based on the industry

**Present the full keyword list to the user for approval/refinement before running.** This is the most critical step — bad keywords = bad leads.

Once approved, save the complete config as JSON:

```bash
# Save config
skills/pain-language-engagers/configs/{client-name}.json
```

Config JSON structure:

```json
{
  "client_name": "example-client",
  "pain_keywords": ["\"can't find X\"", "\"hiring Y\" problems"],
  "pain_patterns": ["can.t find X", "hiring Y", "manual.*process"],
  "icp_keywords": ["industry-term-1", "industry-term-2"],
  "tech_vendor_keywords": ["software engineer", "competitor-name"],
  "hardcoded_companies": ["https://www.linkedin.com/company/example/"],
  "industry_pages": ["https://www.linkedin.com/company/example/"],
  "broad_topic_patterns": ["industry", "sector", "niche-term"],
  "country_filter": "United States",
  "days_back": 60,
  "max_posts_per_keyword": 50,
  "max_posts_per_company": 100
}
```

## Phase 2: Run LinkedIn Scraping Pipeline

Execute the pipeline script with the saved config:

```bash
python3 skills/pain-language-engagers/scripts/pain_language_engagers.py \
  --config skills/pain-language-engagers/configs/{client-name}.json \
  [--test] [--companies "url1,url2"]
```

**Flags:**
- `--config` (required) — path to the client config JSON
- `--test` — limit to 3 keywords, 5 posts per company (for validation)
- `--skip-discovery` — skip keyword search, only scrape hardcoded/extra companies
- `--companies "url1,url2"` — add extra company URLs to scrape

**What the script does:**

1. **Keyword search** — `apimaestro/linkedin-posts-search-scraper-no-cookies` for each pain keyword
2. **Post author extraction** — People who wrote pain posts = direct leads (free, no API call)
3. **Company page discovery** — Extract company pages from keyword results
4. **Company page engager scraping** — `harvestapi/linkedin-company-posts` for each company page, pain-filtered
5. **Profile enrichment** — `harvestapi/linkedin-profile-scraper` for all profiles (gets headline + location)
6. **ICP classification** — Using the client-specific ICP/vendor keyword lists from config
7. **Dedup + CSV export**

**Cost estimate:**
- Keyword search: ~$0.10 per keyword (~$2 for 20 keywords)
- Company page scraping: ~$0.002 per post per company (~$0.20 per company)
- Profile enrichment: ~$0.003 per profile
- Full run with 20 keywords + 10 companies: ~$5-10

**Always run with `--test` first** to validate the config produces relevant results before a full run.

## Phase 3: Review & Refine

After the script completes, present results to the user:

- **ICP breakdown** — counts by tier (Likely / Possible / Unknown / Tech Vendor)
- **Top 15 Likely ICP leads** — name, role, company, engagement type
- **Sample of filtered-out leads** — so user can catch false negatives
- **Keyword performance** — which keywords produced the most leads, which were duds

If the user wants adjustments:
1. Update the config JSON (add/remove keywords, adjust ICP lists)
2. Re-run the script
3. Repeat until the user is satisfied

Common adjustments:
- **Too many Tech Vendor results** — add more vendor names to `tech_vendor_keywords`
- **Missing obvious ICP leads** — add more industry terms to `icp_keywords`
- **Irrelevant posts** — refine `pain_patterns` to be more specific
- **Not enough results** — add more keywords or reduce `days_back` constraint

## Phase 4: Output

CSV exported to the current working directory as `{client-name}-{date}.csv` with columns:

| Column | Description |
|--------|-------------|
| Name | Full name |
| LinkedIn Profile URL | Profile link |
| Role | Parsed from headline |
| Company Name | Parsed from headline |
| Location | From profile enrichment |
| Source Page | Which company page(s) they engaged on |
| Post URL(s) | Links to the post(s) they engaged with |
| Engagement Type | Post Author, Comment, or Reaction |
| Comment Text | Their comment (if applicable — personalization gold) |
| ICP Tier | Likely ICP, Possible ICP, Unknown, or Tech Vendor |
| Niche Keyword | Which pain keyword matched |

## Tools Required

- **Apify API token** — set as `APIFY_API_TOKEN` in `.env`
- **Apify actors used:**
  - `apimaestro/linkedin-posts-search-scraper-no-cookies` (keyword search)
  - `harvestapi/linkedin-company-posts` (company page scraping)
  - `harvestapi/linkedin-profile-scraper` (profile enrichment)

## Example Usage

**Trigger phrases:**
- "Find people complaining about [problem] on LinkedIn"
- "LinkedIn pain-based prospecting for [product]"
- "Find leads who are discussing [pain point]"
- "Scrape LinkedIn for [industry] pain posts"
- "Run the pain-language engagers pipeline for [client]"

**With existing config:**
```bash
python3 skills/pain-language-engagers/scripts/pain_language_engagers.py \
  --config skills/pain-language-engagers/configs/happy-robot.json
```

**Test mode:**
```bash
python3 skills/pain-language-engagers/scripts/pain_language_engagers.py \
  --config skills/pain-language-engagers/configs/happy-robot.json --test
```

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
| **Key findings** | `[OPERACIONAL]: pain-language-engagers — [finding]` | `[OPERACIONAL]: pain-language-engagers — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: pain-language-engagers — [param] works better as [value]` | `[OPERACIONAL]: pain-language-engagers — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: pain-language-engagers — [insight]` | `[ESTRATÉGICO]: pain-language-engagers — Competitor X has no case studies page, vulnerability for battlecard` |

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

