---
execution: inline
agent: "smart_shopper/solomon-verdict"
outputFile: squads/smart_shopper/output/veredito-compra.md
---

# Step 06: Consolidação e Veredito de Compra

## Context Loading

Load these files before executing:
- `squads/smart_shopper/output/precos-pesquisados.md` — Tabela de preços de Priya.
- `squads/smart_shopper/output/cupons-encontrados.md` — Cupons e cashback de Kira.
- `squads/smart_shopper/output/reputacao-analisada.md` — Reputação de Rex.
- `squads/smart_shopper/output/refined-briefing.md` — Briefing original com preferências.
- `ambientes/Bazaar/_data/purchase-history.md` — Histórico para referência.

## Instructions

### Process

1. **Consolidar dados:** Criar uma tabela unificada com preço, cupom, cashback, frete, reputação para cada opção.
2. **Calcular custo real:** Para cada opção: `preço - cupom - cashback + frete = custo real`.
3. **Aplicar multiplicador de reputação:**
   - 🟢: Custo real mantido (multiplicador 1.0x).
   - 🟡: Custo real × 1.05 (custo invisível de risco 5%).
   - 🔴: Eliminado do ranking (a menos que seja a única opção).
4. **Considerar ESG como tiebreaker:** Entre opções com ≤10% de diferença de custo, priorizar ESG.
5. **Gerar ranking final:** Top 3 opções por custo real ajustado.
6. **Produzir veredito:** Recomendação com justificativa, trade-offs entre as opções, e links diretos.
7. **Calcular economia total:** Quanto o usuário economiza vs. o preço de vitrine mais alto encontrado.

## Output Format

Seguir o formato definido no agent Solomon Verdict (veredito com tabela de ranking, trade-offs e links).

## Output Example

```markdown
# Veredito de Compra

## Ranking Final

| Rank | Loja | Custo Real | Reputação | Custo Ajustado | Link | Veredito |
|---:|---|---:|---|---:|---|---|
| 1 | Amazon BR | R$ 2.155,02 | 🟢 | R$ 2.155,02 | https://... | Melhor equilíbrio |
| 2 | Magalu | R$ 2.188,00 | 🟢 | R$ 2.188,00 | https://... | Boa alternativa |
| 3 | Loja Y | R$ 2.020,00 | 🟡 | R$ 2.121,00 | https://... | Só vale pelo preço |

## Recomendação
Comprar na Amazon BR se o objetivo for menor risco. Comprar na Magalu se o desconto PIX for confirmado no checkout.

## Trade-offs
- Amazon: menor risco e entrega rápida, mas preço ligeiramente maior.
- Magalu: preço competitivo, depende de condição PIX.
- Loja Y: barata, mas reputação aumenta custo invisível.

## Economia Total
- Economia contra maior preço de vitrine: R$ 320,00.
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. Custo real não calculado para todas as opções.
2. Reputação não considerada no ranking.
3. Menos de 3 opções no ranking (a menos que não existam mais).
4. Trade-offs não apresentados.

## Quality Criteria

- [ ] Custo real calculado (preço - cupom - cashback + frete).
- [ ] Multiplicador de reputação aplicado.
- [ ] Top 3 apresentado com ranking.
- [ ] Trade-offs entre opções.
- [ ] Economia total calculada.
- [ ] Links diretos incluídos.
