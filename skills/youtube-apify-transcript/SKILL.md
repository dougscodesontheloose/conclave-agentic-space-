---
name: youtube-apify-transcript
description: Fetch YouTube transcripts via APIFY API. Works from cloud IPs (Hetzner, AWS, etc.) by bypassing YouTube's bot detection. Free tier includes $5/month credits (~714 videos). No credit card required.
tags: [research]
---

# youtube-apify-transcript

**Core principle:** Não procure dados que confirmem sua tese; procure assimetrias que o mercado ignora.


Fetch YouTube transcripts via APIFY API (works from cloud IPs, bypasses YouTube bot detection).

## Why APIFY?

YouTube blocks transcript requests from cloud IPs (AWS, GCP, etc.). APIFY runs the request through residential proxies, bypassing bot detection reliably.

## Free Tier

- **$5/month free credits** (~714 videos)
- No credit card required
- Perfect for personal use

## Cost

- **$0.007 per video** (less than 1 cent!)
- Track usage at: https://console.apify.com/billing

## Links

- [APIFY Pricing](https://apify.com/pricing)
- [Get API Key](https://console.apify.com/account/integrations)
- [YouTube Transcript Scraper Actor](https://apify.com/pintostudio/youtube-transcript-scraper)

## Setup

1. Create free APIFY account: https://apify.com/
2. Get your API token: https://console.apify.com/account/integrations
3. Set environment variable:

```bash
# Add to ~/.bashrc or ~/.zshrc
export APIFY_API_TOKEN="apify_api_YOUR_TOKEN_HERE"

# Or use .env file (never commit this!)
echo 'APIFY_API_TOKEN=apify_api_YOUR_TOKEN_HERE' >> .env
```

## Usage

### Basic Usage

```bash
# Get transcript as text (uses cache by default)
python3 scripts/fetch_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Short URL also works
python3 scripts/fetch_transcript.py "https://youtu.be/VIDEO_ID"
```

### Options

```bash
# Output to file
python3 scripts/fetch_transcript.py "URL" --output transcript.txt

# JSON format (includes timestamps)
python3 scripts/fetch_transcript.py "URL" --json

# Both: JSON to file
python3 scripts/fetch_transcript.py "URL" --json --output transcript.json

# Specify language preference
python3 scripts/fetch_transcript.py "URL" --lang de
```

### Caching (saves money!)

Transcripts are cached locally by default. Repeat requests for the same video cost $0.

```bash
# First request: fetches from APIFY ($0.007)
python3 scripts/fetch_transcript.py "URL"

# Second request: uses cache (FREE!)
python3 scripts/fetch_transcript.py "URL"
# Output: [cached] Transcript for: VIDEO_ID

# Bypass cache (force fresh fetch)
python3 scripts/fetch_transcript.py "URL" --no-cache

# View cache stats
python3 scripts/fetch_transcript.py --cache-stats

# Clear all cached transcripts
python3 scripts/fetch_transcript.py --clear-cache
```

Cache location: `.cache/` in skill directory (override with `YT_TRANSCRIPT_CACHE_DIR` env var)

### Batch Mode

Process multiple videos at once:

```bash
# Create a file with URLs (one per line)
cat > urls.txt << EOF
https://youtube.com/watch?v=VIDEO1
https://youtu.be/VIDEO2
https://youtube.com/watch?v=VIDEO3
EOF

# Process all URLs
python3 scripts/fetch_transcript.py --batch urls.txt

# Batch with JSON output to file
python3 scripts/fetch_transcript.py --batch urls.txt --json --output all_transcripts.json
```

## APIFY Actor Input

The script sends the following input to `pintostudio/youtube-transcript-scraper`:

```json
{
  "videoUrl": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Output fields:**

Each result contains a `data` array of transcript segments:

| Field   | Type   | Description                        |
|---------|--------|------------------------------------|
| `start` | number | Segment start time (seconds)       |
| `dur`   | number | Segment duration (seconds)         |
| `text`  | string | Transcript text for this segment   |

### Output Formats

**Text (default):**
```
Hello and welcome to this video.
Today we're going to talk about...
```

**JSON (--json):**
```json
{
  "video_id": "dQw4w9WgXcQ",
  "title": "Video Title",
  "transcript": [
    {"start": 0.0, "dur": 2.5, "text": "Hello and welcome"},
    {"start": 2.5, "dur": 3.0, "text": "to this video"}
  ],
  "full_text": "Hello and welcome to this video..."
}
```

## Error Handling

The script handles common errors:
- Invalid YouTube URL
- Video has no transcript
- API quota exceeded
- Network errors

## Composability

**Receives data from:**
- Skills tagged `monitoring` (e.g., data collection and enrichment)
- Skills tagged `scraping` (e.g., data collection and enrichment)

**Feeds into:**
- `battlecard-generator`
- `cold-email-outreach`
- `content-asset-creator`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: youtube-apify-transcript — [finding]` | `[OPERACIONAL]: youtube-apify-transcript — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: youtube-apify-transcript — [param] works better as [value]` | `[OPERACIONAL]: youtube-apify-transcript — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: youtube-apify-transcript — [insight]` | `[ESTRATÉGICO]: youtube-apify-transcript — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Source diversity:** Findings are supported by at least 2 independent sources
- [ ] **Recency check:** Key data points are from the last 12 months (or explicitly flagged as older)
- [ ] **Confidence labeling:** Every finding has a confidence level (high/medium/low)
- [ ] **Actionability:** Report includes at least 1 concrete next step or recommendation
- [ ] **User checkpoint:** Present key findings summary before generating the full report

**If any check fails:** Note the gap explicitly in the output rather than omitting it.



## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Entidade alvo** — Empresa, pessoa ou tendência?
2. **Profundidade** — Visão geral (quick) ou análise profunda (deep)?
3. **Objetivo** — O que esta pesquisa deve destravar no seu projeto?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
