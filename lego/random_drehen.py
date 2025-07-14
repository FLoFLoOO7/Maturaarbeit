#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
# Setup
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3)
mootor_color = Motor(Port.A)    
motoro_left = Motor(Port.B)     
motoro = Motor(Port.C)          

c=0
d=0
done=True

mootor_color.run_angle(1000,-230)
