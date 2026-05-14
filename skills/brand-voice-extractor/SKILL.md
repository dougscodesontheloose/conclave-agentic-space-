---
name: brand-voice-extractor
description: >
  Analyze a company's published content to extract their brand voice, writing style,
  and tone guidelines. Reads 10-20 of their best content pieces and produces a
  brand voice profile covering tone, vocabulary level, sentence structure, formatting
  patterns, CTAs, and target persona. Useful before writing outreach, content, or
  campaigns that should match a client's existing voice.
tags: [brand]
description_pt-BR: >
  Extrai o DNA comunicativo de uma marca a partir de seu conteúdo público: site, blog, redes sociais e anúncios. Produz um perfil de voz estruturado — vocabulário, regras de tom, padrões de conteúdo e anti-padrões.
type: playbook
---

# Brand Voice Extractor

**Core principle:** Voz é o que sobrevive à tradução; tom é o que muda por canal.

Analyze a company's published content to extract their brand voice and writing style. Reads their top content pieces and produces actionable guidelines for matching their voice in future content, outreach, or campaigns.

## Quick Start

```
Extract brand voice for [company]. Use their blog at [url].
```

Or with content already cataloged:
```
Extract brand voice for [client]. Use the content inventory at clients/[client]/research/content-inventory.json.
```

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| **Content URLs** | Yes | User provides, or pulled from site-content-catalog output |
| **Company name** | Yes | For context in the analysis |
| **Number of pages** | No | Default: 15. How many pages to analyze. |

## Phase 0: Intake

1. **Quais materiais?** — URLs, textos colados, ou ambos? Mínimo 5 amostras representativas.
2. **Contexto da marca** — B2B/B2C, indústria, público-alvo principal.
3. **Objetivo da extração** — Brand book interno, onboarding de copywriter, alinhamento de squad de conteúdo?
4. **Profundidade** — `quick` (3 dimensões) ou `deep` (10 dimensões)?

> **Regra:** Faça TODAS as perguntas em uma única interação.

## Process

### Phase 1: Select Content to Analyze

If content URLs are provided directly, use those. Otherwise:

1. Read the content inventory from `site-content-catalog` output
2. Select a diverse sample of 10-20 pages, prioritizing:
   - **Blog posts** (primary voice indicator)
   - **Landing pages** (marketing voice)
   - **Case studies** (storytelling voice)
   - Mix of recent and older content (to detect voice evolution)
   - Mix of topics (to see consistency across subjects)

**Selection heuristic:**
- 8-10 blog posts (mix of how-to, opinion, product updates)
- 2-3 landing pages (homepage, product page, solutions page)
- 2-3 case studies or customer stories (if available)
- 1-2 comparison/vs pages (if available)

### Phase 2: Fetch and Extract Text

For each selected URL:
1. WebFetch the page
2. Extract the main content body (strip nav, footer, sidebar)
3. Store: title, URL, raw text, word count

### Phase 3: Analyze Voice Dimensions

Analyze across these dimensions:

#### A) Tone
- **Formality spectrum:** Casual ↔ Professional ↔ Academic
- **Emotional register:** Excited ↔ Measured ↔ Dry
- **Authority stance:** Peer/friend ↔ Expert/teacher ↔ Institution
- **Humor usage:** Frequent ↔ Occasional ↔ None
- **Directness:** Direct/bold ↔ Hedged/diplomatic

#### B) Vocabulary & Language
- **Reading level:** Approximate grade level (simple vs. complex)
- **Jargon usage:** Heavy industry jargon ↔ Plain language
- **Technical depth:** Assumes expertise ↔ Explains everything
- **Power words:** Common persuasion/action words they favor
- **Banned patterns:** Words or phrases they conspicuously avoid
- **Unique vocabulary:** Distinctive terms or phrases they use repeatedly

#### C) Sentence Structure
- **Average sentence length:** Short/punchy ↔ Long/complex
- **Paragraph length:** 1-2 sentences ↔ 3-4 ↔ 5+
- **Opening patterns:** How they start articles (question, stat, story, bold claim)
- **Transition style:** How they connect ideas
- **Use of fragments:** Do they use incomplete sentences for emphasis?

#### D) Formatting Patterns
- **Headers:** Frequency, style (question-based, how-to, numbered)
- **Lists:** Bullets vs. numbered, frequency
- **Bold/italic:** How they use emphasis
- **Images/media:** Frequency, types (screenshots, illustrations, photos)
- **CTAs:** Placement, style, frequency, language used
- **Pull quotes/callouts:** Do they use them?

#### E) Content Structure
- **Typical article length:** Short (<800), Medium (800-1500), Long (1500+)
- **Introduction style:** Hook type, length
- **Conclusion style:** Summary, CTA, open question
- **Use of data/stats:** Frequent ↔ Rare
- **Use of examples:** Frequent ↔ Rare
- **Storytelling:** Narrative-driven ↔ Information-driven

#### F) Persona & Audience
- **Who they write for:** Inferred target reader (role, seniority, industry)
- **Assumed knowledge level:** Beginner ↔ Intermediate ↔ Expert
- **Point of view:** First person singular (I) ↔ First person plural (we) ↔ Second person (you) ↔ Third person
- **Reader relationship:** Peer ↔ Teacher ↔ Service provider

### Phase 4: Generate Brand Voice Profile

Produce a Markdown document with this structure:

```markdown
# Brand Voice Profile: [Company Name]
**Analyzed:** [Date] | **Content pieces analyzed:** [N]
**Sources:** [list of URLs analyzed]

---

## Voice Summary (2-3 sentences)

[Company] writes in a [tone] voice that [description]. Their content targets
[audience] and assumes [knowledge level]. The overall feel is [adjectives].

---

## Tone Profile

| Dimension | Position | Evidence |
|-----------|----------|----------|
| Formality | [e.g., Professional-casual] | [Example quote] |
| Emotional Register | [e.g., Measured, occasionally excited] | [Example] |
| Authority | [e.g., Expert/teacher] | [Example] |
| Humor | [e.g., Rare, dry when used] | [Example] |
| Directness | [e.g., Very direct, bold claims] | [Example] |

---

## Language & Vocabulary

### Reading Level
[Grade level estimate and what that means]

### Signature Phrases
- "[phrase 1]" — used frequently to [purpose]
- "[phrase 2]" — recurring pattern in [context]

### Jargon & Technical Depth
[How much industry jargon they use, how they handle technical concepts]

### Words They Love
[List of frequently used power words, adjectives, verbs]

### Words They Avoid
[Notable absences or patterns they steer away from]

---

## Structure & Formatting

### Typical Article Structure
[Outline of how their articles are typically organized]

### Sentence & Paragraph Style
- Average sentence length: [X words]
- Typical paragraph: [X sentences]
- Notable patterns: [fragments, rhetorical questions, etc.]

### Formatting Habits
- Headers: [style]
- Lists: [frequency and style]
- Emphasis: [bold/italic patterns]
- CTAs: [where, how often, what language]

---

## Audience & Persona

### Target Reader
[Role, seniority, industry, pain points they address]

### Knowledge Assumptions
[What they assume the reader already knows]

### Point of View
[I/we/you usage and what it signals]

---

## Writing Guidelines (Actionable)

Use these guidelines when writing content, outreach, or campaigns for [Company]:

### Do
- [Guideline 1 with example]
- [Guideline 2 with example]
- [Guideline 3 with example]

### Don't
- [Anti-pattern 1]
- [Anti-pattern 2]
- [Anti-pattern 3]

### Voice Samples

**Their style:**
> [2-3 representative quotes from their content that exemplify the voice]

**How to match it:**
> [2-3 example sentences written in their voice about a neutral topic]
```

## Tips

- **15 pages is the sweet spot.** Fewer than 10 won't capture enough variation. More than 25 adds cost without much signal.
- **Blog posts are the best voice signal.** Landing pages are more formulaic. Blog posts show the authentic voice.
- **Look for consistency AND inconsistency.** If their tone shifts dramatically between content types, note it — they may have multiple voice modes.
- **Check for ghost-written content.** If some posts feel dramatically different, they may use external writers. Flag this in the analysis.
- **This skill has no code script.** It's an agent-executed skill — the AI agent reads the content via WebFetch and performs the analysis directly. The structured output template above guides the analysis.

## Dependencies

- Web fetch capability (for reading content pages)
- Optional: `site-content-catalog` output (for selecting which content to analyze)
- No API keys or paid tools required

## Cost

| Component | Cost |
| --- | --- |
| WebFetch (materiais públicos) | Free |
| Apify (extração social opcional) | ~$0.50 por canal |
| LLM reasoning | Free |
| **Total típico** | **Free** |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **API/tool unavailable** | HTTP error, timeout, or command failure | Log the specific error. Attempt retry once. If still failing, skip and note in output |
| **Insufficient input data** | Missing required fields or empty dataset | Prompt user for missing data. Do not proceed with assumptions on critical fields |
| **Unexpected data format** | Parse error or schema mismatch | Log the raw response snippet. Attempt best-effort parsing. Flag `⚠️ Data format unexpected` |
| **Rate limiting** | HTTP 429 or throttle signal | Implement exponential backoff (1s → 2s → 4s). Max 3 retries |
| **Partial results** | Some sources succeed, others fail | Deliver partial results with clear indication of which sources failed and why |

**Principle:** Every execution must produce either a result or a clear, actionable error message. Silent failures are unacceptable.


## Composability

**Receives data from:**

- `competitor-intel` — perfis de concorrentes p/ contraste
- `industry-scanner` — pulso de linguagem do setor

**Feeds into:**

- `content-asset-creator` — voice guide vira input criativo
- `campaign-brief-generator` — briefs respeitam guidelines
- `creative-long-form` — long-form herda voz extraída
- `linkedin-writing` — posts seguem o voice guide

**Integration pattern:** Roda uma vez por marca; output é referenciado por múltiplos skills downstream.

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: brand-voice-extractor — [finding]` | `[OPERACIONAL]: brand-voice-extractor — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: brand-voice-extractor — [param] works better as [value]` | `[OPERACIONAL]: brand-voice-extractor — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: brand-voice-extractor — [insight]` | `[ESTRATÉGICO]: brand-voice-extractor — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **Anti-AI pass:** Output text ran through humanization checklist (see below)
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.

---

## Anti-AI Text Purification (Integrated from Humanizer)

Quando este skill gerar texto de saída (voice guidelines, exemplos, ou qualquer prosa), aplique esta verificação final para eliminar sinais de escrita AI.

**Core insight:** LLMs usam algoritmos estatísticos para prever o próximo token. O resultado tende ao mais provável, criando padrões reconhecíveis.

### Padrões a Eliminar

| # | Padrão | Palavras-gatilho | Fix |
|---|---|---|---|
| 1 | Ênfase indevida de significância | "pivotal", "testament", "crucial", "landscape" | Remover inflação. Seja específico. |
| 2 | Linguagem promocional | "vibrant", "groundbreaking", "breathtaking", "nestled" | Tom neutro. Fatos concretos. |
| 3 | Superficial -ing endings | "highlighting...", "showcasing...", "fostering..." | Reescrever sem particípio decorativo. |
| 4 | Atribuições vagas | "Experts argue", "Industry reports" | Citar fontes específicas. |
| 5 | Vocabulário AI overused | "delve", "tapestry", "interplay", "underscore" | Palavras simples e diretas. |
| 6 | Copula avoidance | "serves as", "stands as", "represents" | Use "is", "are", "has". |
| 7 | Rule of Three | Forçar grupos de 3 | Use 2 ou 4 quando natural. |
| 8 | False ranges | "from X to Y" sem escala real | Listar diretamente. |
| 9 | Em dash overuse | "X — Y — Z" | Vírgulas, pontos, parênteses. |
| 10 | Boldface mecânico | **Toda** **palavra** **negrito** | Negrito só quando genuinamente necessário. |
| 11 | Sycophantic tone | "Great question!", "You're absolutely right!" | Remover. Vá direto ao ponto. |
| 12 | Filler phrases | "In order to", "It is important to note" | Simplificar. |
| 13 | Signposting | "Let's dive in", "Here's what you need to know" | Comece com o conteúdo. |

### Processo de Purificação

1. **Escreva** a saída normalmente
2. **Pergunte-se:** "O que torna este texto obviamente AI?"
3. **Identifique** padrões da tabela acima
4. **Reescreva** seções problemáticas
5. **Adicione alma:** opinião, ritmo variado, especificidade, primeira pessoa quando adequado

### Personalidade e Alma

Evitar padrões AI é só metade do trabalho. Escrita estéril e sem voz é tão óbvia quanto slop.

**Regras:**
- **Tenha opiniões.** Não apenas reporte — reaja.
- **Varie o ritmo.** Frases curtas. Depois uma mais longa.
- **Reconheça complexidade.** Humanos têm sentimentos mistos.
- **Use "eu" quando caber.** Primeira pessoa não é improfissional.
- **Seja específico sobre sentimentos.** Não "preocupante" — diga o quê preocupa.

*Baseado em [blader/humanizer](https://github.com/blader/humanizer) (MIT) e [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).*

---

## Conclave Output Convention

Quando rodado dentro de um squad Conclave, o output canônico segue:

Write to `squads/{code}/output/brand-voice-{slug}.md`.

Report:
```
Brand Voice Extractor — output:
— Marca: {name}
— Fontes analisadas: {N}
— Tom predominante: {1-word descriptor}
— Arquivo: output/brand-voice-{slug}.md
```

## When to Use

- "Extrai a voz da marca X a partir desses materiais"
- "Como essa marca soa? Cria um voice guide"
- "Padroniza o tom dos meus textos com base nesses exemplos"
- Análise estilística ou guidelines editoriais

**Auto-trigger:** Ative quando o usuário compartilha materiais de marca (site, posts, vídeos) e pede análise de voz, tom, ou guidelines de comunicação.

## Prerequisites

### Environment Variables

```env
# Nenhuma variável obrigatória
APIFY_API_TOKEN=optional_for_social_extraction
```

### Dependencies

Nenhuma. Pure reasoning com `WebFetch`.
