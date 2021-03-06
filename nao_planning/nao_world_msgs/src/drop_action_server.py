#! /usr/bin/env python

import roslib; roslib.load_manifest('nao_world_msgs')
import rospy
import actionlib
from naoqi import ALProxy
from nao_world_msgs.msg import *

class DropActionServer:
  def __init__(self):
    self.server = actionlib.SimpleActionServer('/nao_world_msgs/drop_action_server', DropAction, self.execute, False)
    self.server.start()
    rospy.loginfo("Drop Action Server started.")

  def execute(self, goal):
    # Do lots of awesome groundbreaking robot stuff here
    self.drop()
    self.server.set_succeeded()
    
  def drop(self):
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadYaw")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00763, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00763, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("HeadPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.03677, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.02143, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.02604, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LShoulderPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.05978, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.03064, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 1.41891, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LShoulderRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.11808, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.82525, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.33130, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LElbowYaw")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.02152, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.11969, [ 3, -0.22222, 0.09818], [ 3, 0.22222, -0.09818]], [ -1.39138, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LElbowRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.04751, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.06132, [ 3, -0.22222, 0.01381], [ 3, 0.22222, -0.01381]], [ -1.02620, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LWristYaw")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00456, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.01070, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.01070, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LHand")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00021, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00020, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00020, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RShoulderPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.07367, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.05220, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 1.41286, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RShoulderRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.16571, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.80539, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.33445, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RElbowYaw")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.03379, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.09660, [ 3, -0.22222, -0.13039], [ 3, 0.22222, 0.13039]], [ 1.39130, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RElbowRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.05527, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.05833, [ 3, -0.22222, -0.00307], [ 3, 0.22222, 0.00307]], [ 1.02782, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RWristYaw")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.01990, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00456, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00456, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RHand")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00017, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00016, [ 3, -0.22222, 0.00000], [ 3, 0.22222, -0.00000]], [ 0.00015, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LHipYawPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00311, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.00149, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LHipRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00464, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00464, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LHipPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.43561, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.43561, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LKneePitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.69946, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.69793, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LAnklePitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.34979, [ 3, -0.22222, 0.00153], [ 3, 0.22222, -0.00153]], [ -0.35133, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("LAnkleRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00004, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00004, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RHipRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00004, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.00303, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00158, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RHipPitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.00311, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.43110, [ 3, -0.22222, 0.00920], [ 3, 0.22222, -0.00920]], [ -0.44030, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RKneePitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.02297, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.69955, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.69341, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RAnklePitch")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ -0.00303, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ -0.34664, [ 3, -0.22222, 0.00460], [ 3, 0.22222, -0.00460]], [ -0.35124, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    names.append("RAnkleRoll")
    times.append([ 0.33333, 1.00000, 1.66667])
    keys.append([ [ 0.00618, [ 3, -0.11111, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00004, [ 3, -0.22222, 0.00000], [ 3, 0.22222, 0.00000]], [ 0.00004, [ 3, -0.22222, 0.00000], [ 3, 0.00000, 0.00000]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", "192.168.105.15", 9559)
      motion.stiffnessInterpolation("Body", 1.0, 0.1)
      motion.angleInterpolationBezier(names, times, keys);
    except BaseException, err:
      print err  
    
if __name__ == '__main__':
  rospy.init_node('drop_action_server')
  server = DropActionServer()
  rospy.spin()
