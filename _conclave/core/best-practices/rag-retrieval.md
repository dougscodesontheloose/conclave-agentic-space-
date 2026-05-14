---
name: RAG Retrieval (POSEIDON)
description: Diretrizes para agentes sobre como formular buscas e interpretar resultados do cérebro coletivo do Conclave.
maturity: validated
---

# Best Practices: RAG Retrieval

O RAG (Retrieval-Augmented Generation) permite que você acesse a memória histórica do Conclave.
Use-o para não repetir erros e para replicar sucessos.

The engine is `_conclave/tools/scripts/poseidon_engine.py` — ChromaDB + `all-MiniLM-L6-v2` embeddings.
Full documentation in `skills/brain-query/SKILL.md`.

## 1. Query Formulation

A busca é semântica, não por palavra-chave.

| ❌ Ruim | ✅ Bom |
| --- | --- |
| `marketing analytics tone` | `Quais tons de voz foram aprovados em squads de Marketing Analytics?` |
| `rejection reasons` | `Por que o usuário rejeita posts de carrossel? Liste os vetos recorrentes.` |
| `eval failures` | `Which quality criteria has skill linkedin-writing failed in validate steps?` |

## 2. Query Modes

Use the right mode for each type of question:

| Mode | Flag | Best for |
| --- | --- | --- |
| General | (none) | Broad contextual queries |
| Memory | `--mode memory` | Preferences, prohibitions, user model |
| Signals | `--mode signals` | Quality trends, delivery patterns |
| Eval | `--mode eval` | Criterion-level skill failures (eval harness) |
| Gossip | `--mode gossip` | What other squads learned in the same domain |

## 3. Reading Results

Each result carries `quality`, `ts`, `squad`, and `layer` metadata.

- **Recency:** `ts` closer to today = higher authority on current preferences
- **Quality field:** `good` = replicate this; `miss` = use as anti-pattern; empty = structural memory
- **Layer:** `eval` results (from `type:validate` steps) are the strongest evidence of skill behavior — they are measured, not inferred
- **Squad field:** Non-empty squad results are specific to that context; global (empty) results are universal

## 4. Integration in Reasoning

Never copy retrieved content verbatim. Synthesize:

> "Baseado na memória: o usuário rejeitou neon excessivo em 20/04 (squad data_ops, quality: miss).
> A paleta aprovada usa Brutalist P&B. O skill linkedin-writing falhou no critério 'Hook ausente'
> em 3/5 runs recentes — incluirei um hook explícito na primeira linha."

The RAG result becomes a constraint on your generation, not a template to fill in.

## 5. Eval-Aware Retrieval

When an agent step has a `type:validate` step following it, use eval mode before generating:

```bash
python3 _conclave/tools/scripts/poseidon_engine.py query \
  --q "what criteria does {skill-name} fail most often" \
  --mode eval --n 5
```

If recurring failures are returned → actively avoid those failure patterns in your output.
This closes the loop: POSEIDON detects the pattern, the agent acts on it before the validator runs.

## 6. When NOT to Use RAG

- For real-time facts → use `web_search`
- For the current step's instructions → read the step file directly
- For TIER: SECRET data → never query; the engine respects SafeGuard but avoidance is cleaner
- When context budget is critically low → skip RAG, use `company.md` as fallback.
