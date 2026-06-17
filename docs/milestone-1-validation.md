# Milestone 1 validation

Milestone 1 proves that the ROS/Gazebo development base is real enough for Milestone 2 work.

## Commands

```bash
make sim-build
make ros-build-docker
make sim-smoke
```

Optional long-running server check:

```bash
make sim-up
```

## Expected results

`make sim-build` should produce the `bb8-stack:ros-jazzy-gazebo` image.

`make ros-build-docker` should build all packages under `ros_ws/src` with `colcon build --symlink-install`.

`make sim-smoke` should:

1. build `ros_ws`,
2. source `ros_ws/install/setup.bash`,
3. print packages matching `bb8_*`,
4. print the Gazebo CLI version.

`make sim-up` should launch Gazebo server mode against:

```text
sim/worlds/empty_room.sdf
```

## Known non-goals

- The Gazebo GUI is not configured yet.
- The BB-8 model is not spawned into the world yet.
- No ROS actions move the simulated robot yet.
- The MCP server still uses fake runtime behavior for Milestone 0.

## Failure hints

If Docker build fails around `ros-jazzy-*` packages, run:

```bash
docker compose --profile sim build --no-cache ros-sim
```

If `make sim-up` starts and appears to hang, that is normal: Gazebo server is running in the foreground.

If `ros2 pkg list | grep '^bb8_'` prints nothing, the workspace did not build or the install setup file was not sourced.
