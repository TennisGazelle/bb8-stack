from __future__ import annotations

from abc import ABC, abstractmethod


class ModelProvider(ABC):
    """Provider-agnostic boundary for model calls."""

    @abstractmethod
    async def propose_action(self, goal: str, robot_state: dict) -> dict:
        """Return a proposed action dict."""
