---
execution: subagent
agent: "smart_shopper/rex-review"
outputFile: squads/smart_shopper/output/reputacao-analisada.md
isolation: strict
---

# Step 04: Pesquisa de Reputação

## Context Loading

Load these files before executing:
- `squads/smart_shopper/output/precos-pesquisados.md` — Lista de lojas a verificar.
- `squads/smart_shopper/output/refined-briefing.md` — CEP para contexto regional.

## Instructions

### Process

1. **Ler a tabela de preços** para obter a lista de lojas a verificar.
2. **Para cada loja, pesquisar:**
   - **ReclameAqui:** Score geral, taxa de resolução, nota do consumidor, volume de reclamações (últimos 6 meses), classificação (Ótimo/Bom/Regular/Ruim/Não Recomendada).
   - **Google Reviews:** Nota média, volume de avaliações, reclamações recorrentes.
   - **Trustpilot** (quando disponível): Score e tendência.
3. **Analisar red flags:**
   - Atraso de entrega recorrente (especialmente para a região do CEP).
   - Produto diferente do anunciado.
   - Pós-venda inexistente ou demorado.
   - Problemas com devolução/estorno.
   - Cobrança duplicada.
4. **Quando disponível, analisar reviews do produto específico:**
   - Durabilidade, qualidade real vs. foto, problemas comuns.
5. **Atribuir índice de confiança:**
   - 🟢 Confiável: Score ReclameAqui ≥ 7.0 + taxa resolução ≥ 80% + sem red flags graves.
   - 🟡 Atenção: Score entre 5.0-6.9 OU taxa resolução entre 60-79% OU red flags menores.
   - 🔴 Risco: Score < 5.0 OU taxa resolução < 60% OU red flags graves recorrentes.

## Output Format

```markdown
# ⭐ Rex Review — Análise de Reputação

**Produto:** [nome do produto]
**Data:** [data da pesquisa]

## Resumo por Loja

| Loja | ReclameAqui | Taxa Resolução | Google Reviews | Confiança | Red Flags |
|------|-------------|----------------|----------------|-----------|-----------|
| [Loja 1] | 8.5 (Ótimo) | 92% | 4.3/5 (2.1k) | 🟢 | Nenhum |
| [Loja 2] | 6.2 (Regular) | 71% | 3.8/5 (500) | 🟡 | Atrasos no Sul |

## Detalhamento

### [Loja 1]
- **ReclameAqui:** [detalhes]
- **Reclamações recentes (6 meses):** [volume e temas]
- **Red flags:** [detalhes ou "nenhum"]
- **Reviews do produto:** [quando disponível]

### [Loja 2]
...
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. ReclameAqui não consultado para alguma loja.
2. Índice de confiança não atribuído.
3. Red flags não analisados.

## Quality Criteria

- [ ] ReclameAqui consultado para todas as lojas.
- [ ] Google Reviews como cross-check.
- [ ] Taxa de resolução extraída.
- [ ] Red flags listados com evidência.
- [ ] Índice de confiança (🟢/🟡/🔴) atribuído.

## Output Example

```markdown
# Rex Review — Análise de Reputação

**Produto:** Smartphone Modelo X
**Data:** YYYY-MM-DD

## Resumo por Loja

| Loja | ReclameAqui | Taxa Resolução | Google Reviews | Confiança | Red Flags |
|---|---|---:|---|---|---|
| Amazon BR | 8.2 | 91% | 4.5/5 | 🟢 | nenhum crítico |
| Loja Y | 5.4 | 62% | 3.6/5 | 🟡 | atraso recorrente |

## Detalhamento

### Loja Y
- Reclamações recentes: atraso de entrega e dificuldade de estorno.
- Impacto: manter apenas se preço ajustado compensar risco.
```
