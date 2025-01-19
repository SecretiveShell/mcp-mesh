import json
from fastapi import FastAPI

from mcp_mesh.lifespan import lifespan
from mcp_mesh import server
from mcp_mesh.configuration import config

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/nodes")
async def read_nodes():
    return {"nodes": server.node.bootstrappable_neighbors()}

@app.get("/config")
async def read_config():
    return {"config": config.model_dump()}

@app.get("/tools")
async def read_tools():
    server.node.refresh_table()
    
    tools = dict(server.node.storage.data).values()
    print(tools)

    for tool in tools:
        tool = json.loads(tool[1])

    return {"tools": tools}