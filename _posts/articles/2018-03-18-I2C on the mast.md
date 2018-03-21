---
author: Camil
comments: true
date: 2018-03-18 18:57:46+00:00
layout: article
image:
   teaser: IMG_mast_elec2.jpg
   path: /images/IMG_mast_elec2-thumbnail.jpg
published: published
title: "I2C on the mast"
categories:
- articles
---

Together with the new design of the wind vane, we decided to redesign the wiring
between the electronics situated on the mast (IMU, GPS and Wifi) and the Raspberry Pi. One of the main
reasons why we decided to do this is because we wanted to move the WiFi dongle from
inside the boat, to the top of the mast where the signal would be far better. This
posed a couple of challenges. First of all, USB cables are usually well shielded 
from electrical noise. In our case, shielding would have added a lot of weight,
which was undesirable. Another challenge we found was that powering the IMU with 5V,
the level required by the WiFi, would make it output I2C on a 5V level, which would
have been incompatible with the GPS or the Raspberry Pi. Previously, we were powering
the IMU and the GPS with 3.3V and communicating with the GPS via serial.

| Device       | Communication protocol     | Voltage level |
| :------------- |:-------------:| -----:|
| WiFi dongle    | USB | 5V |
| IMU     | I2C only      |   3.3-5V |
| GPS | I2C or Serial     |    3.3V |

Table explaining all the electronics requirements

Adding the WiFi dongle meant we needed a 5V line going up on the mast, but the IMU had an integrated
voltage step down circuit to 3.3V so we were able to easily power the GPS of that, but the
I2C level incompatibility still remained, as we wanted to have the GPS on I2C as well, rather
than serial to avoid adding another 2 cables. Because we knew the IMU has a voltage step down
circuit to 3.3V, the level we needed, we decided to take a closer look at the schematic of
the sensor, which can be found [here](https://www.pololu.com/file/0J772/altimu-10-v4-schematic-diagram.pdf).

![IMU Schematic](/images/0J5198.1200.png)

IMU schematic highlighting the two pull-up resistors considered

Researching how I2C waveform looks, we learned that both lines (SCL and SDA) are pulled high
by pull-up resistors and when data is being transmitted, the microchips pull the lines low, so
individual bits of data can be sent. Those bits are usually sent in groups of 8
forming bytes, which are then converted into sensible values by the code.
It was easy to see that the VIN (the pin that feeds into the voltage step down circuit, which is where we were powering the IMU with 5V) voltage 
was only connected on the I2C lines through pull up resistors and that the chip was working
entirely on 3.3V. Because we knew that if the VIN pin is floating and we power the chip directly
with 3.3V (on the VDD pin which bypasses the voltage step down circuit) the IMU would output on a 3.3V level, we 
decided to look into what would happen if we remove the two pull-up resistors. By looking at the
voltage level before the two transistors (Q1 and Q2 on the schematic) using a logic level analyser
we indeed saw an I2C level of 3.3V. The two transistors, together with the pull-up resistors were
forming a level shifting circuit, which was stepping the I2C level to VIN. This circuit was very
similar to the one of a bi-directional level shifter.

![Lvl shifter](/images/Logic_Level_Bidirectional-1.jpg)

Logic level shifter schematic.

We identified the two pull-up resistors that we wanted to remove by tracing the copper tracks
on the IMU's board and by probing the board with a multimeter. Removing them proved to be
straightforward. The Raspberry Pi has pull-up resistors for 3.3V level, so the lines were not
left floating at any time. Testing the modified sensor, we immediately saw that the I2C level
dropped to 3.3V even when it was powered with 5V, which was exactly what we wanted. 

Adding a separate level shifter on the mast would have worked just as well probably, but this
would have exposed more circuitry to the environment and we wanted to avoid as much as possible
adding extra weight or components on the mast. A small external voltage regular, to drop the voltage
to 3.3V before it being sent to the IMU and the GPS, was also considered, but again, we wanted
to avoid adding extra components.

The waterproof connectors we are using at the moment, have 8 pins that can be used, while our
wiring only uses 6 wires, which means that we still have 2 pins free, that can be used in case
we ever decide to add a new sensor on the mast, such as a sensor that can detect sail flutter.

Our current wiring map of the electronics can be found [here](https://github.com/Maritime-Robotics-Student-Society/Boat-construction/blob/master/Electronics%20Mast/final%20wire%20map.svg)
