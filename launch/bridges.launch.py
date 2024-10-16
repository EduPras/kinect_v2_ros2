from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    gz_bridge = Node(
        package="ros_gz_bridge",
        executable='parameter_bridge',
        name='gz_bridge',
        arguments=[
            '/world/pigs/model/kinect_v2_standalong/link/root/sensor/kinect_v2_rgb_sensor/image@sensor_msgs/msg/Image@ignition.msgs.Image',
            '/world/pigs/model/kinect_v2_standalong/link/root/sensor/kinect_v2_ir_sensor/depth_image/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked'
            # '/world/pigs/model/kinect_v2_standalong/link/root/sensor/kinect_v2_ir_sensor/depth_image/points\
            #     @sensor_msgs/msg/PointCloud@ignition.msgs.PointCloudPacked'
        ],
        remappings=[
            ('/world/pigs/model/kinect_v2_standalong/link/root/sensor/kinect_v2_ir_sensor/depth_image/points', 
             '/kinect_v2_ir_sensor/depth_image'),
            ('/world/pigs/model/kinect_v2_standalong/link/root/sensor/kinect_v2_rgb_sensor/image', 
             '/kinect_v2_rgb_sensor/image'),
            ],
        output='screen'
    )

    return LaunchDescription([gz_bridge])
