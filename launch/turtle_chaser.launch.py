from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node


def generate_launch_description():

    turtlesim = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    spawn_turtle = ExecuteProcess(
        cmd=[
            'ros2', 'service', 'call',
            '/spawn',
            'turtlesim/srv/Spawn',
            "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
        ],
        output='screen'
    )

    chaser = Node(
        package='turtle_chaser',
        executable='chaser',
        name='turtle_chaser'
    )

    return LaunchDescription([
        turtlesim,
        TimerAction(
            period=2.0,
            actions=[
                spawn_turtle,
                TimerAction(
                    period=2.0,
                    actions=[chaser]
                )
            ]
        )
    ])
