#!/usr/bin/env bash
set -euo pipefail

cd /workspace/ros_ws
colcon build --symlink-install
source install/setup.bash

printf '\n[bb8-stack] ROS package smoke check\n'
ros2 pkg list | grep '^bb8_'

printf '\n[bb8-stack] Gazebo CLI check\n'
gz sim --version
