import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class Rate:
    def __init__(self, frequency=1.0):
        self._freq = frequency
        self._interval = 1.0 / self._freq
        self._time_state = time.time()

    def sleep(self):
        current_time = time.time()
        elapsed_time = current_time - self._time_state
        if elapsed_time >= self._interval:
            self._time_state = current_time



class Flip(Node):
    def __init__(self):
        super().__init__('flip')
        # Initialize parameters
        self._linear_speed = 5.0
        self._flip_interval = 2.0

        # Create a publisher to publish Twist messages on the cmd_vel topic
        self._cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self._twist_msg = Twist()
        self._twist_msg.linear.x = self._linear_speed

        # create a Timer
        self.create_timer(self._flip_interval, self.flip)

    def flip(self):
        self._cmd_vel_publisher.publish(self._twist_msg)
        self._twist_msg.linear.x = -self._twist_msg.linear.x


def main(args=None):
    rclpy.init(args=args)
    flip = Flip()
    rclpy.spin(flip)
    flip.destroy_node()
    rclpy.shutdown()