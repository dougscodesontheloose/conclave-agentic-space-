---
name: firecrawl
description: >
  Web scraping fallback for research agents. Handles JavaScript-rendered pages,
  anti-bot sites, and any URL where native web_fetch returns empty or insufficient
  content. Always try web_fetch FIRST — invoke Firecrawl only on confirmed failure.
description_pt-BR: >
  Fallback de scraping para agentes de pesquisa. Lida com páginas JS-renderizadas,
  sites com anti-bot e qualquer URL onde web_fetch retorna vazio ou insuficiente.
  SEMPRE tente web_fetch primeiro — invoque Firecrawl apenas em falha confirmada.
type: mcp
version: "1.0.0"
mcp:
  server_name: firecrawl
  command: npx
  args: ["-y", "firecrawl-mcp"]
  env_key: FIRECRAWL_API_KEY
categories: [research, scraping, web, fallback]
---

# Firecrawl — Web Scraping Fallback

## The Fallback Rule (MANDATORY — never skip)

```
IF web_fetch(url) returns content >= 500 characters
  → Use that content. Do NOT call Firecrawl.

IF web_fetch(url) returns < 500 characters OR empty OR error
  → Call Firecrawl scrape on the same URL.
  → Log: "web_fetch insuficiente para {url} — usando Firecrawl"
```

This rule exists to preserve credits. 500 free credits is the entire free tier.
Each unnecessary scrape is a permanent credit burn.

---

## When to Use

Use this skill when research agents encounter:
- Blank or near-empty web_fetch results (< 500 chars)
- JavaScript-heavy sites (React, Next.js, Vue SPAs)
- Sites with Cloudflare or other anti-bot protection
- Pages that require scrolling or dynamic loading to show content

Do NOT use for:
- Simple static pages (Wikipedia, GitHub README, plain HTML blogs)
- Any URL where web_fetch already returned rich content

---

## Available MCP Tools

After MCP initialization, these tools are available:

### `firecrawl_scrape`
Extracts clean markdown from a single URL. Best for: known URLs where web_fetch failed.

**Parameters:**
- `url` (required) — the URL to scrape
- `formats` (optional) — `["markdown"]` (default) or `["html", "screenshot"]`

**Credit cost:** 1 per call

### `firecrawl_search`
Searches the web AND returns full page content — not just links.
Use instead of web_search when you need the page body, not just titles/snippets.

**Parameters:**
- `query` (required) — search query string
- `limit` (optional) — number of results (default 5)

**Credit cost:** 2 per 10 results

### `firecrawl_crawl`
Crawls a URL and all accessible subpages. Use sparingly — burns credits fast.

**Credit cost:** 1 per page crawled

### `firecrawl_map`
Discovers all URLs on a website without fetching their content.
Use for: finding the right subpage before scraping.

**Credit cost:** 1 per call

---

## Fallback Implementation Pattern

```
# Step 1 — always try native first
content = web_fetch(url)

# Step 2 — evaluate
if len(content.strip()) >= 500:
    use content  # native worked, no credits spent
else:
    # Step 3 — fallback to Firecrawl
    result = firecrawl_scrape(url=url, formats=["markdown"])
    content = result.markdown
    log("Firecrawl fallback used for: {url}")
    use content
```

---

## Credit Budget Awareness

| Plan | Credits | Scrapes equivalent |
|---|---|---|
| Free (one-time) | 500 | ~500 pages |
| Hobby ($19/mo) | 3,000 | ~3,000 pages |

**Design Phase B typically uses:** 5–15 Firecrawl calls per squad (only on failures).
At that rate, the free tier covers 33–100 complete squad creation flows before needing paid.

---

## Output Instructions

When Firecrawl is used as fallback, always include in the research summary:
```
Fontes via Firecrawl fallback: {N} URLs (web_fetch insuficiente)
Fontes via web_fetch nativo: {M} URLs
```
