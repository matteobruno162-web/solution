from launch import LaunchDescription
from launch_ros.actions import Node

pack='reseq'
def generate_launch_description():
    return LaunchDescription([
        Node(package=pack, executable='TemperatureSensor', namespace='temperature',
             output='screen'
             #,prefix='xterm -hold -e'
             ),
        Node(package=pack, executable='TemperatureLogger', namespace='temperature',
             output='screen'
             #,prefix='xterm -hold -e'
             ),

    ])