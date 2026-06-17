# Simulation strategy

## Default stack

Use ROS 2 + Gazebo first.

The project cares most about sim-to-reality continuity, sensor integration, ROS actions/services/topics, and eventually hardware controller swaps. ROS/Gazebo is the least exotic bridge for that path.

## Target pairing

```text
Ubuntu 24.04 / Noble
ROS 2 Jazzy
Gazebo Harmonic
```

The ROS/Gazebo documentation recommends Jazzy + Harmonic as the default LTS pairing for new users on Ubuntu 24.04, and notes that `ros-${ROS_DISTRO}-ros-gz` installs the matching Gazebo libraries for a given ROS distribution.

## Milestone 1 base

Milestone 1 established the containerized ROS/Gazebo base, not the final robot simulation.

Validated path:

```text
make sim-build
make ros-build-docker
make sim-smoke
make sim-up
```

## Milestone 2 body model

Milestone 2 creates the first visible, physically parameterized BB-8 body.

The default world is now:

```text
sim/worlds/bb8_room.sdf
```

The default model is:

```text
sim/models/bb8_rolling_sphere/model.sdf
```

This model is intentionally a first physical body, not a finished drivetrain. It includes:

- dynamic spherical shell
- collision geometry
- mass and inertia
- contact friction and low bounce
- fixed internal ballast approximation
- visual rotation markers
- matching ROS frame semantics in `bb8_description/urdf/bb8.urdf.xacro`

It does not yet include:

- controllable internal pendulum
- motor actuation
- head stabilization
- camera or IMU Gazebo plugins
- ROS action movement
- MCP-to-ROS bridge

## What should I see?

### `make sim-up`

This starts the Gazebo server only:

```text
gz sim -s -r /workspace/sim/worlds/bb8_room.sdf
```

The `-s` flag means server-only. In this mode, the expected result is logs and a long-running foreground process, not a visible window.

The current BB-8 world contains:

- a 20m x 20m ground plane
- a directional sun light
- a dynamic BB-8-inspired sphere
- one wall-like calibration surface
- one low obstacle box

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

The GUI should show a cream-colored sphere with simple orange/gray/dark visual markers. The markers exist so rotation will be visually obvious once controlled motion lands.

## Empty world still exists

Milestone 1's empty world remains available:

```bash
make sim-empty-headless
make sim-empty-gui
```

## Living room / 3D splat note

A living-room scan or splat can become a later visual/environment asset. It should not block the first sim milestones.

Priority order:

1. repeatable physics
2. safety stop tests
3. basic obstacles
4. camera placeholder
5. richer living-room geometry
6. photogrammetry / splat-derived assets
