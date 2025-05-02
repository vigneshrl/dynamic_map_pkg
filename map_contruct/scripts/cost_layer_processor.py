#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from visualization_msgs.msg import MarkerArray
import numpy as np

class CostLayerProcessor(Node):
    def __init__(self):
        super().__init__('cost_layer_processor')
        
        # Subscribe to the cost layer topic
        self.cost_sub = self.create_subscription(
            MarkerArray,
            '/cost_layer',
            self.cost_callback,
            10)
        
        self.get_logger().info('Cost Layer Processor initialized')

    def cost_callback(self, msg):
        # Process the cost layer markers
        self.get_logger().info(f'Received cost layer with {len(msg.markers)} markers')
        
        # Example processing: Count markers by color
        red_count = 0
        green_count = 0
        
        for marker in msg.markers:
            if marker.color.r > 0.5:  # Red markers
                red_count += 1
            elif marker.color.g > 0.5:  # Green markers
                green_count += 1
        
        # self.get_logger().info(f'High cost areas (red): {red_count}, Low cost areas (green): {green_count}')

def main(args=None):
    rclpy.init(args=args)
    node = CostLayerProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 