---
name: category-analyzer
description: >
  Ranqueia categorias de gasto por impacto no orçamento (potencial de economia × dificuldade
  de redução). Determinístico, baseado em regras explícitas.
description_pt-BR: >
  Ranqueia categorias por onde cada R$ economizado tem maior impacto.
type: reasoning
tags: [finance, analytics, budget, cliff-palace]
categories: [finance, analytics]
contract:
  inputs:
    - name: dados_json
      required: true
      description: "Transações canônicas do Cliff Palace"
    - name: period_days
      required: true
      description: "Janela de análise (15, 30, 90)"
    - name: difficulty_override
      required: false
      description: "_memory/category-difficulty.md (sobrescreve mapeamento default se existir)"
  outputs:
    - name: ranking_block
      format: json
      description: "Array ranqueado por impact_score com category, savings_potential, difficulty, rationale"
  quality_criteria:
    - "savings_potential = gasto_atual - mediana_dos_3_meses_mais_baixos (não compara com zero)"
    - "Cada item do ranking inclui difficulty ∈ {easy, medium, hard} com rationale explícito"
    - "impact_score = savings_potential / difficulty_weight (pesos: easy=1, medium=2, hard=3)"
    - "Categorias 'hard' sempre acompanhadas de sugestão de renegociação no rationale (nunca 'cortar')"
    - "Cálculo de mediana ignora outliers via método robusto (não média simples)"
    - "Ranking ordenado por impact_score decrescente"
  on_failure: halt
---

# Category Analyzer

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Ranking de categorias de gasto por **savings potential** × **dificuldade de mudança comportamental**.


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

- Marie e Galileu precisam do ranking para o `biweekly-trends.json` e `monthly-plan.json`.
- Doug pergunta "onde devo cortar primeiro?".


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| `dados.json` | Sim | Transações canônicas |
| `period_days` | Sim | Janela de análise (15, 30, 90) |

## Scoring Rules

1. **Savings potential (R$)**
   - Para cada categoria, calcular: `gasto_atual - mediana_dos_3_meses_mais_baixos`.
   - Esse delta é o "espaço razoável de economia" — não exige cortar tudo, exige voltar ao seu próprio melhor mês.

2. **Dificuldade**
   - `easy`: categoria majoritariamente discricionária (delivery, assinaturas, lazer).
   - `medium`: mista (mercado, transporte).
   - `hard`: predominantemente fixa (aluguel, escola, plano de saúde).

3. **Impact score**
   - `impact = savings_potential / difficulty_weight`
   - Pesos: easy=1, medium=2, hard=3.
   - Quanto maior `impact`, mais alto no ranking.

## Default Difficulty Map

```
easy:    delivery, assinaturas, lazer, restaurantes, app_taxi, compras_online
medium:  mercado, transporte, farmacia, vestuario
hard:    aluguel, condominio, plano_saude, educacao, financiamento, fatura_minimo
```

(O mapeamento pode ser sobrescrito via `_memory/category-difficulty.md` se existir.)

## Output Schema

```json
{
  "ranking": [
    {
      "category": "delivery",
      "current_spend": 0.0,
      "savings_potential": 0.0,
      "difficulty": "easy|medium|hard",
      "impact_score": 0.0,
      "rationale": "..."
    }
  ]
}
```

## Anti-Patterns

- Sugerir cortar categoria `hard` sem renegociação como caminho.
- Calcular potencial baseado em "zero" — irreal para categorias essenciais.
- Ignorar outliers ao calcular mediana dos 3 meses mais baixos.
