---
name: industry-scanner
description: >
  Broad industry landscape analysis across 5+ data dimensions: key players,
  trends, emerging threats, market opportunities, and customer sentiment.
  Produces a strategic overview document for squad research agents.
description_pt-BR: >
  Análise ampla do panorama setorial em 5+ dimensões: principais players,
  tendências, ameaças emergentes, oportunidades de mercado e sentimento do cliente.
  Produz um documento estratégico para agentes de pesquisa.
type: hybrid
version: "1.0.0"
categories: [competitive-intelligence, research, industry-analysis, strategy]
---

# Industry Scanner

## When to Use

Use when a squad needs to understand the landscape of an entire industry or niche
before designing strategy or content. Best used at squad creation time or at the start
of a major research run.
Input: industry name or description. Output: `output/industry-{slug}.md`.

---

## Process

1. **Define scope** — Clarify the exact industry/niche being scanned. Set geographic scope (global / regional / specific market).
2. **Key Players** — Search for top 5–8 companies in the space. For each: name, market position, brief description.
3. **Trends (last 12 months)** — Search for "{industry} trends {year}" and "{industry} news". Extract 4–6 dominant trends with evidence.
4. **Emerging Threats** — Search for "{industry} disruption", "{industry} challenges", new entrants. Extract 2–3 threats.
5. **Market Opportunities** — Search for "{industry} gaps", "what {industry} is missing", customer complaints in the space. Extract 2–4 white-space opportunities.
6. **Customer Sentiment** — Search Reddit, G2, forums for what customers say. Extract top praise and frustration patterns.
7. **Regulatory / Context** — Flag any relevant regulatory, cultural, or economic forces shaping the industry.
8. **Synthesis** — Compile into Output Format with a strategic outlook section.

---

## Output Format

```markdown
# Industry Landscape: {Industry Name}
**Scanned:** {YYYY-MM-DD}
**Scope:** {geographic / segment scope}

## Key Players
| Company | Position | Known For |
|---------|----------|-----------|
| {name} | {leader/challenger/niche} | {differentiator} |

## Dominant Trends (last 12 months)
1. **{Trend}:** {description + evidence}
2. ...

## Emerging Threats
1. **{Threat}:** {description + risk level}
2. ...

## Market Opportunities
1. **{Opportunity}:** {gap description + signals}
2. ...

## Customer Sentiment
- **Praised industry-wide:** {patterns}
- **Frustrated industry-wide:** {patterns}
- **Unmet needs:** {patterns}

## External Forces
- {Regulatory / economic / cultural context}

## Strategic Outlook
{2–3 paragraph synthesis: where this industry is heading, what creates advantage, what to watch}
```

---

## Output Instructions

Write to `squads/{code}/output/industry-{slug}.md`.

Report:
```
Industry Scanner — output:
— Setor: {industry name}
— Players mapeados: {N}
— Tendências identificadas: {N}
— Arquivo: output/industry-{slug}.md
```
