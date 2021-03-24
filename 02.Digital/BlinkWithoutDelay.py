"""
  Blink without Delay

  Turns on and off a light emitting diode (LED) connected to a digital pin,
  without using the sleep() function. This means that other code can run at the
  same time without being interrupted by the LED code.
"""

import utime
from time import sleep
from machine import Pin

#set the digital pin as output
led=Pin(27, Pin.OUT)
#ledState used to set the LED
ledState = 0
#Will store last time LED was updated
PreviousTicks_ms = 0
#interval at which to blink (milliseconds)
interval = 1000

while True:
    #check to see if it's time to blink the LED; that is, if the difference
    #between the current time and last time you blinked the LED is bigger than
    #the interval at which you want to blink the LED.
    CurrentTicks_ms = utime.ticks_ms()
    if CurrentTicks_ms - PreviousTicks_ms >= interval:
        #save the last time you blinked the LED
        PreviousTicks_ms = CurrentTicks_ms
        
        #if the LED is off turn it on and vice-versa
        if ledState == 0:
            ledState = 1
        else:
            ledState = 0
        
        #set the LED with the ledState of the variable
        led.value(ledState)
