# Architecture

## Core principle

The BB-8 robot stack is split into three layers:

```text
Agent brain
  Decides what should happen next.
  Runs offboard on a laptop/server first.
  Uses model-provider adapters and MCP tools.

Robot capability layer
  Exposes safe typed tools/resources/prompts through MCP.
  Runs on the robot runtime, initially a Raspberry Pi 3.
  Bridges agent intent into ROS actions/services/topics.

Robot control layer
  Owns physics, timing, safety, sensors, motor interfaces, and simulation.
  Uses ROS 2 and Gazebo first.
  Uses C++ for safety/control where appropriate.
```

## Deployment v0

```text
Laptop/server
  apps/agent
    LangGraph state machine
    bounded ReAct decision node
    provider-agnostic model adapter
    memory compactor
    MCP client

Raspberry Pi 3 or local dev process
  apps/mcp_server
    FastMCP server
    fake bridge for Milestone 0
    ROS bridge later

ROS/Gazebo
  ros_ws + sim
    rolling sphere physics later
```

## Why MCP here?

MCP is the agent-facing capability contract. It should expose actions such as `motion.roll_forward_safe`, state resources such as `robot://state`, and reusable prompts such as `bb8://prompts/safety-review`.

MCP should not be used as the low-level motor-control loop. The LLM should not directly touch PWM, stepper pulses, GPIO, or current limits.

## Why ROS here?

ROS gives a stable bridge from simulation to hardware: messages, actions, services, controllers, sensor nodes, launch files, mapping/navigation options, and existing robotics patterns.

The desired path is:

```text
MCP tool call
  -> ROS action/service
  -> Gazebo simulation first
  -> real motor/sensor interfaces later
```

## First vertical slice

```text
User: "roll forward a little"
  -> agent perceives robot state
  -> bounded ReAct node proposes roll_forward_safe
  -> deterministic safety gate checks fake state
  -> MCP/fake bridge executes
  -> memory event is stored
```
