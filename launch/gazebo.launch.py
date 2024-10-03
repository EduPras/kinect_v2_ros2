from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([FindPackageShare('gazebo_ros'),
                                  'launch', 'gazebo.launch.py'])
        ])
    )

    # Static transform publisher node
    kinect_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='kinect_tf',
        arguments=['2.2', '0', '1.6', '0', '0', '0', '1', 'root', 'base_link'],
    )

    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_model',
        output='screen',
        arguments=['-topic', 'kinect_robot_description', '-entity', 'kinect_v2']
    )

    return LaunchDescription([gazebo_launch, kinect_tf_node, spawn_model_node])