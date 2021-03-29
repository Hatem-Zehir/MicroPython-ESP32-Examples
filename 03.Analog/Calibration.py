"""
    Calibration

    Demonstrates one technique for calibrating sensor input. The sensor readings
    during the first five seconds of the sketch execution define the minimum and
    maximum of expected values attached to the sensor pin.

    The sensor minimum and maximum initial values may seem backwards. Initially,
    you set the minimum high and listen for anything lower, saving it as the new
    minimum. Likewise, you set the maximum low and listen for anything higher as
    the new maximum.

    The circuit:
    - analog sensor (potentiometer will do) attached to analog GPIO 34
    - LED attached from digital GPIO 27 to ground
"""

import utime
from machine import Pin, ADC, PWM
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

sensorMin = 4095        # minimum sensor value
sensorMax = 0           # maximum sensor value

execution_time = utime.ticks_ms()

#turn on LED to signal the start of the calibration period:
led = Pin(27, Pin.OUT)
led.value(1)

#calibrate during the first five seconds
while utime.ticks_ms() - execution_time < 5000:
    sensorValue = pot.read()

    #record the maximum sensor value
    if sensorValue > sensorMax:
        sensorMax = sensorValue

    #record the minimum sensor value
    if sensorValue < sensorMin:
      sensorMin = sensorValue

#signal the end of the calibration period
led.value(0)

def mapp(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

while True:
    #read the sensor
    sensorValue = pot.read()

    #apply the calibration to the sensor reading
    sensorValue = mapp(sensorValue, sensorMin, sensorMax, 0, 1023)

    #in case the sensor value is outside the range seen during calibration
    sensorValue = constrain(sensorValue, 0, 1023)

    print(sensorValue)
    sleep(0.1)
