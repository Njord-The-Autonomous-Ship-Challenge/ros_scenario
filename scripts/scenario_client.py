#!/usr/bin/env python2

import rospy

from std_msgs.msg import Int32
import geometry_msgs.msg as geomsgs
#from rosgraph_msgs.msg import Clock
import numpy as np

def scenario(type,N_local,E_local, N_global, E_global):
        rate = 1 # 1 Hz
        scenario_gps_pub = rospy.Publisher('scenario/target/gps', geomsgs.Point, queue_size=10)
        scenario_local_pub = rospy.Publisher('scenario/target/local', geomsgs.Point, queue_size=10)
        scenario_type_pub = rospy.Publisher('scenario/type', Int32, queue_size=10)

        gps_msg = geomsgs.Point(
                x = N_global,
                y = E_global,
                z = 0
        )

        local_msg = geomsgs.Point(
                x = N_local,
                y = E_local,
                z = 0
        )

        while not rospy.is_shutdown():
                scenario_gps_pub.publish(gps_msg)
                scenario_local_pub.publish(local_msg)
                scenario_type_pub.publish(type)
                rospy.sleep(1/rate)    


if __name__ == '__main__':
        rospy.init_node('scenario_instance', anonymous=True)
        scenario_params = rospy.get_param('~')
        scenario_type = scenario_params["scenario_type"]
        # Translating from Unity's frame; Positive x->East, Positize z->North
        scenario_E = scenario_params["unity_x_coordinate"]
        scenario_N = scenario_params["unity_z_coordinate"]
        # GPS coordinate of model origin in Unity 
        lat_origo = scenario_params["local_origin_latitude"]
        lon_origo = scenario_params["local_origin_longitude"]

        R_N = 111654.108
        R_M = 115202.011

        lat_global = scenario_N * np.arctan2(1,R_M) + lat_origo
        lon_global = scenario_E * np.arctan2(1,R_N*np.cos(np.deg2rad(lat_origo))) + lon_origo

        try:
                scenario(scenario_type,scenario_N,scenario_E, lat_global, lon_global)
        except rospy.ROSInterruptException:
                pass