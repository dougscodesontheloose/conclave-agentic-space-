# 🇧🇷 MCP Brasil - Prova de Conceito (Lab)

Este projeto visa integrar o servidor `mcp-brasil` ao Conclave para acessar dados públicos brasileiros.

## 🚀 Como Iniciar

Como o ambiente do terminal pode ter restrições de rede, execute o seguinte comando no seu terminal local (onde você tem acesso à internet):

```bash
source .venv/bin/activate
pip install mcp-brasil
```

## 📂 Estrutura
- `explorations/`: Scripts de teste para validar a conexão com as ferramentas.
- `config/`: Configurações de cache e datasets locais.

## 🛠️ Ferramentas Disponíveis (Exemplos)
- **Banco Central:** Selic, IPCA, Câmbio.
- **Câmara dos Deputados:** Proposições, votações.
- **Transparência:** Gastos governamentais.

## 🧠 Próximos Passos
1. Validar a instalação do pacote.
2. Criar um script "Bridge" que permita ao Conclave chamar o servidor MCP via Python.
