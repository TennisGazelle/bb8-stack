from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class AgentConfig:
    model_provider: str
    openai_model: str
    mcp_transport: str
    mcp_http_url: str
    memory_db: Path


def load_config() -> AgentConfig:
    load_dotenv()
    return AgentConfig(
        model_provider=os.getenv("BB8_MODEL_PROVIDER", "mock"),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        mcp_transport=os.getenv("BB8_MCP_TRANSPORT", "fake"),
        mcp_http_url=os.getenv("BB8_MCP_HTTP_URL", "http://localhost:8765/mcp"),
        memory_db=Path(os.getenv("BB8_MEMORY_DB", "memory/bb8_memory.sqlite3")),
    )
