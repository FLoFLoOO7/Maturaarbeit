from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
# Setup
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S3)
mootor_color = Motor(Port.A)     # Dreharm für den Sensor
motoro_left = Motor(Port.B)      # Dreht den Würfel (z. B. Plattform)
motoro = Motor(Port.C)  
motor_push = Motor(Port.D)

# Reset Winkel
mootor_color.reset_angle(0)
motoro_left.reset_angle(0)
motoro.reset_angle(0)

# Bewegungen als Funktionen speichern
kippen = [
    lambda: motoro_left.run_angle(1000, 180),
    lambda: motor_push.run_angle(1000, -180),
    lambda: motor_push.run_angle(1000, 180)
]
uhrzeigersinn = lambda: motoro.run_angle(1000, -90)
normal = lambda: motoro.run_angle(1000, 90)
doppel = lambda: motoro.run_angle(1000, 180)
vorne = lambda: motoro_left.run_angle(1000, -180)

# Dictionary mit Moves
moves = {
    'F': [*kippen, vorne, *kippen, vorne, *kippen, vorne, normal, *kippen, vorne],
    'Fr': [*kippen, vorne, *kippen, vorne, *kippen, vorne, uhrzeigersinn, *kippen, vorne],
    'F2': [*kippen, vorne, *kippen, vorne, *kippen, vorne, doppel, *kippen, vorne],
    'B': [*kippen, vorne, normal, *kippen, vorne, *kippen, vorne, *kippen, vorne],
    'Br': [*kippen, vorne, uhrzeigersinn, *kippen, vorne, *kippen, vorne, *kippen, vorne],
    'B2': [*kippen, vorne, doppel, *kippen, vorne, *kippen, vorne, *kippen, vorne],
    'U': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, normal, *kippen, uhrzeigersinn, vorne, *kippen, vorne],
    'Ur': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, uhrzeigersinn, *kippen, uhrzeigersinn, vorne, *kippen, vorne],
    'U2': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, doppel, *kippen, uhrzeigersinn, vorne, *kippen, vorne],
    'D': [normal],
    'Dr': [uhrzeigersinn],
    'D2': [doppel],
    'R': [*kippen, normal, vorne, *kippen, vorne, normal, *kippen, normal, vorne, *kippen, vorne],
    'Rr': [*kippen, normal, vorne, *kippen, vorne, uhrzeigersinn, *kippen, normal, vorne, *kippen, vorne],
    'R2': [*kippen, normal, vorne, *kippen, vorne, doppel, *kippen, normal, vorne, *kippen, vorne],
    'L': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, normal, *kippen, uhrzeigersinn, vorne, *kippen, vorne],
    'Lr': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, uhrzeigersinn, *kippen, uhrzeigersinn, vorne, *kippen, vorne],
    'L2': [*kippen, uhrzeigersinn, vorne, *kippen, vorne, doppel, *kippen, uhrzeigersinn, vorne, *kippen, vorne]
}
def optimize_moves(move_list):
    optimized = []
    i = 0
    while i < len(move_list):
        # Zähle wie oft derselbe Move hintereinander vorkommt
        count = 1
        while i + count < len(move_list) and move_list[i + count] == move_list[i]:
            count += 1

        move = move_list[i]

        # Regel 1: Viermal derselbe -> löschen
        if count % 4 == 0:
            pass  # nix hinzufügen

        # Regel 2: Zweimal derselbe -> Move2
        elif count % 4 == 2:
            optimized.append(move + "2")

        # Regel 3: Dreimal derselbe
        elif count % 4 == 3:
            if move.endswith("r"):   # z.B. "Fr Fr Fr" -> "F"
                optimized.append(move[:-1])  
            else:                   # z.B. "F F F" -> "Fr"
                optimized.append(move + "r")

        # Normaler einzelner Move
        elif count % 4 == 1:
            optimized.append(move)

        i += count

    return optimized
#Farben
def colorsensor():

    cube_faces = []                  
    for side_num in range(6):        
    
        current_face = [None] * 9     

        motoro_left.run_angle(800, 180)
        motor_push.run_angle(1000,-180)
        motor_push.run_angle(1000,180)
    
        wait(300)
        ev3.speaker.beep()

     #  Mitte scannen 
        mootor_color.run_angle(1000, -380)   
        wait(300)
        middle_rgb = color_sensor.rgb()      
        current_face[4] = middle_rgb
        ev3.speaker.beep()
        mootor_color.run_angle(1000, 150)    
        wait(300)

    # Randfelder scannen 
        for i in range(8):
            rgb = color_sensor.rgb()
            if i==0:
                index=1
            elif i==1:
                index=2
            elif i==2:
                index=5
            elif i==3:
                index=8
            elif i==4:
                index=7
            elif i ==5:
                index=6
            elif i==6:
                index=3
            else:
                index=0     
        
            current_face[index] = rgb
            ev3.speaker.beep()
            wait(300)

            motoro.run_angle(800, 45)   
            wait(300)

        cube_faces.append(current_face)


        mootor_color.run_angle(1000, 230)
        wait(200)
        if side_num==3:
            motoro.run_angle(1000,90)
        motoro_left.run_angle(800, -180)
        motor_push.run_angle(1000,-180)
        motor_push.run_angle(1000,180)
        if side_num==4:
            motoro_left.run_angle(1000,180)
            motor_push.run_angle(1000,-180)
            motor_push.run_angle(1000,180)
            motoro_left.run_angle(1000,-180)
        wait(500)

    print(cube_faces)
    return cube_faces

# Funktion zum Ausführen
def do_moves(move_list):
    a=color_sensor()
    move_list=optimize_moves(move_list)
    for move in move_list:
        if move in moves:
            for action in moves[move]:
                action()  # führt Motoraktion aus
        else:
            print("Unbekannter Move:", move)


# Beispiel: Liste ausführen
x=['Rr', 'Dr', 'Ur', 'Rr', 'L', 'F', 'F', 'D', 'F', 'F', 'B', 'B', 'Rr', 'Br', 'R', 'R', 'Br', 'Rr', 'B', 'B', 'Dr', 'Br', 'D', 'Lr', 'Br', 'L', 'B', 'R', 'B', 'Rr', 'Rr', 'Br', 'R', 'B', 'D', 'B', 'Dr', 'B', 'Rr', 'B', 'R', 'B', 'D', 'Br', 'Dr', 'Br', 'L', 'Br', 'Lr', 'Br', 'Dr', 'B', 'D', 'B', 'U', 'Br', 'Ur', 'Br', 'Lr', 'B', 'L', 'B', 'B', 'R', 'Br', 'Rr', 'Br', 'Ur', 'B', 'U', 'B', 'B', 'B', 'U', 'R', 'Br', 'Rr', 'Br', 'R', 'B', 'Rr', 'Ur', 'Rr', 'B', 'Rr', 'Br', 'Rr', 'Br', 'Rr', 'B', 'R', 'B', 'R', 'R', 'B', 'Ur', 'L', 'Ur', 'R', 'R', 'U', 'Lr', 'Ur', 'R', 'R', 'U', 'U']
do_moves(x)
