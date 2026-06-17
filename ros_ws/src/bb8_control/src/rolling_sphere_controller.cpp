#include <rclcpp/rclcpp.hpp>

class RollingSphereControllerNode : public rclcpp::Node {
public:
  RollingSphereControllerNode() : Node("rolling_sphere_controller") {
    RCLCPP_INFO(get_logger(), "rolling_sphere_controller placeholder started");
  }
};

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<RollingSphereControllerNode>());
  rclcpp::shutdown();
  return 0;
}
