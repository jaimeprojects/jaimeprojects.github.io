---
title: "Washroom Status Monitor"
excerpt: "Taking guesswork out of doing laundry <br/><img src='/images/wash_render.png'>"
collection: portfolio
---

## Goal: 
Be able to monitor my laundry from anywhere in the world, and it would be compatible with any standard household washer/dryer

# Hardware:
[Adafruit_Feather](https://www.adafruit.com/)

# Method:

The original idea that I had was to make an Internet of Things device that would utilize a 3-axis accelorometer to monitor activity. Once the wash would be completed it would pin a website that then talks to [IFTT](https://www.iftt.com) to then alert me that its complete either through adding an event to my calendar or sending me a message

## Obstacles

# Environment
Some of the things I had to think about was how I was going to make the unit resistant to shock, temperature fluxuation, and submersion. 

# Network
The original plan was to have the unit link with the school network. However I later learned that the type of network utilized by the school was incompatible with my unit.

# My Solution
I designed several iterations at my on campus lab and 3D printed the enclsosures for testing. Most enclosures had the minimal amount ports. For the networking I simply used a standard Wlan network to connect my device for testing.

# Stretch Goals
* using additional position sensors I wanted to add a cycle recognition feature so that you could see live what stage the wash was in. 



### Other Docs
[Here](https://drive.google.com/open?id=1gRtXX9cHztKwmjANzcIc4jyLvEAVqZaw) is a small introduction to the project that I had made to pitch for an on campus program.