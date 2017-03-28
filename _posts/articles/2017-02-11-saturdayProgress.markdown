---
author: smaria
comments: true
date: 2017-02-11 20:42:59+00:00
layout: article
image:
   teaser: opensource_logo.gif
title: We're officially sailing under MIT licence!
categories:
- articles
---
In the spirit of the physical cleanup a few weeks ago, at our first Saturday meeting we dedicated ourselves to some tasks
we had in the back of our minds and in our issue tracker for a while now: Licencing, tracking when our boat is autonomous and analysing data collected during experiments.

We completed our check of all code, to see if files that are not our own had a correct licence file attached. After the conclusion of this, we were finally happy to add
 an MIT licence file to our repository.
You may ask - a what? The licence file clearly states how others can use our code, making it easier for others to decide if our code can be used for their own projects
without having to fear legal consequences and making clear where the work comes from. There exist a large variety of licences, with various restrictions.
We always agreed we wanted to go for an open licence like MIT or BSD, that allow both commercial and private use, as long as the information in the licence file is kept
as detailed in the licence. We choose MIT since there only exists one version of that, which we found simpler.

For a long time we also had added a wire connecting the remote control to the raspberry pi,
with the plan to record when we were using the remote control.
Today we completed the software connecting this wire to a logged output: Our new node "sensor driver multiplexer" now publishes the sailing autonomy state in a topic.

And finally, a bit meta, our task cleanup started work on simplifying the cleanup after each experiment.
After returning from eventful sunny screen blinding or rainy laptop endangering experiments,
it is always tedious to manually search through the recorded data and find out what exactly happened.
We now have an automated index for `rosbags`, connecting the GPS traces, `rosbags` and parameters of each experiment with the time and day of the experiment..

Now we conclude the cleanup of our digital house for today, this somewhat complex construct is not as quickly cleared as the hardware...
