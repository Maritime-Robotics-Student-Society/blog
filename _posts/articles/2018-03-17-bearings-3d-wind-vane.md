---
author: Camil
comments: true
date: 2018-03-17 18:57:46+00:00
layout: article
image:
   teaser: wind-vane-3d-view.png
   path: /images/wind-vane-3d-view-thumbnail.png
published: false
title: "Wind vane design"
categories:
- articles
---
We are currently looking to redesign our wind vane for many reasons. Firstly, we are looking into smaller sailing robots,
called footies, which require a much smaller wind vane, than our big robot, Black Python. Secondly, we want to reduce
the weight that is added to the top of the mast, and finally we want to create a nice platform that can house and protect
all the electronics that are going to be added to the mast. Because we are redesigning electronic circutry that connects 
all sensor (GPS,IMU and WiFi) to the Raspberry Pi, as explained in a later blog post, to eliminate as many wires as possible,
we needed a new support for those. This new design can be scaled by modifying just a few top level paramenters, such as 
the size of the fin. The parametric design automatically rescales the wind vane in order to keep the centre of mass exactly
above the support. This ensures that the wind vane spins with the least possible friction and reacts to the smallest 
changes in the wind's direction.

The first wind vane we used was the smallest one we were able to find and buy. The fact that this was unscalable and that
designing a support for the electronics was adding a lot of extra material and weight, made us decide to not use this one,
but design our very own wind vane from scratch.

Our first prototype used a steel bearing to separate the rotating part of the vane from its support. Although
it was spinning without friction, due to the bearing, it was not reacting to small changes in the wind's direction
as the viscous grease in the bearing was providing some resistance. Removing the grease wouldn't have been a 
solution, due to the higly corrosive enviroment of the sea. For the second prototype, we stumbled upon [this](https://www.westcoastweathervanes.com/instructions-for-installing-your-weathervane-on-a-galvanized-pipe-or-wooden-post/) 
article, that gave us a very idea for reducing friction. The rotating body of the vane would be separated from its support
using one ball bearing resting on top of a metal rod with a flat top surface. Due to the low weight of the rotating body,
friction between the ball and the metal surface would be minimal, so the vane can react even to the smallest
changes in wind direction.

![Wind vane assembly](/images/wind-vane.png)

Wind vane assembly, section view

The support of the wind vane is designed to fit perfectly on the mast of the robot, high above the water level,
where the wind is not disrupted by the water or even the robot itself. This way we minimise the flutter of the
vane. This support also needs to accomodate all the electronics that are necesary. Attaching the vane to the mast
is done using rubber bands, which makes it very easy to remove if we need to change the sails and the mast.

<img src="/images/wind-vane-on-mast.jpg" height="400">

Wind vane attached to the boat's mast

The wind vane was 3D printed using ABS and PLA plastic for different components due to difficulties in the
manufacturing process. We used PLA for the bigger components as shrinking of the plastic would not pose such a bad problem.
ABS was used for the rest of them as it was more easily available. After manufacturing, the centre of mass was not quite 
in the right spot. To eliminate this, we've added some weights on one end of the vane. 

![Wind vane iterations](/images/wind-vanes.jpg)

The three wind vanes that are discussed in this post

A very interesting discovery that we have made recently, are zirconium dioxide bearings (ZrO2), that do not corrode,
so they can be used without grease, removing the viscous resistance that we were experiencing in our first prototype.
This might be an alternative to our current design, but because of the high price of those bearings, we have decided 
not to use them yet.

The files of the latest design can be found [here](https://github.com/Maritime-Robotics-Student-Society/Boat-construction/tree/master/Wind_Vane/v3)
