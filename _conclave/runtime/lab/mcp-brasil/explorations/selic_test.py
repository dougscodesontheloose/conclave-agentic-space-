"""
POC: Consulta de Taxa Selic via mcp-brasil
Este script demonstra como poderemos chamar o servidor MCP diretamente do Python
quando a integração estiver concluída.
"""

import sys
import subprocess
import json

def get_selic_now():
    print("Iniciando consulta ao servidor mcp-brasil...")
    
    # Nota: No futuro, usaremos o mcp-client oficial. 
    # Por enquanto, esta é uma demonstração do que o comando fará.
    
    # Exemplo de comando que listar as ferramentas para provar que o servidor está vivo
    try:
        # Comando hipotético para testar se o servidor responde
        # mcp-brasil geralmente é chamado via stdio pelo Claude, 
        # mas podemos usar o CLI dele se disponível.
        print("Dica: Use 'python -m mcp_brasil.server' para ver o status.")
        
    except Exception as e:
        print(f"Erro ao conectar com o servidor: {e}")

if __name__ == "__main__":
    get_selic_now()
