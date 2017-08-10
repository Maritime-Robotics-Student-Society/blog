---
author: thomas
comments: true
date: 2017-07-30 18:57:46+00:00
layout: article
image:
   teaser: data_index2.png
   path: /images/data_index2.png
published: true
title: Finding needles in a data haystack
categories:
- articles
---

Every time our robotic boat, the *Black Python*, goes out on the water, it's
recording data so that we can study what it was doing later on. The most
important data is from [rosbag](http://wiki.ros.org/rosbag), which can record
all the messages being sent between parts of our [ROS](http://www.ros.org/)
based system. This is really useful for reconstructing what the robot was
'thinking' when it does something we didn't expect. We also save the parameters
each time we launch the robot, and a separate record of our GPS position in
the format required for the WRSC competition.

But before long we'd got a new problem:

![lots of data files](/images/data_files.png)

So far, this folder has got about 460 files in, and it grows every time we test
the boat. All the data you could want is there, but where's the bit you're
interested in? It can be fiddly and tedious to find.

We've built a couple of tools to help us make sense of the data files we collect.

## Leaving a sign

First, when the boat does something unexpected (i.e. wrong), we want an easy
way to make a note of it, which will point us to the data it's recording just
then.

Our answer to this is [a script](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/a9776b5342c6b548a81922bee30015d6c5199243/recorded_data/notes/log_timed_note.py)
which records a short message with the current time. On my laptop, I run
``sailnote`` in a terminal (I've always got a terminal open!). It grabs the time
immediately and prompts me for a message. This relies on the robot's clock being
roughly in line with my laptop's – but that's a topic for another day.

With this, we can also record when we change something on the boat, or if the
wind conditions suddenly change. The tiny note files are added to our git
repository so all our computers end up with a copy.

## Making an index

The other tool we made is an index of the data files we've gathered. It's a
relatively simple HTML web page:

![index of data files](/images/data_index2.png)

In several ways, this is more convenient than the normal list of files:

- Files from the same run are grouped together, and runs on the same day make
  up a larger group.
- It's easy to see really short runs, where we stopped the system before it did
  anything. The size of the green bar shows the run length for easy scanning.
- Some information about the recorded data, like what message topics rosbag
  recorded, is visible without opening the files.
- You can see the timed notes we recorded during a run, and up to a minute
  before or after.

To get the metadata from rosbag files, you need ROS installed, which can
be a pain, but thanks to some earlier work by Martin, we can conveniently run
the script in a docker container with ROS installed, which is easier to set up.

Would you like to use our data indexing tool? Have we missed a better tool that
already does something like this? At the moment, it's [a script in our robot
repository](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/a9776b5342c6b548a81922bee30015d6c5199243/utilities/index_recorded_data.py), but we could
make it a separate tool you can install.

## Syncthing

![syncthing logo](/images/syncthing-logo.png)

This isn't something we wrote, but it's a nifty tool we use to share the data
between our computers.

Most of our files for the project are shared in a git repository. Git is great
for code and notes, but it's not designed for storing large files. There's a
[large files plugin](https://git-lfs.github.com/), but it's a bit fiddly to use.
And our data is already close to how much you can store in a free Dropbox
account.

[Syncthing](https://syncthing.net/) works a bit like Dropbox, but it syncs files
directly between your computers, rather than storing them on a server in the
cloud. That means the only size limit is your hard drive!

The downside is that your computers have to be online at the same time to
synchronise, but in our case that's not a problem.
