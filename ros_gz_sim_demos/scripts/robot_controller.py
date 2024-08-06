import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_blue = self.create_publisher(Twist, '/model/vehicle_blue/cmd_vel', 10)
        self.publisher_green = self.create_publisher(Twist, '/model/vehicle_green/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_velocity)

    def publish_velocity(self):
        twist = Twist()
        twist.linear.x = 0.5
        twist.angular.z = 0.1
        self.publisher_blue.publish(twist)
        self.publisher_green.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    rclpy.spin(robot_controller)
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
