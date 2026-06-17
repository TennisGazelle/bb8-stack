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

Status: complete. Validated locally after PR #2 was merged.

Non-goals:

- no GUI forwarding requirement
- no physically faithful rolling sphere yet
- no MCP-to-ROS bridge yet
- no motor or sensor hardware access yet

## Milestone 2: rolling sphere simulation body

Goal: create the first physically meaningful BB-8 body in Gazebo.

Pass condition:

- `make sim-build` still builds the ROS/Gazebo image.
- `make sim-smoke` verifies `sim/worlds/bb8_room.sdf` and the BB-8 model assets exist.
- `make sim-smoke` starts Gazebo headlessly against `bb8_room.sdf` long enough to prove the world loads.
- `make sim-gui` or `make sim-bb8-gui` can open a world where the BB-8 sphere is visible.
- The SDF model contains collision geometry, mass, inertia, ground friction, and an internal ballast approximation.
- The URDF/xacro contains matching shell, ballast, IMU, and camera frames for ROS-side semantics.

Non-goals:

- no ROS action movement yet
- no motor controller yet
- no MCP-to-ROS bridge yet
- no head stabilization yet
- no camera/IMU Gazebo plugins yet

## Milestone 2.5: controlled sphere motion

Goal: add a bounded ROS-side command path that can move the simulated sphere.

Pass condition:

- A ROS command/action can request bounded motion.
- Pose feedback is observable.
- A stop command halts motion.
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
