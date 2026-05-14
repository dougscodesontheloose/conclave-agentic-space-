import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def list_features():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🚀 Listando Features (APIs) disponíveis no mcp-brasil...")
            
            response = await session.call_tool("listar_features", {})
            
            print("\n📊 Features (Bacen):")
            for content in response.content:
                for line in content.text.split('\n'):
                    if 'bacen' in line.lower():
                        print(line)

if __name__ == "__main__":
    asyncio.run(list_features())
