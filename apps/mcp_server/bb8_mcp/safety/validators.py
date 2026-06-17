from __future__ import annotations

from .limits import MAX_ROLL_DISTANCE_M, MAX_ROLL_SPEED_MPS


def validate_roll_forward(distance_m: float, speed_mps: float) -> None:
    if distance_m <= 0 or distance_m > MAX_ROLL_DISTANCE_M:
        raise ValueError(f"distance_m must be > 0 and <= {MAX_ROLL_DISTANCE_M}")
    if speed_mps <= 0 or speed_mps > MAX_ROLL_SPEED_MPS:
        raise ValueError(f"speed_mps must be > 0 and <= {MAX_ROLL_SPEED_MPS}")
