#include <rclcpp/rclcpp.hpp>

class Bb8SensorStateNode : public rclcpp::Node {
public:
  Bb8SensorStateNode() : Node("bb8_sensor_state") {
    RCLCPP_INFO(get_logger(), "bb8_sensor_state placeholder started");
  }
};

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Bb8SensorStateNode>());
  rclcpp::shutdown();
  return 0;
}
