---
name: subagent-development
description: >
  Execução de planos via subagents frescos por task com review de spec compliance e code quality
  em duas fases. Fresh context por task evita poluição. Catch issues early.
type: orchestration
tags: [development, orchestration, automation]
---

# Subagent-Driven Development

Execute planos de implementação despachando subagents frescos por task com revisão sistemática em duas fases.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = alta qualidade, iteração rápida.

## When to Use

- "Execute este plano de implementação"
- "Implemente estas tasks em paralelo"
- Quando existe um plano (do `development-planning`) com tasks independentes
- Quando qualidade e conformidade com spec são importantes

**Auto-trigger:** Quando um plano de implementação é aprovado e pronto para execução.

## Prerequisites

### Dependencies

Nenhuma. Pure orchestration skill — usa capacidades nativas do sistema.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Plano de implementação** | Yes | Arquivo markdown com tasks numeradas |
| **Contexto do projeto** | Yes | Stack, estrutura, convenções |

## Phase 0: Intake

1. **Onde está o plano?** — caminho do arquivo ou conteúdo direto
2. **Qual a stack do projeto?** — linguagem, framework, test runner

## Phase 1: Parse do Plano

Leia o plano COMPLETO. Extraia TODAS as tasks com texto e contexto. Crie todo list.

**Key:** Leia o plano UMA VEZ. Não faça subagents lerem o plano — forneça texto completo no contexto.

## Phase 2: Execução Por Task

Para CADA task:

### Step 2A: Dispatch Implementador

Subagent fresco com contexto completo:
- Task text completo do plano
- Instruções TDD (se aplicável)
- Contexto do projeto (stack, paths, convenções)

### Step 2B: Spec Compliance Review

Após implementação, verificar contra spec original:
- Todos os requisitos implementados?
- File paths corretos?
- Comportamento esperado?
- Nada extra adicionado (scope creep)?

**Se issues encontrados:** Fix → re-review. Só prosseguir quando PASS.

### Step 2C: Code Quality Review

Após spec compliance PASS:
- Segue convenções do projeto?
- Error handling adequado?
- Nomes claros?
- Cobertura de testes adequada?
- Sem bugs óbvios ou security issues?

**Se issues encontrados:** Fix → re-review. Só prosseguir quando APPROVED.

### Step 2D: Mark Complete

Atualizar task tracker.

## Phase 3: Integração Final

Após TODAS as tasks:
- Review de integração (componentes funcionam juntos?)
- Suite de testes completa
- Commit final

## Red Flags — Nunca Faça

- Iniciar sem plano
- Pular reviews (spec OU quality)
- Prosseguir com issues não resolvidos
- Despachar subagents para tasks que tocam os mesmos arquivos
- Fazer subagent ler o plano (forneça texto no contexto)
- Aceitar "close enough" em spec compliance
- Iniciar quality review ANTES de spec compliance PASS

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Código implementado** | Arquivos do projeto | Diretórios do projeto |
| **Testes** | Arquivos de teste | `tests/` |
| **Status de cada task** | Todo list | Task tracker |

## Cost

| Component | Cost |
|---|---|
| Subagent invocations | 3 por task (impl + spec + quality) |
| Trade-off | Mais invocações, mas issues early |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Subagent falha** | Task não completa | Novo subagent com instruções sobre o que falhou |
| **Spec não atendida** | Review FAIL | Fix → re-review |
| **Quality issue** | Review REQUEST_CHANGES | Fix → re-review |

## Composability

**Receives data from:**
- `development-planning` — plano com tasks para executar

**Feeds into:**
- `tdd-protocol` — implementadores seguem TDD
- `code-review` — review final de integração

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Task patterns** | `[OPERACIONAL]: subagent-development — [insight]` | `Tasks de 2-5 min funcionam melhor` |
| **Review patterns** | `[OPERACIONAL]: subagent-development — [insight]` | `Spec review antes de quality review evita retrabalho` |

## Quality Gate

- [ ] **Todas as tasks completas**
- [ ] **Spec compliance PASS em todas**
- [ ] **Code quality APPROVED em todas**
- [ ] **Suite de testes verde**
- [ ] **User checkpoint:** Apresentar status final

**If any check fails:** Identificar tasks com issues e re-executar o ciclo.
