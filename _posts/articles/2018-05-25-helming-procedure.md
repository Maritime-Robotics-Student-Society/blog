---
author: seb
comments: true
date: 2018-05-25 18:57:46+00:00
layout: article
image:
   teaser: logo.jpg
   path: /images/logo.jpg
published: false
title: "Helming node: some sailing knowledge inside a robot"
categories:
- articles
---

In this blog we talk about our hardware, electronic, lake and sea test etc. But not too often about our software. Today we will
present a new component that have just been implemented and tested in water a couple of weeks ago, we called it the helming node.

Since our first competition in Portugal in 2016, we have noticed that switching tack can be quite tricky on such small
boats. There is several reasons for this, first you can imagine that a 1m boat in 10-20 cm waves can have issues with
tacking. Then our boat, like most RC boats, just have one control to operate both the main sail and the jib, which is
not ideal for the fine tuning that is sometimes needed to tack.


Sailors know that on a proper sailing boat you try to time the moment you start a tack with the waves to make them help your maneuver,
this is one of the problem we are trying to solve with this helming node.
In some cases tacking will also need some fine tuning of the sails to find the right balance. If sheets are too in the jib will
have too much power and this will lead to trouble when trying to tack (the jib being at the
front of the boat, it tends to make the boat go more downwind). On the other side, if we sheet out too much during a
tack the boat will lose speed and momentum and tacking can become more difficult.

Until now, to be able to switch tack in adverse weather we had a parameter that would make the boat jibe instead of tacking,
even when beating upwind, because jibing is usually not an issue. However, it makes you loose quite some distance when
trying to go upwind, and if you are against the current as well you sometimes can't even progress.

To circumvent all of these issues we have implemented a new component to handle switching tacks. Our high-level
code is taking care of the global path planning, how to go to a waypoint, how to stay in position etc. and when the boat
needs to switch tack it will tell so to the helming node. This helming then have a list of procedure to handle
tacks/jibes, and it will choose in this list which one to try. If a procedure doesn't succeed after a certain amount of
time, the helming node  will try the next one on the list. For now we have implemented only simple procedures:

* A simple tack: just rudder fully in one direction and wait
* A simple jibe: rudder in the opposite direction compared to a tack, and sheets out
* A building momentum tack: the boat will go at 80 degree form the wind for a bit to build up some speed and tack just
  after (for now it is based on a timer, but in the future this can be based on the boat velocity for example)
* Sheet out tack: the boat will sheet out a bit to tack, this is to prevent the issue described above when the jib has
  too much power

For now, the order in list of procedure is fixed, but in the future this can be dynamic, assigning positive points to
manoeuvres that were a success and negative to the failures to make the boat learn from its past tries.

Something we are also working on is the wave detection and tack timing. Based on the sensors we have on board like the
accelerometer, we can detect the progress of the boat on a wave and time the tack.

In the end the helming node is a framework that allows us to implement and handle these procedures very easily, now we just
have to implement more of them and tune them to have the best in all weather conditions.

Since our code is opensource, you can have a look at our implementation
[here](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/helming).
 



