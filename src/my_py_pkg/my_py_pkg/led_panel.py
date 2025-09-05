#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):  
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0,0,0]
        self.led_states_pub_ = self.create_publisher(LedStateArray, "led_panel_state", 10)
        self.led_states_timer_ = self.create_timer(5.0, self.publish_led_state)
        self.set_led_service_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.get_logger().info("LED panel has been started")
        
    def publish_led_state(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_pub_.publish(msg)
    
    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        led_number = request.led_number
        state = request.state
        
        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False
            return response

        if state not in [0, 1]:
            response.success = False
            return response
        
        self.led_states_[led_number] = state
        #you can publish on topic from anywhere
        self.publish_led_state()
        #when we change the state we publish immediately 
        response.success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()