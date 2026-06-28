import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class DynamicTractionNode(Node):
    def __init__(self):
        # 1. Initialize the Node with a name
        super().__init__('traction_controller')
        
        # 2. Set our hardware parameters as internal state
        self.base_cruising_speed = 5.0
        self.max_track_width = 5.0
        
        # 3. Create a Subscriber (Input Port from LiDAR)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10
        )
            
        # 4. Create a Publisher (Output Port to Motors)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.get_logger().info("Dynamic Traction Node is active and listening...")

    def lidar_callback(self, msg):
        """
        This function is triggered by a hardware interrupt. 
        It runs automatically every single time the LiDAR finishes a 360-degree spin.
        """
        # Convert the raw incoming ROS 2 message into our high-speed NumPy array
        scan_matrix = np.array(msg.ranges)
        
        # --- PHASE 2 LOGIC INTEGRATED ---
        # 1. Slice left_clearance and right_clearance
        left_clearance = np.min(scan_matrix[1:3])
        right_clearance = np.min(scan_matrix[6:8])
        
        # 2. Find the tightest_clearance 
        tightest_clearance = min(left_clearance, right_clearance)
        
        # 3. Calculate the throttle_scale proportionally (using self.)
        throttle_scale = tightest_clearance / self.max_track_width
        
        # 4. Calculate the target_velocity (using self.)
        safe_scale = min(throttle_scale, 1.0)
        target_velocity = self.base_cruising_speed * safe_scale
        
        # --- SENDING THE PHYSICAL COMMAND ---
        # We package your target_velocity into a standard ROS 2 Twist message
        cmd_msg = Twist()
        cmd_msg.linear.x = float(target_velocity) # Forward velocity
        
        # Publish it to the motors
        self.publisher.publish(cmd_msg)
        self.get_logger().info(f"Walls pinching! Adjusting Motors to: {target_velocity:.2f} m/s")

def main(args=None):
    rclpy.init(args=args)
    node = DynamicTractionNode()
    
    try:
        rclpy.spin(node) # This keeps the node alive, waiting for LiDAR data
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()