import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)  #enable
GPIO.setup(15,GPIO.OUT)  #step
GPIO.setup(18,GPIO.OUT) #direction
GPIO.setup(23,GPIO.OUT) #VDD

GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.HIGH)

delay=0.01

while True:
    GPIO.output(15, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(15, GPIO.LOW)
    time.sleep(delay)

GPIO.cleanup()