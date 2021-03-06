cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
rosbuild_gensrv()

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})

rosbuild_add_executable(move_arm_client_node src/nodes/move_arm_client_node.cpp 
	src/utilities/utilities.cpp src/move_arm_action_clients/MoveArmActionClient.cpp)
rosbuild_add_executable(move_pick_place_server_node src/nodes/move_pick_place_server_node.cpp
	src/utilities/utilities.cpp src/move_arm_action_clients/MovePickPlaceServer.cpp src/move_arm_action_clients/MoveArmActionClient.cpp)
rosbuild_add_executable(move_pick_place_test src/nodes/move_pick_place_test.cpp
	src/utilities/utilities.cpp src/move_arm_action_clients/MovePickPlaceServer.cpp src/move_arm_action_clients/MoveArmActionClient.cpp)
	
#rosbuild_add_executable(material_handling_server_test src/nodes/material_handling_server_test.cpp 
#	src/utilities/utilities.cpp)

rosbuild_add_executable(test_state_machine src/tests/test_state_machine.cpp)
rosbuild_add_executable(mtconnect_state_machine_server src/nodes/mtconnect_state_machine_server.cpp 
	src/state_machine/state_machine.cpp src/utilities/utilities.cpp src/move_arm_action_clients/MoveArmActionClient.cpp)

rosbuild_add_executable(grasp_action_server src/nodes/grasp_execution_action_server.cpp src/gripper_message/gripper_message.cpp)
target_link_libraries(grasp_action_server simple_message)

rosbuild_add_executable(grasp_test_utility src/nodes/grasp_test_utility.cpp src/gripper_message/gripper_message.cpp)
target_link_libraries(grasp_test_utility simple_message)

