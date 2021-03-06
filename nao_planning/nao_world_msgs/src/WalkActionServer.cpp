#include <nao_world_msgs/WalkAction.h>
#include <actionlib/server/simple_action_server.h>
#include "ros/ros.h"

typedef actionlib::SimpleActionServer<nao_world_msgs::WalkAction> Server;

void execute(const nao_world_msgs::WalkGoalConstPtr& goal, Server* as)
{
  // Do lots of awesome groundbreaking robot stuff here
  std::cout<<"\n\n\n\nWRONG SERVER\n\n\n\n\n";
  ROS_INFO();
  as->setSucceeded("\n\n\n\nWRONG SERVER\n\n\n\n\n");
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "walk_server");
  ros::NodeHandle n;
  Server server(n, "/nao_world_msgs/walk_action_server", boost::bind(&execute, _1, &server), false);
  server.start();
  ros::spin();
  return 0;
}
