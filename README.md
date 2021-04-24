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

# Requirements
To begin, you'll need a board with an ESP32 chip. The ESP32 chip is supported by the MicroPython software, and any board should work. The most important feature of a board is how the GPIO pins are connected to the outside world, as well as whether it has a built-in USB-serial converter to connect the UART to your PC.

# Flash/Upload MicroPython Firmware to ESP32
Make sure you install uPyCraft IDE on your computer:
- [uPyCraft IDE for Windows](https://github.com/DFRobot/uPyCraft/raw/master/uPyCraft.exe)
- [uPyCraft IDE for MAC OS X](https://github.com/DFRobot/uPyCraft_src)
- [uPyCraft IDE for Linux](https://github.com/DFRobot/uPyCraft_src)

You can easily flash your ESP32 board with MicroPython firmware if you have the uPyCraft IDE installed on your computer.

## Getting the firmware
The first step is to get the most recent MicroPython firmware.bin file and load it onto your ESP32 device. It's available for download on the [MicroPython downloads page](https://micropython.org/download/esp32/). You have three options:
- Stable firmware builds
- Daily firmware builds
- Daily firmware builds with SPIRAM support

## Deploying the firmware
### Selecting Serial Port
Go to Tools > Serial and select your ESP32 COM port (in our case it’s COM3).

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/uPyCraft-IDE-Select-Serial-Port-COM3.png">
</p>

### Selecting the Board
Go to Tools > Board. make sure you select the "esp32" option:

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/uPyCraft-IDE-Select-Board-ESP32.png">
</p>

### Flashing/Uploading MicroPython Firmware
Finally, go to Tools > BurnFirmware menu to flash your ESP32 with MicroPython.

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/uPyCraft-IDE-Tools-burn-Firmware.png">
</p>

Select all these options to flash the ESP32 board:
* board: esp32
* burn_addr: 0x1000
* erase_flash: yes
* com: COM3
* Firmware: Select "Users" and choose the .bin file downloaded earlier

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/flash-firmware-esp32-prepare.png">
</p>

Having all the settings selected, hold-down the "BOOT/FLASH" button in your ESP32 board. While holding down the “BOOT/FLASH“, click the “ok” button in the burn firmware window:

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/OK-update-firmware-esp32.png">
</p>

When the "EraseFlash" process begins, you can release the "BOOT/FLASH" button. After a few seconds, the firmware will be flashed into your ESP32 board.

# Further Reading
- [Built-In Examples | Arduino](https://www.arduino.cc/en/Tutorial/BuiltInExamples)
- [Getting started with MicroPython on the ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [Flash/Upload MicroPython Firmware to ESP32 and ESP8266](https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/)
- [Getting Started with MicroPython on ESP32 and ESP8266](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)
