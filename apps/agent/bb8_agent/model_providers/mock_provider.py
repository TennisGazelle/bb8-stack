from __future__ import annotations

from .base import ModelProvider


class MockModelProvider(ModelProvider):
    async def propose_action(self, goal: str, robot_state: dict) -> dict:
        normalized = goal.lower().strip()
        if "stop" in normalized:
            return {"name": "motion.stop_now", "args": {}}
        if "roll" in normalized or "forward" in normalized:
            return {
                "name": "motion.roll_forward_safe",
                "args": {"distance_m": 0.25, "speed_mps": 0.05},
            }
        return {"name": "diagnostics.healthcheck", "args": {}}
