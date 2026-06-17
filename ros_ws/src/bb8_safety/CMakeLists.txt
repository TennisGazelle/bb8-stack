cmake_minimum_required(VERSION 3.16)
project(bb8_safety)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(watchdog_node src/watchdog_node.cpp)
ament_target_dependencies(watchdog_node rclcpp)

install(TARGETS watchdog_node DESTINATION lib/${PROJECT_NAME})
ament_package()
