.PHONY: help install milestone0 agent mcp test lint ros-build sim-up

help:
	@echo "bb8-stack targets"
	@echo "  install      Install Python deps into the active environment"
	@echo "  milestone0  Run the fake robot Milestone 0 loop"
	@echo "  agent       Run the agent CLI"
	@echo "  mcp         Run the MCP server"
	@echo "  test        Run Python tests"
	@echo "  ros-build   Build ROS workspace if ROS is installed"
	@echo "  sim-up      Placeholder for ROS/Gazebo compose profile"

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
	cd ros_ws && colcon build

sim-up:
	docker compose --profile sim up
