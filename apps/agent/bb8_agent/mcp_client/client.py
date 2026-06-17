from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FakeRobotClient:
    """Milestone 0 fake MCP/robot client.

    This mirrors the eventual MCP tool/resource surface without requiring a running
    MCP server or ROS graph.
    """

    state: dict = field(
        default_factory=lambda: {
            "battery_percent": 84,
            "nearest_obstacle_m": 1.5,
            "tilt_deg": 0.0,
            "pose": {"x": 0.0, "y": 0.0, "yaw_deg": 0.0},
            "last_motion": None,
        }
    )

    async def read_resource(self, uri: str) -> dict:
        if uri == "robot://state":
            return dict(self.state)
        if uri == "robot://battery":
            return {"battery_percent": self.state["battery_percent"]}
        raise ValueError(f"Unknown fake resource URI: {uri}")

    async def call_tool(self, name: str, args: dict) -> dict:
        if name == "motion.stop_now":
            self.state["last_motion"] = {"kind": "stop"}
            return {"ok": True, "status": "stopped"}

        if name == "motion.roll_forward_safe":
            distance_m = float(args["distance_m"])
            self.state["pose"]["x"] += distance_m
            self.state["last_motion"] = {"kind": "roll_forward_safe", **args}
            return {"ok": True, "status": "rolled", "pose": self.state["pose"]}

        if name == "diagnostics.healthcheck":
            return {"ok": True, "status": "fake robot healthy"}

        raise ValueError(f"Unknown fake tool: {name}")
