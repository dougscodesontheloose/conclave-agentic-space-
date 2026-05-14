---
name: pattern-detector
description: >
  Identifica padrões recorrentes de gasto (sazonalidade, hábitos, vazamentos silenciosos)
  e calcula deltas vs. baselines (quinzena anterior, média móvel). Saída determinística em JSON.
description_pt-BR: >
  Identifica padrões de gasto recorrente, sazonalidade e vazamentos silenciosos.
  Calcula deltas vs. baseline (quinzena anterior, média de 90 dias).
type: reasoning
tags: [finance, analytics, patterns, cliff-palace]
categories: [finance, analytics]
contract:
  inputs:
    - name: dados_json
      required: true
      description: "Transações canônicas do Cliff Palace"
    - name: window_days
      required: false
      description: "Janela atual de análise (default: 15)"
    - name: baselines
      required: false
      description: "Lista de baselines a comparar (default: previous_window, ma_90d)"
  outputs:
    - name: trends_block
      format: json
      description: "Bloco com trends, leaks, burn_rate_daily e month_projection"
  quality_criteria:
    - "Tendência só é reportada se |delta_pct| > 15% E valor_absoluto > R$ 50"
    - "Cada trend inclui campo 'vs' explícito (previous_biweek | ma_90d)"
    - "Confidence 'high' SOMENTE com histórico ≥ 90 dias E variância intra-mês < 20%"
    - "Confidence 'low' obrigatório quando histórico < 30 dias"
    - "Leaks identificados com ≥ 2 ocorrências em meses consecutivos OU last_used > 60 dias"
    - "burn_rate_daily = total_gasto_janela / dias_janela (sem ajustes implícitos)"
    - "Não reportar tendência baseada em < 3 transações na janela atual"
  on_failure: halt
---

# Pattern Detector

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Detecção de padrões de consumo de médio prazo para o Cliff Palace.


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

- Marie (estrategista quinzenal) precisa do mapeamento de tendências do `biweekly-trends.json`.
- Quando o Doug pergunta "tô gastando mais com X?" ou "que cobranças tão me sangrando?".


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| `dados.json` | Sim | Transações canônicas |
| `window_days` | Não (default: 15) | Janela atual de análise |
| `baselines` | Não | Lista de baselines a comparar (default: previous_window, ma_90d) |

## Detection Rules

1. **Tendência por categoria**
   - Calcular total por categoria na janela atual.
   - Calcular o mesmo para cada baseline.
   - `delta_pct = (atual - baseline) / baseline * 100`.
   - Reportar apenas categorias com `|delta_pct| > 15%` E `valor_absoluto > R$ 50`.

2. **Vazamentos (leaks)**
   - Cobranças recorrentes (≥ 2 ocorrências em meses consecutivos com mesmo merchant) abaixo de R$ 50/un mas que somam > 5% do gasto mensal.
   - Assinaturas com `last_used_estimate` (heurística simples: data da última transação relacionada) > 60 dias.

3. **Burn rate**
   - `burn_rate_daily = total_gasto_janela / dias_janela`.
   - Projeção de fechamento do mês = `burn_rate_daily * dias_no_mes`.

4. **Confiança da projeção**
   - `high` se histórico ≥ 90 dias E variância intra-mês < 20%.
   - `medium` se 30–90 dias.
   - `low` se < 30 dias.

## Output Schema

```json
{
  "trends": [
    {"category": "...", "current": 0.0, "baseline": 0.0, "delta_pct": 0.0, "vs": "previous_biweek|ma_90d"}
  ],
  "leaks": [
    {"merchant": "...", "monthly_cost": 0.0, "occurrences": 0, "last_used_estimate": "..."}
  ],
  "burn_rate_daily": 0.0,
  "month_projection": {"expense": 0.0, "confidence": "low|medium|high"}
}
```

## Anti-Patterns

- Reportar tendência baseada em < 3 transações na janela atual.
- Cravar `confidence: high` com histórico curto.
- Misturar análise mensal (Galileu) na janela quinzenal.
