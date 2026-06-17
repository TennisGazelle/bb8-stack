# 0007: Stage Milestone 2 as a visible physics body before controlled motion

## Status

Accepted for Milestone 2.

## Context

The project wants a physically faithful BB-8 simulation rather than a differential-drive robot wearing a spherical costume. The eventual target includes a rolling shell, internal mass or drive carriage, sensor frames, pose feedback, and safety-relevant behavior.

Jumping directly from an empty Gazebo world to motor-controlled rolling physics risks conflating several problems:

- valid Gazebo model loading
- visual debugging
- collision geometry
- inertia and contact friction
- ROS frame semantics
- controller architecture
- command timeout and stop behavior

## Decision

Split the original rolling-sphere milestone into two stages:

1. **Milestone 2: rolling sphere simulation body**
   - visible BB-8-inspired sphere
   - dynamic SDF model
   - explicit collision, mass, inertia, friction
   - fixed internal ballast approximation
   - default BB-8 Gazebo world
   - ROS frame tree for shell, ballast, IMU, and camera

2. **Milestone 2.5: controlled sphere motion**
   - bounded ROS command/action path
   - pose feedback
   - stop command
   - timeout safety

## Rationale

A known-good physical body gives the controller work a stable target. It also gives the user an immediate visual validation path through `make sim-gui` without requiring the full ROS action bridge yet.

## Consequences

- Milestone 2 becomes smaller and easier to validate locally.
- The BB-8 model exists before it can intentionally move.
- The first sphere uses a fixed ballast approximation rather than a controllable internal pendulum.
- Controller work moves to Milestone 2.5.
