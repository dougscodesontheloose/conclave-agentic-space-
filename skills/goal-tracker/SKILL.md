---
name: goal-tracker
description: >
  Monitora progresso em relação a metas financeiras declaradas em _memory/goals.md.
  Status determinístico: on_track, behind, missed, achieved.
description_pt-BR: >
  Monitora progresso de metas financeiras (poupança, teto por categoria, dívida).
type: reasoning
tags: [finance, goals, cliff-palace]
categories: [finance, planning]
contract:
  inputs:
    - name: goals_md
      required: true
      description: "squads/cliff_palace/_memory/goals.md (ausência => retorna goals: [])"
    - name: dados_json
      required: true
      description: "Transações canônicas do Cliff Palace"
  outputs:
    - name: goals_block
      format: json
      description: "Array de metas com type, target, actual, status e rationale"
  quality_criteria:
    - "Status ∈ {on_track, behind, missed, achieved, n/a} sempre justificado em rationale"
    - "Ausência de goals.md NÃO é falha — retornar 'goals': [] silenciosamente"
    - "Status 'missed' só é cravado quando o mês não tem dias suficientes para reverter"
    - "Pacing usa proporção dia_atual/dias_no_mes — não data calendário absoluta"
    - "Não inventar metas — apenas as declaradas em goals.md devem aparecer"
    - "savings: actual = receita_mes - despesa_mes (líquido, não bruto)"
    - "category_cap: actual = soma de transações da categoria no mês"
  on_failure: halt
---

# Goal Tracker

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Tracker determinístico de metas financeiras pessoais.


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

- Galileu precisa do status das metas no `monthly-plan.json`.
- <user_name> pergunta "tô cumprindo o que combinei comigo?".


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| `goals.md` | Sim | `squads/cliff_palace/_memory/goals.md` (formato abaixo) |
| `dados.json` | Sim | Transações canônicas |

## Goals File Format

Arquivo `squads/cliff_palace/_memory/goals.md`:

```markdown
# Metas — Cliff Palace

## Meta 1: Poupar R$ 2.000/mês
- type: savings
- target: 2000
- period: monthly

## Meta 2: Limitar delivery a R$ 300/mês
- type: category_cap
- category: delivery
- target: 300
- period: monthly

## Meta 3: Quitar cartão até dezembro
- type: debt_payoff
- target: 0
- deadline: 2026-12-31
```

## Status Rules

1. **savings (poupança líquida no mês)**
   - `actual = receita_mes - despesa_mes`
   - `on_track`: dia atual / dias_no_mes ≤ actual / target
   - `behind`: dia atual / dias_no_mes > actual / target (defasagem ≤ 20%)
   - `missed`: defasagem > 20%
   - `achieved`: actual ≥ target

2. **category_cap (teto por categoria)**
   - `actual = gasto_categoria_mes`
   - `on_track`: actual / target ≤ dia_atual / dias_no_mes
   - `behind`: 1.0 ≥ ratio > pacing
   - `missed`: actual > target

3. **debt_payoff**
   - Trajetória linear até `deadline`.
   - Status segue a mesma lógica de `savings` (proporcional a tempo decorrido).

## Output Schema

```json
{
  "goals": [
    {
      "name": "...",
      "type": "savings|category_cap|debt_payoff",
      "target": 0.0,
      "actual": 0.0,
      "status": "on_track|behind|missed|achieved|n/a",
      "rationale": "..."
    }
  ]
}
```

## Anti-Patterns

- Cravar `missed` sem checar se o mês ainda tem dias suficientes para reverter.
- Tratar ausência do arquivo `goals.md` como falha — deve retornar `[]` graciosamente.
- Inventar metas que o <user_name> não declarou.
