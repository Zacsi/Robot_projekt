import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/telegdicsongor/Robot_projekt/pparm_ws/install/pparm_ros2'
