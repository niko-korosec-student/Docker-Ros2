#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Int64

class NumberPublisherParamNode(Node):  
    def __init__(self):
        super().__init__("number_publisher_param")
        # name of the parameter and default value if we dont provide one
        # it will also set the data type for the parameter, it uses the data type for the default value
        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0)
        # insted of hardcoded value we use .get_parameter...
        # not value but parameter object so we need to .value (not method so no ())
        self.number_ = self.get_parameter("number").value
        self.timer_period = self.get_parameter("timer_period").value
        self.number_publisher_param_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(self.timer_period, self.publish_number)
        self.get_logger().info("Number Publisher (parameters) has been started")
        
    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_param_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherParamNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()