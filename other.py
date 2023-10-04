import os
import time

# Define GPIO pins for motor control
motor1_a = 37
motor1_b = 35
motor2_a = 33
motor2_b = 31

# Export GPIO pins
os.system(f"gpio export {motor1_a} out")
os.system(f"gpio export {motor1_b} out")
os.system(f"gpio export {motor2_a} out")
os.system(f"gpio export {motor2_b} out")

# Function to move the robot forward
def move_forward():
    os.system(f"gpio -g write {motor1_a} 1")
    os.system(f"gpio -g write {motor1_b} 0")
    os.system(f"gpio -g write {motor2_a} 1")
    os.system(f"gpio -g write {motor2_b} 0")

# Function to stop the robot
def stop():
    os.system(f"gpio -g write {motor1_a} 0")
    os.system(f"gpio -g write {motor1_b} 0")
    os.system(f"gpio -g write {motor2_a} 0")
    os.system(f"gpio -g write {motor2_b} 0")

try:
    move_forward()
    time.sleep(2)  # Move forward for 2 seconds
    stop()
    
except KeyboardInterrupt:
    stop()
