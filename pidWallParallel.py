import ev3dev.ev3 as ev3
from time import sleep
s = ev3.UltrasonicSensor('in4')
m = ev3.LargeMotor('outA')
n = ev3.LargeMotor('outB')

# Millimeters from wall
desiredValue = 200
#for iterations
error_prev = 0
iterationTime = 1
#PID-controller coeffs
kp = 0.03
ki =0.05
kd = 0.01

while True:
    #Read sensor data
    actualValue = s.value()
    error = desiredValue - actualValue
    #Integral part
    integral = error * iterationTime
    #Derivative part. Not necessary.
    derive = (error - error_prev) / iterationTime
    #PID regulator equation
    speed = kp * error + ki * integral + kd * derive
    #set the motor speeds
    n.run_timed(time_sp=1000, speed_sp=-(desiredValue + speed))
    m.run_timed(time_sp=1000, speed_sp=-abs(speed - desiredValue))
    error_prev = error