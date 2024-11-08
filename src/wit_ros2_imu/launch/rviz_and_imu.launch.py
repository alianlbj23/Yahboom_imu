from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    rviz_and_imu_node = Node(
        package='wit_ros2_imu',
        executable='wit_ros2_imu',  # 使用 'executable' 而不是 'node_executable'
        name='imu',  # 使用 'name' 而不是 'node_name'
        remappings=[('/wit/imu', '/imu/data')],
        parameters=[{'port': '/dev/imu_usb'},
                    {"baud": 9600}],
        output="screen"
    )

    rviz_display_node = Node(
        package='rviz2',
        executable="rviz2",  # 使用 'executable'
        output="screen"
    )

    return LaunchDescription(
        [
            rviz_and_imu_node,
            # rviz_display_node
        ]
    )
