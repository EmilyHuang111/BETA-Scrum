import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins for motor power signal
motor_power_pin = 10

# Define GPIO pins for controlling the motors
motor_left_forward_pin = 4
motor_left_backward_pin = 14
motor_right_forward_pin = 17
motor_right_backward_pin = 27

# Set up GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor control pins as output
GPIO.setup(motor_left_forward_pin, GPIO.OUT)
GPIO.setup(motor_left_backward_pin, GPIO.OUT)
GPIO.setup(motor_right_forward_pin, GPIO.OUT)
GPIO.setup(motor_right_backward_pin, GPIO.OUT)

# Set up motor power pin as input
GPIO.setup(motor_power_pin, GPIO.IN)

# Define a forward function to move the robot forward
def FWD():
    GPIO.output(motor_left_forward_pin, GPIO.HIGH)
    GPIO.output(motor_right_forward_pin, GPIO.HIGH)

# Define a stop function to stop the motors
def stop_motors():
    GPIO.output(motor_left_forward_pin, GPIO.LOW)
    GPIO.output(motor_right_forward_pin, GPIO.LOW)

try:
    # Check if motor power is available (binary signal)
    if GPIO.input(motor_power_pin) == GPIO.HIGH:
        # Motor power is available, move forward
        FWD()

        # Keep moving forward for 10 seconds
        sleep(10)

        # Stop the motors
        stop_motors()
    else:
        # Motor power is not available
        print("No motor power")

except:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
