#!/usr/bin/env bash
set -eo pipefail

cd /workspace/ros_ws
colcon build --symlink-install

# ROS-generated setup scripts may touch optional environment variables before
# defining them, so do not source them under nounset.
source install/setup.bash

set -u

printf '\n[bb8-stack] ROS package smoke check\n'
ros2 pkg list | grep '^bb8_'

printf '\n[bb8-stack] Gazebo CLI check\n'
if ! gz sim --version; then
  gz sim --versions
fi
