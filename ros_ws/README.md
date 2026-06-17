# ROS workspace

This workspace is intentionally thin during Milestone 1. Its job is to prove that the Dockerized ROS/Gazebo development loop can build and discover BB-8 packages.

## Build on host

Only use this if ROS 2 Jazzy is installed on the host:

```bash
cd ros_ws
colcon build --symlink-install
```

## Build in Docker

Preferred for Milestone 1:

```bash
make ros-build-docker
```

## Package roles

```text
bb8_description   URDF/Xacro and visual/collision description
bb8_bringup       launch files for sim/runtime entrypoints
bb8_control       C++ control placeholders
bb8_safety        C++ watchdog/safety placeholders
bb8_sensors       C++ sensor-state placeholder
bb8_skills_ros    future ROS action servers for deterministic skills
bb8_navigation    future mapping/localization/navigation integration
```

## Milestone 1 acceptance

```bash
make sim-smoke
```

This builds the workspace, checks that `bb8_*` packages are visible to ROS, and verifies the Gazebo CLI is present.
