"""
    Physical Pixel

    An example of using the Arduino board to receive data from the computer. In
    this case, the Arduino boards turns on an LED when it receives the character
    'H', and turns off the LED when it receives the character 'L'.

    The data can be sent from the Arduino Serial Monitor, or another program like
    Processing (see code below), Flash (via a serial-net proxy), PD, or Max/MSP.

    The circuit:
    - LED connected from digital GPIO27 to ground
"""

from machine import Pin
from time import sleep

led = Pin(27, Pin.OUT) # the pin that the LED is attached to

while True:
    incomingByte = input("Enter a letter: ")
    # if it's a capital H turn on the LED:
    if incomingByte == "H":
        led.value(1)
    # if it's an L turn off the LED:
    if incomingByte == "L":
        led.value(0)
    
    sleep(0.005)
