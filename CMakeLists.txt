cmake_minimum_required(VERSION 3.5)
project(kinect_v2)

# Find ament packages and other dependencies
find_package(ament_cmake REQUIRED)

find_package(std_msgs REQUIRED)
find_package(trajectory_msgs REQUIRED)
find_package(rclcpp REQUIRED)

install(DIRECTORY launch meshes urdf rviz
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()

