from typing import Any
from pydantic import BaseModel

class ToolModel(BaseModel):
    name: str
    description: str
    inputSchema: dict[str, Any]
    node: str