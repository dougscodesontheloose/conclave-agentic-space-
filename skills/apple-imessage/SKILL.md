---
name: apple-imessage
description: >
  Envie e receba iMessages/SMS via CLI imsg no macOS. Leia histórico de conversas,
  envie mensagens com anexos, e monitore novos recebimentos.
type: tool_orchestration
tags: [system, automation, outreach]
---

# Apple iMessage

Leia e envie iMessage/SMS via macOS Messages.app usando `imsg`.

**Core principle:** Sempre confirme destinatário e conteúdo antes de enviar.

## When to Use

- "Envie uma mensagem para [X]"
- "Leia minhas mensagens recentes"
- "Verifique conversas do iMessage"

**Auto-trigger:** Quando o usuário menciona "iMessage", "mensagem de texto", ou "SMS".

## Prerequisites

### Dependencies

```bash
brew install steipete/tap/imsg
# Conceder Full Disk Access ao terminal (System Settings → Privacy)
# Conceder permissão de Automation ao Messages.app
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Ação** | Yes | send/chats/history/watch |
| **Destinatário** | Yes (para send) | Número ou Apple ID |
| **Mensagem** | Yes (para send) | Texto a enviar |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Operações

### Listar Conversas

```bash
imsg chats --limit 10 --json
```

### Ver Histórico

```bash
imsg history --chat-id 1 --limit 20 --json
```

### Enviar

```bash
imsg send --to "+14155551212" --text "Hello!"
imsg send --to "+14155551212" --text "Check this" --file /path/to/image.jpg
```

### Monitorar

```bash
imsg watch --chat-id 1 --attachments
```

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Conversas** | JSON | Terminal |
| **Confirmação envio** | Texto | Terminal |

## Cost

| Component | Cost |
|---|---|
| imsg | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Sem permissão** | Erro de acesso | Conceder Full Disk Access |
| **Destinatário inválido** | Erro no envio | Verificar número/Apple ID |

## Composability

**Receives data from:**
- Workflows de outreach que precisam de canal iMessage

**Feeds into:**
- Comunicação direta com contatos

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Contatos** | `[OPERACIONAL]: apple-imessage — [contato] = [número]` | `Mom = +1555123456` |

## Quality Gate

- [ ] **Confirmar destinatário antes de enviar**
- [ ] **Nunca enviar a números desconhecidos sem aprovação**
- [ ] **Verificar paths de anexos**
- [ ] **Não spammar**

**If any check fails:** Parar e confirmar com usuário.
