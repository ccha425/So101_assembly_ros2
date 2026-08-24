"""
This is a simple example for publishing robot joint states to the ROS2 network for the lerobot arms
On the raspberry pi side, the hardware interface with the robot arms are setup and remapped to their 
corresponding numbers.

This example is adapted from 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

"""
import rclpy
import time
import threading

from std_msgs.msg import String
from sensor_msgs.msg import JointState

rclpy.init()

# Create nodes for publishers
node1 = rclpy.create_node('robot1_position_publisher')
node2 = rclpy.create_node('robot2_position_publisher')
node3 = rclpy.create_node('robot3_position_publisher')
node4 = rclpy.create_node('robot4_position_publisher')
# Assign publishers to nodes
pub1 = node1.create_publisher(JointState, 'robot1_follower/joint_commands', 10)
pub2 = node2.create_publisher(JointState, 'robot2_follower/joint_commands', 10)
pub3 = node3.create_publisher(JointState, 'robot3_follower/joint_commands', 10)
pub4 = node4.create_publisher(JointState, 'robot4_follower/joint_commands', 10)

# Spin for single separate thread
# thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
# thread.start()
# Spetup multi thread
executor = rclpy.executors.MultiThreadedExecutor()
executor.add_node(node1)
executor.add_node(node2)
executor.add_node(node3)
executor.add_node(node4)
# Spetup for multi thread
executor_thread = threading.Thread(target=executor.spin, daemon=True)
executor_thread.start()

# define dummy state variables for joints
joint_state_position = JointState()
joint_state_position.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
joint_state_position.position = [0.0, 0.0, 0.0, 0.0, 0.0, -1.0]

rate = node1.create_rate(50) # Create a Rate object for 50 Hz


try:
    while rclpy.ok():
        # Set waypoint 1
        joint_state_position.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        node1.get_logger().info(f'moving to state: {joint_state_position.position}')
        # Assign waypoint 1 as goal to robots
        pub1.publish(joint_state_position)
        pub2.publish(joint_state_position)
        pub3.publish(joint_state_position)
        pub4.publish(joint_state_position)
        # wait some time for joint completion
        time.sleep(2)
        # alternatively you can call a function to check if the follower has reached the target position
        # this can be done by using a subscriber to the robot follower joint_states topic
        # alternatively you can use the rate.sleep() 
        # rate.sleep()

        # Set waypoint 2
        joint_state_position.position = [-1.0, 0.0, 0.0, 0.0, 0.0, -1.0]
        node1.get_logger().info(f'moving to state: {joint_state_position.position}')
        # Assign waypoint 2 as goal to robots
        pub1.publish(joint_state_position)
        pub2.publish(joint_state_position)
        # Set waypoint 3
        joint_state_position.position = [1.0, 0.0, 0.0, 0.0, 0.0, -1.0]
        # Assign waypoint 3 as goal to robots
        pub3.publish(joint_state_position)
        pub4.publish(joint_state_position)
        time.sleep(2)
        # rate.sleep()
    
except KeyboardInterrupt:
    pass
rclpy.shutdown()
thread.join()
