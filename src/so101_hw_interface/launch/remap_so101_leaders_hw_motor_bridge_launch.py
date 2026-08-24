from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """
    Generate a launch description for topic remapping
 
    Returns
    -------
    LaunchDescription
        A launch description object containing the configured nodes
    """
    return LaunchDescription([
        # Create and configure the leader robot1~4 node
        # This node will publish messages on the remapped topic '/so101_follower/joint_commands'
        # and '/so101_follower/joint_states'
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge_leader', # The name of the executable, use leader package with torque disabled
            name='leader1_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                # to '/robot3_follower/joint_commands'
                ('/so101_follower/joint_commands', '/robot1_leader/joint_commands'),
                ('/so101_follower/joint_states', '/robot1_leader/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot1_leader"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/leader1_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge_leader',           # The name of the executable
            name='leader2_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                ('/so101_follower/joint_commands', '/robot2_leader/joint_commands'),
                ('/so101_follower/joint_states', '/robot2_leader/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot2_leader"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/leader2_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge_leader',           # The name of the executable
            name='leader3_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                ('/so101_follower/joint_commands', '/robot3_leader/joint_commands'),
                ('/so101_follower/joint_states', '/robot3_leader/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot3_leader"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/leader3_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge_leader',           # The name of the executable
            name='leader4_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                ('/so101_follower/joint_commands', '/robot4_leader/joint_commands'),
                ('/so101_follower/joint_states', '/robot4_leader/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot4_leader"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/leader4_calibration.yaml"}
            ]
        )
    ])
