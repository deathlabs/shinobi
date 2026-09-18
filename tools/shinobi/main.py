# Local imports.
from shinobi.config import FASTMCP_PORT
from shinobi.server import get_mcp_server


def main():
    """Start the MCP server."""
    mcp = get_mcp_server()
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(FASTMCP_PORT),
    )


if __name__ == "__main__":
    main()
