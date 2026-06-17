# Safety model

The robot should be charming, not legally interesting.

## Non-negotiable rules

1. The LLM never directly controls motors, GPIO, PWM, current, or stepper pulse timing.
2. Motion commands expire quickly.
3. Every motion command has max speed, max duration, and stop conditions.
4. A deterministic safety gate runs before physical execution.
5. A ROS/runtime safety layer can veto or stop motion even after MCP approves a command.
6. E-stop and watchdog logic must not depend on model availability.
7. Low battery blocks exploration and should eventually trigger docking behavior.
8. Sensor uncertainty reduces autonomy.
9. Tool calls and safety decisions are logged.
10. Hardware tests start on the bench, not inside the closed sphere.

## Safety gate ownership

```text
Agent safety review
  advisory, useful for explanation

MCP safety validation
  input bounds, state checks, runtime sanity

ROS safety package
  watchdogs, motion limits, emergency stop, hardware stop

Motor controller / firmware
  final timing and electrical bounds
```

## Early blocked conditions

- battery below configured threshold
- nearest obstacle too close
- tilt above configured threshold
- stale command heartbeat
- unknown pose when pose is required
- requested speed/distance outside tool schema bounds
