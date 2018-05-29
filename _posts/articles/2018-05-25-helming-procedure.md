---
author: nanoseb
comments: true
date: 2018-05-26 18:57:46+00:00
layout: article
image:
   teaser: logo.jpg
   path: /images/logo.jpg
published: true
title: "Helming node: some sailing knowledge inside a robot"
categories:
- articles
---

In this blog we often talk about our hardware, electronic, lake and sea test etc. But we don't talk about software very often, so today we will present a new component that we just been implemented and tested in water a couple of weeks ago. We call it the helming node.

Since our first competition in Portugal in 2016, we have noticed that switching tack can be quite tricky on such small
boats. There are several reasons for this: Firstly, you can imagine that a 1m boat in 10-20 cm waves can have issues with
tacking. Secondly, our boat, like most RC boats, has just one control to operate both the main sail and the jib, which is
not ideal for the fine tuning that is sometimes needed to tack.


Sailors know that on a proper sailing boat you try to time the moment you start a tack with the waves, to make the waves help your maneuver rather than hinder it. This is one of the technical improvements we are trying to provide with the helming node.
In some cases tacking will also need some fine tuning of the sails to find the right balance. If sheets are in too much, the jib will
have too much power and this will lead to trouble when trying to tack (the jib being at the
front of the boat, it tends to make the boat go more downwind). On the other side, if we sheet out too much during a
tack, the boat will lose speed and momentum and tacking can become more difficult.

Until now, to be able to switch tack in adverse weather we had a parameter that would make the boat jibe instead of tacking,
even when beating upwind, because jibing is usually not an issue. However, the boat looses quite some distance when
trying to go upwind, and if you are against the current as well, you might end up making no progress at all.

To circumvent these issues, we have implemented a new component to handle switching tacks. Our high-level
code is taking care of the global path planning, like how to go to a waypoint or how to stay in position. When the boat
needs to switch tack, it will tell the helming node. This helming node then has a list of procedures to handle
tacking/jibing, and it will choose the technique to be used next from this list. If a procedure doesn't succeed after a certain amount of
time, the helming node will try the next one on the list. For now we have implemented only simple procedures:

* A simple tack: just rudder fully in one direction and wait
* A simple jibe: rudder in the opposite direction compared to a tack, and sheets out
* A building momentum tack: the boat will go at 80 degree form the wind for a bit to build up some speed and tack just
  after (for now this is based on a timer, but in the future it can use more information like the boat velocity)
* Sheet out tack: the boat will sheet out a bit to tack, to prevent the jib having much power

Currently, the order in the list of procedure is fixed, but in the future it can be dynamic, assigning positive points to
manoeuvres that were a success and negative to the failures to make the boat learn from its recent attempts.

Something we are also working on is the wave detection and tack timing. Based on the sensors we have on board like the
accelerometer, we can detect the progress of the boat on a wave and time the tack.

In the end, the helming node is a framework that allows us to implement and handle these procedures very easily. Now we just
have to implement more of them and tune the selection, so the boat chooses the right manoeuvre in all weather conditions.

Since our code is opensource, you can have a look at our implementation
[here](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/helming).
 



