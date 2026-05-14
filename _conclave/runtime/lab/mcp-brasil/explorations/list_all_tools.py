import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def list_all_tools():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            print(f"Total: {len(tools.tools)}")
            for tool in tools.tools:
                print(f"TOOL_NAME: {tool.name}")

if __name__ == "__main__":
    asyncio.run(list_all_tools())
