import asyncio
from kademlia.network import Server
from loguru import logger
# this is a small script to create the initial bootstrap node


async def run_create_initial_node():
    # Create a node and start listening on port 5678
    node = Server()
    await node.listen(5678)

    logger.info("Initial node created and listening on port 5678")

    await asyncio.Future()

def create_initial_node():
    asyncio.run(run_create_initial_node())
