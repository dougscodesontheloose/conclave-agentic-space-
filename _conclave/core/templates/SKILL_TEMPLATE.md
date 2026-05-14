---
name: skill-name-here
description: >
  Uma descrição completa em 2-3 linhas que explica O QUE o skill faz, PARA QUE serve,
  e QUANDO deve ser ativado. Esta descrição é o principal vetor de descoberta semântica.
type: playbook  # playbook | prompt | tool_orchestration | linting_refactoring | orchestration
tags: [primary-cluster, secondary-function, tertiary-context]
# Tags válidas: system, scraping, monitoring, competitive-intel, lead-generation,
# content, research, signals, outreach, design, development, quality-assurance,
# orchestration, seo, ads, linkedin, social-media, events, brand, strategy,
# automation, data, analytics, enrichment, qualification, collaboration,
# memory, maintenance, optimization, core, decision-making, debugging, code,
# visualization, presentations
---

# Skill Name

Uma frase que explica o propósito em linguagem direta. Sem jargão. O leitor deve entender o valor em 5 segundos.

**Core principle:** A frase que define a filosofia de execução deste skill. Ex: "Os melhores ângulos de ads não são inventados — são extraídos da linguagem real dos compradores."

## When to Use

- "Frase exata que o usuário diria para ativar este skill"
- "Segunda frase trigger"
- "Terceira frase trigger"
- Qualquer request que envolva [domínio funcional do skill]

**Auto-trigger:** Descreva as condições em que o sistema deve carregar este skill automaticamente.

## Prerequisites

### Environment Variables

```env
VARIABLE_NAME=description_of_what_this_is
```

### Dependencies

```bash
pip install package-name  # ou npm, etc.
```

Se não há dependências externas, escreva: "Nenhuma. Pure reasoning skill."

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Input principal** | Yes | O que o skill precisa para funcionar |
| **Input secundário** | Recommended | Enriquece o output mas não é bloqueante |
| **Configuração** | No | Parâmetros opcionais com defaults sensatos |

## Phase 0: Intake

Perguntas que o skill deve fazer ao usuário antes de executar. Agrupe por categoria.
Numere todas. Indique quais podem ser inferidas vs. quais precisam de resposta explícita.

1. **Pergunta obrigatória** — contexto
2. **Pergunta obrigatória** — escopo
3. **Pergunta opcional** — refinamento

> **Regra:** Faça TODAS as perguntas em uma única interação. Não fragmente em múltiplas rodadas.

## Phase 1: [Nome da Fase]

Descreva cada passo de execução com:

### Step 1A: [Sub-passo]

Instrução específica. Se envolve API ou script:

```bash
python3 skills/skill-name/scripts/script.py \
  --param1 "value" \
  --param2 "value" \
  --output json
```

Documente os campos de output relevantes.

### Step 1B: [Sub-passo]

Continue com o nível de detalhe que permite execução autônoma sem ambiguidade.

## Phase 2: [Nome da Fase]

[Continuação das fases necessárias]

## Phase N: Output

### Output Format

| Output | Format | Location |
| --- | --- | --- |
| **Entrega principal** | Markdown / CSV / JSON / HTML | Caminho do arquivo |
| **Resumo** | Tabela markdown | Exibido ao usuário |
| **Dados brutos** | JSON | Arquivo auxiliar |

### Output Template

```markdown
# [Título do Output]

## Summary
[Resumo executivo]

## Findings
[Dados estruturados — tabelas, listas, etc.]

## Recommendations
[Ações concretas]
```

## Cost

| Component | Cost |
| --- | --- |
| [Componente 1] | Free / $X por uso |
| [Componente 2] | Free / $X por uso |
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **[Modo de falha 1]** | Como detectar | Como recuperar |
| **[Modo de falha 2]** | Como detectar | Como recuperar |
| **[Modo de falha 3]** | Como detectar | Como recuperar |

**Principle:** [Princípio-guia de error handling para este tipo de skill]

## Composability

**Receives data from:**

- `skill-upstream-1` — o que recebe
- `skill-upstream-2` — o que recebe

**Feeds into:**

- `skill-downstream-1` — o que passa
- `skill-downstream-2` — o que passa

**Integration pattern:** Descrição de como encaixar este skill em pipelines.

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
| --- | --- | --- |
| **Key findings** | `[OPERACIONAL]: skill-name — [finding]` | Exemplo concreto |
| **Parameter tuning** | `[OPERACIONAL]: skill-name — [param] works better as [value]` | Exemplo concreto |
| **Strategic insights** | `[ESTRATÉGICO]: skill-name — [insight]` | Exemplo concreto |

**Rules:**

- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

## Quality Gate

Before delivering the final output, verify:

- [ ] **[Check 1]:** Descrição do que verificar
- [ ] **[Check 2]:** Descrição do que verificar
- [ ] **[Check 3]:** Descrição do que verificar
- [ ] **User checkpoint:** Apresentar resumo ao usuário antes de finalizar

**If any check fails:** [Ação de recovery]
