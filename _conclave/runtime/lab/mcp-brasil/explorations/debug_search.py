import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def debug_search():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🔍 Debugging search_tools...")
            
            try:
                response = await session.call_tool("search_tools", {
                    "query": "economia"
                })
                
                print(f"\nResponse type: {type(response)}")
                print(f"Content: {response.content}")
                
                if not response.content:
                    print("Nenhum conteúdo retornado.")
            except Exception as e:
                print(f"Erro ao chamar tool: {e}")

if __name__ == "__main__":
    asyncio.run(debug_search())
