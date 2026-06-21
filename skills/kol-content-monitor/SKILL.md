---
name: kol-content-monitor
description: >
  Track what key opinion leaders (KOLs) in your space are posting on LinkedIn and Twitter/X.
  Surfaces trending narratives, high-engagement topics, and early signals of emerging
  conversations before they peak. Chains linkedin-profile-post-scraper and twitter-mention-tracker.
  Use when a marketing team wants to ride trends rather than create them from scratch,
  or when a founder wants to know which topics are resonating with their audience.
tags: [monitoring]
---

# KOL Content Monitor

Track what Key Opinion Leaders in your space are writing about. Surface trending narratives early — before they peak — so your team can join the conversation at the right time with relevant content.

**Core principle:** For seed-stage teams, the fastest path to content distribution is riding a wave that's already breaking, not creating one from scratch.


## Prerequisites

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

- "What are the top voices in [our space] posting about?"
- "What topics are trending on LinkedIn in [industry]?"
- "I want to know what content is resonating before I write anything"
- "Track [list of founders/experts] and tell me what they're saying"
- "Find trending narratives I can contribute to"


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Phase 0: Intake

### KOL List
1. Names and LinkedIn URLs of KOLs to track (if known)
   - If unknown: use `kol-discovery` skill first to build the list
2. Twitter/X handles for the same KOLs (optional but recommended for full picture)
3. Any specific topics/keywords you care about? (for filtering noisy feeds)

### Scope
4. How far back? (default: 7 days for weekly monitor, 30 days for first run)
5. Minimum engagement threshold to include a post? (default: 20 reactions/likes)

Save config to the current working directory as `kol-monitor.json` (or user-specified path).

```json
{
  "kols": [
    {
      "name": "Lenny Rachitsky",
      "linkedin": "https://www.linkedin.com/in/lennyrachitsky/",
      "twitter": "@lennysan"
    },
    {
      "name": "Kyle Poyar",
      "linkedin": "https://www.linkedin.com/in/kylepoyar/",
      "twitter": "@kylepoyar"
    }
  ],
  "days_back": 7,
  "min_reactions": 20,
  "keywords": ["GTM", "growth", "AI", "outbound", "founder"],
  "output_path": "kol-monitor-[DATE].md"
}
```

## Phase 1: Scrape LinkedIn Posts

Run `linkedin-profile-post-scraper` for all KOL LinkedIn profiles:

```bash
python3 skills/linkedin-profile-post-scraper/scripts/scrape_linkedin_posts.py \
  --profiles "<url1>,<url2>,<url3>" \
  --days <days_back> \
  --max-posts 20 \
  --output json
```

Filter results: only include posts with reactions ≥ `min_reactions`.

## Phase 2: Scrape Twitter/X Posts

Run `twitter-mention-tracker` for each handle:

```bash
python3 skills/twitter-mention-tracker/scripts/search_twitter.py \
  --query "from:<handle>" \
  --since <YYYY-MM-DD> \
  --until <YYYY-MM-DD> \
  --max-tweets 20 \
  --output json
```

Filter: only include tweets with likes ≥ `min_reactions / 2` (Twitter engagement is lower than LinkedIn).

## Phase 3: Topic Clustering

Group all posts across all KOLs by topic/theme:

### Clustering approach:
1. Extract the main topic from each post (1-3 word label)
2. Group similar topics together
3. Count: how many KOLs touched this topic? How many total posts?
4. Rank by: total engagement (sum of reactions/likes across all posts on that topic)

This surfaces topics with **broad consensus** (multiple KOLs talking about it) vs. individual takes.

### Signal types to flag:

| Signal | Meaning | Example |
|--------|---------|---------|
| **Convergence** | 3+ KOLs on same topic in same week | Multiple founders posting about "AI SDR fatigue" |
| **Spike** | Topic that 2x'd in volume vs last week | Suddenly everyone's talking about [new thing] |
| **Underdog** | 1 KOL posting about topic nobody else covers | Potential early-mover opportunity |
| **Controversy** | Posts with high comment/reaction ratio | Debate you could weigh in on |

## Phase 4: Output Format

```markdown
# KOL Content Monitor — Week of [DATE]

## Tracked KOLs
[N] KOLs | [N] LinkedIn posts | [N] tweets | Period: [date range]

---

## Trending Topics This Week

### 1. [Topic Name] — CONVERGENCE SIGNAL
- **KOLs discussing:** [Name 1], [Name 2], [Name 3]
- **Total posts:** [N] | **Total engagement:** [N] reactions/likes
- **Trend direction:** ↑ New this week / ↑↑ Growing / → Stable

**Best posts on this topic:**

> "[Post excerpt — first 150 chars]"
— [Author], [Date] | [N] reactions
[LinkedIn URL]

> "[Tweet text]"
— [@handle], [Date] | [N] likes
[Twitter URL]

**Content opportunity:** [1-2 sentences on how to contribute to this conversation]

---

### 2. [Topic Name]
...

---

## High-Engagement Posts (Top 5 This Week)

| Post | Author | Platform | Engagement | Topic |
|------|--------|----------|------------|-------|
| "[Preview...]" | [Name] | LinkedIn | [N] reactions | [topic] |
...

---

## Emerging Topics to Watch

Topics picked up by 1 KOL this week — too early to call a trend but worth tracking:
- [Topic] — [KOL name] — [brief description]
- [Topic] — ...

---

## Recommended Content Actions

### This Week (Ride the Wave)
1. **[Topic]** is peaking — ideal moment to publish your take. Suggested angle: [angle]
2. **[Controversy]** is generating debate — consider a nuanced response post. Your positioning: [suggestion]

### Next Week (Get Ahead)
1. **[Emerging topic]** is early-stage — write something now before it gets crowded.
```

Save to the current working directory as `kol-monitor-[YYYY-MM-DD].md` (or user-specified path).

## Phase 5: Build Trigger-Based Content Calendar

Optional: from the monitor output, propose a content calendar entry for each "Ride the Wave" opportunity:

```
Topic: [topic]
Best post format: [LinkedIn insight post / tweet thread / blog]
Suggested hook: [hook]
Supporting points: [3 bullets from your product/experience]
Ideal publish date: [within 3 days of peak]
```

## Scheduling

Run weekly (Friday afternoon — catches the week's peaks and gives weekend to draft):

```bash
0 14 * * 5 python3 run_skill.py kol-content-monitor --client <client-name>
```

## Cost

| Component | Cost |
|-----------|------|
| LinkedIn post scraping (per profile) | ~$0.05-0.20 (Apify) |
| Twitter scraping (per run) | ~$0.01-0.05 |
| **Total per weekly run (10 KOLs)** | **~$0.50-2.00** |

## Tools Required

- **Apify API token** — `APIFY_API_TOKEN` env var
- **Upstream skills:** `linkedin-profile-post-scraper`, `twitter-mention-tracker`
- **Optional upstream:** `kol-discovery` (to build initial KOL list)

## Trigger Phrases

- "What are the top voices in [space] posting about this week?"
- "Track my KOL list and give me content ideas"
- "Run KOL content monitor for [client]"
- "What's trending on LinkedIn in [industry]?"

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
| **Key findings** | `[OPERACIONAL]: kol-content-monitor — [finding]` | `[OPERACIONAL]: kol-content-monitor — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: kol-content-monitor — [param] works better as [value]` | `[OPERACIONAL]: kol-content-monitor — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: kol-content-monitor — [insight]` | `[ESTRATÉGICO]: kol-content-monitor — Competitor X has no case studies page, vulnerability for battlecard` |

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

