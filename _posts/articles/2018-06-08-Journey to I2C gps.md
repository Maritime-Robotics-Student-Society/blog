---
author: Camil
comments: true
date: 2018-06-08 18:57:46+00:00
layout: article
image:
   teaser: logo.jpg
   path: /images/logo.jpg
published: true
title: "Journey to I2C GPS"
categories:
- articles
---
Redesigning the mast electronics, meant at the same time adressing an issue from the past. Up until now,
the GPS was wired through its Serial port, but this required us to have a total of 8 wires going up on
the mast. Having the GPS on I2C would eliminate the two Serial wires and bring the total number down to 
6. In order to achieve this, a few changes needed to be done, first of all the I2C level was incompatible
with the GPS and from reading some other articles, we got the impression that the I2C of the GPS was 
working slightly differently than expected. In the datasheet of the chip, the I2C port is described as being
DDC I2C compatible, which is different from an I2C, in the sense that data is being pushed from the slaves 
to the master. Nevertheless, we thought it is worth to look into this issue.

First step was to ensure compatibility between the I2C level of the GPS, IMU and Pi. The GPS we are using is the uBlox MAX-M8C.
As discussed in a
previous blog article, this was done by removing the two pull-up resistors from the IMU. At this point,
we simply wired in the GPS to see if we can get some messages coming from it. We immediately saw
messages coming from the GPS, but only about 40% of the messages where readable, as the rest of them 
were not passing a checking algorithm (a basic message checksum) that was designed to filter corrupted messages. Another issue 
that appeared was that through Serial, it was possible to write some messages to the GPS to filter out
data we don't need and to increase the frequency of the readings, but some articles were saying that this
cannot be done via I2C.

Another problem that we were concerned with at this point, was that the messages coming from the IMU would clash
with the messages coming from the GPS, as the GPS was simply pushing messages to the Pi, without it
requesting them. Looking at this issue with the logic level analyser, we were able to see IMU messages in 
the middle of GPS messages, which was encouraging as it meant that I2C can differentiate between the 
messages and ensure that they don't mix togheter. At the same time on the logic analyser, we saw that the long
lines coming from the mast, had some parasitic capacitance and inductance between them, as a change in 
one line, was producing a small spike (about 0.25V) in the other line. This didn't seem to be an issue 
as the conversion into digital of the signal looked very good.

![GPS waveform](/images/GPS_signal.png)
Waveform of the GPS signals and the spikes resulting from the parasitic capacitance and inductance

Further testing of the GPS only seemed to send messages at a frequency of 0.4-0.5 Hz, which was way less
than the 5 Hz we were getting from Serial and not enough for us, as a position update every 2 seconds would
make it very difficult to find out if the boat passed a waypoint and would make global planning of the route
quite difficult. Another issue we noticed was that the GPS settings sent via
Serial were not surviving a reboot. This meant we needed to reprogram the GPS via Serial after each start up.
At this point, I2C seemed to not be worth it. Further research into 
this problem revealed that settings can in fact, be sent via I2C to the GPS, which we thought it was 
impossible. Removing the unnecesary data from the messages increased the frequency to 3.7-4 Hz, which
was a lot better than before, but the problem of the corrupt messages still remained As discussed in a 
improved. Now about 80% of the messages were passing the checking algorithm, but regardless, I2C 
began to look promising. 

Further testing revealed a big issue in that the GPS would randomly hang up the Pi, stopping all scripts
running on it, and the only solution to recover from that was to reboot. We stumbled 
across [this](http://www.advamation.com/knowhow/raspberrypi/rpi-i2c-bug.html) article that introduced
to us the concept of "clock stretching". This occurs when the slave cannot send the data fast enough 
and it keeps the clock low for and extended period of time, while it compiles the necessary bits of data.
In I2C, the clock (SCL) is controlled by 
the master, the Pi in this case. The I2C bus on the Pi cannot cope with this stretching of the clock 
and it continues to read the SDA line as normal and the messages get corrupted. Looking at the waveforms 
recorded, we were able to see this phenomenon in action.

![Clock stretching](/images/clock-stretching.png)
Clock stretching of the SCL line (circled in red)

This was a surprise for us, as the data sheet of the GPS was stating that the chip can run at a 
frequency of 400kHz, while the Pi was only running the clock at 100kHz. It was, if anything, just 
a random thought to see what would happen if we set the Pi to 400kHz, to match the GPS. All of a 
sudden, all the messages were passing the checking algorithm and they were coming in at a frequency of
exactly 5 Hz, even steadier than the Serial connection, which was very good to see. Further tests to
ensure the reliability of the connection were succesful, with all the messages passing. Checking the 
other I2C devices to see if they can cope with the new, higher frequency proved succesful aswell.
This was excellent news, as we finally had a reliable connecting between all of our sensors through I2C.
We also stumbled across a software created by the GPS's manufactureres (uBlox) that provides a GUI to communicate
with the GPS, but it requires a Serial connection for this. We've managed to find a way of sending
a Serial port from the Pi via WiFi to a Windows computer, as the GUI can only be used on a Windows system,
to communicate with the GPS, for debbuging purposes. 



