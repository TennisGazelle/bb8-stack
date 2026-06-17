#include <rclcpp/rclcpp.hpp>

class RollForwardSafeActionNode : public rclcpp::Node {
public:
  RollForwardSafeActionNode() : Node("roll_forward_safe_action") {
    RCLCPP_INFO(get_logger(), "roll_forward_safe_action placeholder started");
  }
};

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<RollForwardSafeActionNode>());
  rclcpp::shutdown();
  return 0;
}
