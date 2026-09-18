# Contributing

## Ingredients

We assume you have or will get the following installed:

* `make`
* `docker`
* `syft`
* `grype`
* `jq`
* `yq`
* `codex`

## Setup

**Step 1.** Clone the `shinobi` repository.

```bash
git clone https://github.com/deathlabs/shinobi.git
```

**Step 2.** Change directories to the `tools` folder.

```bash
cd shinobi/tools
```

**Step 3.** Run `make`.

```bash
make
```

**Step 4.** Run the command below to confirm the server is working.

```bash
curl localhost:8002/api/v1/health
```

The server should return:

```json
{"status":"ok"}
```

**Step 5.** Change directories to `client` and run the command below to list the skills exposed by Shinobi.

```bash
uv run python main.py
```

Confirm that the Security Requirements Guide (SRG) and Security Technical Implementation Guide (STIG) skills are exposed by the MCP server.

The SRG/STIG skill is intended to support analysis against security guidance such as:

* Application Layer Gateway (ALG) SRG
* Application Programming Interface (API) SRG
* Application Security and Development (AS&D) STIG
* Container Platform SRG
* Network Infrastructure Policy STIG
* Azure SQL Database STIG

**Step 6.** Create the Codex configuration directory in your user profile if it does not already exist.

```bash
mkdir -p ~/.codex
```

Create or update `~/.codex/config.toml` and add the following MCP server configuration:

```toml
[mcp_servers.shinobi]
enabled = true
url = "http://localhost:8002/mcp"
```

This configuration is stored in your Codex user profile and makes the Shinobi MCP server available to Codex regardless of which workspace is open.

If Codex is already running, restart it after updating `~/.codex/config.toml`.

**Step 7.** Confirm Codex has loaded the Shinobi MCP server.

```bash
codex mcp list
```

Shinobi should appear as an enabled MCP server:

```text
Name     Url                        Status
shinobi  http://localhost:8002/mcp  enabled
```

**Step 8.** Start Codex.

```bash
codex
```

From the Codex TUI, run:

```text
/mcp verbose
```

Confirm that `shinobi` is connected and that the SRG/STIG skill is exposed as an MCP resource. For example:

```text
shinobi: connected (0 tools)

Resources:
  alg-stig/SKILL.md

Resource templates:
  skill://alg-stig/{path*}
```

**Step 9.** Test that Codex can discover and use the SRG/STIG skill.

For example, enter:

```text
Use the Shinobi MCP server to analyze this repository against the Application Security and Development STIG.
```

Codex should identify the SRG/STIG skill, read its `SKILL.md` resource, and follow its instructions when analyzing the repository.

The same workflow can be used for repositories or infrastructure that must be evaluated against the Container Platform SRG, Network Infrastructure Policy STIG, or Azure SQL Database STIG. For example:

```text
Use the Shinobi MCP server to analyze this repository against the Container Platform SRG.
```

or:

```text
Use the Shinobi MCP server to analyze this repository against the Network Infrastructure Policy STIG.
```

or:

```text
Use the Shinobi MCP server to analyze this repository against the Azure SQL Database STIG.
```

A successful test should include Codex reading:

```text
skill://alg-stig/SKILL.md
```

Codex may perform operations similar to:

```text
list_mcp_resource_templates

read_mcp_resource
  server: shinobi
  uri: skill://alg-stig/SKILL.md
```

A successful test confirms that:

1. Codex can connect to the Shinobi MCP server.
2. Codex can discover the SRG/STIG skill.
3. Codex can read the skill's `SKILL.md`.
4. Codex can apply the skill's instructions when analyzing a repository against supported guidance such as the AS&D STIG, Container Platform SRG, Network Infrastructure Policy STIG, and Azure SQL Database STIG.
