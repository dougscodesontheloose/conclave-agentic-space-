---
name: research-paper-writer
description: >
  Pipeline end-to-end para produção de papers acadêmicos de ML/AI para NeurIPS, ICML, ICLR.
  Cobre design de experimentos, execução, análise estatística, escrita, review e submissão.
  Inclui verificação rigorosa de citações e workflow de BibTeX programático.
type: playbook
tags: [research, content, strategy]
---

# Research Paper Writer

Pipeline completo para papers acadêmicos publication-ready em ML/AI.

**Core principle:** Paper é uma história, não coleção de experimentos. Uma contribuição clara, uma frase.

## When to Use

- "Escreva um paper sobre [pesquisa]"
- "Preciso submeter para [conferência]"
- "Design de experimentos para paper"
- "Responda reviews com novos dados"

**Auto-trigger:** Quando o contexto envolve escrita acadêmica ou submissão a conferências.

## Prerequisites

### Dependencies

```bash
pip install semanticscholar requests scipy numpy matplotlib
# LaTeX: brew install --cask mactex
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Contribuição** | Yes | O que o paper contribui (uma frase) |
| **Venue** | Recommended | NeurIPS, ICML, ICLR, ACL, etc. |
| **Codebase** | Recommended | Repositório com código e resultados |

## Phase 0: Setup do Projeto

1. Explorar repositório e identificar contribuição
2. Articular: The What (claim), The Why (evidência), The So What (por que importa)
3. Criar workspace organizado (paper/, experiments/, results/)
4. Estimar budget de compute

## Phase 1: Literature Review

Usar `arxiv-paper-scanner` para descoberta e Semantic Scholar para citações.

**REGRA:** NUNCA gere BibTeX de memória. SEMPRE busque programaticamente.

```python
# Verificação de citação (OBRIGATÓRIO por citação):
# 1. SEARCH → Semantic Scholar
# 2. VERIFY → Confirmar em 2+ fontes
# 3. RETRIEVE → BibTeX via DOI
# 4. VALIDATE → Claim realmente aparece no paper
# 5. ADD → BibTeX verificado ao .bib
# Se QUALQUER step falha → [CITATION NEEDED]
```

## Phase 2: Design de Experimentos

Mapear claims → experiments. Cada experimento responde uma pergunta específica.

| Claim | Experiment | Expected Evidence |
|---|---|---|
| "Method outperforms baselines" | Main comparison | Win rate, significance |
| "Effect is larger for X" | Scaling study | Monotonic curve |

## Phase 3: Execução e Monitoramento

- `nohup python run_experiment.py > logs/exp.log 2>&1 &`
- Scripts devem skip trabalho completado (crash recovery)
- Commit após cada batch de resultados

## Phase 4: Análise

- Sempre compute: error bars, 95% CI, McNemar's test, Cohen's d
- Identificar a história: main finding, surprises, failures, follow-ups

## Phase 5: Escrita

**Time allocation:** 25% abstract, 25% intro, 25% figures, 25% rest.

Workflow narrativo: contribuição → abstract → intro → methods → results → related work → conclusion.

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Paper** | LaTeX + PDF | `paper/` |
| **BibTeX** | `.bib` | `paper/references.bib` |
| **Figuras** | PDF vetorial | `paper/figures/` |
| **Dados** | JSON/CSV | `results/` |

## Cost

| Component | Cost |
|---|---|
| APIs acadêmicas | Free |
| Compute (GPU/API) | Variável |
| LaTeX | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Citação inválida** | Busca retorna vazio | Marcar [CITATION NEEDED] |
| **Experiment timeout** | Processo stale | Re-run com checkpoint |
| **Resultados negativos** | Hypothesis wrong | Reframe ou pivotar |

## Composability

**Receives data from:**
- `arxiv-paper-scanner` — papers e citações
- `data-toolkit` — análise de dados

**Feeds into:**
- Submissão a conferências
- `manim-video-creator` — paper explainer em vídeo

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Venue deadlines** | `[OPERACIONAL]: research-paper-writer — [venue] deadline [data]` | `NeurIPS deadline May 2026` |
| **Citation patterns** | `[OPERACIONAL]: research-paper-writer — [insight]` | `Semantic Scholar mais confiável que Google Scholar` |

## Quality Gate

- [ ] **Contribuição em uma frase**
- [ ] **Todas citações verificadas programaticamente**
- [ ] **Resultados com significância estatística**
- [ ] **Figuras em PDF vetorial**
- [ ] **User checkpoint antes de submeter**

**If any check fails:** Iterar no componente que falhou.
