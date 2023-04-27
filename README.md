# MicroPython-ESP32-Examples
Explore this repository to discover the conversion of Arduino's built-in examples to MicroPython. These resources offer developers the ability to learn and utilize the versatility and functionality of MicroPython. Take advantage of this valuable resource and expand your coding skills today.

# Requirements:
To get started with this project, you will need to ensure that you have the appropriate software and hardware. You will require an IDE such as Thonny, or your preferred alternative, to facilitate the coding process. Additionally, you will need an ESP32 and a USB cable to connect it to your computer. With these necessary components, you can begin working on your project.

# What are Arduino built-In Examples?
If you're new to Arduino, the built-in examples are an essential resource to help you understand how to use the device's basic commands. These simple programs can be found in the Arduino Software (IDE) by selecting File > Examples from the toolbar menu. From digital and analog IO to sensor and display usage, these examples cover everything from the basics of a sketch to more complex tasks. With the built-in examples, you can quickly get started with your Arduino projects.

## 01.Basics
- [Analog Read Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/AnalogReadSerial.py): Learn how to read the state of a potentiometer and output it to the Serial Monitor.

- [Blink](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/Blink.py): Discover how to toggle an LED on and off with ease.
- [Digital Read Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/DigitalReadSerial.py): Learn how to read the state of a switch and output it to the Serial Monitor.
- [Fade](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/Fade.py): Discover how to control the brightness of an LED with analog output in this example that demonstrates the fading effect..
- [Read Analog Voltage](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/01.Basics/ReadAnalogVoltage.py): Learn how to read an analog input and output the voltage to the Serial Monitor.

## 02.Digital
- [Blink Without Delay](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/BlinkWithoutDelay.py): Explore how to blink an LED without utilizing the sleep() function.
- [Button](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/Button.py): Learn how to use a pushbutton to control an LED.
- [Debounce](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/Debounce.py): Discover how to read a pushbutton while filtering out noise.
- [Digital Input Pullup](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/02.Digital/DigitalInputPullUp.py): Explore the utilization of Pin.PULL_UP in this example, which demonstrates its effectiveness in pulling up the input value of a pin.

## 03.Analog
- [Analog In Out Serial](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/AnalogInOutSerial.py): Learn how to read an analog input pin, map the result, and utilize that data to adjust the brightness of an LED.
- [Calibration](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Calibration.py): Learn how to define a minimum and maximum for expected analog sensor values.
- [Fading](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Fading.py): Discover how to use an analog output (PWM pin) to create a fading effect on an LED.
- [Smoothing](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/03.Analog/Smoothing.py): Learn how to smooth multiple readings of an analog input with this example, which provides step-by-step guidance..

## 04.Communication
- [ASCIITable](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/ASCIITable.py): Explore the advanced serial output functions of the ESP32 with this comprehensive example, which demonstrates its features and capabilities.
- [Dimmer](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/Dimmer.py): Learn how to adjust the brightness of an LED by moving the mouse.
- [Physical Pixel](https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/04.Communication/PhysicalPixel.py): Discover how to toggle an LED on and off by transmitting data to your ESP32 from Processing or Max/MSP.

# What is MicroPython
MicroPython is a specialized version of Python 3, created specifically for use in microcontrollers and embedded systems. While standard Python and MicroPython are similar, the latter is optimized for smaller devices. If you're already familiar with Python, you'll find programming in MicroPython straightforward. Using MicroPython to program the ESP32 board is an excellent way to take full advantage of its capabilities. Furthermore, the ESP32 chip is an ideal platform for using MicroPython, making it easy to develop projects for a variety of applications.

# Requirements
Before you can get started, you'll need a board equipped with an ESP32 chip. Fortunately, the MicroPython software supports the ESP32 chip, and any board should suffice. The critical consideration when selecting a board is how the GPIO pins are connected to external devices, as well as whether it includes a built-in USB-serial converter that connects the UART to your PC. With these requirements met, you can start programming your board using MicroPython to create a wide range of projects.

# Flash/Upload MicroPython Firmware to ESP32
To begin using MicroPython with your ESP32 board, you'll need to flash/upload the MicroPython firmware. To do so, you must first install the uPyCraft IDE on your computer. Depending on your operating system, you can download the uPyCraft IDE for Windows, MAC OS X, or Linux from the provided links. Once you have installed the uPyCraft IDE, you can proceed with flashing the MicroPython firmware onto your ESP32 board and start programming it using MicroPython.
- [uPyCraft IDE for Windows](https://github.com/DFRobot/uPyCraft/raw/master/uPyCraft.exe)
- [uPyCraft IDE for MAC OS X](https://github.com/DFRobot/uPyCraft_src)
- [uPyCraft IDE for Linux](https://github.com/DFRobot/uPyCraft_src)

Flashing your ESP32 board with MicroPython firmware is a straightforward process if you have the uPyCraft IDE already installed on your computer. With the uPyCraft IDE, you can upload the firmware and begin programming your ESP32 board with MicroPython to create a wide range of projects.

## Getting the firmware
To flash your ESP32 board with MicroPython firmware, you must first download the latest MicroPython firmware.bin file from the official [MicroPython downloads page](https://micropython.org/download/esp32/). You have three firmware options to choose from:
- Stable firmware builds
- Daily firmware builds
- Daily firmware builds with SPIRAM support

## Deploying the firmware
### Selecting Serial Port
To deploy the MicroPython firmware onto your ESP32 board, you need to select the correct serial port in the uPyCraft IDE. To do this, navigate to the "Tools" menu and click on "Serial." From the drop-down menu, select the COM port that corresponds to your ESP32 board (e.g., COM3). This will ensure that the firmware is uploaded to the correct device and ready for use.

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/uPyCraft-IDE-Select-Serial-Port-COM3.png">
</p>

### Selecting the Board
To continue with deploying the MicroPython firmware, the next step is to select the correct board in the uPyCraft IDE. Simply navigate to the "Tools" menu and click on "Board." From the options available, select "esp32" to ensure that the firmware is compatible with your board. This step is essential to ensure that the firmware and board communicate correctly and avoid any errors during the upload process.

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/uPyCraft-IDE-Select-Board-ESP32.png">
</p>

### Flashing/Uploading MicroPython Firmware
Finally, to flash your ESP32 with MicroPython firmware, go to Tools > BurnFirmware menu in uPyCraft IDE. Select the firmware.bin file you downloaded and click the "Burn" button to start the flashing process. Once the process is completed, you can start programming your ESP32 with MicroPython!

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

To flash the ESP32 board with MicroPython firmware, ensure that you have selected the appropriate board, burn address, erased the flash, and chosen the COM port and firmware file. Then, press and hold the "BOOT/FLASH" button on your ESP32 board while clicking the "ok" button in the firmware burning window. This will initiate the firmware flashing process.

<p align="center">
  <img  src="https://github.com/Hatem-Zehir/MicroPython-ESP32-Examples/blob/main/assets/OK-update-firmware-esp32.png">
</p>

After starting the "EraseFlash" process, you can release the "BOOT/FLASH" button on your ESP32 board. Within a few seconds, the firmware will be flashed onto the board.

# Further Reading
- [Built-In Examples | Arduino](https://www.arduino.cc/en/Tutorial/BuiltInExamples)
- [Getting started with MicroPython on the ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [Flash/Upload MicroPython Firmware to ESP32 and ESP8266](https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/)
- [Getting Started with MicroPython on ESP32 and ESP8266](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)
