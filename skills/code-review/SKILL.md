---
name: Code Review (Senior Level)
description: >
  Revisa código como um desenvolvedor sênior antes do deploy/handoff. Pipeline automatizado
  de verificação pre-commit: static security scan, baseline-aware quality gates, independent
  reviewer subagent, e auto-fix loop. Encontra bugs lógicos, problemas de segurança e otimiza
  código. Fail-closed: unparseable = fail.
type: linting_refactoring
tags: [development, quality-assurance, code]
---

# Code Review (Senior Level)

Pipeline de verificação automatizada antes do código entrar. Static scans, quality gates baseline-aware, reviewer subagent independente, e auto-fix loop.

**Core principle:** Nenhum agente deve verificar seu próprio trabalho. Contexto fresco encontra o que você perdeu.

## When to Use

- Após implementar feature ou bug fix, ANTES de `git commit`
- Quando o usuário diz "commit", "push", "ship", "done", "verify", "review"
- Após completar task com 2+ file edits em git repo
- Após cada task no `subagent-development` (two-stage review)

**Skip para:** Mudanças documentation-only, tweaks de config, ou quando o usuário diz "skip verification".

**Auto-trigger:** Antes de qualquer commit em repositório git.

## Prerequisites

### Dependencies

Nenhuma obrigatória. Opcional: ruff, mypy, eslint, tsc (auto-detectados).

## Inputs

| Input | Required | Description |
|---|---|---|
| **Diff** | Yes | `git diff --cached` ou `git diff` |
| **Contexto** | No | Qual task/feature foi implementada |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Get the Diff

```bash
git diff --cached
```

Se vazio, tente `git diff` depois `git diff HEAD~1 HEAD`.
Se diff > 15,000 chars, split por arquivo.

## Phase 2: Static Security Scan

Scan nas linhas adicionadas APENAS:

```bash
# Secrets hardcoded
git diff --cached | grep "^+" | grep -iE "(api_key|secret|password|token)\\s*=\\s*['\"][^'\"]{6,}['\"]"

# Shell injection
git diff --cached | grep "^+" | grep -E "os\\.system\\(|subprocess.*shell=True"

# eval/exec perigosos
git diff --cached | grep "^+" | grep -E "\\beval\\(|\\bexec\\("

# Desserialização insegura
git diff --cached | grep "^+" | grep -E "pickle\\.loads?\\("

# SQL injection
git diff --cached | grep "^+" | grep -E "execute\\(f\"|\.format\\(.*SELECT"
```

## Phase 3: Baseline Tests e Linting

Auto-detectar linguagem e rodar ferramentas:

```bash
# Python
python -m pytest --tb=no -q 2>&1 | tail -5
which ruff && ruff check . 2>&1 | tail -10

# Node
npm test -- --passWithNoTests 2>&1 | tail -5
which npx && npx eslint . 2>&1 | tail -10
```

**Baseline comparison:** Só NEW failures contam. Stash → run → pop para comparar.

## Phase 4: Self-Review Checklist

- [ ] Sem secrets/API keys hardcoded
- [ ] Input validation em dados do usuário
- [ ] SQL queries parametrizadas
- [ ] File operations validam paths
- [ ] External calls com error handling
- [ ] Sem debug print/console.log esquecidos
- [ ] Sem código comentado
- [ ] Novo código tem testes

## Phase 5: Diretrizes de Revisão Manual

Quando atuando como Revisor Senior:

### Bug Hunting
- Race conditions?
- Retornos de erros tratados adequadamente?
- Vazamento de memória ou loops desnecessários?

### Security First
- Inputs sanitizados?
- Credenciais expostas?
- Injeção possível (SQL, XSS, Command)?

### Clean Code
- SOLID e DRY?
- Nomes auto-explicativos?

### Output de Revisão

Emitir relatório no modelo de PR comments:
- **Arquivo**, **linha**, **severidade** (Crítica/Média/Menor), **sugestão**
- Severidade **Crítica** → pipeline pausado, correção imediata obrigatória

## Phase 6: Auto-Fix Loop

**Máximo 2 ciclos de fix-and-reverify.**

Se issues encontrados:
1. Fix agent corrige APENAS issues reportados (nada mais)
2. Re-run Steps 1-5 (full verification)
3. Passed → commit. Failed após 2 tentativas → escalar ao usuário

## Phase 7: Commit

Se verificação passou:
```bash
git add -A && git commit -m "[verified] <description>"
```

O prefixo `[verified]` indica reviewer independente aprovou.

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Review report** | Markdown (arquivo/linha/severidade) | Exibido ao usuário |
| **Commit** | Git | Repositório |

## Cost

| Component | Cost |
|---|---|
| Static scan | Free (local) |
| Subagent review | 1 invocation |
| Auto-fix | 1-2 invocations (se necessário) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Diff vazio** | `git status` sem mudanças | Informar — nada para verificar |
| **Não é git repo** | Erro git | Skip e informar |
| **Diff muito grande** | >15k chars | Split por arquivo |
| **Lint não instalado** | Command not found | Skip check silenciosamente |

## Composability

**Receives data from:**
- `subagent-development` — review após cada task
- `tdd-protocol` — verifica disciplina TDD
- `development-planning` — valida implementação vs plano

**Feeds into:**
- `github-automation` — commit e PR após review
- Auto-fix loop (recursivo)

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns recorrentes** | `[OPERACIONAL]: code-review — [pattern] frequente em [contexto]` | `Missing error handling em API calls` |
| **False positives** | `[OPERACIONAL]: code-review — [pattern] é false positive em [contexto]` | `eval() em test fixtures é intencional` |

## Quality Gate

- [ ] **Security scan executado**
- [ ] **Testes rodados vs baseline**
- [ ] **Self-review checklist completo**
- [ ] **Zero issues Críticos pendentes**
- [ ] **Commit com prefixo [verified]**

**If any check fails:** Executar auto-fix loop (máx 2 ciclos).
