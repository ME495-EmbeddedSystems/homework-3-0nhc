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
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    """Generate launch description."""
    # Declare launch arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value=PathJoinSubstitution([FindPackageShare('diff_drive'),
                                            'worlds/ddrive.world.sdf']),
        description='Path to the world file'
    )
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=PathJoinSubstitution([FindPackageShare('diff_drive'),
                                            'rviz/diff_drive.rviz']),
        description='Customized Rviz configuration file.'
    )
    robot_description_path_arg = DeclareLaunchArgument(
        'robot_description_path',
        default_value=PathJoinSubstitution([FindPackageShare('diff_drive'),
                                            'urdf/ddrive.robot.xacro']),
        description="Path to the robot's xacro file."
    )
    view_only_arg = DeclareLaunchArgument(
        'view_only',
        default_value='false',
        description='Set to true to only view the robot in Rviz.'
    )

    # Include the diff_drive launch file
    ddrive_rviz_launch = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('diff_drive'), 'launch/ddrive_rviz.launch.py']),
        launch_arguments={
            'rviz_config': LaunchConfiguration('rviz_config'),
            'robot_description_path': LaunchConfiguration('robot_description_path'),
            'view_only': LaunchConfiguration('view_only'),
        }.items()
    )

    # Spawn the Gazebo world
    gz_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('ros_gz_sim'), 'launch/gz_sim.launch.py'])
        ),
        launch_arguments={
            'gz_args': ['-r ', LaunchConfiguration('world')]
        }.items()
    )

    # Spawn the robot in Gazebo
    create_robot_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='create_robot',
        output='screen',
        parameters=[{
            'topic': '/robot_description',
            'R': 0.0,
            'P': 0.0,
            'Y': 0.0,
            'x': 0.0,
            'y': 0.0,
            'z': 0.3,
        }]
    )

    # Parameter bridge Node
    parameter_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'
        ]
    )

    # Flip Node
    flip_node = Node(
        package='diff_drive',
        executable='flip',
        name='flip'
    )

    return LaunchDescription([
        world_arg,
        rviz_config_arg,
        robot_description_path_arg,
        view_only_arg,
        ddrive_rviz_launch,
        gz_sim_launch,
        create_robot_node,
        parameter_bridge_node,
        flip_node
    ])
