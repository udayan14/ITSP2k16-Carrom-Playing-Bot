import math
import time
import RPi.GPIO as GPIO
import sys
sys.path.append("/Users/udayanjoshi/opencv/build/lib")    #change this later
import cv2
from pyimagesearch.transform import four_point_transform
import numpy as np

GPIO.setmode(GPIO.BCM)

xboard=1172
yboard=-1171
ystrip=-1012
xplace1=213
xplace2=953
yloc=-980

#image capturing code

vidcap=cv2.VideoCapture()
vidcap.open(1) #this can be 0,1,2 .just experiment
retval, image = vidcap.retrieve()
vidcap.release()
cv2.imwrite("capimage.jpg",image)

x="capimage.jpg"
gray=cv2.imread(x,0)
image=cv2.imread(x)


          
cornercircles=[]   ##add co-ordinates later



#perspective transform starts here

pts = np.array(cornercircles, dtype = "float32")

# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
cv2.imwrite("a2.jpg", warped)

# image subtraction $$$

img1=cv2.imread('a1.jpg')  #change this name
img2=cv2.imread('a2.jpg') # change this name

z=cv2.subtract(img1,img2)
gray1=cv2.cvtColor(z, cv2.COLOR_BGR2GRAY)
circles1 = cv2.HoughCircles(gray1, cv2.HOUGH_GRADIENT, 1.2, 10, np.array([]), 100, 20, 1, 50)
# ensure at least some circles were found
if circles1 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles1 = np.round(circles[0, :]).astype("int")
 
 #Class definition starts here 
	
class point:

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        return list((self.x,self.y))
        

class line:

    def __init__(self,p1=point(0,0),p2=point(0,0)):
        self.p1=p1
        self.p2=p2
        
def dist(p1,p2):
    return math.hypot(p1.x-p2.x,p1.y-p2.y)
    
    
def slope(p1,p2):
    return (p1.y-p2.y)/float((p1.x-p2.x))
    

def intersectx(l1,l2):
    x1=float(l1.p1.x)
    x2=float(l1.p2.x)
    y1=float(l1.p1.y)
    y2=float(l1.p2.y)
    x3=float(l2.p1.x)
    x4=float(l2.p2.x)
    y3=float(l2.p1.y)
    y4=float(l2.p2.y)
    
    
    a=(x1*y2-y1*x2)*(x3-x4)
    b=(x1-x2)*(x3*y4-y3*x4)
    c=(x1-x2)*(y3-y4)
    d=(y1-y2)*(x3-x4)
    p=(x1*y2-y1*x2)*(y3-y4)
    q=(y1-y2)*(x3*y4-y3*x4)
    if c!=d:
        return float((a-b))/(c-d)
    
def intersecty(l1,l2):
    x1=float(l1.p1.x)
    x2=float(l1.p2.x)
    y1=float(l1.p1.y)
    y2=float(l1.p2.y)
    x3=float(l2.p1.x)
    x4=float(l2.p2.x)
    y3=float(l2.p1.y)
    y4=float(l2.p2.y)
    
    
    a=(x1*y2-y1*x2)*(x3-x4)
    b=(x1-x2)*(x3*y4-y3*x4)
    c=(x1-x2)*(y3-y4)
    d=(y1-y2)*(x3-x4)
    p=(x1*y2-y1*x2)*(y3-y4)
    q=(y1-y2)*(x3*y4-y3*x4)
    if c!=d:
        return (p-q)/(c-d)
def theta(l1,l2):
    m1=slope(l1.p1,l1.p2)
    m2=slope(l2.p1,l2.p2)
    angle=(m1-m2)/(1.0+m1*m2)
    return math.degrees(math.atan(angle))
def actual(x):
    return x*0.435/(xplace2-xplace1)      #change 1 to                                      #metres per pixel
    
def numsteps(x):
    return (x/8.3)*(360/1.8)
    


def near(x):
    if x-int(x)>0.5:
        return int(x)+1
    else:
        return int(x)
        
        
def movehorizontal(x):    
    GPIO.setup(2,GPIO.OUT)  #enable
    GPIO.setup(3,GPIO.OUT)  #step
    GPIO.setup(4,GPIO.OUT)  #direction
    GPIO.setup(17,GPIO.OUT) #VDD

    GPIO.output(2,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)

    
    delay=0.01
    no_of_steps=x

    for i in range(0,no_of_steps):
        GPIO.output(3, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(3, GPIO.LOW)
        time.sleep(delay)

    
    

def rotatebot(x):  #rotational
    GPIO.setup(14,GPIO.OUT)  #enable
    GPIO.setup(15,GPIO.OUT)  #step
    GPIO.setup(18,GPIO.OUT) #direction
    GPIO.setup(23,GPIO.OUT) #VDD

    GPIO.output(14,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)

    degrees=x   
    delay=0.01
    no_of_steps=degrees/1.8

    for i in range(0,no_of_steps):
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)

    
    
    
def strike():     #striking mechanism
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(5,GPIO.OUT)
    
    GPIO.output(10,GPIO.HIGH)    #enable
    GPIO.output(5,GPIO.HIGH)          #VDD
    
    GPIO.output(9,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    time.sleep(3)
    
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(11,GPIO.LOW)
    time.sleep(1)


def clean():            #diabling all ic's 
                        #clearing all gpio pins
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(5,GPIO,LOW)
    GPIO.cleanup()

hole1=point(0,0)
hole2=point(xboard,0)
hole3=point(xboard,yboard)
hole4=point(0,yboard)

coin=point(circles1[0],-circles1[1])

#Shot selection starts here and we also make the shot$$$


if coin.x>xboard/2.0 and coin.y>yloc:
    
    p1=point(xplace1,ystrip)
    p2=point(xplace2,ystrip)
    l1=line(p1,p2)
    l2=line(hole2,coin)
    
    xpoint=intersectx(l1,l2)
    
    if xpoint< xplace1:
        rpoint= xplace1
    elif xplace1<=xpoint and xpoint<=xplace2:
        rpoint= xpoint
        
    else :
        rpoint= xplace2
    hitpos=point(rpoint,ystrip)
    m=slope(coin,hole2)
    sslope=m/math.hypot(m,1)
    cslope=1/math.hypot(m,1)
    endpos=point(coin.x-cslope*37,coin.y-sslope*37) #random sum of radii(37)
    l3=line(endpos,hitpos)
    theta=90-math.degrees(math.atan(slope(l3.p1,l3.p2)))    #theta is measured in degrees
    phi=theta(l2,l3)             #phi is measured in radians
    
    
    len2=actual(dist(hole1,coin))
    len1=actual(dist(endpos,hitpos))
    mu1=0.1    # co-efficient of friction for coin  
    mu2=0.1   #co-efficient of friction for striker
    res=1       # co-efficient of restitution   
    m1=0.01
    m2=0.01
    r1=0.01
    r2=0.01
    g=9.8
    k=0   #parameter to be changed for ideal shot, final kinetic energy
    
    v2=math.sqrt(2.0*(k+mu2*m2*g*len2)/m2)
    v1f=((m1+m2)*v2)/(m1*math.cos(phi)*(1.0+res))
    v1=math.sqrt(v1f*v1f+2.0*mu1*g*len1)
    
    time.sleep(1)
    movehorizontal(numsteps(actual(rpoint-xplace1)))
    time.sleep(1)
    rotatebot(theta)
    time.sleep(1)
    strike()
    


elif coin.x<=xboard/2 and coin.y>(yloc):
    
    p1=point(xplace1,ystrip)
    p2=point(xplace2,ystrip)
    l1=line(p1,p2)
    l2=line(hole1,coin)
   
    xpoint=intersectx(l1,l2)
    
   
    
    if xpoint<xplace1:
        rpoint=xplace1
    elif xpoint>xplace2
        rpointp=xplace2
    else :
        rpoint= xpoint
    
    m=slope(coin,hole1)
    sslope=m/math.hypot(m,1)
    cslope=1/math.hypot(m,1)
    hitpos=point(rpoint,ystrip)
    endpos=point(coin.x-cslope*37,coin.y-sslope*37) #random sum of radii(IN PIXELS)
    l3=line(endpos,hitpos)
    theta=90-math.degrees(math.atan(slope(l3.p1,l3.p2)))    #theta is measured in degrees
    phi=theta(l2,l3)             #phi is measured in radians
    
    
    len2=actual(dist(hole1,coin))
    len1=actual(dist(endpos,hitpos))
    mu1=0.1    # co-efficient of friction for coin  
    mu2=0.1    #co-efficient of friction for striker
    res=1
    m1=0.01
    m2=0.01
    r1=0.01
    r2=0.01
    g=9.8
    k=0   #parameter to be changed for ideal shot, final kinetic energy
    
    v2=math.sqrt(2.0*(k+mu2*m2*g*len2)/m2)
    v1f=((m1+m2)*v2)/(m1*math.cos(phi)*(1+res))
    v1=math.sqrt(v1f*v1f+2*mu1*g*len1)
    
    
    
    time.sleep(1)
    movehorizontal(numsteps(actual(rpoint-xplace1)))
    time.sleep(1)
    rotatebot(theta)
    time.sleep(1)
    strike()