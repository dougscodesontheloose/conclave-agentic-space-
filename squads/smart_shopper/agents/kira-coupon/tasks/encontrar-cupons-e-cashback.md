---
task: "encontrar-cupons-e-cashback"
order: 1
---

# Encontrar Cupons e Cashback

## Context Loading
- `precos-pesquisados.md`

## Process

1. Para cada loja identificada no arquivo de preços pesquisados, buscar cupons de desconto ativos.
2. Registrar a validade do cupom. Cupons expirados devem ser marcados com `Status: Expirado`.
3. Identificar opções de cashback ativas (ex: Méliuz, Banco Inter, Cuponomia) informando a porcentagem exata (%).
4. Calcular a economia real em Reais (R$) para facilitar a comparação final pelo Solomon Verdict.
5. Validar se o cupom é aplicável ao produto em questão ou se há restrições (ex: "apenas primeira compra").
6. Consolidar os dados encontrados em formato estruturado.

## Output Format
```markdown
### [Nome da Loja]
- **Cupom:** [CÓDIGO] (-R$ XX) | Status: [Validado/Expirado]
- **Cashback:** XX% (R$ XX) via [Plataforma]
- **Economia Total:** R$ XX
```

## Veto Conditions
- Rejeitar cupons que não têm fonte verificável.

## Quality Criteria
- [ ] Pelo menos 3 fontes de cupons/cashback consultadas.
- [ ] Valores em R$ calculados e explícitos.
- [ ] Regras de uso do cupom descritas.

## Output Example
```markdown
### Fast Shop
- **Cupom:** FAST10 (-R$ 150) | Status: Validado
- **Cashback:** 5% (R$ 75) via Méliuz
- **Economia Total:** R$ 225
```
















