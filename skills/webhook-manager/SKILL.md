---
name: webhook-manager
description: >
  Crie e gerencie webhooks event-driven para que serviços externos (GitHub, Stripe, CI/CD)
  possam triggerar execuções do agente via HTTP POST. Suporte a templates com dot-notation
  e autenticação HMAC-SHA256.
type: tool_orchestration
tags: [automation, development, orchestration]
---

# Webhook Manager

Configure webhooks para que serviços externos disparem ações automaticamente via HTTP POST.

**Core principle:** Event-driven > polling. Webhooks transformam serviços passivos em triggers ativos.

## When to Use

- "Configure um webhook para [serviço]"
- "Quero receber notificações quando [evento]"
- "Automatize respostas a eventos do GitHub/Stripe/CI"

**Auto-trigger:** Quando o usuário quer automação baseada em eventos externos.

## Prerequisites

### Dependencies

Gateway webhook habilitado no sistema. Verificar com verificação de plataforma local.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Serviço** | Yes | GitHub, Stripe, CI/CD, etc. |
| **Evento(s)** | Yes | issues, payment_intent.succeeded, etc. |
| **Template** | Recommended | Prompt com `{payload.fields}` |
| **Destino** | No | telegram, discord, slack, log |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Configuração

### Padrão de Template

Templates suportam `{dot.notation}` para acessar campos do payload:
- `{issue.title}` — título do issue GitHub
- `{pull_request.user.login}` — autor do PR
- `{data.object.amount}` — valor Stripe

### Exemplos Comuns

**GitHub Issues:**
```
New issue #{issue.number}: {issue.title}
Author: {issue.user.login}
Body: {issue.body}
```

**Stripe Payments:**
```
Payment {data.object.status}: {data.object.amount} cents
```

**CI/CD Builds:**
```
Build {object_attributes.status} on {project.name}
Branch: {object_attributes.ref}
```

## Phase 2: Segurança

- Cada webhook recebe HMAC-SHA256 secret auto-gerado
- Validação de assinatura em cada POST
- Bind sempre a `127.0.0.1` (nunca `0.0.0.0` em rede pública)
- Para dev local, usar tunnel (ngrok, cloudflared)

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Webhook URL** | URL | Exibido ao usuário |
| **Secret** | String | Exibido uma vez |
| **Config** | JSON | Persistido |

## Cost

| Component | Cost |
|---|---|
| Webhook server | Free (local) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Gateway offline** | Health check falha | Reiniciar gateway |
| **Signature mismatch** | 401 no POST | Verificar secret |
| **Port em uso** | Bind error | Trocar porta |

## Composability

**Receives data from:**
- Serviços externos (GitHub, Stripe, CI/CD)

**Feeds into:**
- Pipelines de automação do Conclave
- Notificações em canais de comunicação

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Webhooks ativos** | `[OPERACIONAL]: webhook-manager — [nome] → [evento]` | `github-issues → issues events` |

## Quality Gate

- [ ] **Health check positivo**
- [ ] **Secret armazenado de forma segura**
- [ ] **Template testado com payload de exemplo**

**If any check fails:** Debug via logs do gateway.
