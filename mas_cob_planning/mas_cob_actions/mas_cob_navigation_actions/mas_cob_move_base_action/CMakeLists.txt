cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_move_base_action)

find_package(catkin REQUIRED COMPONENTS
  mdr_move_base_action
  mas_cob_move_arm_action
)

catkin_package(
 CATKIN_DEPENDS
   mdr_move_base_action
   mas_cob_move_arm_action
)

install(DIRECTORY ros/launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/ros/launch
)
