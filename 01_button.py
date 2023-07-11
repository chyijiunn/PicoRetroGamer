from machine import Pin
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1

print(buttonA.value(),buttonB.value())
