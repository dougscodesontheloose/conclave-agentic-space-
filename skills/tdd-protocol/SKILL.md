---
name: tdd-protocol
description: >
  Protocolo rigoroso de Test-Driven Development: RED-GREEN-REFACTOR. Enforce testes antes do código,
  verificação de falha antes da implementação, e minimal code to pass.
type: playbook
tags: [development, quality-assurance, code]
---

# TDD Protocol

Escreva o teste primeiro. Veja-o falhar. Escreva código mínimo para passar.

**Core principle:** Se você não viu o teste falhar, você não sabe se ele testa a coisa certa.

## When to Use

- "Implemente [feature] com TDD"
- "Crie testes para [funcionalidade]"
- Qualquer implementação de features, bug fixes, ou refactoring

**Auto-trigger:** Sempre que um agente implementador receber tarefa de código.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill. Funciona com qualquer test runner (pytest, vitest, jest).

## Inputs

| Input | Required | Description |
|---|---|---|
| **Feature/Bug** | Yes | O que implementar ou corrigir |
| **Stack do projeto** | Recommended | Linguagem, framework, test runner |

## Phase 0: Intake

1. **O que precisa ser implementado?** — obrigatório
2. **Qual o test runner do projeto?** — pode ser inferido

## The Iron Law

```
NENHUM CÓDIGO DE PRODUÇÃO SEM UM TESTE FALHANDO PRIMEIRO
```

Escreveu código antes do teste? Delete. Comece de novo. Sem exceções.

## Phase 1: RED — Teste Falhando

Escreva UM teste mínimo por comportamento. Nome claro e descritivo.

```bash
pytest tests/test_feature.py::test_specific_behavior -v
```

Confirme: teste FALHA porque a feature não existe.

## Phase 2: GREEN — Código Mínimo

Escreva o código mais simples para passar. Cheating OK (hardcode, copy-paste). Verificar que suite completa passa.

```bash
pytest tests/ -q
```

## Phase 3: REFACTOR — Limpeza

Remover duplicação, melhorar nomes, extrair helpers. Manter testes verdes.

## Phase 4: Repeat

Próximo teste falhando para o próximo comportamento.

## Red Flags — PARE e Recomece

- Código antes do teste → Delete e recomece
- Teste passa imediatamente → Corrija o teste
- Racionalização de "só desta vez" → Pare

## Common Rationalizations

| Desculpa | Realidade |
|---|---|
| "Simples demais para testar" | Código simples quebra. |
| "Testo depois" | Testes que passam imediatamente não provam nada. |
| "TDD me atrasa" | TDD é mais rápido que debugging. |

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Código + Testes** | Arquivos do projeto | Diretórios do projeto |
| **Resultado** | Terminal output | Exibido ao usuário |

## Cost

| Component | Cost |
|---|---|
| Execução local | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Teste não falha no RED** | Passa imediatamente | Corrigir teste |
| **Regressão** | Outros testes falham | Corrigir antes de prosseguir |

## Composability

**Receives data from:**
- `development-planning` — plano com tasks para implementação TDD
- `subagent-development` — subagents recebem instrução TDD

**Feeds into:**
- `systematic-debugging` — bug → teste que reproduz → correção
- `code-review` — testes como documentação

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Test runner** | `[OPERACIONAL]: tdd-protocol — Projeto usa [runner]` | `Projeto usa pytest -q` |
| **Patterns** | `[OPERACIONAL]: tdd-protocol — [pattern] para [contexto]` | `Fixtures em conftest.py` |

## Quality Gate

- [ ] **Cada função tem teste**
- [ ] **Cada teste falhou primeiro**
- [ ] **Suite completa verde**
- [ ] **Output limpo**

**If any check fails:** Voltar ao ciclo RED-GREEN-REFACTOR.
