---
task: "analisar-reputacao-lojas"
order: 1
---

# Analisar Reputação das Lojas

## Context Loading
- `cupons-encontrados.md`
- `precos-pesquisados.md`

## Process

1. Consultar a reputação das lojas finalistas identificadas em plataformas como Reclame Aqui e Consumidor.gov.
2. Pesquisar problemas recorrentes e crônicos com a entrega ou suporte pós-venda daquela loja específica.
3. Avaliar opiniões de usuários em fóruns comunitários (Reddit) e análises em vídeo (YouTube) sobre a durabilidade e problemas crônicos do produto em si.
4. Identificar e listar claramente "Red Flags" críticas (ex: "não entregam sistematicamente", "falsificações relatadas").
5. Gerar um sumário de riscos de compra para a loja e para o produto.

## Output Format
```markdown
### Avaliação: [Loja]
- **Nota RA:** [X.X/10]
- **Red Flags da Loja:** [Lista de problemas graves]

### Avaliação: [Produto]
- **Percepção Geral:** [Positiva/Negativa/Mista]
- **Problemas Crônicos Relatados:** [Lista]
```

## Veto Conditions
- Rejeitar lojas com nota abaixo de 6.0 no Reclame Aqui (sinalizar como Risco Extremo).

## Quality Criteria
- [ ] Histórico de pelo menos 6 meses considerado.
- [ ] Produto avaliado além da loja.
- [ ] Red flags destacadas visualmente.

## Output Example
```markdown
### Avaliação: Mercado Livre (Loja Oficial Samsung)
- **Nota RA:** 8.5/10
- **Red Flags:** Nenhuma crítica grave na loja oficial.

### Avaliação: Monitor Odyssey G5
- **Percepção Geral:** Positiva, mas com ressalvas.
- **Problemas Crônicos:** Usuários do Reddit relatam ghosting excessivo em jogos FPS de ritmo acelerado.
```














