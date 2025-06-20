#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Setup
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3)
mootor_color = Motor(Port.A)    
motoro_left = Motor(Port.B)     
motoro = Motor(Port.C)          

# Farbzuordnung
color_map = {
    Color.RED: "red",
    Color.GREEN: "green",
    Color.BLUE: "blue",
    Color.YELLOW: "yellow",
    Color.WHITE: "white",
    Color.ORANGE: "orange"
}


mootor_color.reset_angle(0)
motoro_left.reset_angle(0)
motoro.reset_angle(0)


cube_faces = []

for side_num in range(6):


    current_face = [""] * 9  

    motoro_left.run_angle(800, 180)
    wait(300)
    ev3.speaker.beep()
    # Mitte scannen 
    mootor_color.run_angle(1000, -380)  # Sensor nach innen
    wait(300)
    middle_color = color_sensor.color()
    current_face[4] = color_map.get(middle_color, "unknown")
    ev3.speaker.beep()
    mootor_color.run_angle(1000, 150)   
    wait(300)

    # Aussen
    for i in range(8):
        color = color_sensor.color()
        index = i if i < 4 else i + 1  
        current_face[index] = color_map.get(color, "unknown")
        ev3.speaker.beep()
        wait(300)

        motoro.run_angle(800, 45)
        wait(300)

    cube_faces.append(current_face)

    # 
    mootor_color.run_angle(1000, 230)
    wait(200)

    # 
    motoro_left.run_angle(800, -180)
    wait(500)

print(cube_faces)    



