from adafruit_motorkit import MotorKit
kit = MotorKit(0x40)
import time
 
# Forward at full speed
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
 
# Run both motors for 1 second. Adjust the time for the proper distance to go
time.sleep(1.0)
 
# Stop the motors.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
