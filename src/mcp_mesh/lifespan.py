from contextlib import asynccontextmanager
from fastapi import FastAPI
import mcp_mesh.server

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mcp_mesh.server.run_server()

    yield