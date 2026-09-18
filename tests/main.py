# Standard library imports.
from asyncio import run
from os import getenv

# Third party imports.
from fastmcp import Client
from fastmcp.utilities.skills import list_skills

MCP_URL = getenv("MCP_URL", "http://localhost:8002/mcp")
SKILL_NAME = "alg-stig"


async def main() -> None:
    async with Client(MCP_URL) as client:
        # Test 1: Confirm the SRG/STIG skill is exposed.
        skills = await list_skills(client)
        skill = next(
            (skill for skill in skills if skill.name == SKILL_NAME),
            None,
        )

        assert skill is not None, f"Skill '{SKILL_NAME}' was not found."
        print(f"PASS: Found skill '{skill.name}'.")

        # Test 2: Confirm the skill instructions can be read.
        contents = await client.read_resource(
            f"skill://{SKILL_NAME}/SKILL.md",
        )

        assert contents, f"Skill '{SKILL_NAME}' returned no content."
        assert contents[0].text, f"Skill '{SKILL_NAME}' SKILL.md is empty."

        print(f"PASS: Read skill://{SKILL_NAME}/SKILL.md.")


if __name__ == "__main__":
    run(main())
