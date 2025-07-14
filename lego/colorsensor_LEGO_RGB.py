#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Setup
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3)
mootor_color = Motor(Port.A)     # Dreharm für den Sensor
motoro_left = Motor(Port.B)      # Dreht den Würfel (z. B. Plattform)
motoro = Motor(Port.C)           # Dreht den Würfel um 45 °

# Motoren nullen
mootor_color.reset_angle(0)
motoro_left.reset_angle(0)
motoro.reset_angle(0)

cube_faces = []                   # Liste aller gescannten Seiten

for side_num in range(6):         # =1, solange du nur eine Seite scannst
    
    current_face = [None] * 9     # Platz für 9 RGB-Werte

    # Würfelseite in Position bringen
    motoro_left.run_angle(800, 180)
    wait(300)
    ev3.speaker.beep()

    # --- Mitte scannen ---
    mootor_color.run_angle(1000, -380)   # Sensor nach innen
    wait(300)
    middle_rgb = color_sensor.rgb()      # (R, G, B) – Werte 0-1023
    current_face[4] = middle_rgb
    ev3.speaker.beep()
    mootor_color.run_angle(1000, 150)    # Sensor zurück
    wait(300)

    # --- Randfelder scannen ---
    for i in range(8):
        rgb = color_sensor.rgb()
        index = i if i < 4 else i + 1    # Position im 3×3-Raster
        current_face[index] = rgb
        ev3.speaker.beep()
        wait(300)

        motoro.run_angle(800, 45)        # Würfel 45 ° weiterdrehen
        wait(300)

    cube_faces.append(current_face)


    # Sensor ganz zurückfahren
    mootor_color.run_angle(1000, 230)
    wait(200)
    if side_num==3:
        motoro.run_angle(1000,90)
    # Würfelplattform zurückdrehen
    motoro_left.run_angle(800, -180)
    if side_num==4:
        motoro_left.run_angle(1000,180)
        motoro_left.run_angle(1000,-180)
    wait(500)

# Alle gesammelten RGB-Werte ausgeben
print(cube_faces)
