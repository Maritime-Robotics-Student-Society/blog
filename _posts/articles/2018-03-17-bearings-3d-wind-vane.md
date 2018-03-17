---
author: Camil
comments: true
date: 2018-03-17 18:57:46+00:00
layout: article
image:
   teaser: logo.jpg
   path: /images/logo.jpg
published: false
title: "Wind vane design"
categories:
- articles
---

As we started to look more and more into footies, the need for a scalable wind vane design became apparent,
as we needed a wind vane for the small boats and for the bigger one. This new design can be scaled by 
modifying just a few top level paramenters, such as the size of the fin. The centre of mass is always kept
at the support, regardless of the values of the top level parameters. This ensures that the wind vane spins
with the least possible friction and reacts to the smallest changes in the wind's direction.

Our first prototype used a steel bearing to separate the rotating part of the vane from its support. Although
it was spinning without friction, due to the bearing, it was not reacting to small changes in the wind's direction
as the viscous grease in the bearing was providing some resistance. Removing the grease wouldn't have been a 
solution, due to the higly corrosive enviroment of the sea. The second prototype ditched the idea of a standard bearing
and used a much simpler way of reducing friction. The rotating body of the vane would be separated from its support
using one ball bearing resting on top of a metal rod with a flat top surface. Due to the low weight of the rotating body,
friction between the ball and the metal surface would be minimal, so the vane can react even to the smallest
changes in wind direction.

![Wind vane assembly](/images/wind-vane.png)
Wind vane assembly

The support of the wind vane is designed to fit perfectly on the mast of the robot, high above the water level,
where the wind is not disrupted by the water or even the robot itself. This way we minimise the flutter of the
vane. This support also needs to accomodate all the electronics that are necesary. Attaching the vane to the mast
is done using rubber bands, which makes it very easy to remove is we need to change the sails and the mast.

The wind vane was 3D printed using ABS and PLA plastic for different components due to difficulties in the
manufacturing procces. After manufacturing, it was clear that the centre of mass was not in the correct position,
because of the different fillings that occur in 3D printing procces. To eliminate this, we've added some weights
on one end of the vane. 

A very interesting dicorvery that we have made recently, are zirconium oxide bearings (ZrO2), that do not corrode,
so they can be used without grease, removing the viscous resistance that we were experiencing in our first prototype.
This might be an alternative to our current design, but because of the high price of those bearings, we have decided 
not to use them yet.

