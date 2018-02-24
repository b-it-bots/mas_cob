cmake_minimum_required(VERSION 2.8.3)
project(mas_cob_emergency_stop_monitor)

find_package(catkin REQUIRED
  COMPONENTS
    roscpp
    std_msgs
    cob_relayboard
    mdr_speech_msgs
)

catkin_package(
  CATKIN_DEPENDS
    message_runtime
    std_msgs
    cob_relayboard
    mdr_speech_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(emergency_stop_monitor
  ros/src/emergency_stop_monitor.cpp
)

target_link_libraries(emergency_stop_monitor
  ${catkin_LIBRARIES}
)

add_dependencies(emergency_stop_monitor
  ${catkin_EXPORTED_TARGETS}
)

install(TARGETS emergency_stop_monitor
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
