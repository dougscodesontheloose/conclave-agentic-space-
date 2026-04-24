---
name: landing-page-intel
description: >
  Analyzes any landing page URL for positioning, copy structure, conversion strategy,
  and persuasion patterns. Outputs an intel report agents can use for competitive
  benchmarking or improving their own landing page copy.
description_pt-BR: >
  Analisa qualquer URL de landing page: posicionamento, estrutura de copy, estratégia
  de conversão e padrões de persuasão. Útil para benchmarking competitivo e melhoria
  de copy própria.
type: hybrid
version: "1.0.0"
categories: [competitive-intelligence, landing-pages, copy-analysis, conversion]
---

# Landing Page Intel

## When to Use

Use when an agent needs to understand how a competitor (or reference brand) structures
its landing page for conversion. Input: one URL. Output: `output/lp-intel-{slug}.md`.

---

## Process

1. **Fetch the page** — Use `web_fetch` on the provided URL. Capture full text content.
2. **Structure map** — Identify the page sections in order (Hero, Problem, Solution, Social Proof, Pricing, CTA, FAQ, etc.).
3. **Copy analysis** — For each section extract:
   - Headline / subheadline text
   - Key claims and proof points
   - Emotional triggers used (fear, aspiration, urgency, curiosity, social proof)
4. **CTA analysis** — Count CTAs, note their text, placement, and style (soft / direct / scarcity-based).
5. **Social proof inventory** — Logos, testimonials, numbers, certifications present.
6. **Conversion strategy classification** — Classify the overall conversion approach:
   - Direct response (buy now / sign up now)
   - Lead nurture (demo / free trial / newsletter)
   - Trust-build (case studies / long-form proof)
7. **Strengths & weaknesses** — What this page does well and what it misses.

---

## Output Format

```markdown
# Landing Page Intel: {Brand/Page Name}
**URL:** {url}
**Analyzed:** {YYYY-MM-DD}

## Page Structure
1. {Section}: {what it does}
2. ...

## Copy Breakdown
### Hero
- **Headline:** "{text}"
- **Subheadline:** "{text}"
- **Emotional trigger:** {trigger type}
- **Promise:** {what they claim}

### Key Claims
| Claim | Proof Offered | Believability |
|-------|-------------|---------------|
| {claim} | {proof type} | {strong/weak/absent} |

## CTA Analysis
| CTA Text | Position | Style |
|----------|----------|-------|
| {text} | {above fold / mid / footer} | {direct/soft/scarcity} |

## Social Proof
- Logos: {Y/N — count}
- Testimonials: {Y/N — count}
- Numbers/stats: {list}
- Certifications: {list}

## Conversion Strategy
**Type:** {direct response / lead nurture / trust-build}
**Primary emotion targeted:** {aspiration / fear / curiosity / urgency / belonging}

## Strengths
- {what works well}

## Weaknesses / Gaps
- {what's missing or weak}
```

---

## Output Instructions

Write to `squads/{code}/output/lp-intel-{slug}.md`.

Report:
```
Landing Page Intel — output:
— URL analisada: {url}
— Seções mapeadas: {N}
— CTAs encontrados: {N}
— Estratégia: {conversion strategy type}
— Arquivo: output/lp-intel-{slug}.md
```
