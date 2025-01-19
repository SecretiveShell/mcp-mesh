from kademlia.network import Server
from loguru import logger
import asyncio
import os

node = Server()

async def run_server():
    await node.listen(5678)
    logger.info("Server started and listening on port 5678")
    
    # bootstrap node
    bootstrap = os.getenv("BOOTSTRAP_NODE", "localhost:5678")
    bootstrap = bootstrap.split(":")
    await node.bootstrap([(bootstrap[0], int(bootstrap[1]))])
