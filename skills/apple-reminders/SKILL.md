---
name: apple-reminders
description: >
  Gerencie Apple Reminders via remindctl no terminal. Crie, liste, complete e delete lembretes
  que sincronizam com todos os dispositivos Apple via iCloud.
type: tool_orchestration
tags: [system, automation, productivity]
---

# Apple Reminders

Gerencie Apple Reminders diretamente do terminal via `remindctl`. Sincroniza com iPhone/iPad via iCloud.

**Core principle:** Reminders são para tarefas pessoais com due dates que sincronizam ao telefone.

## When to Use

- "Crie um lembrete para [X]"
- "Quais meus lembretes de hoje?"
- "Complete o lembrete [X]"
- Qualquer menção a "reminder" ou "Reminders app"

**Auto-trigger:** Quando o usuário menciona "lembrete", "reminder", ou "Reminders app".

**Quando NÃO usar:**
- Alertas do agente → use cronjob
- Eventos de calendário → use Calendar
- Project management → use GitHub Issues

## Prerequisites

### Dependencies

```bash
brew install steipete/tap/remindctl
# Conceder permissão ao Reminders quando solicitado
remindctl status   # verificar
remindctl authorize  # se necessário
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Ação** | Yes | add/list/complete/delete |
| **Título** | Yes (para add) | Texto do lembrete |
| **Due date** | No | today/tomorrow/YYYY-MM-DD |
| **Lista** | No | Nome da lista (default: padrão) |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Operações

### Ver Lembretes

```bash
remindctl              # Hoje
remindctl today        # Hoje
remindctl tomorrow     # Amanhã
remindctl week         # Esta semana
remindctl overdue      # Atrasados
remindctl all          # Tudo
```

### Gerenciar Listas

```bash
remindctl list               # Listar todas
remindctl list Work          # Ver lista específica
remindctl list Projects --create   # Criar lista
```

### Criar Lembretes

```bash
remindctl add "Buy milk"
remindctl add --title "Call mom" --list Personal --due tomorrow
remindctl add --title "Meeting prep" --due "2026-02-15 09:00"
```

### Completar / Deletar

```bash
remindctl complete 1 2 3       # Completar por ID
remindctl delete 4A83 --force  # Deletar por ID
```

### Output Formats

```bash
remindctl today --json    # JSON para scripting
remindctl today --plain   # TSV
remindctl today --quiet   # Só contagens
```

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Lista de lembretes** | Tabela/JSON | Terminal |
| **Confirmação** | Texto | Terminal |

## Cost

| Component | Cost |
|---|---|
| remindctl | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Sem permissão** | Erro de acesso | `remindctl authorize` |
| **remindctl não instalado** | Command not found | `brew install steipete/tap/remindctl` |

## Composability

**Receives data from:**
- `apple-notes` — notas que geram lembretes

**Feeds into:**
- Workflow de produtividade pessoal

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Listas usadas** | `[OPERACIONAL]: apple-reminders — Lista [X] para [contexto]` | `Lista "Work" para tarefas profissionais` |

## Quality Gate

- [ ] **Confirmar conteúdo e data antes de criar**
- [ ] **Disambiguar:** Reminder (Apple) vs alert (agente)
- [ ] **Usar --json para parsing programático**

**If any check fails:** Confirmar com usuário antes de prosseguir.
