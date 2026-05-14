---
execution: inline
agent: "smart_shopper/solomon-verdict"
outputFile: squads/smart_shopper/output/refined-briefing.md
---

# Step 00: Refinamento do Pedido de Compra

## Context Loading

Load these files before executing:
- `_conclave/state/memory/company.md` — Perfil do Doug.
- `ambientes/Bazaar/_data/retailer-registry.md` — Para sugerir categorias.
- `ambientes/Bazaar/_data/purchase-history.md` — Para referência de compras anteriores.

## Instructions

### Process

1. **Receber o input do usuário:** O que ele quer comprar.
2. **Fazer perguntas de refinamento** (em uma única interação quando possível):
   - **Produto:** Qual produto exato? Marca, modelo, especificações mínimas.
   - **Faixa de preço:** Mínimo e máximo aceitáveis em R$.
   - **Preferência de loja:** Alguma loja favorita ou a evitar?
   - **Urgência:** Prazo máximo aceitável de entrega (dias úteis).
   - **Cartão:** Algum cartão de crédito específico para desconto?
   - **CEP:** CEP de entrega para cálculo de frete.
   - **ESG:** Prefere marcas com agenda de sustentabilidade?
   - **Condição de pagamento:** Prefere PIX (desconto) ou parcelamento?
3. **Consultar histórico:** Verificar se o usuário já pesquisou algo similar no `purchase-history.md`.
4. **Gerar briefing refinado:** Documento estruturado com todos os critérios definidos.

## Output Format

```markdown
# 📋 Briefing de Compra Refinado

## Produto
- **Descrição:** [produto com especificações]
- **Categoria:** [categoria do retailer-registry]

## Critérios
- **Faixa de preço:** R$ [min] — R$ [max]
- **CEP de entrega:** [CEP]
- **Prazo máximo:** [X] dias úteis
- **Cartão preferido:** [cartão ou "nenhum"]
- **Pagamento preferido:** [PIX / Parcelamento / Sem preferência]
- **Priorizar ESG:** [Sim / Não / Indiferente]

## Preferências
- **Lojas preferidas:** [lista ou "nenhuma"]
- **Lojas a evitar:** [lista ou "nenhuma"]

## Contexto
- **Compras anteriores relacionadas:** [referência do histórico ou "nenhuma"]
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O produto não está definido com especificações suficientes para pesquisar.
2. Não há faixa de preço definida (mesmo que ampla).
3. Não há CEP para cálculo de frete.

## Quality Criteria

- [ ] Produto definido com especificações claras.
- [ ] Faixa de preço estabelecida.
- [ ] CEP de entrega informado.
- [ ] Categoria do retailer-registry identificada.
