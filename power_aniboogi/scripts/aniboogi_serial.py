#!/usr/bin/env python
#import roslib; roslib.load_manifest('numpy_tutorials') #not sure why I need this
import rospy
from std_msgs.msg import String
from keyboard.msg import Key
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

def talker():
 while not rospy.is_shutdown():
   data= ser.read(10) # I have "hi" coming from the arduino as a test run over the serial port
   rospy.loginfo(data)
   pub.publish(String(data))
   rospy.sleep(1.0)

def callback(data):
    rospy.loginfo(data)
    rospy.loginfo(data.code)
    ser.write(String(data.code))

if __name__ == '__main__':
  try:
    pub = rospy.Publisher('encoder', String)
    rospy.init_node('aniboogi_serial')
    rospy.Subscriber("keyboard/keydown", Key, callback)
    talker()
  except rospy.ROSInterruptException:
    pass
