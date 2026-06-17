# Milestone 2 validation

Milestone 2 proves that the repository has a visible, physically parameterized BB-8 body in Gazebo.

## Commands

```bash
make sim-build
make sim-smoke
```

Optional headless server check:

```bash
make sim-up
```

Optional GUI check:

```bash
make sim-gui
```

If the GUI does not open on Linux/X11 or XWayland:

```bash
xhost +local:docker
make sim-gui
xhost -local:docker
```

## Expected `make sim-smoke` behavior

`make sim-smoke` should:

1. build `ros_ws`,
2. verify all `bb8_*` packages are discoverable,
3. verify `gz sim` is installed,
4. verify these files exist:
   - `sim/worlds/empty_room.sdf`
   - `sim/worlds/bb8_room.sdf`
   - `sim/models/bb8_rolling_sphere/model.config`
   - `sim/models/bb8_rolling_sphere/model.sdf`
5. verify `bb8_room.sdf` includes `model://bb8_rolling_sphere`,
6. start Gazebo server mode against `bb8_room.sdf` long enough to prove the world loads.

A timeout exit code from the brief Gazebo run is treated as success because `gz sim -s -r` is a long-running server process.

## Expected GUI result

`make sim-gui` should show:

- gray ground plane,
- cream-colored BB-8-inspired sphere,
- orange/gray/dark visual markers on the sphere,
- one dark wall-like calibration surface,
- one low orange obstacle box.

The sphere is dynamic, but it is not intentionally commanded yet. If it settles or drifts slightly under physics, that is acceptable. Controlled motion belongs to Milestone 2.5.

## Known non-goals

- no ROS action movement yet,
- no motor controller yet,
- no MCP-to-ROS bridge yet,
- no simulated camera or IMU plugin yet,
- no head stabilization yet.

## Failure hints

If Gazebo cannot find the model, check:

```bash
docker compose --profile sim run --rm ros-sim bash -lc 'echo $GZ_SIM_RESOURCE_PATH'
```

It should include:

```text
/workspace/sim/models
```

If the GUI does not open but `make sim-smoke` passes, the issue is likely X11/Wayland forwarding rather than Gazebo model validity.
