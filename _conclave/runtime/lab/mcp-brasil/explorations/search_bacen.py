import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def search_bacen():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🔍 Buscando ferramentas do Bacen...")
            
            response = await session.call_tool("search_tools", {
                "query": "bacen"
            })
            
            print("\n🛠️ Ferramentas encontradas:")
            for content in response.content:
                print(content.text)

if __name__ == "__main__":
    asyncio.run(search_bacen())
