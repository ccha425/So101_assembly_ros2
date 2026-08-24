"""
This is a simple example for publishing robot joint states to the ROS2 network for the lerobot arms using multi threading
On the raspberry pi side, the hardware interface with the robot arms are setup and remapped to their corresponding numbers.

This example is adapted from 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html


"""
import rclpy
import threading
import time


from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import String
from sensor_msgs.msg import JointState

class MultiPublisherNode(Node):
    def __init__(self):
        super().__init__('multi_publisher_node')
        
        self.state_1 = 0
        self.state_2 = 0
        self.state_3 = 0
        self.state_4 = 0
        # Initialize joint states 
        self.joint_state_position1 = JointState()
        self.joint_state_position2 = JointState()
        self.joint_state_position3 = JointState()
        self.joint_state_position4 = JointState()

        self.joint_state_position1.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position1.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_state_position2.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position2.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_state_position3.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position3.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.joint_state_position4.name = ["shoulder_pan", "shoulder_lift","elbow_flex","wrist_flex","wrist_roll","gripper"]
        self.joint_state_position4.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        ## create publishers
        self.pub1 = self.create_publisher(JointState, 'robot1_follower/joint_commands', 10)
        self.pub2 = self.create_publisher(JointState, 'robot2_follower/joint_commands', 10)
        self.pub3 = self.create_publisher(JointState, 'robot3_follower/joint_commands', 10)
        self.pub4 = self.create_publisher(JointState, 'robot4_follower/joint_commands', 10)
        
        ## create and attach threads
        self.thread1 = threading.Thread(target=self.publish_data1)
        self.thread2 = threading.Thread(target=self.publish_data2)
        self.thread3 = threading.Thread(target=self.publish_data3)
        self.thread4 = threading.Thread(target=self.publish_data4)
        
        ## start the threads
        self.thread1.start()
        self.thread2.start()
        self.thread3.start()
        self.thread4.start()

    def robot_sequence_1(self):
        # Initial position
        self.joint_state_position1.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.pub1.publish(self.joint_state_position1)
        time.sleep(1)
        
        # waypoint 1
        self.joint_state_position1.position = [0.0, 0.1, 0.3, 0.9, 0.0, -1.0]
        self.pub1.publish(self.joint_state_position1)
        time.sleep(0.5)
        
        # waypoint 2
        self.joint_state_position1.position = [0.0, 0.1, 0.3, 0.9, 0.0, 1.0]
        self.pub1.publish(self.joint_state_position1)
        time.sleep(0.5)
        
        # waypoint 3
        self.joint_state_position1.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.pub1.publish(self.joint_state_position1)
        time.sleep(0.5)
        
        self.state_1 = 1

    def robot_sequence_2(self):
        time.sleep(0.5)
        
    def robot_sequence_3(self):
        # waypoint 1
        self.joint_state_position3.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.pub3.publish(self.joint_state_position3)
        time.sleep(0.5)

    def robot4_sequence_1(self):
        # for robot4 to pickup box and place on workbench
        # waypoint 1 (initial pose)
        self.joint_state_position4.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 2 (reach box grasp pose)
        self.joint_state_position4.position = [0.24, 0.85, -0.93, 1.5, 0.0, 1.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 3 (close gripper)
        self.joint_state_position4.position = [0.24, 0.85, -0.93, 1.5, 0.0, -0.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 4 (pickup)
        self.joint_state_position4.position = [0.24, 0.05, -0.3, 1.4, 0.0, -0.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 5 (place)
        self.joint_state_position4.position = [0.0, -0.17, 0.68, 1.1, 0.0, -0.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 6 (release box)
        self.joint_state_position4.position = [0.0, -0.17, 0.68, 1.1, 0.0, 0.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        # waypoint 7 (clear box)
        self.joint_state_position4.position = [0.0, -0.69, 0.68, 1.6, 0.0, 1.5]
        self.pub4.publish(self.joint_state_position4)
        time.sleep(0.5)
        
        self.state_4 = 1

    def publish_data1(self):
        while rclpy.ok():
            if self.state_1 == 0:
                # initial condition to move and pickup part
                self.robot_sequence_1()
            elif self.state_1 == 1:
                # state 1 grasp achieved
                if self.state_2 == 1:
                    # second robot complete cycle
                    # restart sequence
                    self.state_1 = 0
                    self.state_2 = 0
                else:
                    # wait for state 2 completion
                    time.sleep(0.5)
            else:
                # unexpected condition catch?
                time.sleep(0.5)
                
    def publish_data2(self):
        while rclpy.ok():
            time.sleep(0.5) 

    def publish_data3(self):
        while rclpy.ok():
            time.sleep(0.5) 
            # check for operating state
            # set arm to desired monitoring position
            # check for incoming image
            # check if QA pass or not
            # if pass -> set to new operating state
            # else execute object clearing sequence

    def publish_data4(self):
        while rclpy.ok():
            # check for operating state
            if self.state_4 == 0:
                self.robot4_sequence_1()  # pickup box and place on floor
            elif self.state_4 == 1:
                # box is ready - wait for QA state check (state3)
                if self.state_3 == 1:
                    # passed QA, begin pick and place object into box
                    # object placed in box, begin place lid
                    # lid placed, begin removal stack of box - remember to count which target place
                    # restart sequence
                    self.state_1 = 0
                    self.state_2 = 0
                    self.state_3 = 0
                    self.state_4 = 0
                else:
                    # wait for state QA completion
                    time.sleep(0.5)
            else:
                # unexpected condition - can use switch instead
                time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    multi_publisher_node = MultiPublisherNode()
    
    ## if you would like to use MultiThreadedExecutor
    executor = MultiThreadedExecutor()
    executor.add_node(multi_publisher_node)
    
    try:
        ## spin the multithread node
        executor.spin()
    except KeyboardInterrupt:
        ## exit function when code stops by keyboard
        ## stop the publisher node, and stop rclpy
        multi_publisher_node.destroy_node()
        rclpy.shutdown()
    finally:
        # Wait for all threads to complete
        multi_publisher_node.thread1.join()
        multi_publisher_node.thread2.join()
        multi_publisher_node.thread3.join()
        multi_publisher_node.thread4.join()

if __name__ == '__main__':
    main()



