# Standard library imports.
from pathlib import Path

# Third party imports.
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from starlette.requests import Request
from starlette.responses import JSONResponse

# Local imports.
from shinobi.tools import TOOLS

SKILLS_DIR = Path(__file__).parent / "skills"


def get_mcp_server() -> FastMCP:
    """Create, config, and return a FastMCP server.

    Returns:
        A FastMCP server instance that is configured with tools and skills.
    """

    # Init a MCP server.
    mcp = FastMCP(name="shinobi")

    # Register tools with the MCP server.
    for tool in TOOLS:
        mcp.add_tool(tool)

    # Register skills with the MCP server.
    mcp.add_provider(
        SkillsDirectoryProvider(
            roots=SKILLS_DIR,
        )
    )

    @mcp.custom_route("/api/v1/health", methods=["GET"])
    async def health(request: Request) -> JSONResponse:
        """Respond to health checks.

        Returns:
            A JSON-based response that indicates the service is running.
        """
        return JSONResponse(content={"status": "ok"})

    return mcp
