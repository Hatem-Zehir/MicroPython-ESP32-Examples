"""
    Dimmer

    Demonstrates sending data from the computer to the ESP32 board, in this case
    to control the brightness of an LED. The data is sent in individual bytes.
    ESP32 reads these bytes and uses them to set the brightness of the LED.

    The circuit:
    - LED attached from GPIO27 to ground.
    - Serial connection to Processing, Max/MSP, or another serial application
"""

from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(27), frequency)

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
           print("Not an integer! Try again.")
           continue
        else:
           return userInput 
           break 

while True:
    brightness = inputNumber("Enter brightness: ")

    led.duty(brightness)
    sleep(0.005)

