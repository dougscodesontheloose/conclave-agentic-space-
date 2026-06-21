---
title: "Family Ties — Otimizacao Operacional de Evidencias"
date: 2026-05-19
type: architecture_optimization
era: "Memory & Log Optimization (v3)"
impact: high
---

# Family Ties — Otimizacao Operacional de Evidencias

## Contexto

A pesquisa genealogica do Family Ties evoluiu de buscas nominais para cadeias P0/P1/P2/H0, com foco em fontes civis, paroquiais, FamilySearch, cartorios e Arquivo Nacional. A meta-analise mostrou que o gargalo principal passou a ser validacao, acesso e economia de contexto, nao falta de agentes.

## Decisao

Foi definido `squads/family_ties_ancestral_radar/` como executor canonico para novas rodadas genealogicas. O squad `family_ties_research` passa a funcionar como camada historica/de descoberta.

Tambem foi criada a skill `genealogy-evidence-validation`, com contrato de qualidade para classificar achados como `A`, `B`, `C`, `D`, `X`, `qualified_negative` ou `access_block`.

## Capacidade adicionada

- Ledger estruturado em `ambientes/Family Ties/05_saidas/evidence-ledger.csv`.
- Arquitetura operacional em `ambientes/Family Ties/05_saidas/arquitetura-operacional-family-ties-2026-05-19.md`.
- Gates explicitos para impedir promocao de indice, OCR, arvore de terceiro ou nome isolado.
- Politica de tokens: usar contexto compacto e ledger antes de carregar relatorios longos.

## Impacto

O Family Ties agora tem um ciclo mais rigido:

1. unidade de busca;
2. fonte;
3. classificacao;
4. ledger;
5. atualizacao da arvore apenas quando autorizada.

Isso reduz repeticao de web aberta, homonimia, drift entre squads e gasto de tokens em contexto historico redundante.
