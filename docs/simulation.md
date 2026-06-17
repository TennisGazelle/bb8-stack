# Simulation strategy

## Default stack

Use ROS 2 + Gazebo first.

The project cares most about sim-to-reality continuity, sensor integration, ROS actions/services/topics, and eventually hardware controller swaps. ROS/Gazebo is the least exotic bridge for that path.

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
