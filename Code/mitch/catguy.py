#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
from decimal import Decimal


def feed():
    # let the GPIO library know where we've connected our servo to the Pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    sleeptime = Decimal(sys.argv[1])

    try:
        servo = GPIO.PWM(12, 50)
        servo.start(12.5)

        # spin left, right, then left again rather than in a continuous circle
        # to prevent the food from jamming the servo
        for index in range(0, 4):
            dutyCycle = 2.5 if (index % 2 == 0) else 12.5
            servo.ChangeDutyCycle(dutyCycle)
            # adjust the sleep time to have the servo spin longer or shorter in that direction
            print(sleeptime)
            time.sleep(sleeptime)
    finally:
        # always cleanup after ourselves
        servo.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    # kick off the feeding process (move the servo)
    feed()
