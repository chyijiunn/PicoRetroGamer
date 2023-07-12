from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)

oled.fill(0)
x = 64
y = 32
direction = 0
path =[]
goal = []
    
def maze(fileSerial):
    global direction
    global x , y
    mazeName = '{:0>2}'.format(fileSerial)#格式化、前面補零
    oled.fill(0)
    data = open('data/maze/'+mazeName,'r')
    head = data.readline().split(',')   
    num = len(head)-1                   
    b = head[:num]                      
    
    direction = int(b[0])          
    x = int(b[1])                   
    y = int(b[2])
    for i in range(int((num-3)/2)):   
        goal.append([int(b[2*i+3]),int(b[2*i+4])])

    mazelist = data.readlines()
    for line in mazelist:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            oled.pixel(xAxis,yAxis,1)
            path.append([xAxis,yAxis])
    data.close()
    oled.show()

def direction_thread():
    global direction
    while True:
        if buttonR.value() == 0:direction = 0
        if buttonD.value() == 0:direction = 1
        if buttonL.value() == 0:direction = 2
        if buttonU.value() == 0:direction = 3
        sleep(0.14)
        
_thread.start_new_thread(direction_thread, ())

maze(0)

while True:
    if x > 127: x =0
    if x <0: x = 127
    if y > 63 : y =0
    if y <0 : y = 63
    
    if direction == 0:x = x + 1
    if direction == 1:y = y + 1
    if direction == 2:x = x - 1
    if direction == 3:y = y - 1
    oled.pixel(x,y,1)
    oled.show()
    
    if buttonA.value() == 0 and buttonB.value() == 0:break
    if [x,y] in path:break
    path.append([x,y])