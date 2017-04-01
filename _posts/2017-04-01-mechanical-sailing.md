---
author: smaria
comments: true
date: 2017-04-01 19:57:46+00:00
layout: post
title: Mechanical sailing for the win!
categories:
- Sailing Robot Team
---

If you have been following our blog posts over the last years, you will know: 
Software is full of errors and waterproofing electronics is a pain!
We are excited to announce that this year we will take a completely novel approach to the
world robotic sailing championship this year, which will solve all our problems. 
We are going fully mechanical with our newest mechanical robot DaVinci, gearing up to 
be victorious!

![Mechanical Robot concept](/assets/images/operation.png)

How will this work you ask?
Over the last two months we have designed gearboxes that will implement the rudder and sail motions for
all manoeuvres we need: Tacking, jibing, and keeping a heading.
Before any competition event, we will pre-program the heading and distance the vehicle has to
go between each waypoint. We have made a simulation of the gearboxes, which allows us to test our settings
beforehand.
To make our sailing robot more accurate than ever, we incorporate the rotation of an anemometer 
at the top of our boat and the rotation of a current measuring wheel below our boat. A faster spinning 
anemometer decreases the time between manoeuvres, allowing the DaVinci to consider the speed of the wind
and thus its own speed. The spinning speed and direction of the current measuring wheel 
corrects the heading settings.
To increase stability and improve the tacking capability of our boat, we added two spinning wheels.
One to keep the boat from heeling, spinning in the horizontal plane. A second wheel to help with keeping
a constant heading, which is also actuated to support rudder actions.   

![Wind anemometer detail](/assets/images/mechanical.png)

With the system described above, we are convinced we can better solve the racing, area scanning and
position keeping tasks. The obstacle avoidance though is a larger challenge. Our main plan are
four long whiskers. Thanks to the physics of leaver arms, a light touch on the obstacles at a very
long distance will be enough to induce a small, strong torque motion on DaVinci which will 
set in motion our obstacle avoidance.
Should the touching of the whiskers count as a collision, our alternative plan is
to resign to using a camera
with a servo motor to integrate the camera results in our mechanics.

Of course, we are not completely rid of the problems caused by operating in salt water. To avoid crystallized
salt clogging up our gears, we will use de-ionised water. With the relatively short missions of the sailing
robot this should be sufficient protection.

Now the implementation starts: This week we are starting to 3D print the gear parts that have
lower torque on them and won`t be under a lot of stress. The higher stress parts will be machined
from aluminium, or where needed from stainless steel at the EDMC.
Keep an eye on our blog for future posts explaining the intricate details of our gear design, 
our manufacturing progress and details on our simulation.

Veni, Vidi, Vi(n)ci!
