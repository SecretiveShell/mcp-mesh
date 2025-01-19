# mcp-mesh

MCP mesh is a mesh overlay network for using MCP servers across multiple devices.

## The goal

- mesh p2p for tool calling
- sse/stdio gateway for incoming clients
- sse/stdio client worker nodes for hosting MCP servers

## How it works

### Bootstrap node

The bootstrap node is the first node to join the mesh. It is responsible for creating the initial node and maintaining the mesh.

### Nodes

Nodes host MCP servers and register themselves/their tools with the DHT.

## How to run

See the example [compose.yml](compose.yml) file for how to run the bootstrap node and the nodes.
