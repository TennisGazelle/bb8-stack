# ADR 0002: Offboard agent, onboard runtime

## Status

Accepted for scaffold.

## Context

The available onboard computer is a Raspberry Pi 3. It is suitable for runtime glue, sensors, and lightweight ROS pieces, but the first agent loop can run offboard on a laptop/server.

## Decision

Run the agent offboard first. Run the MCP/ROS runtime on the robot side later. During Milestone 0, both may run locally.

## Consequences

- Faster agent iteration.
- Provider APIs can be used without forcing inference onto the Pi.
- The robot requires a network connection at first.
- Later offline/Bluetooth modes remain possible but are not in scope now.
