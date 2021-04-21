"""
    Fading

    This example shows how to fade an LED using the analogWrite() function.

    The circuit:
    - LED attached from digital GPIO27 to ground
"""
from time import sleep
from machine import Pin, PWM

frequency = 5000
led = PWM(Pin(27), frequency)

while True:
    #fade in from min to max in increments of 5 points:
    for fadeValue in range (0, 1024, 5):
        led.duty(fadeValue)
        #wait for 30 milliseconds to see the dimming effect
        sleep(0.003)
        print("min to max: ", fadeValue)
        
    #fade out from max to min in increments of 5 points:
    for fadeValue in range (1024, 0, -5):
        led.duty(fadeValue)
        #wait for 30 milliseconds to see the dimming effect
        sleep(0.003)
        print("max to min: ", fadeValue)
