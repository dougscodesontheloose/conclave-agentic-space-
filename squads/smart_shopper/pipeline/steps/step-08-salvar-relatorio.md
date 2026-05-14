---
execution: inline
agent: "smart_shopper/solomon-verdict"
---

# Step 08: Salvar Relatório Final

## Context Loading

Load these files before executing:
- `squads/smart_shopper/output/veredito-compra.md` — Veredito aprovado.
- `squads/smart_shopper/output/refined-briefing.md` — Briefing original.
- `ambientes/Bazaar/_data/purchase-history.md` — Histórico para append.

## Instructions

### Process

1. **Salvar relatório completo** no diretório de output do run atual.
2. **Append ao purchase-history.md** do ambiente Bazaar:
   - Data da pesquisa
   - Produto pesquisado
   - Faixa de preço do briefing
   - Veredito (loja recomendada)
   - Preço final (custo real)
   - Link direto
3. **Informar ao usuário** que o relatório foi salvo e onde encontrá-lo.

## Output Format

Append ao `purchase-history.md`:

```markdown
| [data] | [produto] | R$ [min] — R$ [max] | [recomendação] | [loja] | R$ [custo real] | [link] |
```

## Quality Criteria

- [ ] Relatório salvo no output do run.
- [ ] Histórico atualizado com nova entrada.
- [ ] Caminho do relatório informado ao usuário.

## Veto Conditions

- Rejeitar e pausar a execução se o arquivo `veredito-compra.md` estiver vazio ou não existir.
- Rejeitar se não houver permissão de escrita para atualizar o arquivo `purchase-history.md` no histórico.
- Rejeitar se os links não estiverem validados e acessíveis.

## Output Example

```markdown
Relatório salvo com sucesso em: `squads/smart_shopper/output/run-2026-05-08/relatorio-final.md`

Append realizado em `purchase-history.md`:
| 2026-05-08 | Monitor Dell 27" 4K | R$ 2.000 — R$ 2.500 | Dell Store | Dell | R$ 2.150 | [Link](#) |
```




















