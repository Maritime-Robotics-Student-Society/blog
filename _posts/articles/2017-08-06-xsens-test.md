---
author: thomas
comments: true
date: 2017-07-30 18:57:46+00:00
layout: article
image:
   teaser: xsens-logo.png
published: true
title: Testing the Xsens MTi-3
categories:
- articles
---

![Xsens logo](xsens-logo.png)

[Xsens](https://www.xsens.com/) has generously sponsored us with one of their
MTi-3 motion tracker modules and a developer board. This is a major upgrade for
the Black Python's electronic compass, replacing the Pololu
[MinIMU-9](https://www.pololu.com/product/2468) we have been using.

The Xsens device not only has more accurate sensors, it also does onboard
processing to calculate its orientation, integrating magnetic field readings,
acceleration and gyroscope data. Our own code to calculate the heading from
the MinIMU's sensors was not entirely reliable, so if we can benefit from
Xsens' clever algorithms, it's a definite win.

Armed with a [ROS driver](https://github.com/ethz-asl/ethzasl_xsens_driver)
from ETH Zurich, Sunday was our first chance to put our new toy through its
paces, with a morning test at Southampton Sailing Club.

The good news was that the Xsens appeared to be performing nicely: we could
watch the heading updating smoothly as we turned the boat round. But it
wasn't without challenges; due to a configuration issue which we're still
working out, the boat thought that whichever way it was pointing when we started
ROS was east.

Struck by some mysterious issues with the GPS, we decided not to try autonomous
sailing on this test. But the boat wasn't staying dry! We sent it into the water
under remote control, with the Xsens on board to collect accelerometer data as
it bobbed on the waves. With that data, we plan to see if we can pick up the
pattern of the waves to decide when the boat should tack.

After the test, and the tidy-up, the team enjoyed a well-earned Sunday roast
at a nearby pub.
