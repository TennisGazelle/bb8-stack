# Simulation strategy

## Default stack

Use ROS 2 + Gazebo first.

The project cares most about sim-to-reality continuity, sensor integration, ROS actions/services/topics, and eventually hardware controller swaps. ROS/Gazebo is the least exotic bridge for that path.

## Milestone 1 base

Milestone 1 establishes a containerized ROS/Gazebo base, not the final robot simulation.

Target pairing:

```text
Ubuntu 24.04 / Noble
ROS 2 Jazzy
Gazebo Harmonic
```

The ROS/Gazebo documentation recommends Jazzy + Harmonic as the default LTS pairing for new users on Ubuntu 24.04, and notes that `ros-${ROS_DISTRO}-ros-gz` installs the matching Gazebo libraries for a given ROS distribution.

Milestone 1 acceptance:

```text
make sim-build
make ros-build-docker
make sim-smoke
make sim-up
```

`sim-up` runs Gazebo server mode against `sim/worlds/empty_room.sdf`. It is intentionally headless, so it does not open a visual simulator window.

## What should I see?

### `make sim-up`

This starts the Gazebo server only:

```text
gz sim -s -r /workspace/sim/worlds/empty_room.sdf
```

The `-s` flag means server-only. In this mode, the expected result is logs and a long-running foreground process, not a visible window.

The current world contains:

- a 20m x 20m ground plane
- a directional sun light
- no BB-8 model yet
- no moving robot yet

So even with a GUI, Milestone 1 should look like an empty lit plane. The rolling BB-8 body begins in Milestone 2.

### Inspecting a running headless sim

In terminal 1:

```bash
make sim-up
```

In terminal 2:

```bash
make sim-inspect
```

`sim-inspect` checks:

- BB-8 ROS packages
- ROS topics
- Gazebo topics

This is the main Milestone 1 visibility path. It confirms that the server/runtime plumbing exists before there is a useful robot to watch.

### Trying the Gazebo GUI

On Linux with X11 or XWayland, try:

```bash
make sim-gui
```

If no Gazebo window opens, allow local Docker clients to connect to X11, then retry:

```bash
xhost +local:docker
make sim-gui
```

When finished, you can tighten X11 access again:

```bash
xhost -local:docker
```

This GUI path is a convenience target. The canonical Milestone 1 path remains headless because it is more reliable in Docker and CI.

## Physical fidelity target

The simulated BB-8 should be a rolling sphere, not a differential-drive rectangle wearing a costume.

Milestone 2 should approximate:

- outer sphere body
- internal mass or drive carriage
- IMU frame
- motor state
- pose feedback
- contact/collision behavior

## Living room / 3D splat note

A living-room scan or splat can become a later visual/environment asset. It should not block the first sim milestone.

Priority order:

1. repeatable physics
2. safety stop tests
3. basic obstacles
4. camera placeholder
5. richer living-room geometry
6. photogrammetry / splat-derived assets
