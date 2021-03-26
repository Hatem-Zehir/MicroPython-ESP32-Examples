"""
  Turns on and off a light emitting diode(LED) connected to GPIO 27,
  when pressing a pushbutton attached to GPIO 34.

  The circuit:
  - LED attached from GPIO 27 to ground
  - pushbutton attached to GPIO 34 from +3.3V
  - 10K resistor attached to GPIO 34 from ground
"""
from machine import Pin
from time import sleep

button = Pin(34, Pin.IN)
led = Pin(27, Pin.OUT)

while True:
    #check if the pushbutton is pressed
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)
