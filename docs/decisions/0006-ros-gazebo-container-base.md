# 0006: Use ROS 2 Jazzy + Gazebo Harmonic in Docker for Milestone 1

## Status

Accepted for Milestone 1.

## Context

The project needs a simulation stack that can eventually bridge to real robot hardware. The user is developing on Ubuntu 24.04 now and wants a mostly Docker-dependent workflow.

## Decision

Use a Dockerized ROS 2 Jazzy + Gazebo Harmonic environment for the first simulation base.

Milestone 1 will prove:

- Docker image builds.
- `ros_ws` builds with `colcon` inside the image.
- `gz sim` is available.
- an empty SDF world launches headlessly.

Milestone 1 will not yet implement the rolling-sphere controller or agent-to-ROS bridge.

## Rationale

ROS 2 + Gazebo gives the most direct path from simulated sensors/controllers to real ROS nodes. Gazebo Harmonic is the recommended pairing for ROS 2 Jazzy on Ubuntu 24.04.

Docker keeps the host machine cleaner and gives Codex/local agents a repeatable build target.

## Consequences

- The first sim container is larger than a pure Python or PyBullet environment.
- GUI forwarding is deferred to avoid host-specific X11/Wayland noise.
- Future Pi deployment may use a slimmer runtime image rather than the full Gazebo image.
- Milestone 2 should focus on the physically faithful rolling sphere and controller seam.
