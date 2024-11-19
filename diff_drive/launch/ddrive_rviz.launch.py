#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004

#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#   0. You just DO WHAT THE FUCK YOU WANT TO.

"""Launch file to load the robot description."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    """Generate launch description."""
    # Declare launch arguments
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=[FindPackageShare('diff_drive'), '/rviz/diff_drive.rviz'],
        description='Customized Rviz configuration file.'
    )
    robot_description_path_arg = DeclareLaunchArgument(
        'robot_description_path',
        default_value=[FindPackageShare('diff_drive'), '/urdf/ddrive.robot.xacro'],
        description="Path to the robot's xacro file."
    )
    view_only_arg = DeclareLaunchArgument(
        'view_only',
        default_value='false',
        description='Set to true to only view the robot in Rviz.'
    )

    # Robot State Publisher Node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='rsp',
        parameters=[{
            'robot_description': Command([
                'xacro ', LaunchConfiguration('robot_description_path')
            ])
        }]
    )

    # Joint State Publisher GUI Node (conditionally launched)
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('view_only'))
    )

    # Rviz
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', LaunchConfiguration('rviz_config')],
        condition=UnlessCondition(LaunchConfiguration('view_only'))
    )

    return LaunchDescription([
        rviz_config_arg,
        robot_description_path_arg,
        view_only_arg,
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node,
    ])
