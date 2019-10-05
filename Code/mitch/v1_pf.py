#!/usr/bin/env python3
########################################################################
# Filename    : SteppingMotor.py
# Description :
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time

# define pins connected to four phase ABCD of stepper motor
motorPins = (12, 16, 18, 22)
# define power supply order for coil for rotating anticlockwise
CCWStep = (0x01, 0x02, 0x04, 0x08)
# define power supply order for coil for rotating clockwise
CWStep = (0x08, 0x04, 0x02, 0x01)

buttonPin = 11    # define the buttonPin


def setup():
    print('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)


def moveOnePeriod(direction, ms):
    for j in range(0, 4, 1):  # cycle for power supply order
        for i in range(0, 4, 1):  # assign to each pin, a total of 4 pins
            print(j, i)
            GPIO.output(
                motorPins[i], ((CWStep[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))

        if(ms < 3):  # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)
# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle


def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
# function used to stop rotating


def motorStop():
    for i in range(0, 4, 1):
        GPIO.output(motorPins[i], GPIO.LOW)


def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            print('Button pressed ...')
            moveSteps(1, 100, 512)
        else:
            print('Button not pressed ...')


def destroy():
    GPIO.cleanup()             # Release resource


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
