from time import sleep
import RPi.GPIO as GPIO

DIR = 27   # Direction GPIO Pin
PUL = 17  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = .0208

for x in range(step_count):
    print('moving forward')
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    print('moving Back, I think ')
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()
