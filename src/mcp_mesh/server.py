from kademlia.network import Server
from loguru import logger
from mcp_mesh.configuration import config


node = Server()

async def run_server():
    await node.listen(5678)
    logger.info("Server started and listening on port 5678")
    
    # bootstrap node
    initial = config.bootstrap.bootstrap_node.split(":")
    await node.bootstrap([(initial[0], int(initial[1]))])

    return node
