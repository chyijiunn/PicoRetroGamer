from machine import Pin, I2C ,PWM
from ssd1306 import SSD1306_I2C
from time import sleep

oled = SSD1306_I2C(128, 64, I2C(0,sda=Pin(20), scl=Pin(21), freq=40000))
buttonU = Pin(0, Pin.IN, Pin.PULL_UP)
buttonD = Pin(1, Pin.IN, Pin.PULL_UP)
buttonL = Pin(2, Pin.IN, Pin.PULL_UP)
buttonR = Pin(3, Pin.IN, Pin.PULL_UP)
buttonA = Pin(14, Pin.IN, Pin.PULL_UP)
buttonB = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(13))

message = {'buttonU':'buttonU',
           'buttonD':'buttonD',
           'buttonL':'buttonL',
           'buttonR':'buttonR',
           'buttonA':'buttonA',
           'buttonB':'buttonB',
           'try':'PressAny'
    }

def buttonTry():
    if buttonU.value()== 0:
        buzzer.freq(523)
        buzzer.duty_u16(1000)
        return message['buttonU']
    elif buttonD.value()== 0:
        buzzer.freq(587)
        buzzer.duty_u16(1000)
        return message['buttonD']
    elif buttonL.value()== 0:
        buzzer.freq(659)
        buzzer.duty_u16(1000)
        return message['buttonL']
    elif buttonR.value()== 0:
        buzzer.freq(698)
        buzzer.duty_u16(1000)
        return message['buttonR']
    elif buttonA.value()== 0:
        buzzer.freq(784)
        buzzer.duty_u16(1000)
        return message['buttonA']
    elif buttonB.value()== 0:
        buzzer.freq(880)
        buzzer.duty_u16(1000)
        return message['buttonB']
    else:
        buzzer.duty_u16(0)
        return message['try']
       
while 1:
    try:
        oled.fill(0)
        oled.text(buttonTry(),40,30,1)
        oled.show()
    except KeyboardInterrupt:break