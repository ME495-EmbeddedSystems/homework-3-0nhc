#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004

#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#   0. You just DO WHAT THE FUCK YOU WANT TO.

"""
The flip ROS 2 node for homework-3.

The flip node communicates through several ROS 2 protocols:

PUBLISHERS:
  + cmd_vel (geometry_msgs.msg.Twist) - The velocity command used to control
    the robot
"""

from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node


class Flip(Node):
    """
    The flip ROS 2 node for homework-3.

    The flip node communicates through several ROS 2 protocols:

    PUBLISHERS:
    + cmd_vel (geometry_msgs.msg.Twist) - The velocity command used to control
        the robot
    """

    def __init__(self):
        """
        Initialize the flip node.

        Sets up ROS 2 publishers and timers, along with several parameters.
        """
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
        """
        Flip the robot by reversing its linear velocity.

        This function is called by the flip timer.
        """
        self._cmd_vel_publisher.publish(self._twist_msg)
        self._twist_msg.linear.x = -self._twist_msg.linear.x


def main(args=None):
    """
    Entry point for the flip node.

    Initializes the ROS 2 node, spins to process callbacks, and shuts down.

    :param args: Command-line arguments passed to rclpy.init().
    :type args: list, optional
    """
    rclpy.init(args=args)
    flip = Flip()
    rclpy.spin(flip)
    flip.destroy_node()
    rclpy.shutdown()
