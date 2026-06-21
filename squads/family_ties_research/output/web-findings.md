# Web Findings

## Resumo executivo

Esta rodada nao confirmou ainda um registro nominal confiavel, em aberto, para `Joao Moura da Silva`, `Maria das Gracas da Silva`, `Pedro Jacinto/Pedro Teixeira de Paula` ou `Herotildes Teixeira de Paula`. O que apareceu com valor alto foi a infraestrutura de busca:

- colecoes estaduais do FamilySearch para Alagoas, Pernambuco e Espirito Santo;
- caminhos oficiais para pedir certidoes e checar naturalizacao;
- arquivos publicos estaduais com acervo e referencia institucional.

Inferencia operacional: o bloqueio central continua sendo a falta de municipio exato e, no caso da linha materna, a variacao nominal.

## Achados por alvo

### FT-01 — Joao Moura da Silva, nascimento em Alagoas, 1940

**Queries usadas**

- `"Joao Moura da Silva" Alagoas 1940 nascimento`
- `"João Moura da Silva" "Alagoas" registro civil`
- `site:familysearch.org "Joao Moura da Silva" Alagoas`
- `Alagoas arquivo publico registro civil genealogia`

**Achados**

1. **FamilySearch — Brazil, Alagoas, Civil Registration, 1865-2022**
   - Tipo: colecao/indexador estadual
   - Link: https://www.familysearch.org/en/search/collection/1919217
   - Evidencia util: a colecao permite consulta por nome, sexo, data e local de nascimento. Isso e util para um alvo com data conhecida e municipio ainda ausente.
   - Limitacao: `Joao Moura da Silva` e nome comum; sem municipio o risco de falso positivo e alto.
   - Proximo passo: testar variacoes com data exata `1940-05-01` e usar qualquer documento interno que revele municipio antes de pedido cartorial.

2. **Arquivo Publico de Alagoas / CONARQ**
   - Tipo: referencia institucional
   - Link: https://dibrarq.arquivonacional.gov.br/index.php/arquivo-publico-do-estado-de-alagoas
   - Evidencia util: confirma a existencia do arquivo estadual como ponto de apoio para acervos historicos e orientacao de pesquisa.
   - Limitacao: nao entrega, por si, busca nominal imediata.
   - Proximo passo: usar como rota secundaria se FamilySearch e cartorios nao resolverem.

3. **Registro Civil oficial**
   - Tipo: orientacao oficial/procedimento
   - Link: https://www.registrocivil.org.br/
   - Evidencia util: e a via oficial nacional para localizar e pedir segunda via de certidoes brasileiras.
   - Limitacao: funciona melhor quando municipio e cartorio ja foram reduzidos.
   - Proximo passo: deixar pronto para acionamento depois da reducao do municipio.

**Leitura**

Este alvo tem superficie de busca suficiente, mas ainda precisa de um discriminador geografico.

### FT-02 — Maria das Gracas da Silva, nascimento em Pernambuco, 1947

**Queries usadas**

- `"Maria das Gracas da Silva" Pernambuco 1947 nascimento`
- `"Maria das Graças da Silva" Pernambuco registro civil`
- `site:familysearch.org "Maria das Gracas" Pernambuco`
- `Pernambuco arquivo público genealogia registro civil`

**Achados**

1. **FamilySearch — Brazil, Pernambuco, Civil Registration, 1810-2014**
   - Tipo: colecao/indexador estadual
   - Link: https://www.familysearch.org/en/search/collection/1916041
   - Evidencia util: a colecao aceita nome, ano e localidade. Para `1947-12-24`, isso oferece o melhor ponto de partida aberto para localizar o nascimento.
   - Limitacao: sem municipio, a combinacao nome comum + estado grande gera muito ruido.
   - Proximo passo: testar `Birth Place` quando surgir qualquer pista municipal.

2. **Acervo PE / Arquivo Publico Estadual Jordao Emerenciano**
   - Tipo: referencia institucional
   - Link: http://www.acervope.com.br/
   - Evidencia util: oferece caminho institucional para acervos historicos pernambucanos.
   - Limitacao: nao substitui uma colecao nominal bem indexada.
   - Proximo passo: usar se a linha apontar para municipio ou comarca especifica em Pernambuco.

3. **Registro Civil oficial**
   - Tipo: orientacao oficial/procedimento
   - Link: https://www.registrocivil.org.br/
   - Evidencia util: canal oficial para pedido de certidao quando a busca ja estiver estreitada.
   - Limitacao: nao resolve sozinho a falta de municipio.
   - Proximo passo: acionar apos filtrar cartorio provavel.

**Leitura**

O alvo continua promissor, mas depende fortemente de municipio, nome de solteira completo ou comarca.

### FT-03 — Pedro Jacinto de Paula / Pedro Teixeira de Paula, Espirito Santo, circa 1926

**Queries usadas**

- `"Pedro Jacinto de Paula" "Espirito Santo" 1926`
- `"Pedro Teixeira de Paula" "Espirito Santo" 1926`
- `"Pedro Jacinta de Paula" registro`
- `Espírito Santo arquivo público genealogia registro civil`

**Achados**

1. **FamilySearch — Brazil, Espírito Santo, Civil Registration, 1875-2007**
   - Tipo: colecao/indexador estadual
   - Link: https://www.familysearch.org/en/search/collection/1932363
   - Evidencia util: cobre o periodo necessario e aceita busca por nome e localidade; e o melhor campo aberto para testar a variacao `Jacinto` versus `Teixeira`.
   - Limitacao: nenhuma busca aberta desta rodada retornou um hit nominal confiavel via indexacao web externa.
   - Proximo passo: repetir a busca dentro da colecao com variantes e, se possivel, com municipio derivado de outro documento da familia.

2. **APEES — Registros Civis**
   - Tipo: referencia institucional
   - Link: https://ape.es.gov.br/registros-civis
   - Evidencia util: o Arquivo Publico do Estado do Espirito Santo centraliza trilhas de acesso a registros civis e acervos relacionados.
   - Limitacao: a pagina e institucional; nao equivale a resultado nominal.
   - Proximo passo: usar como ponte para consulta dirigida se a busca nominal continuar bloqueada.

**Leitura**

Aqui o gargalo nao e falta de fonte, e sim a identidade oscilante do nome. Sem resolver `Jacinto` versus `Teixeira`, a busca segue suscetivel a perda de sinal.

### FT-04 — Herotildes Teixeira de Paula, filiacao aberta

**Queries usadas**

- `"Herotildes Teixeira de Paula"`
- `"Herotildes de Paula" filiacao`
- `site:familysearch.org "Herotildes Teixeira de Paula"`

**Achados**

1. **Nenhum hit nominal confiavel em busca aberta**
   - Tipo: bloqueio
   - Evidencia util: a ausencia de hit confiavel indica que a web aberta nao esta oferecendo superficie suficiente para atacar este alvo por nome puro.
   - Limitacao: nao prova ausencia documental; prova apenas baixa encontrabilidade na camada aberta pesquisada.
   - Proximo passo: atacar `Herotildes` indiretamente, por casamento, obito, certidoes dos filhos e pela mesma malha de fontes do Espirito Santo.

2. **FamilySearch — Brazil, Espírito Santo, Civil Registration, 1875-2007**
   - Tipo: colecao/indexador estadual
   - Link: https://www.familysearch.org/en/search/collection/1932363
   - Evidencia util: serve como rota indireta para localizar casamento, obito ou registro relacionado que revele a filiacao.
   - Limitacao: sem localidade e sem intervalo temporal mais fechado, a busca nominal aberta permanece fraca.
   - Proximo passo: reabrir o alvo quando um documento da linha materna trouxer municipio ou variante adicional.

**Leitura**

Este alvo nao avancou nominalmente. O caminho mais forte e retroceder para documentos derivados, nao insistir na web aberta pelo nome isolado.

### FT-05 — Linha de apoio institucional e triagem juridica

**Queries usadas**

- `site:gov.br Arquivo Nacional estrangeiros naturalizacao familysearch`
- `site:registrocivil.org.br segunda via certidao busca`
- `site:gov.br certidao positiva negativa naturalizacao`

**Achados**

1. **MJSP — Certidoes de naturalizacao**
   - Tipo: orientacao oficial atual
   - Link: https://www.gov.br/mj/pt-br/assuntos/seus-direitos/migracoes/naturalizacao/certidoes
   - Evidencia util: em 2026-05-18 a pagina informa emissao de certidoes positiva e negativa e menciona consulta via DataNaturalizacao, inclusive com ate cinco variantes nominais.
   - Limitacao: so vira acao concreta quando houver suspeita razoavel de ancestral estrangeiro na linha.
   - Proximo passo: manter como ferramenta pronta para a fase de cidadania, nao para esta rodada inicial.

2. **Policia Federal — FAQ sobre imigrante**
   - Tipo: orientacao oficial atual
   - Link: https://www.gov.br/pf/pt-br/assuntos/imigracao/perguntas-frequentes
   - Evidencia util: para registros anteriores a 1986, a orientacao oficial remete ao Arquivo Nacional.
   - Limitacao: e uma ponte institucional, nao uma base nominal de genealogia.
   - Proximo passo: usar se a linha documental revelar necessidade de trilha migratoria ou de naturalizacao.

3. **Arquivo Nacional + FamilySearch**
   - Tipo: noticia/orientacao institucional
   - Link: https://www.gov.br/arquivonacional/pt-br/canais_atendimento/imprensa/noticias/arquivo-nacional-e-family-search-disponibilizam-documentos-de-registro-civil-para-pesquisa-online
   - Evidencia util: reforca a integracao de acesso a registros civis e acervos historicos relevantes.
   - Limitacao: util como mapa de ecossistema, nao como prova individual.
   - Proximo passo: manter como referencia de cobertura e legitimidade das buscas.

## Bloqueios

1. **Municipio ausente em FT-01 e FT-02**
   - Sem municipio, a busca nominal em estados grandes perde precisao.

2. **Conflito nominal em FT-03**
   - `Pedro Jacinto` versus `Pedro Teixeira` afeta diretamente a recuperacao do registro.

3. **Baixa encontrabilidade por nome puro em FT-04**
   - `Herotildes` nao gerou hit aberto confiavel nesta rodada.

4. **Busca aberta nao equivale a busca dentro da colecao**
   - A camada web encontrou a estrutura de acervo, mas nao substitui pesquisa manual dentro das colecoes do FamilySearch e pedidos dirigidos a cartorios/arquivos.

## Proximos passos sugeridos

1. Reabrir os documentos internos da linha paterna e materna buscando qualquer mencao de municipio, distrito, freguesia ou cartorio.
2. Rodar busca manual dentro das colecoes do FamilySearch com data exata e variantes nominais, especialmente para FT-01, FT-02 e FT-03.
3. Se surgir municipio provavel:
   - acionar `registrocivil.org.br` para pedido de certidao;
   - ou partir para arquivo/cartorio estadual correspondente.
4. Para `Herotildes`, parar de insistir no nome isolado e buscar a filiacao por casamento, obito ou certidoes dos filhos.
5. Guardar as rotas de naturalizacao apenas como camada posterior, quando houver evidencia de ancestral estrangeiro.
