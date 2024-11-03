# Motor Control Using GPIO on Raspberry Pi and Adafruit MotorKit

## Overview

This project provides Python code for controlling DC motors using the GPIO pins of a Raspberry Pi and the Adafruit MotorKit library. The code examples demonstrate how to manage motor movement, including forward and stop functions, with additional motor power status checks.

### Requirements

- Raspberry Pi with RPi.GPIO library installed
- Adafruit MotorKit library (for the third code snippet)
- DC motors connected to the Raspberry Pi GPIO pins
- Power supply for the motors

### Libraries Used

- **RPi.GPIO**: Provides functions to control GPIO pins on a Raspberry Pi.
- **time**: Provides time-related functions, such as delays with `sleep`.
- **adafruit_motorkit**: A library to control motors connected via I2C on Adafruit Motor HAT.

### Wiring Setup

**GPIO Pin Assignments:**
- **motor_power_pin**: Checks for motor power signal, connected to GPIO 10.
- **motor_L_forward_pin** and **motor_left_forward_pin**: Control forward motion of the left motor, connected to GPIO 4.
- **motor_L_backward_pin** and **motor_left_backward_pin**: Control backward motion of the left motor, connected to GPIO 14.
- **motor_R_forward_pin** and **motor_right_forward_pin**: Control forward motion of the right motor, connected to GPIO 17.
- **motor_R_backward_pin** and **motor_right_backward_pin**: Control backward motion of the right motor, connected to GPIO 27.

### Code Examples

#### 1. Basic GPIO Motor Control

This script uses GPIO to control the direction and movement of motors based on a forward function (`FWD`). It checks the motor power status and moves the motors forward for a specified time.

**Key functions:**
- **FWD(duration_seconds)**: Moves the robot forward for a defined duration.
- **stop_motors()**: Stops the motors by setting the motor control pins to low.

#### 2. MotorKit Motor Control

This script uses the Adafruit MotorKit library to control motors connected to an Adafruit Motor HAT. It sets motor speed using PWM and provides a simple forward and stop function.

**Key functionality:**
- **kit.motorX.throttle**: Sets the motor speed. `1.0` is full forward speed, while `0.0` stops the motor.


