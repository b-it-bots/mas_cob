cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_place_action)

find_package(catkin REQUIRED COMPONENTS
  rospy
  genmsg
  geometry_msgs
  actionlib_msgs
  actionlib
  mas_lwr_kinematics
  roslint
  message_generation
)

roslint_python()  # pep8 linting
roslint_cpp()     # ROS wrapper of Google's cpplint

catkin_python_setup()

add_action_files(
  DIRECTORY
  ros/action
  FILES
  Place.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  geometry_msgs
)

catkin_package(
    CATKIN_DEPENDS
    mdr_behavior_msgs
    moveit_msgs
    sensor_msgs
    mas_lwr_kinematics
    actionlib_msgs
    geometry_msgs
    message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
   ros/scripts/place_action
   ros/scripts/place_action_client_test
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)
