import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_selic():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🚀 Consultando Indicadores Atuais (Bacen)...")
            
            # Chamando a ferramenta descoberta: bacen_indicadores_atuais
            response = await session.call_tool("bacen_indicadores_atuais", {})
            
            print("\n📊 Resultado:")
            for content in response.content:
                print(content.text)

if __name__ == "__main__":
    asyncio.run(get_selic())
