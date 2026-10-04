cmake_minimum_required(VERSION 3.5)
project(james_gazebo)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rviz2 REQUIRED)

# Install launch files
install(
  DIRECTORY launch rviz models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()