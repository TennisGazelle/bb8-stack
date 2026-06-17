#!/usr/bin/env bash
set -euo pipefail
python -m apps.agent.bb8_agent.main --goal "${GOAL:-roll forward a little}" --transport "${BB8_MCP_TRANSPORT:-fake}"
