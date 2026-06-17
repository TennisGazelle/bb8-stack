# Skill design

Skills are reusable robot behaviors with clear inputs, safety requirements, and execution backends.

A skill should describe intent. It should not contain raw motor timing.

## Example lifecycle

```text
skill YAML
  -> MCP skills.run(name, args)
  -> ROS action server
  -> safety package and controller
  -> simulated or physical robot
```

## Skill tiers

### Tier 0: diagnostics

- healthcheck
- get_robot_state
- get_sensor_snapshot

### Tier 1: safe motion

- stop_now
- roll_forward_safe
- rotate_in_place
- stop_and_stabilize

### Tier 2: perception-bound behavior

- look_around
- inspect_obstacle
- approach_visible_marker

### Tier 3: autonomy

- patrol_room
- return_to_dock
- explore_until_map_confidence

### Tier 4: personality expression

- greeting_spin
- curious_inspection
- low_battery_expression

Personality skills may call safe primitives. They do not get direct access to motor controls.
