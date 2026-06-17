from __future__ import annotations


def compact_single_event(goal: str, action: dict, result: dict) -> str:
    name = action.get("name", "unknown")
    ok = result.get("ok", False)
    return f"Goal={goal!r}; action={name}; ok={ok}; result={result}"
