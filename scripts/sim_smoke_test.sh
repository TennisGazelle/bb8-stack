#!/usr/bin/env bash
set -eo pipefail

cd /workspace/ros_ws
colcon build --symlink-install

# ROS-generated setup scripts may touch optional environment variables before
# defining them, so do not source them under nounset.
source install/setup.bash
set -u

expected_packages=(
  bb8_description
  bb8_control
  bb8_navigation
  bb8_safety
  bb8_sensors
  bb8_skills_ros
  bb8_bringup
)

printf '\n[bb8-stack] ROS package smoke check\n'
missing_packages=0
for package in "${expected_packages[@]}"; do
  if ros2 pkg prefix "$package" >/dev/null 2>&1; then
    printf '  ✓ %s\n' "$package"
  else
    printf '  ✗ %s was not discoverable through ros2 pkg prefix\n' "$package" >&2
    missing_packages=$((missing_packages + 1))
  fi
done

if [[ "$missing_packages" -gt 0 ]]; then
  printf '\n[bb8-stack] ROS package discovery failed. Diagnostics:\n' >&2
  printf 'AMENT_PREFIX_PATH=%s\n' "${AMENT_PREFIX_PATH:-<unset>}" >&2
  printf '\ncolcon list --names-only:\n' >&2
  colcon list --names-only >&2 || true
  exit 1
fi

printf '\n[bb8-stack] Gazebo CLI check\n'
if ! gz sim --version; then
  gz sim --versions
fi

printf '\n[bb8-stack] Empty world file check\n'
test -f /workspace/sim/worlds/empty_room.sdf
printf '  ✓ /workspace/sim/worlds/empty_room.sdf exists\n'

printf '\n[bb8-stack] Smoke check complete\n'
