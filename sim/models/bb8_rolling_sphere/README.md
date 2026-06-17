# bb8_rolling_sphere

This is the first physically meaningful Gazebo model for the simulated BB-8 body.

It is intentionally modest:

- dynamic spherical shell
- explicit mass and inertia
- ground-contact collision geometry
- friction and low bounce settings
- fixed internal ballast approximation
- simple visual reference marks so rotation is visible in the GUI

It is not yet a complete BB-8 drivetrain simulation. The internal mass is fixed for now so Milestone 2 can focus on a reliable visible physics body before controller work begins.

Future iterations should replace the fixed ballast with a controllable internal carriage or pendulum, then expose control through ROS actions and the MCP runtime.
