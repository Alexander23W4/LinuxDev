#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "ultrasound_sensor_node");
    printf("robot, enjoy your new life!\n");

    ros::NodeHandle nh;  // NodeHandle and inti are both the class in roscpp pkg.
    ros::Publisher pub = nh.advertise<std_msgs::String>("distance_info", 10);
    // distance_info represents the name of topic, second parameter is buffer length

    ros::Rate loop_rate(10); //Attention! this is not delay but times that the loop runs per second.
    

    while(ros::ok()){
        printf("Message Sending:\n");

        std_msgs::String distance_info_msg;
        distance_info_msg.data = "no data right now.";
        pub.publish(distance_info_msg);

        loop_rate.sleep();
    }
    return 0;
}
