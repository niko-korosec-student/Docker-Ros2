#!/bin/bash

# Source base ROS2
source /opt/ros/jazzy/setup.bash

# Source the workspace install setup if it exists
if [ -f /home/ws/install/setup.bash ]; then
    source /home/ws/install/setup.bash
fi
