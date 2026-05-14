---
name: data-toolkit
description: Conjunto de utilitários rápidos para manipulação e exploração de dados — CSV profiling, SQL formatting, data cleaning e cálculo de métricas de marketing.
type: tool_orchestration
tags: [system, data, analytics]
---

# Skill: Data Toolkit

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


## Descrição
Um conjunto de utilitários rápidos para manipulação e exploração de dados, focado em acelerar o trabalho de análise exploratória e saneamento.

## Capacidades
- **CSV Explorer:** Leitura e resumo estatístico rápido de arquivos CSV.
- **SQL Formatter:** Formatação de queries SQL para legibilidade.
- **Data Cleaner:** Script base para remoção de nulos, duplicatas e padronização de tipos.
- **Marketing Metrics Calculator:** Funções para cálculo rápido de ROAS, CAC, e Atribuição básica.

## Instruções de Uso
Sempre que o usuário fornecer um arquivo de dados (CSV, JSON, Excel) para análise, utilize esta skill para realizar o profiling inicial.

### Estrutura de Scripts (Internal)
- `scripts/profile.py`: Gera um relatório de saúde dos dados.
- `scripts/cleaner.py`: Aplica regras de limpeza básicas.

## Princípios
- **Eficiência:** Não carregue datasets massivos na memória sem necessidade (use amostragem se necessário).
- **Segurança:** Nunca exponha dados do `data/` (TIER: SECRET) em saídas públicas.


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use `data-toolkit` when you need to:
- Maintain system health and operational quality
- Apply development best practices
- Support the infrastructure that other skills depend on

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Target scope** | Varies | Files, directories, or codebase to operate on |
| **Configuration** | No | Settings or preferences for the operation |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Status report** | Markdown or terminal | Displayed to user |
| **Changes applied** | Log | Inline in response |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: data-toolkit — [finding]` | `[OPERACIONAL]: data-toolkit — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: data-toolkit — [param] works better as [value]` | `[OPERACIONAL]: data-toolkit — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: data-toolkit — [insight]` | `[ESTRATÉGICO]: data-toolkit — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.

