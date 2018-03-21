---
author: Camil
comments: true
date: 2018-03-19 18:57:46+00:00
layout: article
image:
   teaser: wi-fi-2119225_640.png
   path: /images/wi-fi-2119225_640-thumbnail.png
published: false
title: "Connecting the WiFi dongle"
categories:
- articles
---

As discussed in a previous article on the blog, connecting the WiFi
dongle, situated on the top of the mast, to the Raspberry Pi, inside the
hull of the boat, proved to be much more difficult than expected.
Those WiFi dongles are designed to be plugged directly into an USB port
without a cable. Moreover, USB cables are well shielded from external 
electrical noise by a metal meshing that surrounds the cables, which is
at ground potential. For our application, we wanted to try to see if it's 
possible to connect the dongle using regular wires, without shielding, 
in order to save weight, to reduce the cost and facilitate repairs.

For our first attempt, we soldered 2 metre long wires directly to the USB 
pins of the dongle and connected the other ends to a cut USB cable, which 
was plugged into the Raspberry Pi. We were not able to detect the WiFi signal
and when plugged into a laptop, it was showing as an unreconginesd USB device.
Not even shortening the wires helped, the WiFi was still not showing up. We
decided that soldering directly to the WiFi dongle was a bad idea, so for our
second attempt we soldered a female USB plug to the long wires, into which the
dongle was plugged in. Connecting this setup to a laptop did not work again.
It was still showing up as an unrecognised device, but when tested with an USB mouse,
everything seemed to work just fine. The cursor on the screen was in fact moving,
and we couldn't observe any difference when we connected the mouse directly to the laptop.

This was very interesting for us, so we decided that more research into the 
way USBs use voltage to send data was needed. Connecting the logic level analyser
to the D+ and D- lines of the USB, when the mouse was plugged in, showed us a 
signal that was nothing what we expected. It was clear that USB, at least in this case,
doesn't use just 2 voltage levels, like I2C, but many more.

![USB mouse](/images/USB_mouse.png)

Signal waveform of the mouse, D+ on channel 1 and D- on channel 0

USB uses two data lines, that work opposite from each other, so that their voltage
sum is always the same. Those two lines are physically very close to each other so
they are very likely to pick up the same electrical noise. This noise can be filtered
out as the sum of the two lines is known, so any inconsistency against this know sum is
electrical noise, which is then substracted from each of the two lines.

We used the same setup to look at the WiFi dongle's signal waveform, to see why this doesn't
work, while the mouse does. As we connected the dongle, we saw a very different kind of
signal, one which looked very similar to a digital clock signal, but on two distinct levels.

![Wifi waveform](/images/USB_wifi.png)

Signal waveform on connecting the WiFi dongle to the laptop

This time, the two probes were connected on the same data line, one very close to the 
dongle and the other close to the laptop, because we wanted to see if there's any voltage
loss across the long wires, which would affect the signal quality, but it appeared to 
not be any, which was good news for us, meaning that the wires don't have enough impedance to affect the signal
but the WiFi was still showing up as an unrecognised
USB device. Trying to probe the signal as the mouse was connected, was showing again the 
previous waveform, the one on multiple voltage levels, rather than the strange clock-looking
one. Probing the 5V and the GND lines showed us that the voltage levels stays constant when
any device is connected, so that wasn't the issue.

We then tried to make our long cable more like an actual USB cable, so we simply twisted the 
two data lines togheter, and miraculously, the WiFi started working, togheter with any other
USB device that we connected to our cable. Even though we now have a working USB cable, we still
haven't managed to explain the big difference in the two kinds of USB signals.
