---
name: content-asset-creator
description: >
  Creates beautiful, branded HTML content assets — industry reports, landing pages,
  comparison sheets, one-pagers — from structured data. Uses Gamma API (preferred),
  v0.dev Platform API, or a self-hosted HTML template system with Tailwind CSS.
  Outputs self-contained HTML files that can be hosted as web pages or converted to PDF.
tags: [content, brand, design]
---

# Content Asset Creator

**Core principle:** Atenção não se aluga com volume, se conquista com densidade.


Generates beautiful, branded content assets (reports, landing pages, one-pagers) from structured data. Designed for producing lead magnets, industry reports, and marketing collateral programmatically.

## Quick Start

```
Create a 2-page industry report for Juicebox about "The State of AI Recruiting in 2026".
Use these data points: [list stats]. Brand: Juicebox blue, clean modern design.
```


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Audiência** — Para quem estamos escrevendo/criando?
2. **Tom de Voz** — Qual a diretriz de marca a ser usada?
3. **Canal** — Onde isso será publicado?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## Inputs

- **Asset type** (required) — `report`, `landing-page`, `comparison`, `one-pager`
- **Content data** (required) — structured data for the asset (title, sections, stats, narrative)
- **Brand config** (optional) — colors, fonts, logo URL. Defaults to Juicebox brand.
- **Output** — HTML file path (default: `output/[asset-type]-[date].html`)

## Asset Types

### 1. Industry Report (2-3 pages)

A data-forward document with stats, narrative sections, and visualizations.

**Input structure:**
```yaml
type: report
title: "The State of AI Recruiting — 2026"
subtitle: "Data-driven insights on how AI is transforming talent acquisition"
brand:
  name: "Juicebox"
  primary_color: "#4F46E5"  # Indigo/blue
  secondary_color: "#10B981"  # Green accent
  font: "Inter"
  logo_url: "https://juicebox.ai/logo.svg"
sections:
  - type: hero-stat
    stat: "93%"
    label: "of recruiters plan to increase AI use in 2026"
    source: "LinkedIn Talent Solutions"
  - type: narrative
    title: "The AI Recruiting Revolution"
    body: "AI adoption in recruiting jumped from 26% to 43% in just two years..."
  - type: stat-grid
    stats:
      - { value: "800M+", label: "Profiles searchable by AI" }
      - { value: "47%", label: "Reduction in time-to-fill" }
      - { value: "10x", label: "Cheaper than LinkedIn Recruiter" }
  - type: comparison-table
    headers: ["Feature", "Traditional", "AI-Powered"]
    rows:
      - ["Search method", "Boolean keywords", "Natural language"]
      - ["Data sources", "1 (LinkedIn)", "60+ sources"]
  - type: cta
    headline: "See AI recruiting in action"
    body: "Try PeopleGPT free — search 800M+ profiles in natural language"
    button_text: "Get Started Free"
    button_url: "https://juicebox.ai"
footer:
  text: "© 2026 Juicebox. Data sources cited throughout."
```

### 2. Landing Page (single page with CTA)

A single-page marketing asset with a headline, value props, and email capture.

### 3. Comparison Page (side-by-side)

A visual comparison of two products (e.g., Juicebox vs LinkedIn Recruiter).

### 4. One-Pager (quick reference)

A dense, single-page reference sheet (e.g., "PeopleGPT Prompt Library").

## Step-by-Step Process

### Step 1: Choose Generation Method

Check which tools are available (in priority order):

1. **Gamma API** (preferred) — If `GAMMA_API_KEY` is set, use Gamma Generate API v1.0 (GA since Nov 2025). Requires Pro account ($16/mo). Can create presentations, documents, and web pages programmatically. Supports 60+ languages, up to 100K token input. Rate limit: hundreds per hour.
2. **v0.dev Platform API** — If `V0_API_KEY` is set, use Vercel's v0 Platform API (beta). Requires Premium ($20/mo) or Team plan. Generates React + Tailwind code from prompts. Best for landing pages and interactive web content.
3. **Self-hosted HTML** — Fallback: generate HTML directly using Tailwind CSS templates. No external dependency. Full control over output.

### Step 2A: Gamma API Generation (Preferred)

Gamma's Generate API v1.0 creates presentations, documents, and web pages from text prompts.

**API docs:** https://developers.gamma.app/docs/getting-started

```bash
curl -X POST https://api.gamma.app/v1/generate \
  -H "Authorization: Bearer $GAMMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "<structured content prompt>",
    "format": "document",
    "theme": "<optional theme ID>"
  }'
```

**Tips for Gamma:**
- List your available themes first: `GET /v1/themes`
- Can share via email programmatically
- Supports creating from templates: use `POST /v1/generate-from-template`
- Output can be viewed as a hosted Gamma page or exported

### Step 2B: v0.dev Platform API Generation

v0's Platform API generates React + Tailwind code from natural language prompts.

**API docs:** https://v0.app/docs/api/platform/overview

The workflow: prompt → project → code files → deployment. Output is deployable to Vercel instantly.

```bash
# Create a project with a prompt
curl -X POST https://api.v0.dev/v1/projects \
  -H "Authorization: Bearer $V0_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a professional industry report page with..."
  }'
```

**Tips for v0:**
- Best for interactive web pages and landing pages
- Output is React/Next.js + Tailwind — can be deployed or converted to static HTML
- Usage-based billing on top of subscription

### Step 2C: Self-Hosted HTML Generation (Fallback)

Generate a self-contained HTML file:

1. **Load the template** for the asset type
2. **Inject content** from the structured data
3. **Apply brand styles** (colors, fonts, logo)
4. **Generate data visualizations** using inline SVG or CSS
5. **Output** as a single HTML file with all styles inlined

**HTML Template Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: '{{ primary_color }}',
            accent: '{{ secondary_color }}'
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif']
          }
        }
      }
    }
  </script>
  <style>
    /* Print styles for PDF conversion */
    @media print {
      .page-break { page-break-before: always; }
      body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    }
  </style>
</head>
<body class="font-sans bg-white text-gray-900">
  <!-- Content sections generated here -->
</body>
</html>
```

**Section Templates:**

- `hero-stat`: Large stat number with label and source
- `narrative`: Title + body text in clean typography
- `stat-grid`: 3-4 stats in a responsive grid
- `comparison-table`: Side-by-side table with highlighting
- `chart`: Simple bar/donut chart using CSS or inline SVG
- `cta`: Call-to-action block with button
- `footer`: Branded footer with disclaimers

### Step 3: Output

Save the HTML file:
```
clients/<client>/strategies/<strategy>/content/[asset-name].html
```

Optionally convert to PDF:
```bash
# Using playwright/puppeteer (if installed)
npx playwright screenshot output.html output.pdf --format=pdf
```

Or provide instructions for manual PDF conversion (print to PDF from browser).

## Brand Configurations

### Juicebox Brand
```json
{
  "name": "Juicebox",
  "primary_color": "#4F46E5",
  "secondary_color": "#10B981",
  "accent_color": "#F59E0B",
  "background": "#FFFFFF",
  "text_color": "#111827",
  "font_heading": "Inter",
  "font_body": "Inter",
  "logo_url": "https://juicebox.ai/logo.svg"
}
```

Save brand configs at: `skills/content-asset-creator/brands/[client].json`

## Tips

- Keep reports to 2-3 pages max. Busy recruiters won't read more.
- Lead with the biggest, most surprising stat. Make it impossible to scroll past.
- Every section should have exactly ONE key takeaway. Don't dilute with multiple messages.
- The CTA should feel natural, not bolted on. The data should lead to the conclusion that the reader needs your product.
- For PDF distribution: test that the HTML prints well before sending. Use `@media print` styles.
- For web distribution: add Open Graph meta tags so it looks good when shared on LinkedIn/Twitter.

## Dependencies

- Tailwind CSS (via CDN — no build step)
- Google Fonts (via CDN)
- Optional: Gamma API key (`GAMMA_API_KEY`) — Requires Gamma Pro account ($16/mo). API v1.0 GA. Docs: https://developers.gamma.app
- Optional: v0.dev API key (`V0_API_KEY`) — Requires v0 Premium ($20/mo). Platform API (beta). Docs: https://v0.app/docs/api/platform/overview
- Optional: Playwright/Puppeteer for PDF conversion

## Templates

Templates are stored at `skills/content-asset-creator/templates/`:
- `report.html` — Industry report template
- `landing-page.html` — Landing page with email capture
- `comparison.html` — Product comparison page
- `one-pager.html` — Quick reference sheet

Each template accepts the content data structure defined above.

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **External API unavailable** (Gamma, v0) | HTTP error or timeout | Fall back to self-hosted HTML generation. Log `ℹ️ Using HTML fallback` |
| **Font loading failed** | Timeout on font CDN | Use system font stack as fallback. Note in output |
| **Screenshot generation failed** | Playwright/browser error | Provide HTML files and manual screenshot instructions |
| **Content exceeds format limits** | Text overflow or slide count exceeded | Split into multiple units. Warn user about content volume |
| **Brand config missing** | No brand JSON found | Use neutral default palette. Ask user for brand details |

**Principle:** Always produce a deliverable, even if lower fidelity than ideal.


## Composability

**Receives data from:**
- Skills tagged `brand` (e.g., data collection and enrichment)
- Skills tagged `competitive-intel` (e.g., data collection and enrichment)
- Skills tagged `research` (e.g., data collection and enrichment)

**Feeds into:**
- `create-html-carousel`
- `create-html-slides`
- `linkedin-outreach`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: content-asset-creator — [finding]` | `[OPERACIONAL]: content-asset-creator — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: content-asset-creator — [param] works better as [value]` | `[OPERACIONAL]: content-asset-creator — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: content-asset-creator — [insight]` | `[ESTRATÉGICO]: content-asset-creator — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Brand consistency:** Colors, fonts, and tone match the brand config (or defaults)
- [ ] **Format compliance:** Output meets platform specs (e.g., 1080×1080 for LinkedIn carousel)
- [ ] **Content density:** No slide/section exceeds readability limits
- [ ] **Link integrity:** All URLs in the output are valid and accessible
- [ ] **User checkpoint:** Present preview to user for approval before final export

**If any check fails:** Generate a corrected version and present both options to the user.

