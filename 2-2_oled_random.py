from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time,random

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

for i in range(100):
    oled.pixel(63+random.randint(-63,64),31+random.randint(-31,32),1)
oled.show()
