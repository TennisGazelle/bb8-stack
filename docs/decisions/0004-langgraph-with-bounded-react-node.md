# ADR 0004: LangGraph with bounded ReAct node

## Status

Accepted for scaffold.

## Context

A pure ReAct loop is easy to start but gives the model too much hidden control flow for robotics. A graph makes state, safety, execution, and memory compaction explicit.

## Decision

Use LangGraph as the orchestration skeleton. Put model/tool reasoning inside bounded nodes.

## Consequences

- Sensors and tactile inputs can enter as typed state later.
- Safety and execution remain explicit graph steps.
- The first implementation can run with a mock model provider.
