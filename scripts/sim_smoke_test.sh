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

printf '\n[bb8-stack] World and model file checks\n'
expected_files=(
  /workspace/sim/worlds/empty_room.sdf
  /workspace/sim/worlds/bb8_room.sdf
  /workspace/sim/models/bb8_rolling_sphere/model.config
  /workspace/sim/models/bb8_rolling_sphere/model.sdf
)
for expected_file in "${expected_files[@]}"; do
  test -f "$expected_file"
  printf '  ✓ %s exists\n' "$expected_file"
done

grep -q 'model://bb8_rolling_sphere' /workspace/sim/worlds/bb8_room.sdf
printf '  ✓ bb8_room.sdf includes model://bb8_rolling_sphere\n'

grep -q '<model name="bb8_rolling_sphere">' /workspace/sim/models/bb8_rolling_sphere/model.sdf
printf '  ✓ model.sdf declares bb8_rolling_sphere\n'

printf '\n[bb8-stack] BB-8 world headless load check\n'
set +e
timeout 10s gz sim -s -r /workspace/sim/worlds/bb8_room.sdf >/tmp/bb8_gazebo_smoke.log 2>&1
gazebo_status=$?
set -e

if [[ "$gazebo_status" -eq 0 || "$gazebo_status" -eq 124 ]]; then
  printf '  ✓ Gazebo accepted bb8_room.sdf and ran headlessly\n'
else
  printf '  ✗ Gazebo failed to load bb8_room.sdf; log follows:\n' >&2
  cat /tmp/bb8_gazebo_smoke.log >&2 || true
  exit "$gazebo_status"
fi

printf '\n[bb8-stack] Smoke check complete\n'
