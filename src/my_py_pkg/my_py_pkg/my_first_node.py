#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 

class MyNode(Node): 
    
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello for the first time")
        self.create_timer(1.0, self.timer_callback) #no pharaticies since we are not calling a function!
        
    
    #timer is one of the most imporatnt ros2 functionalities
    def timer_callback(self):
        self.get_logger().info(f"Hello {str(self.counter_)}")
        self.counter_ += 1
    
def main(args=None):
    rclpy.init(args=args) #initilizes ROS2
    node = MyNode()
   
    rclpy.spin(node) #this will keep the node we just created running
    rclpy.shutdown() 

if __name__ == "__main__":
    main()

 #python file is NOT the node, but node is inside the py file!