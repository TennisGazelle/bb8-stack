# ADR 0003: ROS 2 + Gazebo first

## Status

Accepted for scaffold.

## Context

The project needs physics simulation, sensor integration, mapping/navigation options, and a realistic path toward hardware.

## Decision

Use ROS 2 + Gazebo as the primary simulation and robotics middleware stack.

## Consequences

- More up-front robotics structure.
- Better sim-to-reality bridge than a custom-only simulator.
- Docker support matters because development should work across machines.
