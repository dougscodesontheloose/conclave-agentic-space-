---
name: reddit-post-finder
description: Scrape and search Reddit posts using Apify. Use when you need to find Reddit discussions, track competitor mentions, monitor product feedback, discover pain points, or analyze subreddit content. Supports keyword filtering, time-based searches, and subreddit-specific queries.
tags: [scraping, monitoring, research]
---

# Reddit Post Finder

**Core principle:** Dados brutos são passivos; inteligência é o que você recorta do ruído.


Scrape Reddit posts and comments using the Apify `trudax/reddit-scraper-lite` actor.

## Quick Start

Requires `APIFY_API_TOKEN` env var (or `--token` flag).

```bash
# Top posts from r/growthhacking in last week
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit growthhacking --days 7 --sort top --time week

# Hot posts from multiple subreddits
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit "growthhacking,gtmengineering" --days 7 --sort hot

# Keyword-filtered competitor tracking
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit LLMDevs \
  --keywords "Langfuse,Arize,Langsmith" \
  --days 30

# Human-readable summary table
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit growthhacking --days 7 --output summary
```

## How the Script Works

1. Builds full Reddit URLs for each subreddit (e.g. `https://www.reddit.com/r/growthhacking/top/?t=week`)
2. Calls the Apify `trudax/reddit-scraper-lite` actor via REST API
3. Polls until the run completes, then fetches the dataset
4. Applies client-side keyword and date filtering
5. Sorts by upvotes (descending) and outputs JSON or summary

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--subreddit` | *required* | Subreddit name(s), comma-separated |
| `--keywords` | none | Keywords to filter (comma-separated, OR logic) |
| `--days` | 30 | Only include posts from the last N days |
| `--max-posts` | 50 | Max posts to scrape per subreddit |
| `--sort` | top | Sort: `hot`, `top`, `new`, `rising` |
| `--time` | week | Time window for `top` sort: `hour`, `day`, `week`, `month`, `year`, `all` |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (prefer `APIFY_API_TOKEN` env var) |
| `--timeout` | 300 | Max seconds to wait for the Apify run |

## Tips for Small Subreddits

Small or low-traffic subreddits (e.g. `r/gtmengineering`) may return zero posts with `--sort hot` because the hot feed is nearly empty. Use `--sort top --time week` (or `month`) instead — this scrapes the top-ranked posts over the time window and reliably returns results.

## Direct API Usage

If calling the Apify API directly (e.g. via curl), note these **required fields**:

```json
{
  "startUrls": [{"url": "https://www.reddit.com/r/growthhacking/top/?t=week"}],
  "maxItems": 50
}
```

Key notes for `trudax/reddit-scraper-lite`:
- Uses `startUrls` with **full Reddit URLs** (not a `searches` array for subreddit browsing)
- Sort/time are controlled via the **URL path** (e.g. `/top/?t=week`), not separate input fields
- Only `startUrls` and `maxItems` are confirmed working input fields
- Does **not** support `proxyConfiguration`, `scrollTimeout`, or `searchType`

**Output fields:**
- `dataType` — `"post"` or `"comment"`
- `title` — Post title
- `body` — Post body text
- `communityName` — Subreddit name (without `r/` prefix)
- `upVotes` — Number of upvotes
- `numberOfComments` — Comment count
- `url` — Full URL to the post
- `createdAt` — ISO timestamp of when the post was created

## Common Workflows

### 1. Competitor Tracking

```bash
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit "LLMDevs,MachineLearning,LocalLLaMA" \
  --keywords "Langfuse,Arize,Weights & Biases,Langsmith,Braintrust" \
  --days 30 --sort top --time month
```

### 2. Pain Point Discovery

```bash
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit LLMDevs \
  --keywords "frustrating,difficult,hard to,wish there was,better way" \
  --days 30
```

### 3. Brand Monitoring

```bash
python3 skills/reddit-post-finder/scripts/search_reddit.py \
  --subreddit "LLMDevs,MachineLearning" \
  --keywords "YourProductName" \
  --days 7 --sort new
```

## Important: Always Include Post URLs

When presenting Reddit results to the user, **always include the original post URL** for every post. This is critical for allowing users to read the full discussion, comments, and context. Never return a summary table without links.

## Output Format

Posts are returned as JSON array sorted by upvotes. Each post has:

```json
{
  "dataType": "post",
  "title": "Post title",
  "body": "Post body...",
  "communityName": "growthhacking",
  "upVotes": 42,
  "numberOfComments": 15,
  "createdAt": "2026-02-18T12:00:00.000Z",
  "url": "https://reddit.com/r/..."
}
```

## Configuration

See `references/apify-config.md` for detailed API configuration, token setup, and rate limits.

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
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `cold-email-outreach`
- `competitor-intel`
- `content-asset-creator`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`
- `linkedin-outreach`
- `signal-detection-pipeline`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: reddit-post-finder — [finding]` | `[OPERACIONAL]: reddit-post-finder — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: reddit-post-finder — [param] works better as [value]` | `[OPERACIONAL]: reddit-post-finder — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: reddit-post-finder — [insight]` | `[ESTRATÉGICO]: reddit-post-finder — Competitor X has no case studies page, vulnerability for battlecard` |

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

Requer ambiente de execução padrão do Conclave.
