cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_audio_monitor)

find_package(catkin REQUIRED COMPONENTS rospy mdr_monitoring_msgs)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy mdr_monitoring_msgs
)

install(PROGRAMS
  ros/scripts/audio_monitor_node
  ros/src/mas_cob_audio_monitor/audio_monitor.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
