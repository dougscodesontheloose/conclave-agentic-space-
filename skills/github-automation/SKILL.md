---
name: github-automation
description: >
  Automação completa do GitHub via gh CLI e REST API. Issues (criar, triar, labelar, fechar),
  PRs (branch, commit, open, CI, merge), code review, e operações em batch.
  Funciona com gh CLI ou curl fallback.
type: tool_orchestration
tags: [development, automation, collaboration]
---

# GitHub Automation

Gerencie o ciclo completo de desenvolvimento no GitHub: issues, PRs, CI/CD, e code review.

**Core principle:** `gh` CLI quando disponível, `curl` + REST API como fallback universal.

## When to Use

- "Crie um issue para [bug/feature]"
- "Abra um PR com estas mudanças"
- "Verifique o status do CI"
- "Faça merge do PR"
- "Trie os issues abertos"
- Qualquer operação de project management no GitHub

**Auto-trigger:** Quando o contexto envolve repositórios GitHub e operações de desenvolvimento.

## Prerequisites

### Dependencies

```bash
# Preferido: gh CLI
brew install gh && gh auth login

# Fallback: GITHUB_TOKEN como variável de ambiente
export GITHUB_TOKEN="ghp_..."
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Ação** | Yes | issues/pr/ci/merge/triage |
| **Repo** | No | Inferido do git remote |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Issues

### Listar / Buscar

```bash
gh issue list                              # Abertos
gh issue list --state open --label "bug"   # Por label
gh issue list --search "auth error"        # Busca
gh issue view 42                           # Detalhe
```

### Criar

```bash
gh issue create \
  --title "Login redirect ignores ?next=" \
  --body "## Bug\nRedirect always goes to /dashboard.\n\nCloses #42" \
  --label "bug,backend" \
  --assignee "username"
```

### Gerenciar

```bash
gh issue edit 42 --add-label "priority:high"
gh issue edit 42 --add-assignee @me
gh issue comment 42 --body "Root cause found. Fix incoming."
gh issue close 42
```

## Phase 2: Pull Requests

### Workflow Completo

```bash
# 1. Branch
git checkout main && git pull origin main
git checkout -b feat/add-auth

# 2. Commit (Conventional Commits)
git add src/ tests/
git commit -m "feat: add JWT authentication"

# 3. Push
git push -u origin HEAD

# 4. Create PR
gh pr create \
  --title "feat: add JWT authentication" \
  --body "## Summary\nAdds login/register endpoints.\n\nCloses #42"

# 5. Monitor CI
gh pr checks --watch

# 6. Merge
gh pr merge --squash --delete-branch
```

### Naming Conventions

- `feat/description` — features
- `fix/description` — bug fixes
- `refactor/description` — reestruturação
- `docs/description` — documentação

### Commit Messages (Conventional)

```
type(scope): short description

Longer explanation. Wrap at 72.
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `ci`, `chore`, `perf`

## Phase 3: CI/CD

```bash
gh pr checks                                    # Status
gh run list --branch $(git branch --show-current) # Runs
gh run view <RUN_ID> --log-failed               # Logs de falha
```

### Auto-Fix Loop

1. Check CI → identificar falhas
2. Ler logs → entender erro
3. Fix → commit → push
4. Re-check (máx 3 tentativas, depois perguntar)

## Phase 4: Triage

1. `gh issue list --label "needs-triage" --state open`
2. Ler e categorizar cada issue
3. Aplicar labels e prioridade
4. Atribuir se responsável claro
5. Comentar com notas de triage

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Issue/PR criado** | URL | Terminal |
| **CI status** | Tabela | Terminal |

## Cost

| Component | Cost |
|---|---|
| GitHub API | Free (rate limited) |
| gh CLI | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Auth falha** | 401 | `gh auth login` ou verificar GITHUB_TOKEN |
| **CI falha** | Checks fail | Auto-fix loop (máx 3 tentativas) |
| **Rate limit** | 403 | Aguardar reset (header X-RateLimit-Reset) |

## Composability

**Receives data from:**
- `development-planning` — plano gera branches e PRs
- `webhook-manager` — eventos GitHub triggerando ações

**Feeds into:**
- `code-review` — PR aberto dispara review
- `tdd-protocol` — issues geram testes

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Repos** | `[OPERACIONAL]: github-automation — Repo [X] usa [branch strategy]` | `main-based, squash merge` |
| **Labels** | `[OPERACIONAL]: github-automation — Labels padrão: [X]` | `bug, enhancement, priority:high` |

## Quality Gate

- [ ] **Auth funcional** (gh ou token)
- [ ] **Branch naming seguindo convenção**
- [ ] **Commit messages no formato Conventional**
- [ ] **CI verde antes de merge**

**If any check fails:** Corrigir antes de prosseguir.
