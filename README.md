# Autonomous Turtle Chaser

A multi-node ROS 2 application built using Python that enables a user-controlled turtle to be autonomously tracked and followed by a second turtle in the Turtlesim simulation environment.

## Project Overview

This project demonstrates autonomous target tracking and real-time movement control using ROS 2.

The system consists of:

- **Turtle 1 (Leader):** Manually controlled using keyboard teleoperation.
- **Turtle 2 (Chaser):** Autonomously follows the leader using position and orientation data.

## Features

- Multi-node ROS 2 architecture.
- Keyboard-based turtle teleoperation.
- Real-time position tracking using ROS 2 topics.
- Distance and angular error calculations.
- Autonomous velocity control.
- Automated simulation startup using a ROS 2 launch file.

## Technologies Used

- ROS 2 Jazzy
- Python 3
- rclpy
- Turtlesim
- geometry_msgs
- Linux / Ubuntu
- Docker

## Project Structure

```text
turtle_chaser/
├── launch/
│   └── turtle_chaser.launch.py
├── turtle_chaser/
│   ├── __init__.py
│   └── chaser.py
├── resource/
│   └── turtle_chaser
├── test/
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

## Installation and Setup

### 1. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash
```

### 2. Create a workspace

```bash
mkdir -p ~/turtle_chaser_ws/src
cd ~/turtle_chaser_ws/src
```

### 3. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 4. Build the package

```bash
cd ~/turtle_chaser_ws
colcon build --packages-select turtle_chaser
source install/setup.bash
```

## Running the Simulation

### 1. Launch the simulation

```bash
ros2 launch turtle_chaser turtle_chaser.launch.py
```

This automatically:
- Starts the Turtlesim environment.
- Spawns the second turtle.
- Starts the autonomous chaser node.

### 2. Start keyboard teleoperation

Open a second terminal:

```bash
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtle_teleop_key
```

Use the arrow keys to control Turtle 1. Turtle 2 will autonomously track and follow it.

## How the Chasing Algorithm Works

1. The chaser node subscribes to the pose topics of both turtles.
2. It calculates the positional difference between the leader and chaser.
3. It calculates the Euclidean distance between the turtles.
4. It calculates the desired heading using the inverse tangent function.
5. It computes the angular error relative to the chaser's current orientation.
6. It publishes velocity commands to `/turtle2/cmd_vel`.
7. The process repeats continuously using a timer callback.

## ROS 2 Topics

| Topic | Purpose |
|---|---|
| `/turtle1/pose` | Leader position |
| `/turtle2/pose` | Chaser position |
| `/turtle2/cmd_vel` | Chaser velocity commands |

## Author

Dhruvi

## License

Apache-2.0
