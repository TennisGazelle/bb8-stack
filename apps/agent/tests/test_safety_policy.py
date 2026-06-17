from apps.agent.bb8_agent.safety_policy import deterministic_safety_gate


def test_roll_forward_allowed_for_safe_state():
    verdict, reason = deterministic_safety_gate(
        {"name": "motion.roll_forward_safe", "args": {"distance_m": 0.25, "speed_mps": 0.05}},
        {"battery_percent": 90, "nearest_obstacle_m": 1.0, "tilt_deg": 0.0},
    )
    assert verdict == "allow"
    assert "passed" in reason


def test_roll_forward_denied_for_obstacle():
    verdict, reason = deterministic_safety_gate(
        {"name": "motion.roll_forward_safe", "args": {"distance_m": 0.25, "speed_mps": 0.05}},
        {"battery_percent": 90, "nearest_obstacle_m": 0.1, "tilt_deg": 0.0},
    )
    assert verdict == "deny"
    assert "obstacle" in reason
