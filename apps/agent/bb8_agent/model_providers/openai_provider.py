from __future__ import annotations

from .base import ModelProvider


class OpenAIModelProvider(ModelProvider):
    """Placeholder provider.

    Keep this thin. The graph should not care which model provider is behind it.
    """

    def __init__(self, model: str) -> None:
        self.model = model

    async def propose_action(self, goal: str, robot_state: dict) -> dict:
        # TODO: wire OpenAI Responses API / LangChain chat model here.
        # Return the same shape as MockModelProvider.
        raise NotImplementedError("OpenAI provider is intentionally not wired in Milestone 0")
