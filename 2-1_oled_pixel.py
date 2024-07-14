from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(1,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

oled.pixel(0,0,1)
oled.pixel(127,0,1)
oled.pixel(0,63,1)

oled.show()