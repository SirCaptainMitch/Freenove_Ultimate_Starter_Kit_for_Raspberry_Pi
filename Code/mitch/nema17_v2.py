from time import sleep
import RPi.GPIO as GPIO

PUL = 17
DIR = 27
ENA = 22
GPIO.setmode(GPIO.BCM)

GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

delay = 0.01
GPIO.output(ENA, GPIO.LOW)

GPIO.output(DIR, GPIO.LOW)
for x in range(200):
    
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)
    print('moving forward')

sleep(1)
GPIO.output(DIR, GPIO.HIGH)
for x in range(200):
    
    GPIO.output(PUL, GPIO.HIGH)
    sleep(delay)
    GPIO.output(PUL, GPIO.LOW)
    sleep(delay)
    print('moving backward')

GPIO.cleanup()
