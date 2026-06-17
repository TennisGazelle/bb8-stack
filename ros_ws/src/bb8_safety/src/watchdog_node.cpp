#include <rclcpp/rclcpp.hpp>

class WatchdogNode : public rclcpp::Node {
public:
  WatchdogNode() : Node("bb8_watchdog") {
    RCLCPP_INFO(get_logger(), "bb8_watchdog placeholder started");
  }
};

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<WatchdogNode>());
  rclcpp::shutdown();
  return 0;
}
