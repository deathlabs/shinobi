# Standard library imports.
from asyncio import run
from os import getenv
    
# Third party imports.
from fastmcp import Client
from fastmcp.utilities.skills import list_skills

MCP_URL = getenv("MCP_URL", "http://localhost:8002/mcp")


async def main() -> None:
    async with Client(MCP_URL) as client:
        skills = await list_skills(client)

        for skill in skills:
            print(f"{skill.name}: {skill.description}")


if __name__ == "__main__":
    run(main())
