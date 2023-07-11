from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
x = 64
y = 32
direction = 0

def button_thread():
    global direction
    while True:
        if buttonA.value() == 0:direction = direction - 1
        if buttonB.value() == 0:direction = direction + 1
        sleep(0.14)
    
_thread.start_new_thread(button_thread, ())

while True:
    oled.fill(0)
    if direction % 4 == 0:x = x + 1
    if direction % 4 == 1:y = y + 1
    if direction % 4 == 2:x = x - 1
    if direction % 4 == 3:y = y - 1
    oled.pixel(x,y,1)
    
    if buttonA.value() == 0 and buttonB.value() == 0:break
    oled.show()