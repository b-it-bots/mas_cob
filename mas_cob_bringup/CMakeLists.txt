cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_bringup)
find_package(catkin REQUIRED)

catkin_package(
  CATKIN_DEPENDS
    mcr_default_env_config
    mcr_teleop
    cob_bringup
    hokuyo_node
    robot_state_publisher
    openni2_launch
    tf
)

install(FILES robot.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY robots/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY components/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY tools/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS env.sh
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
