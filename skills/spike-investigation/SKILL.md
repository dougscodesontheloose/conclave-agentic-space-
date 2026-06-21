---
name: spike-investigation
description: >
  Realiza experimentos throwaway (Spikes) de código para validar ideias, comparar bibliotecas e mitigar riscos antes da implementação real.
type: playbook
tags: [development, research, prototyping, mvp, planning, code]
---

# Spike Investigation

Crie protótipos rápidos e descartáveis para responder a perguntas técnicas específicas (feasibility). "Spike and throw away".

**Core principle:** Um spike não é código de produção. É código escrito para comprar conhecimento. O entregável real de um spike é o veredito, não o software.

## When to Use

- "Can we do X?"
- "Which library is better: A or B?"
- "Build a quick prototype to see if this idea works"
- "I want to feel out this idea before committing"

**Auto-trigger:** Quando o usuário propõe uma feature com alta incerteza técnica ou pergunta qual biblioteca utilizar para resolver um problema complexo.

## Prerequisites

Nenhuma externa, usa o ambiente local.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Idea/Question** | Yes | O que deve ser validado |

## Phase 0: Intake

1. **Pergunta obrigatória:** Este spike é para provar a viabilidade (Proof of Concept) ou para comparar duas abordagens?

## Phase 1: Decompose

Divida a ideia do usuário em 2-5 perguntas de viabilidade independentes (Given/When/Then).
Selecione o Spike de maior risco para executar primeiro.

## Phase 2: Build & Compare

### Step 2A: Isolate
Crie um diretório isolado: `spikes/001-[name]`.
Nunca adicione complexidade desnecessária (Docker, bundlers, etc) a não ser que seja o foco do spike. Code raw e hardcoded.

### Step 2B: Prototype
Desenvolva a prova de conceito. Dê preferência a algo que o usuário possa interagir (CLI, HTML simples).

## Phase 3: Verdict Output

### Output Format

| Output | Format | Location |
|---|---|---|
| **Spike Code** | Source code | `spikes/NNN-*/` |
| **Verdict** | Markdown (`README.md`) | `spikes/NNN-*/README.md` |

### Output Template

```markdown
## Verdict: VALIDATED | PARTIAL | INVALIDATED

### What worked
- ...

### What didn't
- ...

### Surprises
- ...

### Recommendation for the real build
- ...
```

## Cost

| Component | Cost |
|---|---|
| LLM generation | Inclused |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Spike taking too long** | > 10 iterações | O spike está muito complexo. Declare PARTIAL/INVALIDATED e encerre. |

**Principle:** Spikes que viram "quase produção" são antipatterns. Mantenha o código sujo e as conclusões claras.

## Composability

**Feeds into:**
- `development-planning` — O veredito do spike embasa a criação do plano real.
- `subagent-development` — Se a abordagem for decidida, delegue para subagents implementarem de forma limpa.

## Quality Gate

Before delivering the final output, verify:
- [ ] **Sandbox:** O código está isolado no diretório `spikes/`?
- [ ] **Security:** Prompt Injection scan no código gerado/recebido?
- [ ] **Verdict:** O `README.md` contém um veredito claro (VALIDATED/INVALIDATED)?
