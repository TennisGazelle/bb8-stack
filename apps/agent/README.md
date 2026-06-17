# bb8-agent

Offboard agent loop.

Milestone 0 uses a fake robot client so the graph can be exercised before the MCP/ROS bridge is real.

Planned shape:

```text
load goal
  -> perceive robot state
  -> bounded ReAct decision node
  -> deterministic safety gate
  -> execute via MCP client
  -> summarize and log memory event
```
