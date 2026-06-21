---
task: "mapear-lacunas-e-fontes"
order: 1
---

# Task: Mapear Lacunas e Fontes

## Process

1. Ler o escopo da rodada e identificar a pessoa, linha, objetivo e critério de sucesso.
2. Carregar a árvore preliminar, dados declarados, controle documental, catálogo de fontes, triagem de cidadania e `evidence-ledger.csv`.
3. Verificar se a lacuna ja existe no ledger como `access_block`, `qualified_negative` ou `X`; reabrir somente com discriminador novo.
4. Transformar o objetivo em até 5 lacunas documentais, sempre no formato pessoa + evento + localidade + janela temporal.
5. Para cada lacuna, registrar variantes nominais, parentes associados, fonte primária provável e fonte auxiliar.
6. Classificar cada lacuna como:
   - `local`: pode avançar com material já existente no ambiente;
   - `web`: exige pesquisa externa controlada;
   - `bloqueada`: falta dado mínimo para pesquisa responsável.
7. Priorizar pela capacidade de destravar uma geração anterior, resolver conflito nominal ou confirmar filiação.
8. Registrar o critério de validação de cada lacuna antes de recomendar busca.

## Output Format

```markdown
# Matriz de Busca

## Resumo da Rodada
- Linha/Pessoa:
- Objetivo:
- Critério de sucesso:
- Limite de segurança:

## Lacunas Priorizadas

### L-01
- Pessoa-alvo:
- Evento-alvo:
- Localidade-alvo:
- Janela temporal:
- Variações nominais:
- Parentes/pistas auxiliares:
- Fonte primária provável:
- Fonte auxiliar:
- Modo de execução: local / web / bloqueada
- Ledger relacionado:
- Critério de validação:
- Motivo da prioridade:

## Sequência Recomendada
1. ...

## Lacunas Bloqueadas
- ...
```

## Output Example

```markdown
### L-01
- Pessoa-alvo: Joao Moura da Silva
- Evento-alvo: nascimento
- Localidade-alvo: Alagoas
- Janela temporal: 1890-1910
- Variações nominais: João Moura da Silva; Joao Moura; João M. da Silva
- Parentes/pistas auxiliares: pais ou cônjuge a confirmar em documento intermediário
- Fonte primária provável: registro civil ou paroquial de nascimento
- Fonte auxiliar: catálogo FamilySearch por município
- Modo de execução: web
- Critério de validação: documento com nome, data, local e filiação compatíveis
- Motivo da prioridade: pode destravar a geração anterior da linha Moura
```

## Quality Criteria

- [ ] Cada lacuna tem pessoa, evento, localidade e janela temporal.
- [ ] Cada lacuna tem critério de validação antes da busca.
- [ ] Fontes primárias aparecem antes de fontes auxiliares.
- [ ] Conflitos nominais são preservados como variantes.
- [ ] Pessoas vivas e dados privados não aparecem em parâmetros externos.
- [ ] A sequência recomendada explica por que aquela ordem reduz ruído.
- [ ] O ledger foi usado para evitar repetição de negativos, descartes e bloqueios.

## Veto Conditions

1. Refazer se qualquer lacuna sair sem localidade-alvo.
2. Refazer se qualquer lacuna sair sem janela temporal mínima.
3. Refazer se uma hipótese familiar for tratada como fato documental.
4. Refazer se dados de pessoas vivas aparecerem como query ou parâmetro web.
5. Refazer se a saída sugerir cidadania como conclusão jurídica.
6. Refazer se uma busca em bloqueio de acesso for reaberta como web aberta sem novo discriminador.
