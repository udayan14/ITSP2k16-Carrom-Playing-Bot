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
    return x*0.435/(xplace2-xplace1)      #change 1 to metres per pixel
    
def steplen(x):
    init= 0.1    #change this
     
    r=0.01          #change this
    return actual(init+x)/r      
    


def near(x):
    if x-int(x)>0.5:
        return int(x)+1
    else:
        return int(x)
        
def movehorizontal(x):    #horizontal  x is degrees
    GPIO.setup(2,GPIO.OUT)  #enable
    GPIO.setup(3,GPIO.OUT)  #step
    GPIO.setup(4,GPIO.OUT)  #direction
    GPIO.setup(17,GPIO.OUT) #VDD

    GPIO.output(2,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)

    degrees=x
    delay=0.01
    no_of_steps=near(degrees/1.8)

    for i in range(0,no_of_steps):
        GPIO.output(3, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(3, GPIO.LOW)
        time.sleep(delay)

    GPIO.output(2,GPIO.HIGH)
    GPIO.cleanup()
    

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

    GPIO.output(14,GPIO.HIGH)
    GPIO.cleanup()
    
def strike():     #striking mechanism
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    
    GPIO.output(7,GPIO.HIGH)    #enable
    GPIO.output(12,HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)

    time.sleep(2)

    GPIO.cleanup()