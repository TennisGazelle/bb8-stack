from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FakeRosBridgeClient:
    """Temporary ROS bridge for Milestone 0.

    Replace this with rclpy/rclcpp action/service clients in Milestone 3.
    """

    state: dict = field(
        default_factory=lambda: {
            "battery_percent": 84,
            "nearest_obstacle_m": 1.5,
            "tilt_deg": 0.0,
            "pose": {"x": 0.0, "y": 0.0, "yaw_deg": 0.0},
        }
    )

    async def get_state_snapshot(self) -> dict:
        return dict(self.state)

    async def get_battery_snapshot(self) -> dict:
        return {"battery_percent": self.state["battery_percent"]}

    async def stop_motion(self) -> dict:
        return {"ok": True, "status": "stopped"}

    async def roll_forward_safe(self, distance_m: float, speed_mps: float) -> dict:
        self.state["pose"]["x"] += distance_m
        return {"ok": True, "status": "rolled", "pose": self.state["pose"], "speed_mps": speed_mps}
