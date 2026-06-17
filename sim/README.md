# Simulation

Milestone 1 establishes the ROS/Gazebo container base.

## Current target

```bash
make sim-build
make sim-smoke
make sim-up
```

`make sim-up` launches Gazebo server mode against:

```text
sim/worlds/empty_room.sdf
```

This is intentionally headless. GUI forwarding is host-specific and will be handled later if it becomes useful.

## World layout

```text
worlds/
  empty_room.sdf          Minimal ground plane and light source.
  living_room_placeholder.sdf
  obstacle_course.sdf
```

## Milestone 2 direction

Milestone 2 should add:

- spawnable BB-8 sphere model
- physically meaningful shell + internal mass approximation
- controller seam compatible with `ros2_control`
- simulated IMU and pose feedback
- first motion action from ROS
