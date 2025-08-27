#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from example_interfaces.msg import String #msgs type

class RobotNewsStationNode(Node):  
    def __init__(self):
        super().__init__("robot_news_station")
        #Strig, name needs to start with letter
        #last we add que size 
        self.publishers_ = self.create_publisher(String, "robot_news",10)
        #add a timer, time in sec, method to call
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot news radio has been starterd")
        
    def publish_news(self):
        msg = String()
        msg.data = "Hello" # .data is from the msgs type
        self.publishers_.publish(msg)
        #this is how we publish msg on a topic      

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()