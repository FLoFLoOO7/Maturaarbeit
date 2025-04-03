#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait
x=-20
wurfel_unten=Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE)
#wurfel=Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
wurfel_unten.stop()

#wurfel_unten.run_angle(900,x)

wurfel_unten.run_angle(900,x)
