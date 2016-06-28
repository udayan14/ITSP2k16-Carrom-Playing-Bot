import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motion=input()

if motion==0:    #horizontal
    GPIO.setup(2,GPIO.OUT)  #enable
    GPIO.setup(3,GPIO.OUT)  #step
    GPIO.setup(4,GPIO.OUT)  #direction
    GPIO.setup(17,GPIO.OUT) #VDD

    GPIO.output(2,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)

    degrees=input()
    delay=0.01
    no_of_steps=near(degrees/1.8)

    for i in (0,no_of_steps):
        GPIO.output(3, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(3, GPIO.LOW)
        time.sleep(delay)

    GPIO.output(2,GPIO.HIGH)

elif motion==1:  #rotational
    GPIO.setup(14,GPIO.OUT)  #enable
    GPIO.setup(15,GPIO.OUT)  #step
    GPIO.setup(18,GPIO.OUT) #direction
    GPIO.setup(23,GPIO.OUT) #VDD

    GPIO.output(14,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)

    degrees=input()
    delay=0.01
    no_of_steps=degrees/1.8

    for i in (0,no_of_steps):
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)

    GPIO.output(14,GPIO.HIGH)

elif motion==2:     #striking mechanism
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    
    GPIO.output(7,GPIO.HIGH)    #enable
    GPIO.output(12,HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)

    time.delay(2)

else:
    print "error"
