---
execution: subagent
agent: "smart_shopper/priya-price"
outputFile: squads/smart_shopper/output/precos-pesquisados.md
isolation: strict
---

# Step 02: Pesquisa de Preços e Condições

## Context Loading

Load these files before executing:
- `squads/smart_shopper/output/refined-briefing.md` — Briefing de compra com critérios.
- `ambientes/Bazaar/_data/retailer-registry.md` — Varejistas priorizados por categoria.
- `ambientes/Bazaar/_data/sustainable-brands.md` — Marcas com agenda ESG.
- `ambientes/Bazaar/_data/store-blacklist.md` — Lojas a excluir.

## Instructions

### Process

1. **Ler o briefing refinado** para entender produto, categoria, faixa de preço e preferências.
2. **Identificar a categoria** no retailer-registry e obter a lista priorizada de varejistas.
3. **Excluir lojas** da store-blacklist.
4. **Pesquisar em comparadores** (Buscapé, Zoom, Google Shopping) para visão panorâmica.
5. **Pesquisar nos varejistas T1** da categoria.
6. **Pesquisar nos varejistas T2** da categoria.
7. **Pesquisar nos marketplaces gerais** (Mercado Livre, Amazon BR).
8. **Para cada resultado, extrair:**
   - Preço do produto
   - Custo do frete (para o CEP do briefing)
   - Prazo de entrega estimado
   - Condições de pagamento (PIX, parcelas sem juros, cartões com desconto)
   - Disponibilidade de estoque
   - Link direto para o produto
9. **Calcular custo total** (preço + frete) para cada opção.
10. **Sinalizar marcas ESG** quando o produto for moda/calçados/lifestyle.
11. **Sinalizar outliers** (preços 40%+ abaixo da média).
12. **Gerar tabela comparativa** rankeada por custo total.

## Output Format

Seguir o formato definido no agent Priya Price (tabela comparativa com todas as colunas).

## Veto Conditions

Reject and redo if ANY of these are true:
1. Menos de 6 fontes consultadas.
2. Custo total não calculado (preço + frete).
3. Condições de pagamento ausentes.
4. Loja da blacklist incluída nos resultados.

## Quality Criteria

- [ ] Mínimo 6 fontes consultadas.
- [ ] Custo total calculado para todas as opções.
- [ ] Condições de pagamento detalhadas.
- [ ] Flag ESG aplicado quando relevante.
- [ ] Outliers sinalizados.
- [ ] Links diretos incluídos.
