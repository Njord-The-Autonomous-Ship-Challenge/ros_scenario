# ros_scenario

Publishes information about the scenario objective.

Use the config file to customize the scenario.

scenario_type: 0 -> Situational Awareness

scenario_type: 1 -> Docking

scenario_type: 2 -> Maneuvering

In docking and maneuvering scenarios, the unity_x_coordinate and unity_z_coordinate communicate the position of the target that must be reached to complete the scenario. In for example docking scenarios, these parameters are set to the position of the dock in Unity.

The local_origin_latitude and _longitude are used to translate between local Unity coordinates and global latitude and longitude coordinates. These should not be changed.


Running roslaunch ~/catkin_ws/src/ros_scenario/launch/launch_njord_stack.launch will simultaenously launch all 3 nodes that are a part of the platform.
