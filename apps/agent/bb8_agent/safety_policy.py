from __future__ import annotations


def deterministic_safety_gate(action: dict, robot_state: dict) -> tuple[str, str]:
    """Return (verdict, reason)."""

    name = action.get("name", "")
    args = action.get("args", {})

    if name.startswith("motion."):
        if robot_state.get("battery_percent", 100) < 10:
            return "deny", "battery below motion threshold"
        if robot_state.get("nearest_obstacle_m", 999.0) < 0.25:
            return "deny", "nearest obstacle is too close"
        if abs(robot_state.get("tilt_deg", 0.0)) > 20:
            return "deny", "tilt exceeds safe limit"

    if name == "motion.roll_forward_safe":
        distance_m = float(args.get("distance_m", 0.0))
        speed_mps = float(args.get("speed_mps", 0.0))
        if distance_m <= 0 or distance_m > 2.0:
            return "deny", "distance_m outside safe range"
        if speed_mps <= 0 or speed_mps > 0.25:
            return "deny", "speed_mps outside safe range"

    return "allow", "deterministic safety checks passed"
