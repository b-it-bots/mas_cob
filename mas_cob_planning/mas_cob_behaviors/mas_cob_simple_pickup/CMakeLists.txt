cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_simple_pickup)

find_package(catkin REQUIRED COMPONENTS rospy)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
    mdr_behavior_msgs
    moveit_msgs
    sensor_msgs
)

install(PROGRAMS
  ros/scripts/simple_pickup_node
  ros/tools/simple_pickup_test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
