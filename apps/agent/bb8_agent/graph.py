from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from .config import load_config
from .mcp_client import FakeRobotClient
from .memory import EventStore, compact_single_event
from .model_providers import MockModelProvider
from .safety_policy import deterministic_safety_gate
from .state import Bb8AgentState


_fake_client = FakeRobotClient()


async def perceive(state: Bb8AgentState) -> Bb8AgentState:
    robot_state = await _fake_client.read_resource("robot://state")
    return {"robot_state": robot_state}


async def react_decide(state: Bb8AgentState) -> Bb8AgentState:
    # Milestone 0 uses a mock provider. Later this node becomes the bounded ReAct node.
    provider = MockModelProvider()
    action = await provider.propose_action(state["goal"], state["robot_state"])
    return {"proposed_action": action}


def safety_gate(state: Bb8AgentState) -> Bb8AgentState:
    verdict, reason = deterministic_safety_gate(state["proposed_action"], state["robot_state"])
    return {"safety_verdict": verdict, "safety_reason": reason}


async def execute(state: Bb8AgentState) -> Bb8AgentState:
    if state["safety_verdict"] != "allow":
        return {"tool_result": {"ok": False, "error": state["safety_reason"]}}

    action = state["proposed_action"]
    result = await _fake_client.call_tool(action["name"], action.get("args", {}))
    return {"tool_result": result}


def summarize(state: Bb8AgentState) -> Bb8AgentState:
    config = load_config()
    store = EventStore(config.memory_db)
    summary = compact_single_event(state["goal"], state["proposed_action"], state["tool_result"])
    store.append_event(
        "agent_cycle",
        {
            "goal": state["goal"],
            "robot_state": state["robot_state"],
            "proposed_action": state["proposed_action"],
            "safety_verdict": state["safety_verdict"],
            "safety_reason": state["safety_reason"],
            "tool_result": state["tool_result"],
            "summary": summary,
        },
    )
    store.append_summary(summary)
    return {"event_summary": summary}


def build_graph():
    graph = StateGraph(Bb8AgentState)
    graph.add_node("perceive", perceive)
    graph.add_node("react_decide", react_decide)
    graph.add_node("safety_gate", safety_gate)
    graph.add_node("execute", execute)
    graph.add_node("summarize", summarize)

    graph.add_edge(START, "perceive")
    graph.add_edge("perceive", "react_decide")
    graph.add_edge("react_decide", "safety_gate")
    graph.add_edge("safety_gate", "execute")
    graph.add_edge("execute", "summarize")
    graph.add_edge("summarize", END)
    return graph.compile()
