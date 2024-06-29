from machine import Pin
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

if buttonA.value() = 0:
    print(buttonA.value())