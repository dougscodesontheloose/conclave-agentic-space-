---
name: battlecard-generator
description: >
  Generates competitive battlecards: structured head-to-head comparisons designed
  for sales and positioning conversations. Takes competitor profile data (from
  competitor-intel skill or manual input) and produces a ready-to-use battlecard.
description_pt-BR: >
  Gera battlecards competitivos: comparações diretas estruturadas para conversas
  de vendas e posicionamento. Aceita dados de competitor-intel ou input manual
  e produz um battlecard pronto para uso.
type: prompt
version: "1.0.0"
categories: [competitive-intelligence, sales, positioning, battlecard]
---

# Battlecard Generator

## When to Use

Use after running `competitor-intel` (or when competitor data is already available).
Produces a single-page battlecard optimized for sales conversations, positioning statements,
and content strategy decisions.
Input: competitor name + your company profile. Output: `output/battlecard-{slug}.md`.

---

## Process

1. **Load competitor data** — Read from `output/competitor-{slug}.md` if it exists. Otherwise use available context about the competitor.
2. **Load your profile** — Read `_conclave/_memory/company.md` for your positioning, product, and tone.
3. **Map the battlefield** — Identify 4–6 key dimensions where the two companies differ meaningfully (price, target market, features, philosophy, speed, support, etc.).
4. **Write the battlecard** — For each dimension: state the competitor's position, state your position, write a "How to win" line — a single sentence a sales rep could say.
5. **Write objection responses** — Identify 3 most common objections about your product relative to this competitor and write tight 1–2 sentence responses.
6. **Write the kill shot** — One line that summarizes your decisive advantage in this competition.

---

## Output Format

```markdown
# Battlecard: {Your Company} vs {Competitor}
**Generated:** {YYYY-MM-DD}

## The Kill Shot
"{Single sentence: your decisive, memorable advantage}"

## Head-to-Head

| Dimension | {Competitor} | {Your Company} | How to Win |
|-----------|-------------|----------------|-----------|
| {dimension} | {their position} | {your position} | {1-sentence win line} |

## When They Say...

**"{Objection 1}"**
→ {1–2 sentence response}

**"{Objection 2}"**
→ {1–2 sentence response}

**"{Objection 3}"**
→ {1–2 sentence response}

## Their Strongest Points (respect, don't dismiss)
- {honest strength 1}
- {honest strength 2}

## Where You Win Every Time
- {clear advantage 1}
- {clear advantage 2}
- {clear advantage 3}
```

---

## Output Instructions

Write to `squads/{code}/output/battlecard-{slug}.md`.

Report:
```
Battlecard Generator — output:
— Confronto: {Your Company} vs {Competitor}
— Dimensões comparadas: {N}
— Objeções endereçadas: {N}
— Arquivo: output/battlecard-{slug}.md
```
