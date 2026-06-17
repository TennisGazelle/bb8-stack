cmake_minimum_required(VERSION 3.16)
project(bb8_skills_ros)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(roll_forward_safe_action src/roll_forward_safe_action.cpp)
ament_target_dependencies(roll_forward_safe_action rclcpp)

install(TARGETS roll_forward_safe_action DESTINATION lib/${PROJECT_NAME})
ament_package()
