from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3)
mootor_color = Motor(Port.A)     # Dreharm für den Sensor
motoro_left = Motor(Port.B)      # Dreht den Würfel (z. B. Plattform)
motoro = Motor(Port.C)  
mootor_color.reset_angle(0)
motoro_left.reset_angle(0)
motoro.reset_angle(0)
#move_funcs = {
#        'F': F, 'Fr': Fr,
#        'R': R, 'Rr': Rr,
#        'L': L, 'Lr': Lr,
#        'U': U, 'Ur': Ur,
#        'D': D, 'Dr': Dr,
#        'B': B, 'Br': Br
#    }

x=['F', 'F', 'L', 'F', 'F', 'F', 'F', 'Rr', 'F', 'F','TD']
kippen=motoro_left.run_angle(1000, 180)
drehen=motoro.run_angle(1000,-90)
drehenr=motoro.run_angle(1000,90)
vorne=motoro_left.run_angle(1000, -180)

def make_moves(x):
    robotor=[]
    
    ...
def do_moves(x):
    z=0
    if x[1]=='F':#seite 5 vorher
        motoro_left.run_angle(1000, 180)
        motoro.run_angle(1000,-90)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,-90)
    if x[1]=='Fr':
        motoro_left.run_angle(1000, 180)
        motoro.run_angle(1000,-90)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,90)
    if x[1]=='B':
        motoro_left.run_angle(1000, 180)
        motoro.run_angle(1000,90)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,-90)
    if x[1]=='Br':
        motoro_left.run_angle(1000, 180)
        motoro.run_angle(1000,90)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,-90)
    if x[1]=='R':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,-90)
    if x[1]=='Rr':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro.run_angle(1000,90)
    if x[1]=='L':
        motoro.run_angle(1000,-90)
    if x[1]=='Lr':
        motoro.run_angle(1000,-90)
    if x[1]=='U':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro.run_angle(1000,-90)
    if x[1]=='Ur':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro.run_angle(1000,90)
    if x[1]=='D':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro.run_angle(1000,-90)
    if x[1]=='Dr':
        motoro_left.run_angle(800, 180)
        motoro_left.run_angle(800, -180)
        motoro.run_angle(1000,90)
    while z<len(x):
        if x[z].startswith('F'):
            if x[z+1]=='F':
                motoro.run_angle(1000,-90)
                z+=1
                continue
            elif x[z+1]=='Fr':
                motoro.run_angle(1000,90)
                z+=1
                continue
            elif  x[z+1].startswith('B'):
                motoro_left.run_angle(1000,180)
                motoro_left.run_angle(1000,180)
                if x[z+1]=='B':
                    motoro.run_angle(1000,-90)
                    z+=1
                    continue
                else:
                    motoro.run_angle(1000,90)
                    z+=1
                    continue
            if x[z+1].startswith('U'):
                if x[z-1]=='Td':
                    motoro_left.run_angle(1000,180)
                    motoro_left.run_angle(1000,-180)
                    if x[z+1]=='U':
                        motoro.run_angle(1000,-90)
                        z+=1
                        continue
                    else:
                        motoro.run_angle(1000,90)
                        z+=1
                        continue
                if x[z-1].startswith('U'):
                    motoro_left.run_angle(1000,180)
                    motoro_left.run_angle(1000,-180)
                    if x[z+1]=='U':
                        motoro.run_angle(1000,-90)
                        z+=1
                        continue
                    else:
                        motoro.run_angle(1000,90)
                        z+=1
                        continue
                if x[z-1].startswith('R'):#orientierung herausfinden drehung siehe whitboard und würfel orientierung oben orange farb sensor blau 
                    if x[z-2]=='TD':
                        motoro_left.run


                    ...
            ... 
        if x[z].startswith('F') and x[z+1]=='U':
            ...

    

        ...

    ...