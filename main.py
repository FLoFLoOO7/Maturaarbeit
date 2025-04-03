#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
farbe=ColorSensor(Port.D)
#farbe=Motor(Port.B,positive_direction=Direction.CLOCKWISE, gears=None)
#motoro=Motor(Port.A,positive_direction=Direction.CLOCKWISE, gears=None)
#Ultra = UltrasonicSensor(Port.B)
# Write your program here.
ev3.speaker.beep()
ev3.speaker.say("d")
done=False
count=0
speedv=0


while count<=100:
    count+=1
    #motoro.run(200000)
    #speedv=speedv+motoro.speed()
    #farbe.run(800)
    #print(Ultra.distance())

speedv=speedv/10000
print(speedv)
#motoro.stop()
#farbe.sotp()


    