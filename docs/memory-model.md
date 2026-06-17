# Memory model

## Starting point

Use SQLite as the authoritative event log.

A vector index can be added later behind an interface, but the robot needs an exact record of what happened before it needs fuzzy recall.

## Memory layers

```text
Identity / constitution
  human-edited Git files in bb8-soul/

Event log
  exact tool calls, safety decisions, observations, outcomes

Recent summary
  compacted description of recent state and events

Skill memory
  what worked, what failed, calibration hints

Environment memory
  maps, known hazards, dock position, common rooms
```

## Constitution update policy

At first:

- humans edit `bb8-soul/`
- changes happen through Git
- the agent reads these files as context

Later:

- the robot may propose patches
- proposals land under `bb8-soul/proposed_changes/`
- humans review PRs
- the robot never self-merges constitution changes
