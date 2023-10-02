import OPi.GPIO as GPIO
import time

# Define GPIO pins for motor control
motor1_a = 11
motor1_b = 12
motor2_a = 13
motor2_b = 15

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)

# Set up motor pins as output
GPIO.setup(motor1_a, GPIO.OUT)
GPIO.setup(motor1_b, GPIO.OUT)
GPIO.setup(motor2_a, GPIO.OUT)
GPIO.setup(motor2_b, GPIO.OUT)

# Function to move the robot forward
def move_forward():
    GPIO.output(motor1_a, 1)
    GPIO.output(motor1_b, 0)
    GPIO.output(motor2_a, 1)
    GPIO.output(motor2_b, 0)

# Function to stop the robot
def stop():
    GPIO.output(motor1_a, 0)
    GPIO.output(motor1_b, 0)
    GPIO.output(motor2_a, 0)
    GPIO.output(motor2_b, 0)

try:
    move_forward()
    time.sleep(2)  # Move forward for 2 seconds
    stop()
    
except KeyboardInterrupt:
    stop()

finally:
    GPIO.cleanup()
