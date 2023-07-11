from machine import Pin, I2C,PWM
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buzzer = PWM(Pin(13))
buzzer.freq(500)
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

oled.fill(0)
oled.text('hello',0,0)
oled.show()

print(buttonA.value(),buttonB.value())

buzzer.duty_u16(1000)
time.sleep(1)
buzzer.duty_u16(0)