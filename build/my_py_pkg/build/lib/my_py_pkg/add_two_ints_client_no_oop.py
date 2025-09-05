#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop")
    # We dont need spin function
    
    client = node.create_client(AddTwoInts, "add_two_ints")
    # wait for the service to be up
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for server Add two ints...") # warning instead of info
    
    request = AddTwoInts.Request()
    request.a = 123
    request.b = 99
    
    # we can have .call or .call_async
    # .call is snyc call and it can couse errors and get deadlock situation
    future = client.call_async(request)
    # future object
    # spin the node util we get a response (future)
    rclpy.spin_until_future_complete(node, future) # not good to use
    
    response = future.result()
    node.get_logger().info(f"{str(request.a)} + {str(request.b)} = {str(response.sum)} ")
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()