import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)  # enable
GPIO.output(12, HIGH)

while True:
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)

GPIO.cleanup()
