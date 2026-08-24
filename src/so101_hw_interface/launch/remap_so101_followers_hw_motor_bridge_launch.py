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
        # Create and configure the follower robot1~4 node
        # This node will publish messages on the remapped topic '/so101_follower/joint_commands'
        # and '/so101_follower/joint_states'
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge',     # The name of the executable - defualt motor torque on
            name='robot1_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                # to '/robot1_follower/joint_commands'
                ('/so101_follower/joint_commands', '/robot1_follower/joint_commands'),
                ('/so101_follower/joint_states', '/robot1_follower/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot1_follower"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/robot1_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge',           # The name of the executable
            name='robot2_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                # to '/robot2_follower/joint_commands'
                ('/so101_follower/joint_commands', '/robot2_follower/joint_commands'),
                ('/so101_follower/joint_states', '/robot2_follower/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot2_follower"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/robot2_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge',           # The name of the executable
            name='robot3_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                # to '/robot3_follower/joint_commands'
                ('/so101_follower/joint_commands', '/robot3_follower/joint_commands'),
                ('/so101_follower/joint_states', '/robot3_follower/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot3_follower"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/robot3_calibration.yaml"}
            ]
        ),
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge',           # The name of the executable
            name='robot4_motor_bridge',           # A unique name for this node instance
            remappings=[
                # Remap the default '/so101_follower/joint_commands' topic 
                # to '/robot4_follower/joint_commands'
                ('/so101_follower/joint_commands', '/robot4_follower/joint_commands'),
                ('/so101_follower/joint_states', '/robot4_follower/joint_states'),
            ],
            output='screen',
            parameters=[
            {"port":"/dev/robot4_follower"},
            {"calib_file":"~/Lerobot_ros2/src/so101_hw_interface/config/robot4_calibration.yaml"}
            ]
        )
    ])
