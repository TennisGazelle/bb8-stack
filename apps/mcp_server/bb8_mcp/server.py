from __future__ import annotations

from fastmcp import FastMCP

from .ros_bridge import FakeRosBridgeClient
from .safety.validators import validate_roll_forward

mcp = FastMCP("bb8-stack")
ros = FakeRosBridgeClient()


@mcp.tool
async def stop_now() -> dict:
    """Immediately stop robot motion."""
    return await ros.stop_motion()


@mcp.tool
async def roll_forward_safe(distance_m: float, speed_mps: float = 0.05) -> dict:
    """Roll forward using bounded, safety-checkable inputs."""
    validate_roll_forward(distance_m, speed_mps)
    return await ros.roll_forward_safe(distance_m=distance_m, speed_mps=speed_mps)


@mcp.tool
async def healthcheck() -> dict:
    """Return runtime health information."""
    return {"ok": True, "runtime": "fake", "ros_bridge": "fake"}


@mcp.resource("robot://state")
async def robot_state() -> dict:
    """Current robot state snapshot."""
    return await ros.get_state_snapshot()


@mcp.resource("robot://battery")
async def battery() -> dict:
    """Current battery state."""
    return await ros.get_battery_snapshot()


@mcp.prompt
def safety_review(action_name: str, action_args: dict, robot_state: dict) -> str:
    return f"""
Review whether this BB-8 robot action is safe.

Action: {action_name}
Arguments: {action_args}
Robot state: {robot_state}

Return one of: ALLOW, DENY, REQUIRE_HUMAN.
Include a short reason.
"""


if __name__ == "__main__":
    mcp.run()
