---
title: "Family Ties Research Squad"
date: 2026-05-18
type: capability_addition
era: "Memory & Log Optimization (v3)"
impact: high
---

# Family Ties Research Squad

## Contexto

O ambiente `Family Ties` ja possuia arvore preliminar, fichas privadas de pessoas, OCR documental, fontes-base e uma triagem inicial de cidadania. Faltava um mecanismo nativo do Conclave para transformar esse acervo em buscas externas controladas, sem jogar dados sensiveis diretamente na web.

## Decisao

Criar o squad `family_ties_research`, desenhado com tres funcoes complementares:

1. `Selene Mapper` sanitiza o contexto interno e gera a fila de alvos de busca.
2. `Orion Finder` pesquisa acervos e fontes oficiais com isolamento estrito.
3. `Minerva Audit` consolida achados em proximos passos documentais e impacto preliminar nas hipoteses de cidadania.

## Principio Arquitetural

A busca web passou a ter uma etapa formal de **sanitizacao obrigatoria** antes de qualquer query externa. Isso reduz risco de vazamento de dados de pessoas vivas e alinha o Family Ties com a `security.policy.md`, que veta o envio de dados secretos para ferramentas externas.

## Impacto

- Introduz um fluxo genealogico nativo no Conclave.
- Conecta `Family Ties` ao sistema de squads sem quebrar o isolamento de dados sensiveis.
- Estrutura pesquisas em rodadas auditaveis, com checkpoints e dossie final.
