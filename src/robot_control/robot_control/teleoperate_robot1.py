"""
This is a simple teleoperating code for transferring the monitored leader arm values to the follower arm joint_commands
You will need to have the robot interface running on the network for both the leader and followers first
angle mismatch will come from manufacturing of the arms and calibration 

using timer instead of rate, code can be optimized for threading and timing 

This code is designed to be run from the main host or from the leader raspberry pi computer - robot2
"""

# import required libraries
import rclpy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from rclpy.node import Node

# main teleop subscriber-publisher node
class Teleop_Publisher(Node):

    def __init__(self):
        super().__init__('teleoperate_publisher_1') # init node
        # Creates publisher nodes
        self.pub_1 = self.create_publisher(JointState, 'robot1_follower/joint_commands', 10)
        self.pub_2 = self.create_publisher(JointState, 'robot2_follower/joint_commands', 10)
        # Create subscriver nodes and assign callbacks for processing the data
        self.sub_1 = self.create_subscription(JointState, 'robot1_leader/joint_states', self.teleop_robot1_callback, 10)
        self.sub_2 = self.create_subscription(JointState, 'robot2_leader/joint_states', self.teleop_robot2_callback, 10)
        # Define operating frequency - how frequent should the code publish new datapoints
        timer_period = 0.0167  # seconds (60Hz)
        # create a scheduled timer callback function to ensure publishing at correct period
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # Define variable for JointState() format
        self.joint_state_position_robot1 = JointState()
        self.joint_state_position_robot2 = JointState()
        # Iniitalize dummy positions and name format
        self.joint_state_position_robot1.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position_robot1.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_state_position_robot2.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position_robot2.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.sub_1  # prevent unused variable warning
        self.sub_2  # prevent unused variable warning

    # data renamed as msg inside this callback
    # update robot position as the new position from leader when new data comes in
    def teleop_robot1_callback(self, msg):
        self.joint_state_position_robot1.position=msg.position
        # self.get_logger().info(f'Publishing: {self.joint_state_position_robot1.position}')
     
    # update robot position as the new position from leader when new data comes in
    def teleop_robot2_callback(self, msg):
        self.joint_state_position_robot2.position=msg.position
        # self.get_logger().info(f'Publishing: {self.joint_state_position_robot2.position}')
 
    # Timer function to publish the currently stored data to the robots
    def timer_callback(self):
        self.pub_1.publish(self.joint_state_position_robot1)
        self.pub_2.publish(self.joint_state_position_robot2)

def main(args=None):
    rclpy.init(args=args)
    tel_pub = Teleop_Publisher()
    try:
        rclpy.spin(tel_pub)
    except KeyboardInterrupt:
        pass
    finally:
        tel_pub.destroy_node()
        rclpy.shutdown()
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
if __name__ == '__main__':
    main()
