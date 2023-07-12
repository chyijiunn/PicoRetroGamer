from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import _thread

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
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
    
    if direction % 4 == 0:oled.text('>',63,31,1)
    if direction % 4 == 1:oled.text('v',63,31,1)
    if direction % 4 == 2:oled.text('<',63,31,1)
    if direction % 4 == 3:oled.text('^',63,31,1)
    
    if buttonB.value() == 0 and buttonA.value() == 0:break
    oled.show()
    sleep(0.1)