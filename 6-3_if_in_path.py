# 如果在軌跡內，則....，條件式要放哪？
# if [x,y] in path:
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread , random

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))

buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)
direction = random.randint(0,3)
print(direction)
path = set()
x = 64
y = 32

def direction_thread():
    global direction
    while True:
        if buttonR.value() == 0:direction = 0
        if buttonD.value() == 0:direction = 1
        if buttonL.value() == 0:direction = 2
        if buttonU.value() == 0:direction = 3
        sleep(0.14)
    
_thread.start_new_thread(direction_thread, ())

while True:
    if direction == 0:x = x + 1
    if direction == 1:y = y + 1
    if direction == 2:x = x - 1
    if direction == 3:y = y - 1
    if x > 127 : x = 0
    if x < 0 : x = 127
    if y > 63 : y = 0
    if y < 0 : y = 63
    oled.pixel(x,y,1)
    
    if buttonA.value() == 0 and buttonB.value() == 0:
        print(len(path))
        break
    if (x,y) in path:
        oled.fill(1)
        oled.text(str(len(path)),56,30,0)
        oled.show()
        break
    oled.show()
    path.add((x,y))