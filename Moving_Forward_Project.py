from gpiozero import Motor
import OPi.GPIO as GPIO

robot = Robot((4, 14), (17, 27))
left_motor = Motor(4, 14)
right_motor = Motor(17, 27)
robot.forward()
