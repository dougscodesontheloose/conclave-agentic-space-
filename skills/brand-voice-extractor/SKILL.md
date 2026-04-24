---
name: brand-voice-extractor
description: >
  Extracts a brand's communication DNA from its public content: website copy,
  blog posts, social media, and ads. Outputs a structured voice profile —
  vocabulary, tone rules, content patterns, and anti-patterns.
description_pt-BR: >
  Extrai o DNA comunicativo de uma marca a partir de seu conteúdo público:
  site, blog, redes sociais e anúncios. Produz um perfil de voz estruturado —
  vocabulário, regras de tom, padrões de conteúdo e anti-padrões.
type: hybrid
version: "1.0.0"
categories: [competitive-intelligence, brand, research, voice-analysis]
---

# Brand Voice Extractor

## When to Use

Use when an agent needs to understand HOW a brand communicates — not just what they sell.
Useful for investigation phase, competitive research, and tone-of-voice benchmarking.
Input: brand name or URL. Output: `output/brand-voice-{slug}.md`.

---

## Process

1. **Gather sources** — Fetch homepage, About page, 2–3 blog posts (most recent), and LinkedIn page. Search for any visible ad copy or taglines.
2. **Vocabulary extraction** — Identify recurring words and phrases:
   - Power words used (e.g., "transform", "effortless", "proven")
   - Jargon or proprietary terms
   - Words conspicuously avoided
3. **Tone mapping** — Classify communication style across dimensions:
   - Formality: corporate ↔ casual
   - Energy: calm ↔ urgent
   - Stance: humble ↔ bold
   - Complexity: simple ↔ technical
4. **Structure patterns** — Analyze content format patterns:
   - Typical headline structure (question / statement / how-to / data-lead)
   - Paragraph length tendencies
   - Use of lists, numbers, stories
   - CTA style
5. **Anti-patterns** — What this brand explicitly avoids (inferred from absence and contrast)
6. **Synthesis** — Compile into Output Format.

---

## Output Format

```markdown
# Brand Voice Profile: {Brand Name}
**Analyzed:** {YYYY-MM-DD}
**Sources:** {N pages / posts reviewed}

## Vocabulary
### Always Uses
- {word/phrase}: {why / context}

### Avoids
- {word/phrase}: {why / what they use instead}

### Proprietary Terms
- {term}: {meaning / how used}

## Tone Map
| Dimension | Score (1–10) | Evidence |
|-----------|-------------|---------|
| Formality (1=casual, 10=corporate) | | |
| Energy (1=calm, 10=urgent) | | |
| Boldness (1=humble, 10=bold) | | |
| Technical depth (1=simple, 10=expert) | | |

## Content Patterns
- **Headlines:** {pattern description + example}
- **Paragraph style:** {short punchy / long narrative / mixed}
- **Structure:** {list-heavy / story-driven / data-led}
- **CTA style:** {soft ask / direct / social proof}

## Anti-Patterns (what they avoid)
- {pattern}: {why this seems intentional}

## Summary: Their Voice in One Sentence
"{Write a single sentence that captures the brand's unique voice personality}"
```

---

## Output Instructions

Write to `squads/{code}/output/brand-voice-{slug}.md`.

Report:
```
Brand Voice Extractor — output:
— Marca: {name}
— Fontes analisadas: {N}
— Tom predominante: {1-word descriptor}
— Arquivo: output/brand-voice-{slug}.md
```
