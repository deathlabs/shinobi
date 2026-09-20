# `shinobi`
[![CI Pipeline](https://github.com/deathlabs/shinobi/actions/workflows/ci.yml/badge.svg)](https://github.com/deathlabs/shinobi/actions/workflows/ci.yml)  

Shinobi is an MCP server that exposes tools and skills that agents can use to evaluate cloud-native platforms for compliance with applicable Security Requirements Guides (SRGs) and Security Technical Implementation Guides (STIGs).

## Quickstart

This section describes *one* way to get Shinobi up and running. These instructions assume you are using Windows Subsystem for Linux (WSL), VS Code, and OpenAI Codex. They also assume you have or will get the following software installed: [`make`](https://www.gnu.org/software/make/), [Docker](https://docs.docker.com/get-started/get-docker/), [Syft](https://github.com/anchore/syft#installation), [Grype](https://github.com/anchore/grypet#installation), [`jq`](https://jqlang.org/download/), [`yq`](https://github.com/mikefarah/yq), [VS Code](https://code.visualstudio.com/), and the [VS Code Extension for Codex](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt&utm_source=gemini).

Syft and Grype were included in Shinobi's development workflow to help identify and reduce security risks introduced by Shinobi itself.

**Again, WSL, VS Code, and OpenAI Codex are NOT required to use Shinobi. They are only relevant to this Quickstart.**

**Step 1.** Clone the repository.

```bash
git clone https://github.com/deathlabs/shinobi.git
```

**Step 2.** Change directories to the repository you just downloaded. 

```bash
cd shinobi
```

**Step 3.** Make a file called `.env` in the `src` folder using the `.env.example` as a reference. Feel free to change the default values it defines.

```bash
cp src/.env.example src/.env
```

**Step 4.** Use `make` and the provided Makefile to build, start, and test the Shinobi MCP server. The default Make target will also download and start the Terraform MCP server maintained by Hashicorp.

```bash
make 
```

**Step 5.** Enable **Run Codex In Windows Subsystem For Linux** inside your VS Code extension settings.

**Step 6.** Open the repository in VS Code. The Shinobi repository includes a Codex agent definition for `compliance_analyst` under `.codex/agents/`. 

**Step 7.** Give Codex a prompt similar to the one below.

> Have `compliance_analyst` evaluate the Application Layer Gateway (ALG) Terraform module in `examples/modules/` for compliance with the ALG Security Requirements Guide (SRG) in `examples/benchmarks/`. Then, generate a SRG checklist and save it under `examples/checklists/`.
