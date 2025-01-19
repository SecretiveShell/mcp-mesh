from os import getenv
from typing import Annotated, Optional, Union
from mcp import StdioServerParameters
from pydantic import BaseModel, Field

class BootstrapConfig(BaseModel):
    bootstrap_node: str = getenv("BOOTSTRAP_NODE", "localhost:5678")
    
MCPServer = Annotated[
    Union[StdioServerParameters],
    Field(description="MCP server configuration"),
]

class Config(BaseModel):
    bootstrap: BootstrapConfig = BootstrapConfig()
    mcp_servers: list[MCPServer] = Field(default_factory=list)

config_json = getenv("CONFIG")

if config_json is not None:
    config = Config.model_validate_json(config_json)

else:
    config = Config.model_validate({})


# cannot start without a bootstrap node
assert config.bootstrap.bootstrap_node is not None
