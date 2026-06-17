# Milestones

## Milestone 0: fake robot loop

Goal: prove the software seams before hardware or Gazebo complexity arrives.

Pass condition:

- `make milestone0` runs.
- Agent receives a goal.
- Agent reads fake robot state.
- Agent proposes one safe motion action.
- Safety gate approves or denies deterministically.
- Fake robot state changes.
- Event is logged to SQLite.

Status: complete. Validated locally after PR #1 was merged.

## Milestone 1: Dockerized ROS/Gazebo base

Goal: run ROS 2 + Gazebo in a containerized development loop.

Pass condition:

- `make sim-build` builds the ROS/Gazebo image.
- `make ros-build-docker` builds `ros_ws` with `colcon build` inside the container.
- `make sim-smoke` verifies `bb8_*` packages are discoverable and the `gz sim` CLI is installed.
- `make sim-up` launches `sim/worlds/empty_room.sdf` headlessly through Docker Compose.

Non-goals:

- no GUI forwarding yet
- no physically faithful rolling sphere yet
- no MCP-to-ROS bridge yet
- no motor or sensor hardware access yet

## Milestone 2: rolling sphere simulation

Goal: simulate a physically faithful rolling sphere model.

Pass condition:

- A sphere model appears in Gazebo.
- A ROS action can move it forward.
- A stop command halts it.
- Timeout safety stops stale commands.

## Milestone 3: MCP to ROS bridge

Goal: replace fake runtime calls with ROS actions/services/topics.

Pass condition:

- The offboard agent calls the MCP server over HTTP.
- MCP calls a ROS action.
- Gazebo robot moves.
- `robot://state` returns simulated state.

## Milestone 4: sim evals

Goal: repeatable safety and behavior tests.

Pass condition:

- obstacle stop scenario passes
- low battery motion block passes
- tilt stop scenario passes
- scorecards produce pass/fail output

## Milestone 5: Raspberry Pi 3 runtime

Goal: move MCP server and ROS runtime pieces onto the Pi 3.

Pass condition:

- laptop agent calls Pi-hosted MCP server
- Pi returns runtime state
- no heavy model inference is required on the Pi

## Milestone 6: FlashForge motor bench test

Goal: safely command salvaged motors on a bench.

Pass condition:

- motor inventory is documented
- one motor spins under bounded command
- stop command works
- current/voltage assumptions are recorded
