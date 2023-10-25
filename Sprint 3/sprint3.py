import OPi.GPIO as GPIO
import time

# Define GPIO pins for motor control
left_motor_pwm = 37  
left_motor_direction = 35
right_motor_pwm = 33
right_motor_direction = 31

# Set up GPIO mode
GPIO.setmode(GPIO.SUNXI)

# Set up motor control pins as outputs
GPIO.setup(left_motor_pwm, GPIO.OUT)
GPIO.setup(left_motor_direction, GPIO.OUT)
GPIO.setup(right_motor_pwm, GPIO.OUT)
GPIO.setup(right_motor_direction, GPIO.OUT)

# Create PWM objects for motor speed control
left_motor_pwm_obj = GPIO.PWM(left_motor_pwm, 1000)
right_motor_pwm_obj = GPIO.PWM(right_motor_pwm, 1000)

# Start PWM with 0% duty cycle (motors are initially stopped)
left_motor_pwm_obj.start(0)
right_motor_pwm_obj.start(0)

# Function to move the robot forward
def move_forward(speed_percent):
    # Set motor directions (adjust pins as needed)
    GPIO.output(left_motor_direction, GPIO.HIGH)
    GPIO.output(right_motor_direction, GPIO.HIGH)
    
    # Set motor speeds
    left_motor_pwm_obj.ChangeDutyCycle(speed_percent)
    right_motor_pwm_obj.ChangeDutyCycle(speed_percent)

# Move forward at 50% speed for 3 seconds (adjust speed and duration as needed)
try:
    move_forward(50)  # 50% speed
    time.sleep(3)     # Run for 3 seconds

except KeyboardInterrupt:
    pass

finally:
    # Stop the motors and cleanup GPIO
    left_motor_pwm_obj.stop()
    right_motor_pwm_obj.stop()
    GPIO.cleanup()
