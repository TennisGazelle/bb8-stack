from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class McpServerConfig:
    host: str = "0.0.0.0"
    port: int = 8765


def load_config() -> McpServerConfig:
    load_dotenv()
    return McpServerConfig(
        host=os.getenv("BB8_MCP_HOST", "0.0.0.0"),
        port=int(os.getenv("BB8_MCP_PORT", "8765")),
    )
