#!/usr/bin/env bash
set -euo pipefail

source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"

if [[ -f /workspace/ros_ws/install/setup.bash ]]; then
  source /workspace/ros_ws/install/setup.bash
fi

exec "$@"
