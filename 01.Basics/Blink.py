"""
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.
"""

import time
from machine import Pin

led=Pin(27,Pin.OUT)
 
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
