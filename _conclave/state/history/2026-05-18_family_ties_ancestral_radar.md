# 2026-05-18 — Family Ties: Squad Ancestral Radar

## O que mudou

Foi adicionada uma capacidade nova ao ambiente `Family Ties`: um squad autocontido de pesquisa genealogica chamado `Ancestral Radar`, com um agente especializado em transformar lacunas da arvore em buscas parametrizadas por pessoa, evento, localidade, faixa temporal e fonte documental.

## Decisao arquitetural

O squad foi ancorado no arquivo publicado `ambientes/Family Ties/03_fontes/fontes-e-acessos.md`, que agora funciona como catalogo-base de fontes e criterio de priorizacao. A intencao foi evitar um design abstrato de "agente de cidadania" e criar uma automacao realmente orientada por evidencia genealogica.

## Capacidade adicionada

- checkpoint inicial para definir pessoa, linha e objetivo da rodada
- mapeamento de lacunas em matriz de busca
- pesquisa controlada com separacao entre fonte oficial, catalogo genealogico e fonte auxiliar
- consolidacao final em plano de expansao da arvore e fila documental

## Restricoes preservadas

- sem conclusao automatica de cidadania
- sem salto geracional
- com principio explicito de que conteudo externo e materia-prima, nunca autoridade
