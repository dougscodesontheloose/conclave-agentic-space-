---
name: brain-query
description: >
  Semantic search over Conclave's collective memory. Retrieves relevant chunks
  from squad learnings, user model, eval signals, preferences, run history, and
  cross-squad gossip. Invoke at the start of any squad run to load historical
  context, or mid-run to answer "what did we learn about X before?".
description_pt-BR: >
  Busca semântica sobre a memória coletiva do Conclave. Recupera chunks relevantes
  de aprendizados de squads, modelo do usuário, sinais de eval, preferências,
  histórico de runs e gossip cross-squad. Invoque no início de qualquer run para
  carregar contexto histórico.
type: script
version: "2.0.0"
script:
  runtime: python3
  path: _conclave/tools/scripts/poseidon_engine.py
  subcommand: query
categories: [rag, memory, retrieval, context]
contract:
  inputs:
    - name: query_text
      required: true
      description: "A semantic question or description of what you need to find"
  quality_criteria:
    - "Query is formulated as a complete semantic question, not keywords"
    - "Results are interpreted in context — not copied verbatim into output"
    - "Recency and quality metadata are used to weight conflicting signals"
    - "If no results returned, agent proceeds with defaults from company.md"
  on_failure: skip
---

# Brain Query — Semantic Memory Retrieval

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


## The Engine

Brain Query runs against a live ChromaDB index of Conclave's collective memory,
powered by `all-MiniLM-L6-v2` embeddings. The index covers:

| Source | Layer | What it contains |
| --- | --- | --- |
| `company.md`, `user-model.md`, `preferences.md` | global | Who Douglas is, what he values, inferred patterns |
| `linkedin-insights.md`, `visual-identity.md` | global | Platform-specific voice and aesthetic |
| `squads/*/memories.md` | squad | Per-squad writing/visual/structure preferences |
| `squads/*/runs.md` | squad | Run history (topics, outcomes) |
| `skill-signals.jsonl` | signal | Skill quality patterns (run-level + eval criterion-level) |
| `squad-signals.jsonl` | signal | Per-squad delivery signals |
| `implicit-signals.jsonl` | signal | Observed patterns from accepted runs |
| `gossip.jsonl` | signal | Cross-squad preference propagation |
| `session-log.jsonl` | signal | Session events |
| `squads/*/output/*/steps.jsonl` | eval | Per-step validate/review verdicts |

---

## Commands

### General query (all sources)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "preferências de escrita aprovadas para LinkedIn" \
  --n 5
```

### Squad-specific (filter to one squad's learnings)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "rejected patterns in this squad" \
  --squad sexy_content \
  --n 5
```

### Eval mode (criterion-level failures from the eval harness)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "what criteria does linkedin-writing fail most often" \
  --mode eval \
  --n 10
```

### Signals only (quality patterns, no preference text)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "squad delivery trends in the last runs" \
  --mode signals \
  --n 5
```

### Good-quality results only (filter out miss/partial signals)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "visual design choices that were approved" \
  --quality good \
  --n 5
```

### Memory only (preferences, user model — no signals)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "design identity and aesthetic rules" \
  --mode memory \
  --n 5
```

### Keep the index current (incremental — only re-index changed files)

```bash
python3 _conclave/tools/scripts/poseidon_engine.py index --incremental
```

---

## Query Formulation Rules

**Write complete semantic sentences, not keywords.**

| ❌ Bad | ✅ Good |
| --- | --- |
| `linkedin tone` | `Qual tom de voz o usuário aprovou em posts de LinkedIn sobre dados?` |
| `rejection reasons` | `Por que o usuário costuma rejeitar carrosséis? Quais os vetos mais comuns?` |
| `visual style` | `Qual paleta de cores e tipografia foram aprovadas em designs de carrossel?` |
| `eval failures` | `Which quality criteria has skill linkedin-writing failed in validate steps?` |

The model understands intent, not just words. A richer query returns richer results.

---

## Interpreting Results

Each result has:

- `score` — cosine similarity after re-ranking (recency + quality boost applied)
- `content` — the retrieved chunk text
- `source` — relative path to the source file
- `squad` — squad this came from (empty = global)
- `quality` — `good | partial | miss` (empty = not a signal)
- `ts` — when it was indexed or when the signal was generated
- `layer` — `global | squad | signal | eval | history`

**Weighting rules when signals conflict:**

1. Newer timestamp wins over older
2. `quality: good` gets a score boost; `quality: miss` gets a penalty — use miss results as anti-patterns
3. Squad-specific results outrank global results when querying within that squad's domain
4. `eval` layer results (from the eval harness) are the strongest evidence of skill behavior

---

## Integration Pattern

When using Brain Query at the start of a pipeline step:

```text
1. Formulate 1–3 targeted queries covering: preferences, prohibitions, recent patterns
2. Run each query; collect results
3. Extract relevant facts — do not inject raw JSON into the context
4. Summarize as: "Baseado na memória: X foi aprovado, Y foi vetado, Z é padrão"
5. Use that summary as grounding for generation — never copy content verbatim
```

---

## Maintenance Commands

```bash
# Full re-index (after major memory changes)
python3 _conclave/tools/scripts/poseidon_engine.py index

# Incremental (fast, daily use)
python3 _conclave/tools/scripts/poseidon_engine.py index --incremental

# Show index stats
python3 _conclave/tools/scripts/poseidon_engine.py status

# Reset everything (nuclear option)
python3 _conclave/tools/scripts/poseidon_engine.py reset
```

---

## Restrictions

- **Never search for TIER: SECRET data** — the engine respects SafeGuard but avoidance is cleaner
- **If the engine returns an empty result**, do not invent content — fall back to `company.md` and `global-preferences.md`
- **If the script errors with "Missing dependencies"**, run: `pip install chromadb sentence-transformers`
- **Eval mode will return no results until `type:validate` steps with `skill_contract:` have run at least once** — this is expected behavior, not a bug


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
# Nenhuma variável obrigatória estrita
```

### Dependencies

Requer ambiente de execução padrão do Conclave.
