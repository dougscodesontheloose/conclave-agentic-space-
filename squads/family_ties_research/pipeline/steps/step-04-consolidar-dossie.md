---
id: "step-04-consolidar-dossie"
execution: inline
agent: minerva-audit
outputFile: squads/family_ties_research/output/research-dossier.md
model_tier: powerful
---

# Step 04: Consolidar Dossie da Rodada

## Context Loading

Load these files before executing:
- `squads/family_ties_research/output/search-brief.md`
- `squads/family_ties_research/output/web-findings.md`
- `ambientes/Family Ties/02_documentos/controle-documentos.md`
- `ambientes/Family Ties/04_hipoteses_cidadania/triagem.md`
- `ambientes/Family Ties/05_saidas/evidence-ledger.csv`

## Instructions

### Process

1. Consolidar os achados por linha familiar.
2. Classificar o valor de cada achado:
   - destrava a busca;
   - melhora a precisao;
   - apenas contextualiza;
   - descartar.
3. Aplicar o gate A/B/C/D/X antes de qualquer sugestao de atualizar arvore.
4. Produzir uma fila priorizada de proximos passos, incluindo:
   - busca complementar;
   - pedido de certidao;
   - validacao de grafia;
   - consulta a arquivo ou cartorio especifico.
5. Apontar impacto preliminar nas hipoteses de cidadania de Italia, Portugal e Espanha, sem concluir elegibilidade.
6. Fechar com uma recomendacao objetiva para a proxima rodada de pesquisa.

## Output Format

```markdown
# Research Dossier

## Sintese da rodada

## Achados por linha familiar

## Fila priorizada de proximos passos

## Impacto preliminar em hipoteses de cidadania

## Recomendacao para a proxima rodada
```

## Veto Conditions

1. Nao converter achados em proximos passos.
2. Tratar cidadania como conclusao fechada.
3. Nao separar achado util de ruido.
4. Sugerir atualizacao de arvore sem evidencia A/B ou ressalva explicita.

## Quality Criteria

- [ ] Dossie consolidado por linha.
- [ ] Fila priorizada.
- [ ] Impacto preliminar tratado com cautela.
- [ ] Recomendacao final objetiva.
- [ ] Atualizacoes respeitam o ledger e a escala A/B/C/D/X.

## Output Example

```markdown
# Research Dossier

## Achados por linha familiar

### Linha Moura
- Achado: catalogo util para orientar busca de nascimento.
- Classificacao: melhora a precisao.
- Limitacao: ainda nao confirma filiacao.

## Fila priorizada de proximos passos
1. Refinar municipio de nascimento de Joao Moura da Silva.
2. Buscar registro integral ou pedir certidao.
3. Validar grafias alternativas antes de nova rodada web.

## Impacto preliminar em hipoteses de cidadania
- Sem conclusao juridica. A rodada apenas melhora a fila documental.

## Recomendacao para a proxima rodada
- Atacar primeiro o documento que confirma filiacao e localidade.
```
