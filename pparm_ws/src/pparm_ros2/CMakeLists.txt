cmake_minimum_required(VERSION 3.8)
project(pparm_ros2)

# Alapvető ROS 2 csomagok keresése
find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  worlds
  urdf
  rviz
  meshes
  DESTINATION share/${PROJECT_NAME}
)
# Ha le akarod futtatni a teszteket (amiket a fában láttam)
#if(BUILD_TESTING)
# find_package(ament_lint_auto REQUIRED)
# ament_lint_auto_find_test_dependencies()
#endif()

# Ez a parancs zárja le a csomagot és regisztrálja a ROS 2 felé
ament_package()