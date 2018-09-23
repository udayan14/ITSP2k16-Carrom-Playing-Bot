import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)  #enable
GPIO.setup(3,GPIO.OUT)  #step
GPIO.setup(4,GPIO.OUT)  #direction
GPIO.setup(17,GPIO.OUT) #VDD

GPIO.output(2,GPIO.LOW)
GPIO.output(4,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)

delay=0.01

while True:
	GPIO.output(3, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(3, GPIO.LOW)
	time.sleep(delay)

GPIO.cleanup()