from setuptools import find_packages, setup

package_name = 'robot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='robot@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'robo_move = robot_control.robo_move:main',
            'robo_move_multi = robot_control.robo_move_multi:main',
            'teleoperate_robots = robot_control.teleoperate_robots:main',
            'teleoperate_robot1 = robot_control.teleoperate_robot1:main',
            'teleoperate_robot2 = robot_control.teleoperate_robot2:main'
        ],
    },
)
