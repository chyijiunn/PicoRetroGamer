from machine import Pin
buttonA = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
for count in range(100):
    print(count,':',buttonA.value())
    time.sleep(0.1)
