# 📑 Documentação do Processo: Implementação MCP Brasil no Conclave

Este documento registra os passos técnicos realizados para integrar o servidor `mcp-brasil` ao Conclave Data Lab como uma Prova de Conceito (POC).

## 📅 Data: 2026-04-26

## 1. Preparação do Ambiente
- **Diretório:** Criado `_conclave/runtime/lab/mcp-brasil/` para isolar o projeto.
- **Subdiretórios:**
  - `explorations/`: Scripts Python de teste.
  - `config/`: Futuras configurações de ambiente e chaves.

## 2. Instalação de Dependências
O pacote `mcp-brasil` foi instalado no ambiente virtual do projeto:
```bash
source .venv/bin/activate
pip install mcp-brasil
```
*Nota: A instalação foi realizada manualmente pelo usuário no terminal local para garantir acesso estável à rede.*

## 3. Desenvolvimento de Scripts de Ponte (Bridge)
Foram criados scripts `asyncio` usando a biblioteca `mcp` para interagir com o servidor via `stdio`:

- **`list_all_tools.py`**: Conecta ao servidor via `python -m mcp_brasil.server` e enumera as ferramentas de orquestração.
- **`list_features.py`**: Chama a ferramenta `listar_features` para mapear quais APIs governamentais estão ativas.
- **`consultar_selic.py`**: Primeira tentativa de extração de dados reais usando a ferramenta `bacen_indicadores_atuais`.

## 4. Descoberta de Ferramentas
Através do script de debug, identificamos que o servidor expõe ferramentas dinâmicas. As principais descobertas foram:
- `bacen_indicadores_atuais`: Panorama econômico (Selic, IPCA, Dólar).
- `brasilapi_consultar_taxa`: Consulta de taxas específicas por sigla.
- `camara_listar_deputados`: Busca na base da Câmara Federal.

## 5. Resultados e Limitações
- **Integração:** SUCESSO. Conseguimos inicializar o servidor e listar 307 ferramentas registradas.
- **Conexão Externa:** LIMITADA no ambiente de sandbox. As chamadas para as APIs reais (api.bcb.gov.br) falharam por DNS no ambiente restrito, mas funcionarão no terminal local do usuário.

## 6. Integração com Agentes
O agente **Data Mentor** (`_conclave/core/data-mentor.agent.md`) foi atualizado com o contexto deste projeto, tornando-se capaz de sugerir e revisar scripts que utilizem o `mcp-brasil`.
