from machine import Pin, I2C,PWM
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread , sys

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(13))
buzzer.freq(263)

oled.fill(0)
x = 64
y = 32
direction = 0
path =set()
goal =set()


def direction_thread():
    global direction
    while True:
        if buttonR.value() == 0:direction = 0
        if buttonD.value() == 0:direction = 1
        if buttonL.value() == 0:direction = 2
        if buttonU.value() == 0:direction = 3
        sleep(0.14)

def fail():
    buzzer.duty_u16(1000)
    oled.fill(0)
    data = open('data/pics/boom','r')
    for line in data:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            oled.pixel(xAxis,yAxis,1)
    data.close()
    oled.show()
    buzzer.duty_u16(0)
    
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
        goal.add((int(b[2*i+3]),int(b[2*i+4])))

    #以下處理迷宮座標資料，使用 readlines 讀取剩餘資料
    mazelist = data.readlines()
    for line in mazelist:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            oled.pixel(xAxis,yAxis,1)
            path.add((xAxis,yAxis))
    data.close()
    oled.show()
    
def scoreshow(score,mazeName):
    note = [500,630,800,630,830,902]
    for i in note:
        buzzer.freq(i)
        buzzer.duty_u16(1000)
        sleep(0.1)
        buzzer.duty_u16(0)
        sleep(0.1)
        
    oled.fill_rect(0, 55, 127, 63, 1)
    oled.text('score '+str(score),35,55,0)
    
    mazeName = '{:0>2}'.format(fileSerial)
    data = open('data/maze/'+mazeName+'_r')
    top = int(data.readline())
    
    if score < top:
        data = open('data/maze/'+mazeName+'_r','w')
        data.write(str(score))
        top = score
        
    oled.fill_rect(0, 0, 127, 7, 1)
    oled.text('TOP '+str(top),40,0,0)
    data.close()
    oled.show()
    
_thread.start_new_thread(direction_thread, ())

for fileSerial in range(6):
    maze(fileSerial)
    score = -1
    while True:
        if x > 128: x =0
        if x <0: x = 128
        if y > 64 : y =0
        if y <0 : y = 64
        
        if direction == 0:x +=1
        if direction == 1:y +=1
        if direction == 2:x -=1
        if direction == 3:y -=1
        
        oled.pixel(x,y,1)
        score = score + 1
        
        if buttonA.value() == 0 and buttonB.value() == 0:break
        
        oled.show()
        
        if (x,y) in path:
            fail()
            sys.exit()
        path.add((x,y))
        
        if not ( (x,y)  in goal ):continue
        path.clear()
        goal.clear()
        oled.text('Bravo!',40,55)
        scoreshow(score,fileSerial)
        oled.show()            
        for pixel in range(20):
            oled.scroll(-8,0)
            oled.show()
        break
