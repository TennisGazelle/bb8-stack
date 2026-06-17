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

`sim-up` runs Gazebo server mode against `sim/worlds/empty_room.sdf`. GUI forwarding is intentionally deferred.

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
