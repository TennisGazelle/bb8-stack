#!/usr/bin/env bash
set -eo pipefail

# ROS setup scripts may read optional environment variables such as
# AMENT_TRACE_SETUP_FILES before defining them. Keep nounset disabled while
# sourcing them, then restore stricter shell behavior for the command itself.
source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"

if [[ -f /workspace/ros_ws/install/setup.bash ]]; then
  source /workspace/ros_ws/install/setup.bash
fi

set -u
exec "$@"
