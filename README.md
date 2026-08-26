# LeRobot ROS2 Assembly Line Project - SO101 Arms

A ROS2 implementation for the SO101 follower/leader robotic arm, providing complete hardware interface, MoveIt motion planning, and topic-based joint control. Adapted and based on AgRoboticsResearch code: https://github.com/AgRoboticsResearch/Lerobot_ros2.git

## 🤖 Overview

This repository contains ROS2 packages for controlling the SO101 follower arm robot. It includes:

- **Robot Description**: URDF/XACRO models with 3D meshes
- **MoveIt Integration**: Motion planning and execution
- **Hardware Interface**: Direct motor control via Feetech servos
- **Topic-based Control**: Flexible control interface

## 📦 Packages

### `so101_follower_description`
Robot description package containing:
- URDF/XACRO robot model
- 3D mesh files (.stl/.part)
- RViz visualization configuration
- Launch files for robot display

### `so101_follower_moveit`
MoveIt configuration package with:
- Kinematic configuration
- Motion planning setup
- Controller configuration
- Collision detection setup

### `so101_hw_interface`
Hardware interface package providing:
- Motor control via Feetech protocol
- Calibration utilities
- Hardware abstraction layer
- LeRobot integration utilities

### `robot_control`
Generic topic-based control interface for:
- Teleoperation
- Custom control strategies and mulri-robot synced waypoints
- Integration with external systems

## 🚀 Quick Start

### Prerequisites
- ROS2 Humble or later
- MoveIt2
- Python 3.8+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ccha425/So101_assembly_ros2.git
cd So101_assembly_ros2
```

2. Install dependencies:
```bash
rosdep install --from-paths src --ignore-src -r -y
```

3. Build the workspace:
```bash
colcon build
source install/setup.bash
```

### Usage

#### Visualize the robot:
```bash
ros2 launch so101_follower_description display.launch.py
```

#### Launch MoveIt demo WIP:
```bash
ros2 launch so101_follower_moveit demo.launch.py
```

#### Start hardware interface "single":
```bash
ros2 launch so101_hw_interface so101_hw.launch.py
```

#### Calibrate the arm:
```bash
ros2 run so101_hw_interface so101_calibrate
```

## 🎛️ Advanced Usage

### Hardware Control with Joint State Publisher and Teleoperation
For manual joint control with the hardware interface:

```bash
# Terminal 1: Launch follower robot harware nodes (hardware interface)
ros2 launch so101_hw_interface remap_so101_followers_hw_motor_bridge_launch.py

# Terminal 2: Launch leader robot harware nodes (hardware interface)
ros2 launch so101_hw_interface remap_so101_leaders_hw_motor_bridge_launch.py

# Terminal 3: Launch joint state publisher for all 4 robot arms for manual control
ros2 run robot_control teleoperate_robots
```

This setup allows you to:
- **Visualize** the robot in RViz with real joint states from hardware
- **Control** joint positions manually using the GUI sliders
- **Monitor** real-time feedback from the Feetech servos

### Topic Remapping Guide
- `/so101_follower/joint_states`: Real joint positions from hardware
- `/so101_follower/joint_commands`: Desired joint positions to hardware
- Use topic remapping (`-r`) to connect different components

## 🔧 Configuration - single arm

### Hardware Setup
- WIP

### Calibration
1. Run calibration script: `so101_calibrate`
2. Follow on-screen instructions to move joints
3. Calibration data saved automatically

## 📚 Documentation

- [Hardware Setup Guide WIP](docs/hardware_setup.md)
- [Calibration Process WIP](docs/calibration.md)


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

WIP

## 🔗 Related Projects

- [LeRobot](https://github.com/huggingface/lerobot) - Main LeRobot framework
- [SO101 Hardware](https://github.com/TheRobotStudio/SO-ARM101) - Original hardware design
- [ROS2 Integration](https://github.com/AgRoboticsResearch/Lerobot_ros2) - Single arm codebase

---
