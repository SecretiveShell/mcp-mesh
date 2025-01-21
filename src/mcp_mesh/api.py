import json
from fastapi import FastAPI
import kademlia.node

from mcp_mesh.lifespan import lifespan
from mcp_mesh import server
from mcp_mesh.configuration import config

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/nodes")
async def read_nodes() -> list:
    nodes = []
    nodeitems = [bucket.nodes.values() for bucket in server.node.protocol.router.buckets]
    item: kademlia.node.Node
    for node in nodeitems:
        for item in node:
            nodes.append({
                "ip": item.ip,
                "id": item.id.hex(),
                "port": item.port,
            })

    return nodes

@app.get("/self")
async def read_self():
    return {
        "self": server.node.node.id.hex(),
        "bootstrap": config.bootstrap.bootstrap_node,
    }

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