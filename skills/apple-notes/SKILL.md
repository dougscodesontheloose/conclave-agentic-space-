---
name: Apple Notes Integration
description: >
  Sincronização de notas, briefings e planos com o app nativo Notas da Apple via CLI memo.
  Crie, busque, edite, exporte e organize notas que sincronizam com todos os dispositivos Apple via iCloud.
type: tool_orchestration
tags: [system, integration, notes]
---

# Apple Notes Integration

Gerencie Apple Notes diretamente do terminal via `memo`. Notas sincronizam com iPhone/iPad via iCloud.

**Core principle:** Apple Notes é o repositório cross-device. Use para informação que precisa chegar ao telefone.

## When to Use

- "Salve esta nota"
- "Busque nas minhas notas sobre [X]"
- "Crie um briefing no Notas"
- Salvar briefings, registrar decisões de squads, buscar informações históricas
- Qualquer menção a "Notas", "Apple Notes", ou "anotar"

**Auto-trigger:** Quando o usuário menciona "notas", "Notas app", ou pede para salvar informação cross-device.

**Quando NÃO usar:**
- Notas internas do agente → use `memory` tool
- Knowledge management → use Obsidian
- Alertas programados → use cronjob

## Prerequisites

### Dependencies

```bash
brew tap antoniorodr/memo && brew install antoniorodr/memo/memo
# Conceder permissão de Automação ao Notes.app quando solicitado
# (System Settings → Privacy → Automation)
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Ação** | Yes | notes/list/search/edit/export |
| **Título/Query** | Yes (para criar/buscar) | Título da nota ou termo de busca |
| **Conteúdo** | Yes (para criar) | Texto da nota (Markdown suportado) |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Operações

### Ver Notas

```bash
memo notes                        # Listar todas
memo notes -f "Folder Name"       # Filtrar por pasta
memo notes -s "query"             # Buscar (fuzzy search)
```

### Criar/Editar Notas

```bash
memo notes -a                     # Editor interativo
memo notes -a "Note Title"        # Criação rápida com título
memo notes -e                     # Editar (seleção interativa)
```

### Deletar / Mover

```bash
memo notes -d                     # Deletar (seleção interativa)
memo notes -m                     # Mover para pasta (interativo)
```

### Exportar

```bash
memo notes -ex                    # Exportar para HTML/Markdown
```

## Phase 2: Ações do Conclave

### Criar/Atualizar Briefing

Sempre que um squad finalizar um plano estratégico:
```bash
memo edit "CONCLAVE: [Nome do Squad] - Briefing"
```

### Buscar Contexto Pessoal

Se a tarefa envolver informações que o usuário mencionou ter "anotado":
```bash
memo list | grep -i "[Keyword]"
memo cat "[Titulo]"
```

### Registro de Insights Rápidos

Durante execução, insights que não pertencem ao output direto:
```bash
memo edit "CONCLAVE: Scrapbook/Insights"
```

## Regras de Ouro

- **Privacidade (SafeGuard):** Nunca salve dados SECRET (senhas, CPFs) no Notas
- **Prefixos:** Use sempre `CONCLAVE:` para organização
- **Formatação:** Mantenha a elegância do Markdown

> [!IMPORTANT]
> Se `memo` falhar com erro de permissão, o usuário precisa autorizar "Automação" em
> **Ajustes do Sistema > Privacidade e Segurança > Automação**.

## Limitações

- Não edita notas com imagens/anexos
- Prompts interativos requerem acesso ao terminal
- macOS only

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Lista de notas** | Texto/JSON | Terminal |
| **Conteúdo da nota** | Markdown | Terminal |
| **Export** | HTML/MD | Arquivo |

## Cost

| Component | Cost |
|---|---|
| memo CLI | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Sem permissão** | Erro de automação | Autorizar em System Settings |
| **memo não instalado** | Command not found | `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo` |
| **Nota com anexos** | Erro de edição | Informar limitação ao usuário |

## Composability

**Receives data from:**
- Squads do Conclave — briefings e decisões

**Feeds into:**
- `apple-reminders` — notas geram lembretes
- Workflow de produtividade pessoal

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Pastas úteis** | `[OPERACIONAL]: apple-notes — Pasta [X] para [contexto]` | `Pasta "CONCLAVE: Marketing" para briefings` |
| **Notas-chave** | `[OPERACIONAL]: apple-notes — Nota [X] contém [info]` | `Nota "Brand Guidelines" contém paleta de cores` |

## Quality Gate

- [ ] **Confirmar título e conteúdo antes de criar**
- [ ] **Usar prefixo CONCLAVE: para notas do sistema**
- [ ] **Nunca salvar dados SECRET sem aprovação**
- [ ] **Verificar se nota foi criada/atualizada com sucesso**

**If any check fails:** Confirmar com usuário antes de prosseguir.
