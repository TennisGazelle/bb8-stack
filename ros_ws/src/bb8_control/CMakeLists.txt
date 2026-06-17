cmake_minimum_required(VERSION 3.16)
project(bb8_control)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(rolling_sphere_controller src/rolling_sphere_controller.cpp)
ament_target_dependencies(rolling_sphere_controller rclcpp)

install(TARGETS rolling_sphere_controller DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})

ament_package()
