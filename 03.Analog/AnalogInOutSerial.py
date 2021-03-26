"""  
  Analog input, analog output, serial output

  Reads an analog input pin, maps the result to a range from 0 to 255 and uses
  the result to set the pulse width modulation (PWM) of an output pin.
  Also prints the results to the Serial Monitor.

  The circuit:
    -Center pin of the potentiometer goes to GPIO34.
    side pins of the potentiometer go to +3.3V and ground
  - LED connected from GPIO27 to ground
"""

from machine import Pin, ADC, PWM
from time import sleep

led = PWM(Pin(27), freq=5000)
pot = ADC(Pin(34))
#Full range: 3.3v
pot.atten(ADC.ATTN_11DB)

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    #read the analog in value
    sensorValue = pot.read()
    #map it to the range of the analog out
    outputValue = convert(sensorValue, 0, 4095, 0, 1023)
    #change the analog out value
    led.duty(outputValue)
    
    #print the results
    print("sensor = ", sensorValue)
    print("output = ", outputValue)
    
    #wait 50 milliseconds before the next loop for the analog-to-digital
    #converter to settle after the last reading
    sleep(0.05)
