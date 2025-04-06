import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):

    def __init__(self):
        super().__init__("simple_publisher")
        self.pub_ = self.create_publisher(String, "chatter", 10) #https://docs.ros2.org/foxy/api/rclpy/api/topics.html
        self.counter_ = 0
        self.frequency_ = 1.0
        self.get_logger().info("Publishing at %d Hz" % self.frequency_)
        
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback) #The timer will be started and every timer_period_sec number of seconds the provided callback function will be called.

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_
        self.pub_.publish(msg)
        self.counter_ += 1

#https://docs.ros.org/en/iron/p/rclpy/api/init_shutdown.html#rclpy.init
def main():
    rclpy.init() #Initialize ROS communications for a given context.

    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher) #Execute work and block until the context associated with the executor is shutdown.
    
    simple_publisher.destroy_node()
    rclpy.shutdown() #Shutdown a previously initialized context.


if __name__ == '__main__':
    main()