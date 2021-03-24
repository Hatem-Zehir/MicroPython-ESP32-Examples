"""
  ReadAnalogVoltage

  Reads an analog input on GPIO 34, converts it to voltage, and prints the result to the Serial Monitor.
  Attach the center pin of a potentiometer to GPIO 34, and the outside pins to +3.3V and ground.
"""

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    #Convert the analog reading (which goes from 0 - 4095) to a voltage (0 - 3.3V):
    voltage = pot_value * (3.3 / 4095)
    print(voltage)
    sleep(0.1)
