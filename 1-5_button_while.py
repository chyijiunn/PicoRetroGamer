from machine import Pin
import time
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
count = ?
while True:
    print(count,':',buttonA.value())
    count = count + 1
    time.sleep(0.1)

