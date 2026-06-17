.PHONY: help install milestone0 agent mcp test lint ros-build ros-build-docker sim-build sim-shell sim-smoke sim-up sim-headless sim-inspect sim-gui

help:
	@echo "bb8-stack targets"
	@echo "  install           Install Python deps into the active environment"
	@echo "  milestone0        Run the fake robot Milestone 0 loop"
	@echo "  agent             Run the agent CLI"
	@echo "  mcp               Run the MCP server"
	@echo "  test              Run Python tests"
	@echo "  lint              Compile Python packages"
	@echo "  ros-build         Build ROS workspace on host if ROS is installed"
	@echo "  ros-build-docker  Build ROS workspace inside the sim container"
	@echo "  sim-build         Build the ROS/Gazebo Docker image"
	@echo "  sim-shell         Open an interactive shell in the sim container"
	@echo "  sim-smoke         Run a non-GUI ROS/Gazebo smoke check"
	@echo "  sim-up            Build workspace and launch empty world headlessly"
	@echo "  sim-inspect       Inspect ROS/Gazebo state while sim-up is running"
	@echo "  sim-gui           Try launching Gazebo with X11 GUI forwarding"
	@echo "  sim-headless      Run Gazebo server against the empty world once"

install:
	pip install -r apps/agent/requirements.txt -r apps/mcp_server/requirements.txt

milestone0:
	python -m apps.agent.bb8_agent.main --goal "roll forward a little" --transport fake

agent:
	python -m apps.agent.bb8_agent.main --goal "$${GOAL:-roll forward a little}" --transport "$${BB8_MCP_TRANSPORT:-fake}"

mcp:
	python -m apps.mcp_server.bb8_mcp.server

test:
	python -m pytest apps/agent apps/mcp_server

lint:
	python -m compileall apps/agent apps/mcp_server

ros-build:
	cd ros_ws && colcon build --symlink-install

sim-build:
	docker compose build ros-sim

sim-shell:
	docker compose --profile sim run --rm ros-sim bash

ros-build-docker:
	docker compose --profile sim run --rm ros-sim bash -lc "cd /workspace/ros_ws && colcon build --symlink-install"

sim-smoke:
	docker compose --profile sim run --rm ros-sim bash /workspace/scripts/sim_smoke_test.sh

sim-headless:
	docker compose --profile sim run --rm ros-sim bash -lc "cd /workspace/ros_ws && colcon build --symlink-install && source install/setup.bash && gz sim -s -r /workspace/sim/worlds/empty_room.sdf"

sim-up:
	docker compose --profile sim up ros-sim

sim-inspect:
	docker compose --profile sim exec ros-sim bash -lc "cd /workspace/ros_ws && source install/setup.bash && printf '\n[bb8-stack] BB-8 ROS packages\n' && ros2 pkg list | grep '^bb8_' || true; printf '\n[bb8-stack] ROS topics\n' && ros2 topic list || true; printf '\n[bb8-stack] Gazebo topics\n' && gz topic -l || true"

sim-gui:
	@echo "[bb8-stack] If no Gazebo window opens, run: xhost +local:docker"
	docker compose --profile sim run --rm \
		-e DISPLAY=$${DISPLAY} \
		-e QT_X11_NO_MITSHM=1 \
		-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
		ros-sim bash -lc "cd /workspace/ros_ws && colcon build --symlink-install && source install/setup.bash && gz sim -r /workspace/sim/worlds/empty_room.sdf"
