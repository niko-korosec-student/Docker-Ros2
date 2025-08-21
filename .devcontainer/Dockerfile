FROM ros:jazzy
ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
# Base system updates + tools
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
        python3-pip \
        nano \            
    && rm -rf /var/lib/apt/lists/*

ENV SHELL /bin/bash

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************
# Install ROS2 demo nodes (talker/listener)
RUN sudo apt-get update && sudo apt-get install -y \
    ros-jazzy-demo-nodes-cpp \
    ros-jazzy-ros-base \
    ros-jazzy-demo-nodes-py \
    ros-jazzy-rviz2 \
    ros-jazzy-ros2cli \
    ros-jazzy-teleop-twist-keyboard \
    ros-jazzy-turtlesim \
    #ros-jazzy-slam-toolbox \
    #ros-jazzy-nav2-bringup \
 && sudo rm -rf /var/lib/apt/lists/*

# Source ROS automatically in bash
#RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/$USERNAME/.bashrc

# Set the default user. Omit if you want to keep the default as root.
USER $USERNAME
WORKDIR /home/ws
CMD ["/bin/bash"]