import os
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from mcp_mesh.configuration import config
from mcp_mesh.server import node
from mcp_mesh.models import ToolModel

async def run_mcp_client(mcp_server: StdioServerParameters):
    mcp_server.env = mcp_server.env or {}
    mcp_server.env.update(os.environ)

    async with stdio_client(mcp_server) as client:
        async with ClientSession(*client) as session:
            await session.initialize()

            tools = await session.list_tools()
            for tool in tools.tools:
                model = ToolModel(name=tool.name, description=tool.description or "tool description not available", node=node.node.id.hex(), inputSchema=tool.inputSchema)

                await node.set(tool.name, model.model_dump_json())