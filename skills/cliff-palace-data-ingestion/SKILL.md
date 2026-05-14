---
name: cliff-palace-data-ingestion
description: >
  Pipeline especializado em ingestão, conversão (YAML -> JSON) e categorização automatizada de 
  dados financeiros do Cliff Palace usando scripts Python locais.
type: tool_orchestration
tags: [data, analytics, finance, automation, core]
---

# Cliff Palace Data Ingestion

Transforma extratos e orçamentos brutos em formato consumível pelo dashboard financeiro.

**Core principle:** Nenhum dado financeiro sai da máquina; a ingestão deve ser auditável, idempotente e cega para a internet.

## When to Use

- "Rodar ingestão de dados do Cliff Palace"
- "Atualize os dados financeiros no dashboard"
- "Converta os YAMLs financeiros para o JSON final"
- Sempre que houver atualização manual nos arquivos `_data/*.yaml` ou requisição para rodar `ingest.py`.

**Auto-trigger:** O sistema deve carregar este skill automaticamente durante a Step 1 do pipeline do squad `cliff_palace`.

## Prerequisites

### Dependencies
```bash
# Na pasta Projetos/Cliff Palace Agent
pip install -r requirements.txt
# Ou garantir que pyyaml está disponível.
```

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Workspace** | Yes | O path base do Cliff Palace Agent |
| **Ação** | Yes | `ingest` (YAML->JSON) ou `categorize` (categorizador unitário) |

## Phase 0: Intake

1. **Qual script deseja executar?** — `ingest.py` (processamento em batch) ou `main.py` (categorização de transação única)?

> **Regra:** Em execução autônoma pelo Senior Data Analyst, inferir a execução de `ingest.py`.

## Phase 1: Ingestion Batch (YAML to JSON)

### Step 1A: Execução do script
Rodar o script Python para mesclar e transformar os dados locais:
```bash
cd "Projetos/Cliff Palace Agent"
python3 ingest.py
```

### Step 1B: Verificação de Output
Verificar se `dashboard/dados.json` foi atualizado. O script imprime os metadados gerados.

## Phase 2: Transaction Categorization (Optional)

Caso o usuário queira categorizar uma despesa única e inserir no orçamento:
```bash
cd "Projetos/Cliff Palace Agent"
python3 main.py "[Descrição da Despesa]"
```

## Phase N: Output

### Output Format

| Output | Format | Location |
| --- | --- | --- |
| **Base Central** | JSON | `dashboard/dados.json` |
| **Resumo** | Log | Exibido no terminal / output de agente |

## Cost

| Component | Cost |
| --- | --- |
| Script local | Free |
| LLM reasoning | Free (local context) |

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **YAML Inválido** | `yaml.scanner.ScannerError` | Identificar a linha do erro no YAML e consertar a formatação (indentação, aspas) |
| **Arquivo não encontrado** | `FileNotFoundError` | Confirmar que o diretório `_data` tem os YAMLs esperados (`extratos-nubank-conta.yaml`, etc) |

**Principle:** Fail fast and fail loud. Um dado corrompido é pior que um dashboard desatualizado.

## Composability

**Receives data from:**
- YAMLs estruturados criados/modificados manualmente no diretório `_data/`.

**Feeds into:**
- `Senior Data Scientist` — para busca de padrões e anomalias baseadas no JSON/YAML validado.
- `Senior Data Analyst` — para geração do diagnóstico.
- `Wade Web` — para montar o dashboard HTML que consome o JSON.

**Integration pattern:** Step 1 do squad `cliff_palace`.

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
| --- | --- | --- |
| **Key findings** | `[OPERACIONAL]: cliff-palace-ingest — [finding]` | `[OPERACIONAL]: cliff-palace-ingest — Faltam dados no YAML de Março de 2026.` |
| **Strategic insights** | `[ESTRATÉGICO]: cliff-palace-ingest — [insight]` | `[ESTRATÉGICO]: cliff-palace-ingest — A categoria 'Lazer' ultrapassou a média anual em 22%.` |

## Quality Gate

Before delivering the final output, verify:

- [ ] **Execução sem erros:** O script retornou exit code 0.
- [ ] **Timestamp:** O campo `meta.gerado_em` no `dados.json` foi atualizado para hoje.
- [ ] **Tamanho do arquivo:** `dados.json` não está vazio.

**If any check fails:** Pare a execução do squad e alerte o usuário.
