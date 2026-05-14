# Fonte: Como usar MCP para acessar dados do governo brasileiro (passo a passo)

**Autora:** Elisa Terumi
**URL:** https://elisaterumi.substack.com/p/como-usar-mcp-para-acessar-dados

---

## O que é MCP (relembrando)
O Model Context Protocol (MCP) é uma especificação aberta criada pela Anthropic que padroniza como modelos de linguagem se conectam a ferramentas e fontes de dados externas. MCP é para agentes de IA o que o USB foi para dispositivos. Um único padrão. Múltiplas possibilidades.

### Como funciona
Um servidor MCP expõe três elementos principais:
- **tools** → funções que o modelo pode executar
- **resources** → dados que pode consultar
- **prompts** → templates reutilizáveis

O modelo (ou agente) decide quando usar cada um, sem que o usuário precise orquestrar manualmente.

## Acessando dados públicos do Brasil
O Brasil tem um ecossistema robusto de dados públicos (Banco Central, IBGE, Portal da Transparência, INPE, DataSUS, etc). O problema histórico era a barreira técnica de cada API (conhecer endpoints, parâmetros, autenticação).

## É aí que entra mcp-brasil!
O projeto [mcp-brasil](https://github.com/jxnxts/mcp-brasil), criado por Jonatas Soares, organiza esse cenário. Ele empacota dezenas de APIs públicas brasileiras em um único servidor MCP, expondo centenas de tools prontas para uso via linguagem natural.

### Cobertura do mcp-brasil:
- **Economia e finanças:** Selic, IPCA, câmbio, PIB e séries temporais do Banco Central.
- **Legislativo:** Proposições, votações, despesas parlamentares.
- **Transparência:** Dados federais e de diversos tribunais de contas estaduais.
- **Saúde pública:** DataSUS, CNES, ANVISA, vacinação.
- **Meio ambiente e segurança:** INPE (queimadas/desmatamento), ANA, IPEA, SINESP.
