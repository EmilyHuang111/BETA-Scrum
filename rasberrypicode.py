#Importing Libraries Needed
import RPi.GPIO as GPIO
from time import sleep

#Defining Motors
GPIO.setmode(GPIO.BOARD)
left_front_motor = 15
right_front_motor = 15
left_back_motor = 15
right_back_motor = 15

#Setting Up the Motors
GPIO.setup(left_front_motor,GPIO.OUT)
GPIO.setup(right_front_motor,GPIO.OUT)
GPIO.setup(left_back_motor,GPIO.OUT)
GPIO.setup(right_back_motor,GPIO.OUT)

GPIO.output(left_front_motor, GPIO.HIGH)
GPIO.output(right_front_motor, GPIO.HIGH)
GPIO.output(left_back_motor, GPIO.HIGH)
GPIO.output(right_back_motor, GPIO.HIGH)
GPIO.cleanup()
