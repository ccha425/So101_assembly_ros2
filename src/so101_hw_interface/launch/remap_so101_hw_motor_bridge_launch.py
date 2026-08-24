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
        # Create and configure the robot3 node
        # This node will publish messages on the remapped topic '/so101_follower/joint_commands'
        # and '/so101_follower/joint_states'
        Node(
            package='so101_hw_interface',      # The package containing the node
            executable='so101_motor_bridge',           # The name of the executable
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
    ])
