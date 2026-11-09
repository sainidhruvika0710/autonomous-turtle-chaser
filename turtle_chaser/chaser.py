import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math


class Chaser(Node):

    def __init__(self):
        super().__init__('chaser')

        self.leader_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.leader_callback,
            10
        )

        self.chaser_sub = self.create_subscription(
            Pose,
            '/turtle2/pose',
            self.chaser_callback,
            10
        )

        self.publisher = self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10
        )

        self.leader_pose = None
        self.chaser_pose = None

        self.timer = self.create_timer(0.05, self.control_loop)

    def leader_callback(self, msg):
        self.leader_pose = msg

    def chaser_callback(self, msg):
        self.chaser_pose = msg

    def control_loop(self):

        if self.leader_pose is None or self.chaser_pose is None:
            return

        dx = self.leader_pose.x - self.chaser_pose.x
        dy = self.leader_pose.y - self.chaser_pose.y

        distance = math.sqrt(dx**2 + dy**2)

        desired_angle = math.atan2(dy, dx)

        angle_error = desired_angle - self.chaser_pose.theta

        angle_error = math.atan2(
            math.sin(angle_error),
            math.cos(angle_error)
        )

        msg = Twist()

        if distance > 0.5:
            msg.linear.x = min(1.5, distance)
            msg.angular.z = 4.0 * angle_error
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = Chaser()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
