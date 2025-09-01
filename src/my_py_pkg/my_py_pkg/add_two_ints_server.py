#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from example_interfaces.srv import AddTwoInts
#so we added .srv now and AddTwoInts

class AddTwoIntsServerNode(Node):  
    def __init__(self):
        super().__init__("add_two_ints_server")
        # create Service Server
        # chose srv, then service name(USE VERB - action,communication), 
        # and callback
        # callback - server is not going to do aynthing on its 
        # own since it need a client 
        self.server_ = self.create_service(AddTwoInts,"add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add two ints has server has been started")
        
    # adding AddTwoInts.Request and AddTwoInts.Response makes it more explicit 
    # and easier to use and understand
    def callback_add_two_ints(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        # AddTwoInts is combination of two msgs!
        # We want to compute the SUM of a and b
        response.sum = request.a + request.b
        # if we didnt add request: AddTwoInts. we wouldnt have autocomplete
        self.get_logger().info(f"{str(request.a)} + {str(request.b)} = {str(response.sum)}")
        return response 
        # SERVICE NEEDS TO RETURN!
        
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()