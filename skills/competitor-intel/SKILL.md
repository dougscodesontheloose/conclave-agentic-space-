---
name: competitor-intel
description: >
  Structured competitive research framework. Given a competitor name or URL,
  produces a complete competitive profile: positioning, messaging, product,
  pricing, content strategy, and key differentiators vs. your company.
description_pt-BR: >
  Framework de pesquisa competitiva estruturada. Dado um concorrente (nome ou URL),
  produz um perfil competitivo completo: posicionamento, mensagens, produto,
  preço, estratégia de conteúdo e diferenciais.
type: hybrid
version: "1.0.0"
categories: [competitive-intelligence, research, analysis]
---

# Competitor Intel

## When to Use

Use this skill when an agent needs a structured competitive analysis of a specific company.
Input: company name or URL. Output: `output/competitor-{slug}.md`.

---

## Process

1. **Identify entry points** — If given a name, search for official website, LinkedIn page, and main product page.
2. **Positioning & Messaging** — Fetch the homepage and key landing pages. Extract:
   - Primary value proposition (headline)
   - Target audience signals (who they write for)
   - Tone of voice (formal / casual / technical / aspirational)
   - Key claims and proof points
3. **Product & Pricing** — Fetch pricing page or search for pricing data. Extract:
   - Product tiers and names
   - Price points (if public)
   - Feature emphasis per tier
4. **Content Strategy** — Search for recent blog posts, social media activity (LinkedIn, Twitter/X). Extract:
   - Top content themes (last 90 days)
   - Publishing frequency and formats
   - Engagement patterns (if visible)
5. **Reputation Signals** — Search for reviews (G2, Capterra, Reddit, HN). Extract:
   - Top praised features
   - Top complaints
   - Common objections
6. **Synthesis** — Compile all findings into the Output Format below.

---

## Output Format

```markdown
# Competitor Profile: {Company Name}
**Analyzed:** {YYYY-MM-DD}
**URL:** {primary URL}

## Positioning
- **Tagline:** {headline text}
- **Target audience:** {who they write for}
- **Tone:** {formal | casual | technical | aspirational}
- **Core claim:** {1-sentence value prop}

## Product & Pricing
| Tier | Price | Key Features |
|------|-------|-------------|
| {tier} | {price} | {features} |

## Content Strategy
- **Primary themes:** {list}
- **Formats used:** {blog / video / carousel / thread}
- **Posting frequency:** {estimate}

## Reputation
- **Praised for:** {list from reviews}
- **Criticised for:** {list from reviews}
- **Common objections:** {list}

## vs. {Your Company}
| Dimension | {Competitor} | {Your Company} |
|-----------|-------------|----------------|
| Positioning | | |
| Price | | |
| Strengths | | |
| Weaknesses | | |

## Key Takeaways
1. {Insight 1}
2. {Insight 2}
3. {Insight 3}
```

---

## Output Instructions

Write to `squads/{code}/output/competitor-{slug}.md`.

Report:
```
Competitor Intel — output:
— Empresa: {name}
— Seções: Positioning, Product, Content, Reputation, Comparison
— Arquivo: output/competitor-{slug}.md
— Fontes consultadas: {N}
```
