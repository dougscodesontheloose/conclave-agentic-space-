---
name: development-planning
description: >
  Escreva planos de implementação completos com tasks bite-sized (2-5 min cada),
  file paths exatos, código copy-pasteable, e comandos de verificação. DRY. YAGNI. TDD.
  Assume que o implementador tem zero contexto do codebase.
type: playbook
tags: [development, strategy, decision-making]
---

# Development Planning

Escreva planos de implementação que tornam a execução óbvia. Se alguém precisa adivinhar, o plano está incompleto.

**Core principle:** Um bom plano torna a implementação óbvia.

## When to Use

- "Planeje a implementação de [feature]"
- "Quebre este requisito em tasks"
- Antes de implementar features multi-step
- Antes de delegar para subagents via `subagent-development`

**Auto-trigger:** Quando o usuário descreve uma feature complexa que requer múltiplos passos.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Requisitos** | Yes | O que precisa ser construído |
| **Contexto do projeto** | Recommended | Stack, estrutura, convenções |

## Phase 0: Intake

1. **O que precisa ser construído?** — obrigatório
2. **Qual a stack do projeto?** — pode ser inferido
3. **Existem restrições ou convenções?** — opcional

## Phase 1: Entender Requisitos

Leia e compreenda: requirements, design docs, acceptance criteria, constraints.

## Phase 2: Explorar o Codebase

Entenda o projeto antes de planejar. Busque patterns similares, testes existentes, arquivos-chave.

## Phase 3: Escrever o Plano

### Header (obrigatório)

```markdown
# [Feature Name] Implementation Plan

**Goal:** [Uma frase descrevendo o que será construído]
**Architecture:** [2-3 frases sobre a abordagem]
**Tech Stack:** [Tecnologias/libraries chave]
```

### Task Structure

Cada task = 2-5 minutos de trabalho focado.

```markdown
### Task N: [Nome Descritivo]

**Objective:** O que esta task realiza (uma frase)

**Files:**
- Create: `exact/path/to/new_file.py`
- Modify: `exact/path/to/existing.py:45-67`
- Test: `tests/path/to/test_file.py`

**Step 1: Write failing test**
[código completo]

**Step 2: Run test to verify failure**
Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL

**Step 3: Write minimal implementation**
[código completo]

**Step 4: Verify pass**
Run: `pytest tests/ -q`
Expected: PASS

**Step 5: Commit**
`git add ... && git commit -m "feat: ..."`
```

### Princípios

- **DRY:** Não repita. Extraia funções reutilizáveis.
- **YAGNI:** Implemente apenas o necessário agora.
- **TDD:** Teste primeiro para cada task com código.
- **Commits frequentes:** Após cada task.

### Anti-Patterns a Evitar

| Anti-Pattern | Correção |
|---|---|
| Tasks vagas ("Add auth") | Tasks específicas ("Create User model with email field") |
| Código incompleto | Código copy-pasteable completo |
| Sem verificação | Comandos exatos com output esperado |
| Sem file paths | Paths exatos (`src/models/user.py`) |

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Plano** | Markdown | Arquivo no projeto |

## Cost

| Component | Cost |
|---|---|
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Plano incompleto** | Reviewer encontra gaps | Adicionar detalhes faltantes |
| **Tasks muito grandes** | >5 min estimado | Dividir em sub-tasks |

## Composability

**Receives data from:**
- Requisitos do usuário
- Contexto do projeto

**Feeds into:**
- `subagent-development` — plano é executado task por task
- `tdd-protocol` — cada task segue ciclo TDD

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns** | `[OPERACIONAL]: development-planning — [insight]` | `Tasks de 2-5 min otimizam throughput` |

## Quality Gate

- [ ] **Tasks sequenciais e lógicas**
- [ ] **Cada task bite-sized (2-5 min)**
- [ ] **File paths exatos**
- [ ] **Código copy-pasteable**
- [ ] **Comandos com output esperado**
- [ ] **Sem contexto faltante**

**If any check fails:** Revisar e completar o plano.
