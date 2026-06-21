---
name: tiktok-influencer-finder
description: Find TikTok influencers using Apify's Influencer Discovery Agent. Use when the user wants to discover TikTok creators or influencers in any niche.
argument-hint: [niche/description]
disable-model-invocation: true
tags: [scraping, lead-generation, social-media]
---

# TikTok Influencer Finder

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Search for TikTok influencers matching a specific niche using Apify's Influencer Discovery Agent.

## Step 1: Gather Criteria

Before running the search, ask the user for their filtering criteria using AskUserQuestion. Collect ALL of the following:

1. **Niche/Description**: What type of influencer? (use $ARGUMENTS if provided, otherwise ask)
2. **Minimum follower count**: e.g. 5K, 10K, 50K
3. **Maximum follower count**: e.g. 50K, 100K, 500K
4. **Location filter**: e.g. US only, US + Canada, any English-speaking country
5. **Sub-niche preferences**: Any specific content focus within the broader niche

Ask all 5 criteria in a single AskUserQuestion call to minimize back-and-forth. Provide sensible default options but always allow custom input.

## Step 2: Run the Apify Influencer Discovery Agent

Use the `mcp__apify__apify-slash-influencer-discovery-agent` tool with:

- **influencerDescription**: Compose a detailed description combining the user's niche, content style preferences, and target audience. Be specific and descriptive.
- **generatedKeywords**: 5 (maximum for best coverage)
- **profilesPerKeyword**: 10 (maximum for best coverage)

If the MCP connection fails, instruct the user to run `/mcp` to reconnect, then retry.

## Step 3: Filter Results

After receiving results, apply ALL the user's criteria strictly:

- **Remove** profiles below minimum follower count
- **Remove** profiles above maximum follower count
- **Remove** profiles outside the specified location(s)
- **Remove** profiles that don't match the sub-niche (use the `fit` score and `fitDescription` to judge relevance; generally exclude fit < 0.6)
- **Sort** remaining results by fit score (descending), then by follower count (descending)

## Step 4: Present Results

Present filtered results in a clean markdown table with these columns:

| Creator | Handle | Followers | Engagement | Location | Focus | Fit Score |

Include:
- Clickable TikTok profile links
- Follower count formatted readably (e.g. 46.3K)
- Engagement rate as percentage
- Brief description of their content focus
- The AI-generated fit score

After the table, include:
- **Total profiles analyzed** vs **profiles matching criteria**
- A note if very few results matched (suggest adjusting criteria)
- Offer to run another search with different keywords or adjusted criteria

## Notes

- This skill requires the Apify MCP server to be connected. If not connected, tell the user to run `/mcp` first.
- The tool searches TikTok specifically. If the user wants other platforms, let them know this is TikTok-only and suggest alternatives.
- Engagement rates above 100% can occur when viral posts drive disproportionate interaction relative to follower count.


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Alvo** — Qual a URL ou fonte específica?
2. **Foco** — Que tipo de dados são mais críticos?
3. **Formato** — JSON, CSV ou Markdown?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use `tiktok-influencer-finder` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Keywords/Query** | Varies | Search terms or filters |
| **API credentials** | Yes | API key (set via environment variable) |
| **Output format** | No | `json` (default) or `csv` |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Raw data** | JSON or CSV | Current working directory or specified path |
| **Summary** | Markdown table | Displayed to user in terminal |
| **Error log** | Inline notes | Included in output when sources fail |


## Cost

Free. Uses public APIs that do not require paid credentials.

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **API rate limit / 429** | HTTP 429 or `rate_limit` in response | Wait 60s, retry with exponential backoff (max 3 retries) |
| **API key missing/invalid** | HTTP 401/403 or env var not set | Log `❌ Missing API key: [VAR_NAME]`. Stop and inform user with setup instructions |
| **Target page structure changed** | Zero results from a previously working source | Log `⚠️ 0 results from [source]`. Continue with other sources, flag in output |
| **Network timeout** | No response within configured timeout | Retry once. If still failing, skip source and note in output |
| **Empty dataset returned** | Valid API response but 0 results | Distinguish "no data exists" vs "query too narrow". Suggest query adjustments |

**Principle:** Never fail silently. Every error must produce a visible log line and a note in the final output.


## Composability

**Receives data from:**
- Skills tagged `research` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)
- Skills tagged `signals` (e.g., data collection and enrichment)

**Feeds into:**
- `cold-email-outreach`
- `competitor-intel`
- `contact-cache`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`
- `linkedin-message-writer`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: tiktok-influencer-finder — [finding]` | `[OPERACIONAL]: tiktok-influencer-finder — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: tiktok-influencer-finder — [param] works better as [value]` | `[OPERACIONAL]: tiktok-influencer-finder — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: tiktok-influencer-finder — [insight]` | `[ESTRATÉGICO]: tiktok-influencer-finder — Competitor X has no case studies page, vulnerability for battlecard` |

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

