from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)

x = 0
while True:
    if buttonL.value() == 0:
        x = x - 1
        oled.pixel(63+ x,31,1)
        oled.show()
    if buttonR.value() == 0:
        x = x + 1
        oled.pixel(63+ x,31,1)
        oled.show()
