# Contributing

## Ingredients

We assume you have or will get the following installed:

* `make`
* `docker`
* `syft`
* `grype`
* `jq`
* `yq`

## Setup

**Step 1.** Clone the `shinobi` repository. 

```bash
git clone https://github.com/deathlabs/shinobi.git
```

**Step 2.** Change directories to the `tools` folder. 
```bash
cd shinobi/tools
```

**Step 3.** Create a file called `.env` file and add the content below to it.

```bash
export AZURE_TENANT_ID="<INSERT_VALUE>"
export AZURE_CLIENT_ID="<INSERT_VALUE>"
export AZURE_CLIENT_SECRET="<INSERT_VALUE>"

export AZURE_CLOUD="<INSERT_VALUE>"
export AZURE_TOKEN_SCOPES="https://cognitiveservices.azure.us/.default"

export AZURE_OPENAI_ENDPOINT="https://<INSERT_VALUE>.openai.azure.us/"
export AZURE_OPENAI_API_VERSION="<INSERT_VALUE>"
export AZURE_OPENAI_DEPLOYMENT="shinobi"
export MCP_SERVER_ENDPOINT="http://shinobi-tools:8282/sse"
```

**Step 4.** Run `make`. 

**Step 5.** Run the command below to confirm the agent is working. 
```bash
curl localhost:8002/api/v1/health
```
