# RealTimeCoursework
author: Maciej Dudziak

This work was done as a part of the coursework for the RealTime Computing and Embedded Systems module. Coursework instructions could be found below.

## 1. Acknowledgements
This work was done basing on the SDK examples provided by the NXP semiconductors for the MCUExpresso IDE.
Development board used in this work is FRDM-KW41Z.

Used SDK examples are:

    - mwa_coordinator
    - mwa_end_device
From the wireless_examples/ieee_802_15_4.

Those examples were used as a base for implementing simple networking functionality on the IEEE 802.15.4 stack.

## 2. Installation instructions

Project consists of two parts: 

    - Flask web application written in Python that can be run in any browser. 
      To run the application user need to have Python3 installed and ensure that can open
      serial port (for example with Putty software) to which the host board is connected.
      Lines 7-9 of the main.py file will be different depending on the machine and operating system.
      User need to ensure that the correct name of the serial port is used (COM on Windows and /dev/ttyACM
      on Linux) with the correct port number.
      
    - Embedded firmware based on the FreeRTOS. This repository contains only the content of the "source" folder
      of the SDK example as only these files are being changed. To use this work user should first import
      mentioned in Section 1 SDK examples to ensure that all the required drivers, Freescale framework,
      802.15.4 stack is imported. Then, the user should just replace the content of the source folder with the content
      of the corresponding folders in the repository.
      
The project was developed using the MCUXpresso IDE which is the open-source IDE provided by NXP.

## 3. Coursework Instructions

You will need to work somewhat with one other pair, as you will need access to four development boards. 

The intent is to create a simple mesh network for your internet of things (IoT):

    1. One of the four boards should interface to a host computer via serial RS232 emulated over USB. 
    A simple web server program running on the host should issue commands over the serial interface 
    to turn the lights of all three boards on or off. 
    A standard web browser should be able to connect to this server; 
    the server will present a page with “on” and “off” buttons for the lights.
    The web page should also report lights that are uncontrollable because of communication failure.
    
    2.The other three boards should be programmed similarly; they receive, if they can, 
    radio messages from the host interface board or the other slave, act on them locally, 
    and relay to the other slavesif necessary.
    
    3. There should bea convincing demonstration of forwarding and failover; 
    as some of the slave boards go out of range of the master, “mesh” communications 
    should be maintained until failure is eventually reported through the web interface.
    
## 4. Software operation

The system consists from four FRDM KW41Z boards. One of them is operating as a host/master device and is connected through USB cable to the PC. Three other boards are running as slave devices.

User can control the LEDs on the slave devices using the website running on the Python Flask application.

After pressing the button the LED on the corresponding slave will turn on or off. If the master device will not receive confirmation from the slave device within the 3 seconds, it will produce the error message displayed on the website.

The network supports routing operation. it can be observed watching the colour of the LED. It will be white if the message from the master was delivered directly to the slave - the LED will illuminate white. If the message was routed through one node - colour will change to yellow. If through two nodes, it will be red.
