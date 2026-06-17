cmake_minimum_required(VERSION 3.16)
project(bb8_sensors)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(bb8_sensor_state src/bb8_sensor_state.cpp)
ament_target_dependencies(bb8_sensor_state rclcpp)

install(TARGETS bb8_sensor_state DESTINATION lib/${PROJECT_NAME})
ament_package()
