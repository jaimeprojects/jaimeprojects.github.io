---
title: "Washroom Status Monitor"
excerpt: "Taking guesswork out of doing laundry <br/><img src='/images/wash_render.png'>"
collection: portfolio
---

## Project Goal: 
Be able to monitor my laundry from anywhere in the world, and it would be compatible with any standard household washer/dryer

# Hardware:
* [Adafruit_Feather](https://www.adafruit.com/)
* 3 Axis Accelerometer

# Technologies used
* [AdaFruit_IO](https://io.adafruit.com)
* [IFTT](https://giuthub.com)

# Method:
The original idea that I had was to make an Internet of Things device that would utilize a 3-axis accelorometer to monitor activity. Once the wash would be completed it would pin a website that then talks to [IFTT](https://ifttt.com/) to then alert me that its complete either through adding an event to my calendar or sending me a message


## Design Aspects to keep in mind
* Creating a temperature resistant enlosure for exposure to Laundry environment
* Having a device that is also impact resistant to tumbling

### Network
The ESP8266 chipset only supports the WPA2 Wireless Protocol, so I created my own network for the testing since most universities use Enterprise Internet

# Enclosure Design
All 3-D iterations of the enclosure I designed using Blender and printed them using on campus 3-D printers

### Future Additions
* using additional position sensors I wanted to add a cycle recognition feature so that you could see live what stage the wash was in. 
* get logistics for thngs like gallons of water used and energy used based on recorded times

# How it Works

## Before Wash
* The monitor is designed to be placed along with the clothes so that it can better plot all of the data while clothes are being washed

## While in wash
* The monitor is continously plotting the data recieved from the accelerometer and checking to see if it is still in motion

## Once Complete
* Once the monitor has determined that the there is no more motion it will trigger an event by communicating with the Adafruit IO website

## Adafruit IO
* Here is the main point of communication for the monitor and is secured by a Token to ensure they only desired output is recieved
* This is also where the monitor connects to the IFTT website where it commuinicates with an applet that I created

## IFTT Integration
* Adafruit IO has an applet that I relied on to capture the 'DONE' event from the monitor
* Notification to the user can be done in a number of ways  ex: Calendar Entry, Email, SMS Message, Tweet

## Other Docs
[Here](https://drive.google.com/open?id=1gRtXX9cHztKwmjANzcIc4jyLvEAVqZaw) is a small introduction to the project that I had made to pitch for an on campus program.