"""
    Smoothing

    Reads repeatedly from an analog input, calculating a running average and
    printing it to the computer. Keeps ten readings in an array and continually
    averages them.

    The circuit:
    - analog sensor (potentiometer will do) attached to GPIO34
"""
from machine import Pin, ADC
from time import sleep

# Define the number of samples to keep track of. The higher the number, the
# more the readings will be smoothed, but the slower the output will respond to
# the input. Using a constant rather than a normal variable lets us use this
# value to determine the size of the readings array.
numReadings = 10


readings = [0] * numReadings         # the readings from the analog input
readIndex = 0                        # the index of the current reading
total = 0                            # the running total
average = 0                          # the average

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

print(readings)

while True:
    #subtract the last reading:
    total = total - readings[readIndex]
    #read from the sensor:
    readings[readIndex] = pot.read()
    #add the reading to the total:
    total = total + readings[readIndex]
    #advance to the next position in the array:
    readIndex = readIndex + 1

    #if we're at the end of the array...
    if (readIndex >= numReadings):
        #wrap around to the beginning:
        readIndex = 0

    #calculate the average:
    average = total / numReadings
    #send it to the computer as ASCII digits
    print(average)
    sleep(0.1)        # delay in between reads for stability
