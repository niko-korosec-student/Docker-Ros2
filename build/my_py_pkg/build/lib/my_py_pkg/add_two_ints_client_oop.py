#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClient(Node):  
    def __init__(self):
        super().__init__("add_two_ints_client")
        # want to connect to any server providing the service add_two_ints
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")
        
    def call_add_two_ints(self, a, b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server Add two ints...")
        
        #create a request
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        #send a request async
        future = self.client_.call_async(request) 
        # we wont use spin as we do in no oop version
        # registers a callback
            #if you want to add extra arguments, need to add partial
        future.add_done_callback(partial(self.callback_call_add_two_ints, request=request))
        # so we can get it in the callback_call_add_two_ints method
        
    def callback_call_add_two_ints(self, future, request):
        response = future.result()
        self.get_logger().info(f"{str(request.a)} + {str(request.b)} = {str(response.sum)}")
            

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    #calling the node
    node.call_add_two_ints(2,7)
    node.call_add_two_ints(21,90)
    node.call_add_two_ints(2232,1521)
    # we make the node spin
    # node needs to be spinnig to receive response
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()