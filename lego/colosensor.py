from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialisiere den EV3 Brick
ev3 = EV3Brick()

POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
# Initialisiere den Farbsensor am Port S3
color_sensor = ColorSensor(Port.S3)
color=color_sensor.rgb()
print(color)

