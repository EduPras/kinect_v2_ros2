# Kinect v2 URDF Model for ROS 2 🚀🤖

Welcome to the **Kinect v2 URDF** model, migrated to **ROS 2**! This package provides a URDF model of the Kinect v2 sensor, perfect for integration in your **Gazebo** simulations or any ROS 2 application. 🌟

![Kinect v2 Model in RViz](./images/kinect_rviz.png)  
*Example of the Kinect v2 model loaded in RViz*

---

## Features ✨

- 📦 **Fully URDF-based Kinect v2 model** for simulation in Gazebo
- ⚙️ Compatible with **ROS 2** framework
- 🖼️ Works seamlessly with **RViz** for visualization
- 🌍 Static positioning or movable models available
- 🌟 Includes camera and depth sensor simulation in Gazebo

---

## Installation 📥

Clone this repository into your ROS 2 workspace and build it with `colcon`:

```bash
cd ~/ros2_ws/src
git clone https://github.com/edupras/kinect_v2_urdf_ros2.git
cd ~/ros2_ws
colcon build
```
## Usage 🛠️
The repository contains three launch files (Rviz, Gazebo and both)
```bash
ros2 launch kinect_v2 kinect_v2.launch.py 
```

## Contents 📂
 - `urdf/`: Contains the Kinect v2 URDF and XACRO files
 - `meshes`: 3D model meshes (STL format) for the Kinect v2
 - `launch`: Launch files for Gazebo and RViz

## Contributions 🤝
We welcome contributions from the community! Feel free to:
- ⭐ Star this repository if you find it useful
- 🐞 Report any issues you encounter
- 🔧 Submit pull requests for enhancements or fixes

## Acknowledgements 🙌
This package is based on the original Kinect v2 URDF model created for ROS1 by [wangxian4423](https://github.com/wangxian4423/kinect_v2_udrf). Major thanks to the original author! 🎉