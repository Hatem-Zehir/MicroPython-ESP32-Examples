"""
  AnalogReadSerial

  Reads an analog input on GPIO 34, prints the result to the Serial Monitor.
  Attach the center pin of a potentiometer to GPIO 34, and the outside pins to +3.3V and ground.
"""

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
#read voltage in full range
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    print(pot_value)
    sleep(0.1)
