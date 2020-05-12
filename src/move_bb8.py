#!/usr/bin/env python

# Import Needed Packages
import rospy
from geometry_msgs.msg import Twist



class MoveBB8():


    def __init__(self):
        self.bb8_vel_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)


    def publish_once_in_cmd_vel(self):
        """
        Sometimes Topics Fail The First Time You PUblish.
        In Systems That Only Publish Once, We Need To Safe-Gaurd
        Against This.
        """
    
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()


    def shutdownhook(self):
        self.stop_bb8()
        self.ctrl_c = True


    def stop_bb8(self):
        rospy.loginfo("Shutdown: Stopping Robot!")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()


    def move_bb8(self, move_time, linear_speed=0.2, angular_speed=0.2):
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        
        rospy.loginfo("Moving BB8!")

        i = 0
        while not self.ctrl_c and i <= move_time:
            self.publish_once_in_cmd_vel()
            i += 1
            self.rate.sleep()

        self.stop_bb8()



if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()

    try:
        movebb8_object.move_bb8()
    except rospy.ROSInterruptException:
        pass