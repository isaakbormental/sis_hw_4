import ev3dev.ev3 as ev3
from time import sleep

m = ev3.LargeMotor('outA')
n = ev3.LargeMotor('outB')
m.run_timed(time_sp=3000, speed_sp=500)


while True:
    m.run_timed(time_sp=1000, speed_sp=100)
    n.run_timed(time_sp=1000, speed_sp=100)
    sleep(2)
