# ROS_RIA_005_PythonClasses
This repository is further building on the previous, [ROS_RIA_004_CustomServiceMsg](https://github.com/FadedIllusions/ROS_RIA_004_CustomServiceMsg); this time, using an object oriented approach -- Sphero BB8

In the first terminal, launch the service server as you did previously:
```roslaunch my_custom_srv_msg_pkg start_bb8_move_custom_service_server.launch```

Though, being as we haven't a launch file for the newly written script, call the service from a second terminal as follows: ```rosservice call /move_bb8_in_circle_custom TAB-TAB```. Doing so should autofill the needed paramaters for such a call; then, merely modify the parameters as desired.
