# Brief de Pesquisa Genealogica

## Arquivo-base publicado

Usar `ambientes/Family Ties/03_fontes/fontes-e-acessos.md` como catalogo mestre de fontes e barreiras reais. Ele define:

- quais fontes oficiais entram primeiro
- onde a internet ajuda de verdade
- quais gargalos exigem busca presencial ou correspondente
- por que genealogia e cidadania nao devem ser confundidas

Usar tambem `ambientes/Family Ties/05_saidas/evidence-ledger.csv` como memoria compacta de decisao. Ele define o que ja foi confirmado, descartado, bloqueado ou negativado de forma qualificada.

## Unidades de busca

Toda pesquisa deve ser quebrada em:

1. Pessoa-alvo
2. Evento-alvo: nascimento, casamento, obito, naturalizacao, imigracao ou filiacao
3. Localidade-alvo
4. Janela temporal
5. Variacoes de nome
6. Documento esperado
7. Criterio de validacao
8. Linha de ledger relacionada, se existir

## Ordem de prioridade

1. Achado `A`/`B` ja existente no ledger.
2. Documento ja existente no ambiente.
3. Registro civil oficial.
4. Acervo publico oficial.
5. Paroquia/diocese/curia.
6. Catalogo genealogico indexado.
7. Fonte auxiliar: jornal, cemiterio, inventario.

## Regras de busca web

- Comecar por dominio oficial sempre que houver.
- Usar query por nome exato e tambem por variacao nominal.
- Variar cidade, estado e ano em blocos curtos.
- Se a cidade nao estiver confirmada, pesquisar pela menor unidade geografica confiavel disponivel.
- Nunca promover blog, forum ou assessoria a fonte final de regra.
- Nunca tratar `access_block` como negativo de acervo.
- Nunca repetir busca marcada como `qualified_negative` sem novo discriminador.

## Classificacao obrigatoria

Todo resultado precisa terminar como:

- `A`, `B`, `C`, `D` ou `X`;
- `qualified_negative`;
- `access_block`.

## Formato minimo de query

- `"nome completo" "tipo de registro" "cidade" "ano"`
- `"nome alternativo" "pai ou mae" "estado"`
- `"sobrenome" "paroquia" "municipio"`
- `"nome" "obito" "cartorio" "UF"`
- `"nome do ancestral" naturalizacao site:gov.br`
