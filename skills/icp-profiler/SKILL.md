---
name: icp-profiler
description: >
  Defines the Ideal Customer Profile (ICP) for a product or service.
  Combines company context, market signals, and structured frameworks to produce
  a detailed ICP document: demographics, firmographics, pain points, buying signals,
  and objection patterns.
description_pt-BR: >
  Define o Perfil de Cliente Ideal (ICP) para um produto ou serviço. Combina contexto
  da empresa, sinais de mercado e frameworks estruturados para produzir um ICP
  detalhado: demografias, firmografias, dores, sinais de compra e padrões de objeção.
type: hybrid
version: "1.0.0"
categories: [research, audience, icp, lead-generation, strategy]
---

# ICP Profiler

## When to Use

Use when a squad needs a precise audience definition before generating content,
outreach, or positioning strategy. Also useful for content squads to calibrate
tone, vocabulary, and hooks.
Input: company description + product/service being sold. Output: `output/icp-profile.md`.

---

## Process

1. **Load company context** — Read `_conclave/_memory/company.md` for company description, products, and current tone.
2. **Define firmographics (B2B) or demographics (B2C)** — Based on the product, identify:
   - B2B: company size, industry, role/title, revenue range, tech stack signals
   - B2C: age range, income, lifestyle, platform preferences, content consumption habits
3. **Map pain points** — Search for forums, reviews, and LinkedIn conversations around the problem this product solves. Extract the top 3–5 pains people articulate in their own words.
4. **Buying signals** — What events or behaviors indicate a prospect is actively looking? (Job posting changes, funding, new initiative, life event, etc.)
5. **Objections** — What does this audience typically resist? Price sensitivity, trust barriers, status quo bias, competitor loyalty.
6. **Language patterns** — How does this audience talk about their problems? Extract exact phrases from forums/reviews.
7. **Content preferences** — What format and tone works best for this profile (based on platform signals)?
8. **Synthesize into ICP document**.

---

## Output Format

```markdown
# ICP Profile: {Product/Service Name}
**Generated:** {YYYY-MM-DD}

## Profile Summary
"{2–3 sentence description of the ideal customer in plain language}"

## Firmographics / Demographics
| Attribute | Profile |
|-----------|---------|
| {B2B: Company size} | {range} |
| {B2B: Industry} | {list} |
| {B2B: Decision-maker title} | {roles} |
| {B2C: Age range} | {range} |
| {B2C: Platform} | {primary platforms} |

## Top Pain Points (in their words)
1. **"{Verbatim phrase from forums/reviews}"** — {context}
2. ...

## Buying Signals
- {signal}: {why it indicates readiness}

## Common Objections
| Objection | Root cause | Ideal response |
|-----------|-----------|----------------|
| "{objection}" | {why they resist} | {reframe approach} |

## Language Patterns
- Uses: {words/phrases they use}
- Avoids: {words that signal "not for me"}
- Trusted voices: {types of authority they follow}

## Content Preferences
- **Formats:** {blog / video / carousel / thread / podcast}
- **Tone:** {what works: direct / educational / story-driven}
- **Hook types:** {what gets their attention}
```

---

## Output Instructions

Write to `squads/{code}/output/icp-profile.md`.

Report:
```
ICP Profiler — output:
— Produto/Serviço: {name}
— Tipo de mercado: {B2B | B2C | both}
— Dores mapeadas: {N}
— Sinais de compra: {N}
— Arquivo: output/icp-profile.md
```
