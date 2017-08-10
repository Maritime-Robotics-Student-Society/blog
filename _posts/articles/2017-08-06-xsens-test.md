---
author: thomas and sim
comments: true
date: 2017-08-06 18:57:46+00:00
layout: article
image:
   teaser: 20170806_water_test_cover.jpg
   path: /images/20170806_water_test_cover.jpg
published: true
title: 1st Sea Test 2017 Testing the Xsens MTi3
categories:
- articles
---

Last Sunday, the 6th of August, marked 2017's first sea test. It's high time
the Black Python tasted the saltwater once again! This time around, we got our
hands on some new kit to try out. Armed with a
[ROS driver](https://github.com/ethz-asl/ethzasl_xsens_driver) from ETH Zurich,
Sunday was our first chance to put our new toy through its paces, with a morning
test at Southampton Sailing Club.

![2017 water test cover](/images/20170806_water_test_cover.jpg)
*The estuary by the sailing club, complete with great weather*

[Xsens](https://www.xsens.com/) has generously sponsored us with one of their
MTi-3 motion tracker modules and a developer board. This is a major upgrade for
the Black Python's electronic compass, replacing the Pololu
[MinIMU-9](https://www.pololu.com/product/2468) we have been using.

![Xsens logo](/images/xsens-logo.png)
*Snazzy Xsens logo*

The Xsens device not only has more accurate sensors, it also does onboard
processing to calculate its orientation, integrating magnetic field readings,
acceleration and gyroscope data. Our own code to calculate the heading from
the MinIMU's sensors was not entirely reliable, so if we can benefit from
Xsens' clever algorithms, it's a definite win.

![2017 water test setup](/images/20170806-water-test-1.jpg)
*Setting up the Black Python*

![2017 water test calibration](/images/20170806-water-test-2.jpg)
*Tony and Sophia with the good old calibration dance*

![2017 water test accel](/images/20170806-water-test-3.jpg)
*We wanted to show the accelerometer testing screen here. You can just about
make it out. We should probably shop this to brighten the screen.*

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
