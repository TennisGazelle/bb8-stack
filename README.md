# bb8-stack

`bb8-stack` is a simulation-first, robot-centered agent stack for a BB-8-inspired robot.

The first architecture target is deliberately split:

```text
Laptop / server
  bb8-agent: LangGraph orchestration, model-provider adapter, memory compaction, MCP client

Network
  MCP over HTTP for robot runtime, stdio/local transports for development

Raspberry Pi 3 / robot runtime
  bb8-mcp-server: agent-facing tools/resources/prompts, ROS bridge, runtime validation

ROS 2 / control layer
  C++ packages for control, safety, skills, and motor interfaces
  Python only where fast prototyping is useful

Simulation
  ROS 2 + Gazebo, starting with a physically faithful rolling sphere model
```

## Current milestone

This scaffold targets **Milestone 0**:

- repo topology
- architecture docs
- temporary `bb8-soul/` directory, to become a Git submodule later
- fake robot state loop
- starter LangGraph/ReAct-shaped agent
- FastMCP-shaped server surface
- SQLite memory/event-log skeleton
- ROS 2/Gazebo package placeholders for later milestones

## Quick start

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r apps/agent/requirements.txt -r apps/mcp_server/requirements.txt
make milestone0
```

`make milestone0` currently runs the fake robot loop and writes events to `memory/bb8_memory.sqlite3`.

## Design constraints

- The offboard agent may propose actions.
- The MCP server exposes safe, typed capabilities.
- ROS owns the robot-facing execution layer.
- C++ owns low-level control and safety where appropriate.
- The LLM never writes PWM, GPIO, stepper pulses, or motor current directly.
- The personality/constitution is human-edited in Git at first.
- Later, the robot may propose constitution changes as PRs, but it should not self-merge its own soul patches.

## Repository map

```text
apps/agent/        Offboard agent loop, model adapters, memory compaction
apps/mcp_server/   MCP tools/resources/prompts and ROS bridge boundary
bb8-soul/          Temporary personality/constitution repo placeholder
ros_ws/            ROS 2 workspace placeholders
sim/               Gazebo worlds, scenarios, and sim notes
skills/            Skill catalog and schemas
evals/             Scenario scorecards and traces
memory/            SQLite event log schema and migrations
docs/              Architecture, decisions, safety, simulation notes
firmware/          Future MCU and FlashForge motor probe placeholders
scripts/           Dev entrypoints
```

## Next milestone after this scaffold

Milestone 1 should replace the fake ROS bridge with a Dockerized ROS 2 Jazzy + Gazebo Harmonic development environment, then make the same `motion.roll_forward_safe` flow move the simulated sphere.
