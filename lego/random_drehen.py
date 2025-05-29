#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from random import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor_color=Motor(Port.s4)
ColorSensor=ColorSensor(Port.s1)


#motoro=Motor(Port.A)

#motoro_left=Motor(Port.C)
#motoro.run_angle(100,360)
#motoro_left.run_angle(1000,-160)
motor_color.run_angle(1000,90)
c=0
d=0
done=True
#while c<=100:
#    motoro_left.run_angle(1000,140)
#    motoro_left.run_angle(1000,-140)
#    a=randint(0,20)
#    if a<10:
#        if a<10:
#            k=180
#        else:
#            k=90
#        motoro.run_angle(1000,k)
#    c+=1
    

#print(motoro_left.angle())

i=0
#while i<=45:
#    motoro_right.run_angle(1000,i)
#    motoro_left.run_angle(1000,i)
#    i=i+1
#motoro_left.run_angle(1000,40)

#motoro_right.run_angle(1000,45)
# Write your program here.
ev3.speaker.beep()
