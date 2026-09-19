# `shinobi`

Shinobi is a Model Context Protocol (MCP) server designed to provide agents the tools and skills required to assess compliance with the following security benchmarks. 

* Application Layer Gateway SRG
* Application Programming Interface SRG
* Application Security and Development STIG
* Container Platform SRG
* Microsoft Azure SQL STIG
* Network Infrastructure Policy STIG

## Prerequisites

Ensure the following dependencies are installed before getting started:

* Make
* Docker
* Syft
* Grype
* jq
* yq
* VS Code
* [VS Code Extension for Codex](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt&utm_source=gemini)

## Quickstart

**Step 1.** Clone the repository.

```bash
git clone https://github.com/deathlabs/shinobi.git
cd shinobi
```

**Step 2.** Build and start the Shinobi MCP server.

```bash
make start-containers
```

**Step 3.** Run the command below to verify the Shinobi MCP server is running. 

```bash
curl localhost:8002/api/v1/health
```

You should get output similar to below. 

```json
{"status":"ok"}
```

**Step 4.** Run the command below to verify the Shinobi MCP server is running as expected. This specific Make target will print the names of the skills Shinobi provides.

```bash
make tests
```

**Step 5.** Create your Codex configuration directory.

```bash
mkdir ~/.codex
```

**Step 6.** Create a file called `~/.codex/config.toml` and add the Shinobi MCP server to it. 

```toml
[mcp_servers.shinobi]
enabled = true
url = "http://localhost:8002/mcp"
```

**Step 7.** Enable **Run Codex In Windows Subsystem For Linux** inside your VS Code extension settings.


**Step 8.** Open VS Code and prompt Codex to invoke the tools and skills provided by the Shinobi MCP server.

```text
Use the shinobi MCP server to evaluate the ALG Terraform module in ./modules/ for compliance with the ALG SRG in ./benchmarks/ and generate a checklist for it.
```
