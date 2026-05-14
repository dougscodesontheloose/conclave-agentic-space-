import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_deputados():
    server_params = StdioServerParameters(
        command="./.venv/bin/python",
        args=["-m", "mcp_brasil.server"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🏛️ Consultando Deputados (Câmara)...")
            
            # Ferramenta da Câmara: camara_listar_deputados
            try:
                response = await session.call_tool("camara_listar_deputados", {
                    "nome": "Tiririca"
                })
                
                print("\n📊 Resultado:")
                for content in response.content:
                    print(content.text)
            except Exception as e:
                print(f"\n❌ Erro na consulta: {e}")

if __name__ == "__main__":
    asyncio.run(get_deputados())
