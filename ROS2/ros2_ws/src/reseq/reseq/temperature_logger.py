import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the TemperatureLogger node
class TemperatureLogger(Node):
    def __init__(self,logfile):
        super().__init__('temperature_logger')

        self.logfile = open(logfile, "a")
        
        self.declare_parameter('threshold', 50.)
        self.threshold = self.get_parameter("threshold").value

        self.subscription = self.create_subscription(Float32,'/temperature',self.temp_callback, 10)

    def temp_callback(self,msg):
        temperature = msg.data
        
        if temperature >= self.threshold:
         self.get_logger().warn(f'Drone has reached {temperature: .2f} °C')
         #writing on file
         self.logfile.write(f"{temperature: .2f}\n")
         self.logfile.flush()


def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")
    #logger = TemperatureLogger()

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()