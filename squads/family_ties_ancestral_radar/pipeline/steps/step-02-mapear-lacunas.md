---
id: "step-01-mapear-lacunas"
execution: subagent
agent: linhagem_scout
outputFile: squads/family_ties_ancestral_radar/output/matriz-de-busca.md
model_tier: powerful
---

# Step 01: Mapear Lacunas e Parametrizar Busca

## Context Loading

Load these files before executing:
- `squads/family_ties_ancestral_radar/output/escopo-da-rodada.md`
- `ambientes/Family Ties/01_arvore/dados-declarados.md`
- `ambientes/Family Ties/01_arvore/arvore-preliminar.md`
- `ambientes/Family Ties/02_documentos/controle-documentos.md`
- `ambientes/Family Ties/03_fontes/fontes-e-acessos.md`
- `ambientes/Family Ties/04_hipoteses_cidadania/triagem.md`
- `ambientes/Family Ties/05_saidas/contexto-continuacao-genealogia.md`
- `ambientes/Family Ties/05_saidas/evidence-ledger.csv`
- `squads/family_ties_ancestral_radar/pipeline/data/research-brief.md`

## Instructions

1. Ler o escopo da rodada.
2. Consultar o ledger para evitar repetir buscas ja classificadas como `qualified_negative`, `access_block` ou `X`.
3. Identificar ate 5 lacunas diretamente ligadas ao objetivo.
4. Para cada lacuna, montar uma unidade de busca com:
   - pessoa-alvo
   - evento-alvo
   - localidade-alvo
   - janela temporal
   - variacoes nominais
   - parentes ou pistas auxiliares
   - fonte prioritaria
   - criterio de validacao
5. Informar a linha de ledger relacionada quando existir.
6. Ordenar por prioridade operacional.
7. Explicitar quais lacunas podem ser tratadas apenas com material local, quais exigem web e quais estao bloqueadas por acesso.

## Output Format

```markdown
# Matriz de Busca

## Resumo da Rodada
- Objetivo:
- Linha/Pessoa:
- Critico de sucesso:

## Lacunas Priorizadas

### L-01
- Pessoa-alvo:
- Evento-alvo:
- Localidade-alvo:
- Janela temporal:
- Variacoes nominais:
- Pistas auxiliares:
- Fonte prioritaria:
- Precisa de web?: sim/nao
- Ledger relacionado:
- Criterio de validacao:

## Sequencia Recomendada
1. ...
```

## Veto Conditions

1. Refazer se qualquer lacuna sair sem `localidade-alvo`, `janela temporal` ou `criterio de validacao`.
2. Refazer se a matriz pular geracoes sem documento intermediario.
3. Refazer se houver conclusao de cidadania ou elegibilidade juridica.
4. Refazer se dados de pessoas vivas forem usados como parametro de busca externa.
5. Refazer se uma fonte auxiliar aparecer acima de uma fonte primaria sem justificativa.
6. Refazer se ignorar `access_block`, `qualified_negative` ou `X` ja registrado no ledger.

## Quality Criteria

- [ ] Cada lacuna tem pessoa, evento, localidade e janela temporal.
- [ ] Cada lacuna tem variacoes nominais ou uma justificativa para ausencia delas.
- [ ] Cada lacuna aponta fonte prioritaria e criterio de validacao.
- [ ] A ordem de prioridade reduz ruido e evita busca ampla demais.
- [ ] A matriz separa lacunas locais, lacunas web e lacunas bloqueadas.
- [ ] A saida pode alimentar o passo de pesquisa sem consultar fichas privadas.
- [ ] Lacunas ja resolvidas, descartadas ou bloqueadas no ledger nao foram reabertas sem novo discriminador.

## Output Example

```markdown
### L-01
- Pessoa-alvo: Joao Moura da Silva
- Evento-alvo: nascimento
- Localidade-alvo: Alagoas
- Janela temporal: 1890-1910
- Variacoes nominais: Joao Moura da Silva; Joao Moura; Joao M. da Silva
- Pistas auxiliares: filiacao a confirmar em documento intermediario
- Fonte prioritaria: registro civil ou paroquial de nascimento
- Precisa de web?: sim
- Criterio de validacao: registro com nome, data, local e filiacao compativeis
```
