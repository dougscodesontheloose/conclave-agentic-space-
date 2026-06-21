---
name: health-score-calculator
description: >
  Calcula um Health Score financeiro pessoal (0-10) baseado em fluxo de caixa, taxa de
  poupança, concentração de gastos e cobertura de emergência. Determinístico.
description_pt-BR: >
  Score de saúde financeira de 0 a 10, com 4 componentes ponderados.
type: reasoning
tags: [finance, score, cliff-palace]
categories: [finance, analytics]
contract:
  inputs:
    - name: dados_json
      required: true
      description: "ambientes/Cliff Palace/dashboard/dados.json — transações canônicas"
    - name: period
      required: false
      description: "Janela de cálculo (default: mês corrente)"
  outputs:
    - name: health_score_block
      format: json
      description: "Bloco JSON com score 0-10, breakdown dos 4 componentes e interpretation"
  quality_criteria:
    - "final_score é a média ponderada exata: 0.30·fluxo + 0.30·poupanca + 0.20·concentracao + 0.20·emergencia"
    - "Output inclui SEMPRE os 4 componentes individuais — <user_name> precisa saber por que está nesse número"
    - "Score arredondado para 1 casa decimal"
    - "interpretation segue thresholds: ≥8 good, 6-8 ok, 4-6 warning, <4 critical"
    - "Cobertura de emergência calculada com despesa MENSAL MÉDIA, não despesa de mês atípico"
    - "Pesos não foram alterados sem versionamento explícito (compromete comparabilidade temporal)"
  on_failure: halt
---

# Health Score Calculator

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Composição determinística de um score 0–10 da saúde financeira pessoal.


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

Nenhuma. Pure reasoning skill.

## When to Use

- Albert (diário) e Galileu (mensal) consomem este skill.
- Sol expõe o número como resposta para "tô bem?".


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| `dados.json` | Sim | Transações canônicas |
| `period` | Não (default: mês corrente) | Janela de cálculo |

## Components (peso)

1. **Fluxo de caixa (peso 0.30)**
   - `score = clamp(0, 10, 5 + 5 * (saldo_liquido / receita))`
   - Receita > despesa → score alto.

2. **Taxa de poupança (peso 0.30)**
   - `score = clamp(0, 10, savings_rate * 50)` (20% poupança → 10)
   - savings_rate = (receita - despesa) / receita

3. **Concentração de categoria (peso 0.20)**
   - Penaliza se uma única categoria discricionária > 30% do gasto.
   - `score = 10 - max(0, (top_category_pct - 30)) * 0.3`

4. **Cobertura de emergência (peso 0.20)**
   - `meses_cobertos = saldo_atual / despesa_mensal_media`
   - `score = clamp(0, 10, meses_cobertos * 1.67)` (6 meses → 10)

## Aggregation

```
final_score = 0.30 * fluxo + 0.30 * poupanca + 0.20 * concentracao + 0.20 * emergencia
```

Arredondar para 1 casa decimal.

## Output Schema

```json
{
  "health_score": 7.2,
  "components": {
    "fluxo_caixa": 8.0,
    "taxa_poupanca": 6.5,
    "concentracao": 7.0,
    "cobertura_emergencia": 5.0
  },
  "interpretation": "good|ok|warning|critical"
}
```

Interpretation thresholds: ≥ 8 good, 6–8 ok, 4–6 warning, < 4 critical.

## Anti-Patterns

- Mudar pesos sem versionar (compromete comparabilidade temporal).
- Calcular cobertura de emergência com despesa de um único mês atípico.
- Reportar score sem componentes — <user_name> precisa saber *por que* tá nesse número.
