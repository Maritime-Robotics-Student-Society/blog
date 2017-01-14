---
author: simsoton
comments: true
date: 2016-10-11 15:58:18+00:00
layout: post
link: https://sailrobot.wordpress.com/2016/10/11/friday-obstacle-avoidance/
slug: friday-obstacle-avoidance
title: Friday - Obstacle Avoidance
wordpress_id: 782
categories:
- Sailing Robot Team
---

Final challenge of the competition - make runs up and down a rectangular pathway in the water. At the third or fourth run, orange buoys will be placed in the middle, and across the entire width, of the path. The boat must then recognise and sail round the buoys, then back in the path’s area, and complete the run to finish. Also the standings so far are.... we are joint second!

[caption id="attachment_838" align="alignnone" width="4032"]![20160909_100752.jpg](https://sailrobot.files.wordpress.com/2016/10/20160909_100752.jpg) Slightly confusing I know, but take our word for it. Plus you know our final score anyway[/caption]

We started off the day with solving why our boat was going off in weird directions. We figured that this happened because we had removed our heeling compensation, since it never was seemingly effective during boat calibration. Thomas focused on the faulty compensation, while Sophia and Sebastien got on the rib with the boat to record some images of the buoys. We stuck a GoPro on the Black Python's nose to do this. The great outdoors proved too bright for the camera though. A little brainstrorming later, we came to our ingenious solution:

[caption id="attachment_772" align="alignnone" width="2448"]![img_20160909_154507](https://sailrobot.files.wordpress.com/2016/10/img_20160909_154507.jpg) Radical.[/caption]

Turns out our heeling compensation works swimmingly. In fact we could have used it since Day One. It never was faulty during calibration at all. Oh well.

Go time. It sailed in the wrong direction at first again (we still do not know why it does that). But once it got back on track, the Black Python performed amazingly. In fact it was so amazing, the obstacle-bringers had trouble bringing the obstacles onto the course in time before it already began its third run. We excitedly watched the dashboard as the Black Python sailed closer and closer to the buoys. Finally it detected them, and we broke into cheer. Then it bumped into the obstacles, and got run over by a rib that was towing the buoys. One of the shrouts broke. We returned to land.

Post analysis of our run showed that the Black Python had no chance in avoiding the buoys, since they were placed outside the set obstacle zone (which we then programmed into the RPi as well). On the other hand it still probably would have hit the buoys anyway since the detection was quite late, and it was going the quickest ever this whole week.
