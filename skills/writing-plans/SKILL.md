---
name: writing-plans
description: >
  Converte documentos de design em planos de execução granulares e verificáveis.
  Focado em tarefas bite-sized (2-5 min) com ciclos TDD integrados.
type: playbook
tags: [development, strategy, planning, superpowers]
---

# Writing Plans (Superpowers Style)

Um plano de execução medíocre leva a código quebrado e confusão. Um plano Superpowers torna a implementação inevitável e óbvia através de tarefas atômicas e verificação constante.

**Core principle:** Um bom plano divide o problema em partes tão pequenas que o erro se torna quase impossível.

## When to Use

- Após um `brainstorming` bem sucedido e um Design Doc aprovado.
- Antes de iniciar qualquer implementação de feature ou refactoring complexo.
- Quando você precisa de uma lista de tarefas clara para seguir ou delegar para subagentes.

**Auto-trigger:** Ativado após a conclusão de um Design Doc ou quando uma tarefa complexa é solicitada.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Design Doc** | Yes | O documento (`DESIGN.md`) com a especificação técnica |
| **Workspace Context** | Recommended | Estrutura de pastas e padrões de teste do projeto |

## Phase 0: Intake

Antes de mapear as tarefas, valide a viabilidade:

1.  **O Design Doc está completo e aprovado?**
2.  **Qual o framework de testes principal?** (Pytest, Jest, Vitest, etc.)
3.  **Existem dependências externas que precisam ser instaladas primeiro?**

## Phase 1: Decomposição Atômica

### Step 1: Mapeamento de Dependências
Identifique a ordem lógica. Comece pela fundação (DB, modelos) e suba para as interfaces.

### Step 2: Quebra em Tasks "Bite-sized"
Cada tarefa deve ser realizável em **2 a 5 minutos**. Se for maior, divida-a.

---

## Phase 2: Estruturação do Plano

Para cada tarefa, defina os componentes de execução:

### Step 2A: Definição de Arquivos e Testes
Liste exatamente quais arquivos serão tocados e qual o comando de teste específico.

### Step 2B: O Loop TDD
Integre os passos: `Test (Red) -> Implementation -> Test (Green)`.

---

## Phase N: Output

### Output Format

| Output | Format | Location |
| --- | --- | --- |
| **Plano de Implementação** | Markdown | `task.md` ou artefato de planejamento |
| **Tasks individuais** | Checklist | Exibido ao usuário |

### Output Template

```markdown
# [Feature] Implementation Plan

## Tasks

### [ ] Task N: [Título]
- **Files**: `path/to/file.py`
- **Test**: `pytest tests/test_feature.py::test_case`
- **Command (Fail)**: [comando]
- **Minimal Code**: [snippet ou descrição]
- **Command (Pass)**: [comando]
```

## Cost

| Component | Cost |
| --- | --- |
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **Task muito grande** | Estimativa > 5 min | Subdividir em 2 ou mais tasks |
| **Falta de contexto de teste** | Não sabe como testar | Rodar `ls tests/` para encontrar padrões antes de planejar |

## Composability

**Receives data from:**
- `brainstorming` — O Design Doc é o input principal.

**Feeds into:**
- `subagent-development` — Executa as tarefas do plano.
- `tdd-protocol` — Enforça o rigor de testes em cada tarefa.

## Memory & Learning

| What to Save | Format | Example |
| --- | --- | --- |
| **Efficiency Metrics** | `[OPERACIONAL]: writing-plans — Tasks de [X] min funcionam melhor` | `Tasks de 3 min reduzem erros de contexto` |
| **Patterns** | `[OPERACIONAL]: writing-plans — Ordem [A -> B] é mais estável` | `DB migrations antes de modelos` |

## Quality Gate

- [ ] Todas as tarefas são atômicas (2-5 min).
- [ ] Cada tarefa inclui passos de verificação claros.
- [ ] O plano cobre 100% do Design Doc.
- [ ] **User checkpoint:** Plano apresentado para aprovação antes da execução.
