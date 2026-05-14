---
execution: subagent
agent: "smart_shopper/kira-coupon"
outputFile: squads/smart_shopper/output/cupons-encontrados.md
isolation: strict
---

# Step 03: Pesquisa de Cupons e Cashback

## Context Loading

Load these files before executing:
- `squads/smart_shopper/output/precos-pesquisados.md` — Lista de lojas encontradas por Priya.
- `squads/smart_shopper/output/refined-briefing.md` — Briefing com preferências de cartão.

## Instructions

### Process

1. **Ler a tabela de preços** para obter a lista de lojas a pesquisar.
2. **Para cada loja da tabela, pesquisar:**
   - **Cupons de desconto** em: Cuponation, Méliuz, Promobit, Pelando, RetailMeNot Brasil.
   - **Cashback disponível** em: Méliuz, Zoom Cashback, PicPay, Ame Digital.
   - **Programas de fidelidade** aplicáveis: Livelo, Esfera, TudoAzul, Smiles.
   - **Descontos de cartão** específicos mencionados no briefing.
3. **Para cada cupom/cashback encontrado:**
   - Verificar data de validade (ativo/expirado).
   - Verificar condições de uso (valor mínimo de compra, categorias elegíveis).
   - Calcular valor real do desconto em R$ com base no preço de Priya.
   - Verificar se é cumulativo com outras promoções.
4. **Para programas de pontos:**
   - Calcular valor real do ponto (ex: "1.000 pts Livelo = R$ X de desconto nesta compra").
5. **Gerar relatório** agrupado por loja.

## Output Format

```markdown
# 🎟️ Kira Coupon — Cupons e Cashback

**Produto:** [nome do produto]
**Data:** [data da pesquisa]
**Plataformas consultadas:** [lista]

## [Nome da Loja 1]

| Tipo | Código/Link | Desconto | Valor Real | Validade | Cumulativo | Status |
|------|-------------|----------|------------|----------|------------|--------|
| Cupom | CODIGO10 | 10% | R$ XX | dd/mm/aaaa | Sim | ✅ Ativo |
| Cashback Méliuz | [link] | 3% | R$ XX | Permanente | Sim | ✅ Ativo |
| Livelo | — | 2 pts/R$ | ~R$ XX | — | Sim | ✅ Ativo |

**Economia máxima combinada:** R$ XX

## [Nome da Loja 2]
...

## 💡 Resumo: Melhor Combo

| Loja | Economia Total | Detalhamento |
|------|---------------|-------------|
| [Loja] | R$ XX | Cupom X + Cashback Y |
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. Menos de 3 plataformas de cupons consultadas.
2. Valor real do desconto em R$ não calculado.
3. Status de validade não verificado.

## Quality Criteria

- [ ] Mínimo 3 plataformas de cupons consultadas.
- [ ] Valor real em R$ calculado para cada cupom/cashback.
- [ ] Data de validade verificada.
- [ ] Cumulatividade informada.
- [ ] Programas de fidelidade incluídos quando aplicáveis.
