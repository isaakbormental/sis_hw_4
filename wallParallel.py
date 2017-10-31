import ev3dev.ev3 as ev3
from time import sleep

m = ev3.LargeMotor('outA')
n = ev3.LargeMotor('outB')
desiredValue = 200
#Primitive controller, unstable
while True:
    s = ev3.UltrasonicSensor('in4')
    actualValue = s.value()
    if actualValue > desiredValue:
        m.run_timed(time_sp=500, speed_sp=-250)
        n.run_timed(time_sp=500, speed_sp=-150)
    elif actualValue < desiredValue:
        m.run_timed(time_sp=500, speed_sp=-150)
        n.run_timed(time_sp=500, speed_sp=-250)
    elif actualValue == desiredValue:
        m.run_timed(time_sp=500, speed_sp=-250)
        n.run_timed(time_sp=500, speed_sp=-250)