from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os
import xacro
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    xacro_file = os.path.join(
            get_package_share_directory('kinect_v2'),
            'urdf', 
            'kinect_v2_standalong.urdf.xacro'
    )

    assert os.path.exists(xacro_file), "The xacro file doesn't exists in " + str(xacro_file)

    robot_description = xacro.process_file(xacro_file).toxml()
    kinect_path = FindPackageShare('kinect_v2')
    default_rviz_config_path = PathJoinSubstitution([kinect_path,'rviz', 'urdf.rviz'])

    gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                     description='Absolute path to rviz config file')

    model = (DeclareLaunchArgument(
        name='model',
        default_value=xacro_file,
        description='Path to robot urdf file relative to urdf_tutorial package'))

        
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='kinect_joint_state_publisher',
        remappings=[
            ('robot_description', 'kinect_robot_description'),
            ('joint_states', 'kinect_joint_states')
        ],
        parameters=[{'use_gui': LaunchConfiguration('gui')}]
    )
    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='kinect_robot_state_publisher',
        remappings=[
            ('robot_description', 'kinect_robot_description'),
            ('joint_states', 'kinect_joint_states'),
            ('tf_prefix', 'kinect_tf_prefix')
        ],
        parameters=[{'robot_description': robot_description}],
        arguments=[xacro_file]
    ) 
    urdf_launch = (IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'kinect_v2', 
            'urdf_package_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'jsp_gui': LaunchConfiguration('gui')}.items()
    ))

    return LaunchDescription([
        gui_arg,
        rviz_arg, 
        joint_state_publisher_node,
        model, 
        robot_state_publisher_node, 
        urdf_launch])
