import uvicorn
from loguru import logger

def main():
    logger.info("Starting MCP mesh node")
    uvicorn.run("mcp_mesh.api:app", host="0.0.0.0", port=8080)