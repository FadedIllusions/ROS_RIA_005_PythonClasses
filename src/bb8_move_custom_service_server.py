#!/usr/bin/env python

# Import Needed Packages
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from move_bb8 import MoveBB8


# Define Callback
def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom Has Been Called")

    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(request.duration)

    rospy.loginfo("Finished Service move_bb8_in_circle_custom")

    response = MyCustomServiceMessageResponse()
    response.success = True

    return response

# Init Node
rospy.init_node("service_move_bb8_in_circle_custom_server")

# Instantiate Service
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback)

rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()