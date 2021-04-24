"""
    Input Pull-up Serial

    This example demonstrates the use of Pin.PULL_UP. It reads a digital
    input on pin 2 and prints the results to the Serial Monitor.

    The circuit:
    - momentary switch attached from GPIO 34 to ground
    - LED on GPIO 27
"""

from machine import Pin
from time import sleep

#configure GPIO34 as an input and enable the internal pull-up resistor
button = Pin(34, Pin.IN, Pin.PULL_UP)
led = Pin(27, Pin.OUT)

while True:
    #read the pushbutton value into a variable
    sensorVal = button.value()
    print(sensorVal)
    
    #Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
    #HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
    #button's pressed, and off when it's not:
    if sensorVal == 1:
        led.value(0)
    else:
        led.value(1)
    
    sleep(0.1)
