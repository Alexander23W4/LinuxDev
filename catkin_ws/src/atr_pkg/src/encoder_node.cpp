#include <ros/ros.h>
#include <std_msgs/String.h>
using namespace ros;

void distance_receive_callback(std_msgs::String distance_info){

    ROS_INFO(distance_info.data.c_str());
}

int main(int argc, char *argv[])
{
    init(argc, argv, "encoder_node");
    NodeHandle nh;

    Subscriber sub = nh.subscribe("distance_info", 10, distance_receive_callback);

    while(ok){
        spinOnce(); // similar to "have a glimpse of external interrupt(callback functions)"
    }

    return 0;
}


