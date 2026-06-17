from __future__ import annotations

from typing import Literal, TypedDict


SafetyVerdict = Literal["allow", "deny", "require_human"]


class Bb8AgentState(TypedDict, total=False):
    goal: str
    transport: str
    robot_state: dict
    proposed_action: dict
    safety_verdict: SafetyVerdict
    safety_reason: str
    tool_result: dict
    event_summary: str
