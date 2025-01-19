from contextlib import asynccontextmanager
from fastapi import FastAPI
import mcp_mesh.server
import mcp_mesh.mcp_client
from mcp_mesh.configuration import config

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mcp_mesh.server.run_server()

    for mcp_server in config.mcp_servers:
        await mcp_mesh.mcp_client.run_mcp_client(mcp_server)

    yield