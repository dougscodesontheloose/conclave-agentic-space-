---
name: blog-feed-monitor
description: >
  Scrape blog posts via RSS feeds (free, no API key) with Apify fallback for
  JS-heavy sites. Também suporta tracking persistente via blogwatcher-cli com
  read/unread management e OPML import. Use para monitorar blogs de competidores,
  rastrear conteúdo de indústria, ou agregar posts por keyword.
tags: [monitoring, scraping, content]
---

# Blog Feed Monitor

**Core principle:** Sinais só têm valor se a janela de oportunidade ainda estiver aberta.


Scrape blog posts via RSS/Atom feeds (free) with optional Apify fallback for JS-heavy sites.

## Alternative Tool: blogwatcher-cli

Para **monitoramento persistente** (tracking contínuo com estado read/unread), use `blogwatcher-cli`:

```bash
# Instalar (macOS Apple Silicon)
curl -sL https://github.com/JulienTant/blogwatcher-cli/releases/latest/download/blogwatcher-cli_darwin_arm64.tar.gz | tar xz -C /usr/local/bin blogwatcher-cli

# Gerenciar blogs
blogwatcher-cli add "Company Blog" https://example.com
blogwatcher-cli add "Tech Blog" https://example.com --feed-url https://example.com/feed.xml
blogwatcher-cli add "JS Site" https://example.com --scrape-selector "article h2 a"
blogwatcher-cli blogs                    # Listar blogs rastreados
blogwatcher-cli remove "Blog Name" --yes # Remover

# Importar de Feedly/Inoreader
blogwatcher-cli import subscriptions.opml

# Scan e leitura
blogwatcher-cli scan                     # Scan de todos
blogwatcher-cli scan "Company Blog"      # Scan de um
blogwatcher-cli articles                 # Artigos não lidos
blogwatcher-cli articles --all           # Todos
blogwatcher-cli articles --blog "X"      # Filtrar por blog
blogwatcher-cli articles --category "Y"  # Filtrar por categoria
blogwatcher-cli read 1                   # Marcar como lido
blogwatcher-cli read-all                 # Marcar todos como lidos
```

**Quando usar qual:**
- **Script Python (default):** One-shot scraping, keyword filtering, pipeline de dados
- **blogwatcher-cli:** Monitoramento contínuo, estado persistente, read/unread tracking

## Quick Start

No API key needed for RSS mode.

```bash
# Scrape a blog's RSS feed
python3 skills/blog-feed-monitor/scripts/scrape_blogs.py \
  --urls "https://example.com/blog" --days 30

# Multiple blogs with keyword filter
python3 skills/blog-feed-monitor/scripts/scrape_blogs.py \
  --urls "https://blog1.com,https://blog2.com" --keywords "AI,marketing" --output summary

# Force Apify for JS-heavy sites
python3 skills/blog-feed-monitor/scripts/scrape_blogs.py \
  --urls "https://example.com" --mode apify
```

## How It Works

### Auto Mode (default)
1. For each URL, tries to discover an RSS/Atom feed:
   - Checks HTML `<link rel="alternate">` tags
   - Probes common paths: `/feed`, `/rss`, `/atom.xml`, `/feed.xml`, `/rss.xml`, `/blog/feed`, `/index.xml`
2. Parses discovered feeds (supports RSS 2.0 and Atom)
3. If any URLs fail, falls back to Apify `jupri/rss-xml-scraper` (if token available)
4. Applies date and keyword filtering client-side

> **Note:** The Apify fallback actor `jupri/rss-xml-scraper` may need updating -- it has not been verified recently. RSS mode works reliably without it.

### RSS Mode
Only tries RSS feeds, no Apify fallback.

### Apify Mode
Uses Apify actor directly, skipping RSS discovery.

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--urls` | *required* | Blog URL(s), comma-separated |
| `--keywords` | none | Keywords to filter (comma-separated, OR logic) |
| `--days` | 30 | Only include posts from last N days |
| `--max-posts` | 50 | Max posts to return |
| `--mode` | auto | `auto` (RSS + fallback), `rss` (RSS only), `apify` (Apify only) |
| `--output` | json | Output format: `json` or `summary` |
| `--token` | env var | Apify token (only needed for Apify mode/fallback) |
| `--timeout` | 300 | Max seconds for Apify run |

## Cost

- **RSS mode:** Free (no API, no tokens)
- **Apify mode:** Uses `jupri/rss-xml-scraper` -- minimal Apify credits


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

Use `blog-feed-monitor` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Target URL(s)** | Yes | URL(s) to scrape |
| **Keywords/Query** | Varies | Search terms or filters |
| **API credentials** | Yes | API key (set via environment variable) |
| **Output format** | No | `json` (default) or `csv` |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Raw data** | JSON or CSV | Current working directory or specified path |
| **Summary** | Markdown table | Displayed to user in terminal |
| **Error log** | Inline notes | Included in output when sources fail |

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
- Skills tagged `brand` (e.g., data collection and enrichment)
- Skills tagged `competitive-intel` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)

**Feeds into:**
- `competitor-intel`
- `create-html-carousel`
- `create-html-slides`
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
| **Key findings** | `[OPERACIONAL]: blog-feed-monitor — [finding]` | `[OPERACIONAL]: blog-feed-monitor — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: blog-feed-monitor — [param] works better as [value]` | `[OPERACIONAL]: blog-feed-monitor — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: blog-feed-monitor — [insight]` | `[ESTRATÉGICO]: blog-feed-monitor — Competitor X has no case studies page, vulnerability for battlecard` |

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

