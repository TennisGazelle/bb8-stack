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

This branch targets **Milestone 2**:

- visible BB-8-inspired rolling sphere model in Gazebo
- SDF model with collision, mass, inertia, ground friction, and an internal ballast approximation
- BB-8 room world that includes the sphere, ground plane, a wall, and a small obstacle
- GUI/headless make targets that default to the BB-8 world
- smoke test that verifies the BB-8 world can be loaded by Gazebo
- Milestone 0 fake agent loop and Milestone 1 ROS/Gazebo container preserved

Milestone 2 does **not** yet include motor actuation, a ROS action that moves the sphere, or an MCP-to-ROS bridge. Those are intentionally staged after the visible physics body exists.

## Quick start: Milestone 0 fake loop

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r apps/agent/requirements.txt -r apps/mcp_server/requirements.txt
make milestone0
```

`make milestone0` runs the fake robot loop and writes events to `memory/bb8_memory.sqlite3`.

## Quick start: ROS/Gazebo simulation

```bash
make sim-build
make sim-smoke
```

Expected `sim-smoke` behavior:

1. Build the ROS workspace in the container.
2. Verify the `bb8_*` ROS packages are discoverable.
3. Verify the `gz sim` CLI is installed.
4. Verify the BB-8 model and world files exist.
5. Start Gazebo headlessly against `sim/worlds/bb8_room.sdf` long enough to prove the world loads.

To launch the BB-8 world headlessly:

```bash
make sim-up
```

To inspect a running headless sim in another terminal:

```bash
make sim-inspect
```

To try the Gazebo GUI:

```bash
make sim-gui
```

If no window opens on Linux/X11 or XWayland:

```bash
xhost +local:docker
make sim-gui
xhost -local:docker
```

The empty Milestone 1 world is still available:

```bash
make sim-empty-headless
make sim-empty-gui
```

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
sim/               Gazebo worlds, models, scenarios, and Docker sim image
skills/            Skill catalog and schemas
evals/             Scenario scorecards and traces
memory/            SQLite event log schema and migrations
docs/              Architecture, decisions, safety, simulation notes
firmware/          Future MCU and FlashForge motor probe placeholders
scripts/           Dev entrypoints
```

## Milestone after this branch

The next slice should add controlled motion: a ROS-side command path that can apply bounded motion to the simulated sphere, expose pose feedback, and stop on timeout.
