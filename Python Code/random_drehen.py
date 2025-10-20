#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

motoro_left=Motor(Port.B)
motoro=Motor(Port.C)
motor_push=Motor(Port.D)
#motoro.run_angle(100,360)
#motoro_left.run_angle(1000,-160)
c=0
d=0
done=True
while c<=100:
    motoro_left.run_angle(1000,180)
    motor_push.run_angle(1000,-360)
    motoro_left.run_angle(1000,-180)
    
    a=random.randint(0,20)
    if a<10:
        if a<10:
            k=180
        else:
            k=90
        motoro.run_angle(1000,k)
        c+=1