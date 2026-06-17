#!/usr/bin/env bash
set -euo pipefail
python -m compileall apps/agent apps/mcp_server
python -m pytest apps/agent apps/mcp_server
