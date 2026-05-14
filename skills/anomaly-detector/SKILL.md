---
name: anomaly-detector
description: >
  Detecta transações financeiras fora do padrão histórico via z-score por categoria,
  detecção de duplicatas e quebras de recorrência. Saída determinística em JSON.
description_pt-BR: >
  Detecta transações financeiras fora do padrão usando z-score por categoria,
  duplicatas e quebras de recorrência. Saída determinística em JSON.
type: reasoning
tags: [finance, analytics, anomaly, cliff-palace]
categories: [finance, analytics]
contract:
  inputs:
    - name: dados_json
      required: true
      description: "JSON canônico do Cliff Palace com transações"
    - name: lookback_days
      required: false
      description: "Janela histórica para baseline (default: 30)"
  outputs:
    - name: anomalies_block
      format: json
      description: "Array de anomalias com type, severity, evidence determinística"
  quality_criteria:
    - "Toda anomalia tem severity ∈ {low, medium, high, critical} baseada em regra explícita do skill"
    - "Outlier por categoria exige ≥ 5 amostras na categoria — caso contrário, NÃO emitir flag"
    - "Severity 'critical' nunca é emitida em transação única sem contexto histórico suficiente"
    - "Cada anomalia inclui campo evidence com z_score, expected_range e baseline_count"
    - "Determinismo: mesmos dados → mesmo output. Sem aleatoriedade, sem chamada externa"
    - "Duplicata = mesmo valor + mesmo merchant em 48h (high) OU mesmo valor + mesma categoria em 24h (medium)"
  on_failure: halt
---

# Anomaly Detector

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Detecção de transações fora do padrão para análise financeira pessoal local-first.


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

- Albert (analista diário) precisa flaggar transações suspeitas no `daily-briefing.json`.
- Quando o pipeline do Cliff Palace processa novos extratos.
- Sob demanda quando o Doug pergunta "tem alguma cobrança estranha?".


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| `dados.json` | Sim | JSON canônico do Cliff Palace com transações |
| `lookback_days` | Não (default: 30) | Janela histórica para baseline |

## Detection Rules

1. **Outlier por categoria**
   - Calcular média (μ) e desvio padrão (σ) dos valores por categoria nos últimos `lookback_days`.
   - Flag se `|valor - μ| > 2σ` E categoria tem ≥ 5 amostras.
   - Severidade: `medium` se `2σ–3σ`, `high` se `> 3σ`.

2. **Cobrança duplicada**
   - Mesmo valor + mesmo merchant em janela de 48h → severidade `high`.
   - Mesmo valor + mesma categoria em janela de 24h (merchant diferente) → severidade `medium`.

3. **Quebra de recorrência**
   - Assinatura mensal conhecida cujo valor mudou > 10% → severidade `medium`.
   - Assinatura mensal que não chegou no dia esperado ± 3 dias → severidade `low`.

4. **Categoria nova com volume alto**
   - Categoria que não aparecia no histórico e somou > 5% do gasto mensal → severidade `medium`.

## Output Schema

```json
{
  "anomalies": [
    {
      "transaction_id": "...",
      "type": "outlier|duplicate|recurrence_break|new_category",
      "severity": "low|medium|high|critical",
      "category": "...",
      "amount": 0.0,
      "evidence": {"z_score": 0.0, "expected_range": [0, 0], "baseline_count": 0}
    }
  ]
}
```

## Anti-Patterns

- Disparar `critical` em transação única sem contexto histórico suficiente (< 5 amostras na categoria).
- Tratar todo z-score > 2 como "anormal" sem considerar sazonalidade óbvia.
- Inventar uma "anomalia narrativa" sem regra determinística por trás.

## Determinism Contract

Mesmos inputs → mesmo output. Sem chamadas externas. Sem aleatoriedade.
