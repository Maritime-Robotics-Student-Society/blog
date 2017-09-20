---
author: elisavet8
comments: true
date: 2016-07-06 16:22:29+00:00
layout: article
link: https://sailrobot.wordpress.com/2016/07/07/how-autonomous-is-the-robot/
slug: how-autonomous-is-the-robot
title: How autonomous is the robot?
wordpress_id: 406
image:
  teaser: default.png
  path: /images/default-thumbnail.png
categories:
- articles
---

We got an interesting question in our fundraising campaign, so we’d like to share the answer with everyone! Tim Miller, commodore of the [Walnut Valley Sailing Club](http://wvsailing.com), asked us about the autonomy of our robot, and how much racing strategy is involved in its control.



**_Where in the control loop is the human operator, and what are his cues?_**

Before a race or competition task, we have the position of the buoys, so we can set waypoints ourselves. However, from a given time before a race starts, the boat has to be autonomous, so the boat does everything from waiting at the start line until the end of the race. During the race, we’ll watch both the boat and the data it sends back to a laptop.

In fleet races there is one exception: if our boat is at risk of a collision, we will temporarily take control to steer it away from the other boat. We have an off-the-shelf remote control for this purpose.

This manual override is necessary due to the difficulty of sensing more than the difficulty of automated control. At the scale of the sailing robots, detecting another boat is not easy! Whilst crossing the Atlantic, AIS (Automatic Identification System) is useful for large-scale obstacle avoidance. At the sub-100m scale of the racing area, it is out of the question. To enable us to detect the obstacle, we think the most interesting feature is the colour, since it will allow us to detect it with a camera. This year for the collision avoidance task we have to detect an orange moving obstacle. In the future, maybe we all have to use the same sail and boat colour, so sailing robots can detect others?



**_How are decisions about racing rights of way and tactics are taken?_**

As expected, the decisions about sail set for the wind and the point to point navigation are automated. But how are the racing rights and tactics’ decisions can be taken by a robot? To be honest, some of our sailing enthusiasts are a little bit disappointed to be focussing on parameters for different wind conditions, and how to best use the wind direction and heeling angle, rather than tactical considerations for racing. On the other hand, we are happy to cover RYA sailing 1 first before we attempt higher levels!
