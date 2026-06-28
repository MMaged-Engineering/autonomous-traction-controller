Autonomous Dynamic Traction Controller





A high-performance, ROS 2-based orchestrator designed for autonomous emergency braking (AEB) and dynamic traction management. This project demonstrates real-time sensor data processing, proportional control algorithms, and middleware integration within a Linux-based robotics environment.



System Architecture

The software stack follows a modular, hardware-agnostic design, ensuring scalability across various sensor configurations and motor platforms.



Key Technical Features

Middleware Integration: Utilizes ROS 2 (Jazzy) and DDS (Data Distribution Service) for robust, asynchronous inter-process communication via /scan and /cmd\_vel topics.



Vectorized Processing: Leverages numpy for high-speed LiDAR array slicing, enabling microsecond-latency obstacle detection.



Continuous Control: Implements a proportional throttle scaling algorithm that dynamically adjusts velocity based on real-time proximity to surrounding environment boundaries.



Environment: Developed within WSL 2 (Ubuntu 24.04), utilizing a professional-grade Linux workflow.



Project Structure

traction\_node.py: The core ROS 2 orchestrator. Handles subscription to laser scans and publication of motor twist commands.



lidar\_sensor.py: Hardware-abstraction layer for raw laser data acquisition.



aeb\_brain.py: The signal processing core containing the NumPy-based obstacle avoidance logic.



motor\_controller.py: Interface for vehicle dynamics and motor control.



Installation \& Usage

Ensure ROS 2 Jazzy is sourced: source /opt/ros/jazzy/setup.bash



Launch the node: python3 traction\_node.py



Test integration by publishing to the /scan topic:



Bash

ros2 topic pub --once /scan sensor\_msgs/msg/LaserScan "{ranges: \[10.0, 1.5, 1.5, 10.0]}"

