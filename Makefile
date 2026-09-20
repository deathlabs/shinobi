# ---------------------------------------------------------
# Misc.
# ---------------------------------------------------------

# Use BASH as the default shell.
SHELL := /bin/bash

# Set the default Make target.
.DEFAULT_GOAL := build-and-start-container

# Tell Docker Compose to use Bake for builds.
export COMPOSE_BAKE := true

# Set the Docker Compose profile to "all" if one is not provided.
DOCKER_COMPOSE_PROFILE ?= all

# Set the host directory exposed to Shinobi as its workspace.
WORKSPACE ?= $(CURDIR)

# Normalize the workspace path and expose it to Docker Compose.
SHINOBI_WORKSPACE := $(abspath $(WORKSPACE))
export SHINOBI_WORKSPACE

# Centralize the Compose command so every Make target uses the same profile.
COMPOSE := docker compose --profile $(DOCKER_COMPOSE_PROFILE)

# Set the Docker Compose service to build and scan.
SHINOBI_SERVICE := shinobi-mcp

# Set the prefix used for SBOM file names.
SBOM_PREFIX ?= shinobi

# Set VEX metadata.
VEX_AUTHOR ?= Victor Fernandez III
VEX_ID_BASE ?= shinobi

# Set security scanner thresholds.
SEMGREP_CONFIG ?= auto
GRYPE_FAILURE_THRESHOLD ?= medium

# ---------------------------------------------------------
# Validate the workspace folder exists.
# ---------------------------------------------------------

.PHONY: validate-workspace
.SILENT: validate-workspace
validate-workspace:
	if [ ! -d "$(SHINOBI_WORKSPACE)" ]; then \
		echo "ERROR: Workspace does not exist: $(SHINOBI_WORKSPACE)" >&2; \
		exit 1; \
	fi

# ---------------------------------------------------------
# Update uv.lock.
# ---------------------------------------------------------

.PHONY: lock
.SILENT: lock
lock:
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	if [ -n "$$BUILD_CONTEXT" ] && [ -f "$$BUILD_CONTEXT/pyproject.toml" ]; then \
		echo "==> Locking $(SHINOBI_SERVICE) ($$BUILD_CONTEXT)"; \
		(cd "$$BUILD_CONTEXT" && uv lock); \
	fi

# ---------------------------------------------------------
# Check the source code for bugs.
# ---------------------------------------------------------

.PHONY: check
.SILENT: check
check:
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	if [ -n "$$BUILD_CONTEXT" ] && [ -f "$$BUILD_CONTEXT/pyproject.toml" ]; then \
		echo "==> Checking $(SHINOBI_SERVICE) ($$BUILD_CONTEXT)"; \
		ruff check --fix --exclude migrations "$$BUILD_CONTEXT"; \
	fi

# ---------------------------------------------------------
# Format the source code.
# ---------------------------------------------------------

.PHONY: format
.SILENT: format
format:
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	if [ -n "$$BUILD_CONTEXT" ] && [ -f "$$BUILD_CONTEXT/pyproject.toml" ]; then \
		echo "==> Formatting $(SHINOBI_SERVICE) ($$BUILD_CONTEXT)"; \
		ruff format --exclude migrations "$$BUILD_CONTEXT"; \
	fi

# ---------------------------------------------------------
# Check the source code for vulnerabilities.
# ---------------------------------------------------------

.PHONY: sast
.SILENT: sast
sast:
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	if [ -n "$$BUILD_CONTEXT" ] && [ -d "$$BUILD_CONTEXT" ]; then \
		echo "==> Running SAST on $(SHINOBI_SERVICE) ($$BUILD_CONTEXT)"; \
		semgrep scan --config $(SEMGREP_CONFIG) "$$BUILD_CONTEXT"; \
	fi

# ---------------------------------------------------------
# Build the container image.
# ---------------------------------------------------------

.PHONY: build-containers
.SILENT: build-containers
build-containers: lock check format
	$(COMPOSE) build $(SHINOBI_SERVICE)

# ---------------------------------------------------------
# Generate a VEX file for the container image.
# ---------------------------------------------------------

.PHONY: vex
.SILENT: vex

define VEX_FILTER
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": $$VEX_ID,
  "author": $$VEX_AUTHOR,
  "timestamp": $$VEX_TIMESTAMP,
  "version": 1,
  "statements": [
    .advisories[] | {
      "vulnerability": {
        "name": .vulnerability
      },
      "products": [
        .products[] | {
          "@id": .
        }
      ],
      "status": .status,
      "justification": .justification,
      "impact_statement": .impact_statement
    }
  ]
}
endef

export VEX_FILTER

vex:
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	if [ -z "$$BUILD_CONTEXT" ]; then \
		echo "ERROR: $(SHINOBI_SERVICE) does not define a build context." >&2; \
		exit 1; \
	fi; \
	VEX_YAML_PATH="$$BUILD_CONTEXT/vex.yaml"; \
	VEX_JSON_PATH="$$BUILD_CONTEXT/vex.json"; \
	if [ -f "$$VEX_YAML_PATH" ]; then \
		echo "==> Generating VEX for $(SHINOBI_SERVICE)"; \
		VEX_ID="$(VEX_ID_BASE)-$(SHINOBI_SERVICE)-$$(date +%s)"; \
		VEX_TIMESTAMP="$$(date -u +%Y-%m-%dT%H:%M:%SZ)"; \
		if yq --version 2>&1 | grep -qi 'mikefarah'; then \
			yq -o=json '.' "$$VEX_YAML_PATH"; \
		else \
			yq '.' "$$VEX_YAML_PATH"; \
		fi | jq \
			--arg VEX_ID "$$VEX_ID" \
			--arg VEX_AUTHOR "$(VEX_AUTHOR)" \
			--arg VEX_TIMESTAMP "$$VEX_TIMESTAMP" \
			"$$VEX_FILTER" \
			> "$$VEX_JSON_PATH"; \
	else \
		echo "==> No VEX file for $(SHINOBI_SERVICE); skipping"; \
	fi

# ---------------------------------------------------------
# Generate an SBOM for the container image.
# ---------------------------------------------------------

.PHONY: sbom
.SILENT: sbom
sbom: build-containers
	IMAGE_REF=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].image // empty'); \
	SBOM_PATH="$(SBOM_PREFIX)-sbom.json"; \
	if [ -z "$$IMAGE_REF" ]; then \
		echo "ERROR: Compose service $(SHINOBI_SERVICE) does not define an image." >&2; \
		exit 1; \
	fi; \
	echo "==> Generating SBOM for $(SHINOBI_SERVICE) ($$IMAGE_REF)"; \
	syft "$$IMAGE_REF" -o cyclonedx-json="$$SBOM_PATH"

# ---------------------------------------------------------
# Scan the container image's dependencies for CVEs.
# ---------------------------------------------------------

.PHONY: dependency-scan
.SILENT: dependency-scan
dependency-scan: sbom vex
	grype db update
	BUILD_CONTEXT=$$($(COMPOSE) config --format json | \
		jq -r '.services["$(SHINOBI_SERVICE)"].build.context // empty'); \
	SBOM_PATH="$(SBOM_PREFIX)-sbom.json"; \
	VEX_JSON_PATH="$$BUILD_CONTEXT/vex.json"; \
	echo "==> Scanning dependencies for $(SHINOBI_SERVICE)"; \
	if [ -n "$$BUILD_CONTEXT" ] && [ -f "$$VEX_JSON_PATH" ]; then \
		grype sbom:"$$SBOM_PATH" \
			--vex "$$VEX_JSON_PATH" \
			--fail-on $(GRYPE_FAILURE_THRESHOLD); \
	else \
		grype sbom:"$$SBOM_PATH" \
			--fail-on $(GRYPE_FAILURE_THRESHOLD); \
	fi

# ---------------------------------------------------------
# Build and start the container.
# ---------------------------------------------------------

.PHONY: build-and-start-container
.SILENT: build-and-start-container
build-and-start-container: validate-workspace dependency-scan
	echo "==> Using workspace: $(SHINOBI_WORKSPACE)"
	$(COMPOSE) up -d

# ---------------------------------------------------------
# Stop the container.
# ---------------------------------------------------------

.PHONY: stop-container
.SILENT: stop-container
stop-container:
	$(COMPOSE) down

# ---------------------------------------------------------
# Check the status of the container.
# ---------------------------------------------------------

.PHONY: status
.SILENT: status
status:
	$(COMPOSE) ps --format "table {{.Name}}\t{{.Ports}}\t{{.Status}}"

# ---------------------------------------------------------
# Test the container.
# ---------------------------------------------------------

.PHONY: tests
.SILENT: tests
tests:
	cd tests && uv run python main.py
