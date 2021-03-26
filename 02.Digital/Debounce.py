"""
  Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
  press), the output pin is toggled from LOW to HIGH or HIGH to LOW. There's a
  minimum delay between toggles to debounce the circuit (i.e. to ignore noise).
  
  The circuit:
  - LED attached from GPIO 27 to ground
  - pushbutton attached to GPIO 34 from +3.3V
  - 10K resistor attached to GPIO 34 from ground
"""

import utime
from machine import Pin
from time import sleep

button = Pin(34, Pin.IN)
led = Pin(27, Pin.OUT)

#the current state of the output pin
ledState = 0
#the current reading from the input pin
buttonState = 0
#the previous reading from the input pin
lastButtonState = 0

#the last time the output pin was toggled
lastDebounceTime = 0
#the debounce time; increase if the output flickers
debounceDelay = 50

while True:
    if button.value() != lastButtonState:
        #reset the debouncing timer
        lastDebounceTime = utime.ticks_ms()
        
    if (utime.ticks_ms() - lastButtonState) > debounceDelay:
        #whatever the reading is at, it's been there for longer than the debounce
        #delay, so take it as the actual current state
        
        #if the button state has changed
        if button.value() != buttonState:
            buttonState = button.value()
            
            #only toggle the LED if the new button state is HIGH
            if buttonState == 1:
                ledState = not ledState
                
    led.value(ledState)
