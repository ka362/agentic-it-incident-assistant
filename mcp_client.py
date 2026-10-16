import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = StdioServerParameters(
        command=sys.executable,
        args=["-m", "mcp_server.server"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            for tool in tools.tools:
                print("Tool:", tool.name)

            result = await session.call_tool(
                "check_status",
                {"application_name": "Payment API"}
            )

            print("Result:", result.content)


if __name__ == "__main__":
    asyncio.run(main())