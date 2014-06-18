# Script for calculating sharpening jig settings.

import math

def getAngles(angle_sharpen, length_base):
    angle_sharpen = math.radians(angle_sharpen)
    angle_mouth = math.radians(90)
    angle_base = math.radians(180) - angle_mouth - angle_sharpen
    return angle_sharpen, angle_mouth, angle_base
    
def getLenths(length, angle1, angle2)
    length = (length * math.sin(angle1)) / math.sin(angle2)
    b = (c * math.sin(B)) / math.sin(C)
    return length
  
def user():
    angle_sharpen = float(raw_input("Desired Sharpening Angle > "))
    length_base = float(raw_input("Height of Jig Base (cm) > "))
    return angle_sharpen, length_base

user(jigsetting(args))



print "Mouth to Edge %s" % a
print "Base to Edge %s" % b
print "Base to Mouth %s" % c