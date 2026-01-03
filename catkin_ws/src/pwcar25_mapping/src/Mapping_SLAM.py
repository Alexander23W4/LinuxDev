import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import math

# msg is LaserScan data type
def Mapping_lidar_Callback(msg):  # arrange the msg from lidar right here



if __name__ == "__main__":
    rospy.init_node("Mapping_SLAM_node")
    # the /scan topic is from gazebo, once robot(with lidar) in gazezbo runs, 
    # the /scan topic will work
    Mapping_lidar_subscriber = rospy.Subscriber("/scan", LaserScan, Mapping_lidar_Callback, queue_size=10)
    # this includes a callback function which is brought in 
    # the callback function could arrange the data immediately as soon as the data comes
    rospy.spin() # hold the node






# SCAN_FREQUENCY = 5   # define 5 scan 5 round per second 
# SCAN_DENSITY = 360   # define 360 points per round

# Lidar_message = LaserScan()

# Lidar_message.header.frame_id = "Mapping_Lidar"
# Lidar_message.header.stamp = rospy.Time.now()
# Lidar_message.angle_max = 2 * math.pi
# Lidar_message.angle_min = 0
# Lidar_message.angle_increment = (Lidar_message.angle_max  - Lidar_message.angle_min ) / SCAN_DENSITY
# Lidar_message.range_max = 5.0
# Lidar_message.range_min = 0.2
# Lidar_message.scan_time = 1 / SCAN_FREQUENCY
# Lidar_message.time_increment = Lidar_message.scan_time / SCAN_DENSITY
# Lidar_message.scan.ranges = ranges           
# Lidar_message.scan.intensities = [0.0] * SCAN_DENSITY








