import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins for motor power signal
motor_power_pin = 10

# Define GPIO pins for controlling the motors
#We will change these pins values once we figure out the exact pinning 
motor_L_forward_pin = 4
motor_L_backward_pin = 14
motor_R_forward_pin = 17
motor_R_backward_pin = 27

# Set up GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor control pins as output
GPIO.setup(motor_L_forward_pin, GPIO.OUT)
GPIO.setup(motor_L_backward_pin, GPIO.OUT)
GPIO.setup(motor_R_forward_pin, GPIO.OUT)
GPIO.setup(motor_R_backward_pin, GPIO.OUT)

# Set up motor power pin as input
GPIO.setup(motor_power_pin, GPIO.IN)

# Define binary values for motor control
HIGH = 1
LOW = 0

# Define a forward function to move the robot forward for a specified duration
def FWD(duration_seconds):
    GPIO.output(motor_L_forward_pin, HIGH)
    GPIO.output(motor_R_forward_pin, HIGH)
    
    # Move forward for the specified duration
    sleep(duration_seconds)
    
    # Stop the motors
    stop_motors()

# Define a stop function to stop the motors
def stop_motors():
    GPIO.output(motor_L_forward_pin, LOW)
    GPIO.output(motor_R_forward_pin, LOW)

try:
    # Check if motor power is available (binary signal)
    if GPIO.input(motor_power_pin) == HIGH:
        # Motor power is available, move forward for approximately 2 feet
        FWD(5)  # Adjust the duration as needed
    else:
        # Motor power is not available
        print("No motor power")

except:
    pass

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
