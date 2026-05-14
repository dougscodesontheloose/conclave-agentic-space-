# 2026-04-30 — Integração e Desacoplamento do Dashboard Cliff Palace

## Contexto e Motivação
A necessidade de manter o **Dashboard Financeiro do Cliff Palace** (raio-x financeiro) atualizado frequentemente tornou a manutenção manual via HTML insustentável. O painel operava com arrays estáticos hardcoded no código da página. Para alcançar uma solução sustentável, escalável e multiprocessada, toda a base de dados foi desacoplada da estrutura de visualização.

## Implementações Realizadas

### 1. Ingestão Automatizada e Portável (`ingest.py`)
Criamos o script raiz `ingest.py` no escopo do projeto Cliff Palace.
O pipeline Python foi desenvolvido usando PyYAML e implementa um sistema não-destrutivo:
- **Inteligência Estática Preservada**: O script realiza a leitura do `dashboard/dados.json` existente antes de reescrevê-lo, conservando anotações manuais complexas do usuário e análises da IA (tais como *anomalias* e rankings qualitativos de *vendors_top*).
- **Processamento Dinâmico**: Ele parseia os arquivos `_data/extratos-nubank-conta.yaml` e `_data/faturas-nubank-cartao.yaml`, realizando cruzamentos, agrupando métricas por meses, e extraindo picos e variâncias de fluxo.

### 2. Dashboard Dinâmico (Frontend)
Refatoração completa do `dashboard/index.html`. 
- Os containers e variáveis javascript fixas foram inteiramente removidos.
- A função assíncrona `loadData()` foi implementada, lendo de forma limpa o `dados.json` unificado.
- A arquitetura agora garante que o painel escale organicamente, adaptando os grids e renderizando visualmente não importando se o usuário subiu 6 ou 18 meses de dados.
- O visual rico e os modos (claro, escuro, etc.) foram mantidos intactos, respeitando o ecossistema local.

## Aprendizados e Consequências Arquiteturais
- **Data Boundaries**: A fronteira de dados operacionais e de exibição foi delimitada de forma muito clara. Agora a interface é imutável em termos de fonte de verdade, delegando a responsabilidade de formatação ao backend via Python no pipeline de ingestão.
- **Continuidade do Conclave**: Este movimento consolida o Cliff Palace como um esquadrão/agente autônomo e de alta capacidade que respeita as fronteiras e as "city limits" de sua pasta.
- **Self-Documenting**: A inclusão destas notas reforça o fluxo da Crônica e a rastreabilidade do projeto dentro do Conclave.
