# Standard library imports.
from asyncio import run
from os import getenv

# Third party imports.
from fastmcp import Client
from fastmcp.utilities.skills import list_skills

# Constants.
SERVER = "Shinobi MCP Server"
URL = getenv("MCP_URL", "http://localhost:8002/mcp")
HEALTH_ENDPOINT = getenv("HEALTH_URL", "http://localhost:8002/api/v1/health")


async def main() -> None:

    async with Client(URL) as client:
        # Test 1: the server must expose at least one skill.
        skill_list = await list_skills(client)
        skill_exposure_error = f"The {SERVER} is not exposing any skills."
        assert len(skill_list) > 0, skill_exposure_error
        skills = ", ".join([skill.name for skill in skill_list])
        print(f"PASS: The {SERVER} is exposing: {skills}")

        for skill in skill_list:
            mcp_resource = f"skill://{skill.name}/SKILL.md"
            mcp_resource_contents = await client.read_resource(mcp_resource)

            # Test 2: the skill must be readable.
            skill_read_error = f"The '{skill.name}' skill cannot be read."
            assert mcp_resource_contents, skill_read_error
            print(f"PASS: The {skill.name} skill can be read")

            # Test 3: the skill cannot be empty.
            empty_skill_error = f"The {skill.name} skill is empty."
            assert mcp_resource_contents[0].text, empty_skill_error
            print(f"PASS: The {skill.name} skill is not empty")

if __name__ == "__main__":
    run(main())
