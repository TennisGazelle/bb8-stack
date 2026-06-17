# bb8-stack

`bb8-stack` is a simulation-first, robot-centered agent stack for a BB-8-inspired robot.

The architecture is deliberately split:

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
  ROS 2 Jazzy + Gazebo Harmonic, starting with a containerized base and then a physically faithful rolling sphere model
```

## Current milestone

This branch targets **Milestone 1**:

- Dockerized ROS 2 Jazzy development image
- Gazebo Harmonic through the ROS/Gazebo pairing
- `colcon` build path for `ros_ws`
- headless empty-world Gazebo launch
- ROS package smoke checks
- Milestone 0 fake agent loop preserved

Gazebo's ROS integration docs recommend Ubuntu 24.04, ROS 2 Jazzy, and Gazebo Harmonic as the default LTS pairing for new users. The Docker image follows that pairing.

## Quick start: Milestone 0 fake loop

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r apps/agent/requirements.txt -r apps/mcp_server/requirements.txt
make milestone0
```

`make milestone0` runs the fake robot loop and writes events to `memory/bb8_memory.sqlite3`.

## Quick start: Milestone 1 ROS/Gazebo container

```bash
make sim-build
make sim-smoke
```

Expected `sim-smoke` behavior:

1. Build the ROS workspace in the container.
2. Verify the `bb8_*` ROS packages are discoverable.
3. Verify the `gz sim` CLI is installed.

To open a shell in the container:

```bash
make sim-shell
```

To launch the empty world headlessly:

```bash
make sim-up
```

This starts the Gazebo server against `sim/worlds/empty_room.sdf`. GUI forwarding is intentionally not part of Milestone 1.

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
ros_ws/            ROS 2 workspace placeholders and Milestone 1 build target
sim/               Gazebo worlds, scenarios, and Docker sim image
skills/            Skill catalog and schemas
evals/             Scenario scorecards and traces
memory/            SQLite event log schema and migrations
docs/              Architecture, decisions, safety, simulation notes
firmware/          Future MCU and FlashForge motor probe placeholders
scripts/           Dev entrypoints
```

## Milestone after this branch

Milestone 2 should make the simulated robot physically meaningful: a rolling sphere model, internal mass or drive approximation, controller seam, pose feedback, and first safety-relevant sim behavior.
