# MicroPython-ESP32-Examples
This repository features the conversion of Arduino built-In examples to MicroPython.

# What are Arduino built-In Examples?
Built-In Examples are sketches found in the Arduino Software (IDE); to access them, select File > Examples from the toolbar menu. These easy programs show how to use all of the Arduino's basic commands. They cover anything from the bare minimum of a sketch to digital and analog IO, as well as the use of sensors and displays.

## 01.Basics
- [Analog Read Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/AnalogReadSerial.py): Read a potentiometer, print its state out to the Serial Monitor.
- [Blink](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/Blink.py): Turn an LED on and off.
- [Digital Read Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/DigitalReadSerial.py): Read a switch, print the state out to the Serial Monitor.
- [Fade](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/Fade.py): Demonstrates the use of analog output to fade an LED.
- [Read Analog Voltage](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/ReadAnalogVoltage.py): Reads an analog input and prints the voltage to the Serial Monitor.

## 02.Digital
- [Blink Without Delay](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/BlinkWithoutDelay.py): Blink an LED without using the sleep() function.
- [Button](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/Button.py): Use a pushbutton to control an LED.
- [Debounce](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/Debounce.py): Read a pushbutton, filtering noise.
- [Digital Input Pullup](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/DigitalInputPullUp.py): Demonstrates the use of Pin.PULL_UP.

## 03.Analog
- [Analog In Out Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/AnalogInOutSerial.py): Read an analog input pin, map the result, and then use that data to dim or brighten an LED.
- [Calibration](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Calibration.py): Define a maximum and minimum for expected analog sensor values.
- [Fading](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Fading.py): Use an analog output (PWM pin) to fade an LED.
- [Smoothing](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Smoothing.py): Smooth multiple readings of an analog input.

## 04.Communication
- [ASCIITable](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/ASCIITable.py): Demonstrates ESP32's advanced serial output functions.
- [Dimmer](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/Dimmer.py): Move the mouse to change the brightness of an LED.
- [Physical Pixel](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/PhysicalPixel.py): Turn a LED on and off by sending data to your ESP32 from Processing or Max/MSP.

# What is MicroPython?
MicroPython is a re-implementation of Python 3 that is designed for use with microcontrollers and embedded systems. Standard Python and MicroPython are very similar. If you know how to program in Python, you'll be able to program in MicroPython as well.
Using MicroPython to program the ESP32 board is a perfect way to get the best out of it. The ESP32 chip, on the other hand, is an excellent medium for using MicroPython.
