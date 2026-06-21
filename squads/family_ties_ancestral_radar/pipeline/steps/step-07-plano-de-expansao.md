---
id: "step-04-plano-de-expansao"
execution: subagent
agent: linhagem_scout
outputFile: squads/family_ties_ancestral_radar/output/plano-de-expansao.md
model_tier: powerful
---

# Step 04: Consolidar Plano de Expansao

## Context Loading

Load these files before executing:
- `squads/family_ties_ancestral_radar/output/matriz-de-busca.md`
- `squads/family_ties_ancestral_radar/output/achados-e-fontes.md`
- `squads/family_ties_ancestral_radar/output/decisao-da-rodada.md`
- `ambientes/Family Ties/02_documentos/controle-documentos.md`
- `ambientes/Family Ties/04_hipoteses_cidadania/triagem.md`
- `ambientes/Family Ties/05_saidas/evidence-ledger.csv`
- `ambientes/Family Ties/05_saidas/arquitetura-operacional-family-ties-2026-05-19.md`

## Instructions

1. Consolidar apenas o que ficou sustentado pelos achados da rodada.
2. Antes de propor atualizacao da arvore, aplicar o gate:
   - `A`: pode atualizar arvore;
   - `B`: pode orientar atualizacao com ressalva;
   - `C`/`D`: vira proxima busca;
   - `X`: descartar;
   - `qualified_negative`: mudar parametro;
   - `access_block`: acao humana/logada/offline.
3. Traduzir isso em fila operacional de trabalho:
   - o que atualizar na arvore
   - qual documento pedir
   - qual cartorio, paroquia ou acervo atacar
   - qual conflito ainda precisa de prova
4. Separar claramente:
   - fatos confirmados
   - hipoteses fortes
   - pendencias abertas
5. Se houver implicacao para Italia, Portugal ou Espanha, registrar em uma nota curta sem declarar elegibilidade.

## Output Format

```markdown
# Plano de Expansao

## Fatos Confirmados
- ...

## Hipoteses Fortes
- ...

## Atualizacoes na Arvore
- ...

## Fila de Documentos
1. ...

## Atualizacoes de Ledger
- ...

## Proximas Buscas
1. ...

## Nota de Cidadania
- ...
```

## Veto Conditions

1. Refazer se o plano consolidar algo que nao apareceu nos achados da rodada.
2. Refazer se fato, hipotese e pendencia ficarem misturados.
3. Refazer se uma recomendacao nao tiver documento, fonte ou criterio de sucesso.
4. Refazer se houver conclusao de elegibilidade juridica.
5. Refazer se o plano mandar pesquisar novamente sem explicar o parametro novo.
6. Refazer se recomendar P1/P2 quando a P0 correspondente esta apenas em `access_block`, sem acao humana/logada/offline.

## Quality Criteria

- [ ] Fatos confirmados, hipoteses fortes e pendencias abertas aparecem separados.
- [ ] Cada atualizacao de arvore esta vinculada a evidencia ou criterio de validacao.
- [ ] Cada documento na fila tem objetivo e prioridade.
- [ ] Proximas buscas explicam localidade, evento e janela temporal.
- [ ] Nota de cidadania permanece preliminar e sem parecer juridico.
- [ ] O plano e executavel sem reler todo o historico da rodada.
- [ ] Atualizacoes de arvore respeitam os graus A/B/C/D/X e bloqueios registrados no ledger.

## Output Example

```markdown
## Fila de Documentos
1. Certidao de nascimento de Joao Moura da Silva
   - Objetivo: confirmar filiacao e localidade.
   - Prioridade: alta.
   - Criterio de sucesso: nome, data, local e pais compativeis.

## Proximas Buscas
1. Refinar Pedro Jacinto / Pedro Teixeira de Paula por municipio e casamento.
   - Parametro novo: variante nominal e evento especifico.
   - Janela temporal: definir a partir de documento intermediario.
```
