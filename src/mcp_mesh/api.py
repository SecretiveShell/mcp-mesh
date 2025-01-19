from fastapi import FastAPI

from mcp_mesh.lifespan import lifespan
from mcp_mesh import server

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/nodes")
async def read_nodes():
    return {"nodes": server.node.bootstrappable_neighbors()}