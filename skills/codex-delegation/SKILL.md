---
name: Codex Delegation
description: Delegação de tarefas de código para o OpenAI Codex CLI via terminal do Conclave.
version: 1.0.0
author: Conclave Architecture
license: MIT
metadata:
  conclave:
    tags: [Coding-Agent, Codex, OpenAI, Delegation, PTY]
    related_skills: [claude-code-delegation, claude-collaboration]
---

# Skill: Codex Delegation

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Delega tarefas de código rápidas (features, PR reviews) para o [Codex CLI](https://github.com/openai/codex) da OpenAI via terminal do Conclave. 


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

## When to Use

Use esta skill quando precisar delegar tarefas curtas ou revisões rápidas de PR para a engine do Codex em background. O Codex opera obrigatoriamente dentro de repositórios git.

**Auto-trigger:** Quando o usuário solicitar uma automação de código explicitamente orientada à "Codex" ou delegar PR reviews em massa.

## ⚠️ City Limits & Security Rules

1. **PROMPT INJECTION CHECK:** Sanitize a string de prompt que será enviada via comando Codex CLI para evitar escape de aspas ou execução de comandos não intencionais.
2. **CITY LIMITS:** O workdir da execução deve sempre ser limitado aos diretórios de projetos permitidos pelo Conclave (`/Users/douglasdepaulamoura/Documents/Bancada/`).
3. O Codex não deve ser executado com `--yolo` em código de produção não revisado, a menos que especificado.

## Modo de Execução

### One-Shot (Tasks)
Para tarefas únicas:

```bash
# O Codex necessita de PTY ativado.
codex exec 'Adicionar dark mode toggle para settings'
```

### Background & Worktrees (Parallel)
Ideal para correção de múltiplos issues em paralelo:

```bash
# Criar worktree temporária
git worktree add -b fix/issue-78 /tmp/issue-78 main

# Rodar no background
# (Execute a ferramenta de terminal com background=true, pty=true)
codex --full-auto exec 'Fix issue #78: descricao. Commit ao final.'

# Limpeza após push
git worktree remove /tmp/issue-78
```

## Inputs e Parâmetros

| Flag | Efeito |
|---|---|
| `exec "prompt"` | Execução One-shot |
| `--full-auto` | Sandboxed mas aprova automaticamente as mudanças nos arquivos |
| `--yolo` | Sem sandbox, permissões totais (MAIOR RISCO) |

## Memory & Learning

Persistir no `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Melhorias de Pipeline** | `[OPERACIONAL]: codex-delegation — [insight]` | `[OPERACIONAL]: codex-delegation — Sempre garanta git init em diretórios temporários, codex recusa executar sem git repo.` |

## Quality Gate

Antes de finalizar:
- [ ] **Segurança Validada:** Inputs sanitizados e worktrees/repositórios dentro dos limites.
- [ ] **PTY Empregado:** Confirme que `pty=true` foi ativado no comando de terminal.
- [ ] **Limpeza de Arquivos:** Remoção de worktrees ou dirties temporários.
- [ ] **Feedback ao Usuário:** Resumo de sucesso/falha e links para PRs criados.
