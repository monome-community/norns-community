---
title: rangl
description: granular prayer wheels using arc (any number of encoders)
published: true
date: 2021-10-05T06:39:57.098Z
tags: 
editor: markdown
dateCreated: 2021-10-05T06:39:54.389Z
---

# rangl

Arc based granular four track sampler with live recording and friction.

<iframe src="https://player.vimeo.com/video/545457820" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>


Adapted from [ash/angl](https://llllllll.co/t/ash-a-small-collection/21349) after being heavily inspired by @dan_derks to have a poke around scripts (thanks!) and from @infinitedigits and his work on [granchild](https://llllllll.co/t/granchild/41894). rangl is a small arc controlled granular player with four tracks. It is based on angl but adds support for

- adjusting the level of each track,
- live recording of tracks, and
- adding friction to tracks (think spinning prayer wheels).

## Requirements

norns, arc, and the Glut engine (comes with ash).


## Documentation

Press K3 to switch modes. The modes are

**speed:** adjust the speed on the four tracks. Hold K2 and touch arc
to set speed to zero.

**pitch:** adjust pitch on the four tracks. Hold K2 for fine control.

**record:** touch arc to select track. Hold K2 and press K3 to start
recording. Touch another track to end recording or hold K2 and press
K3.

**level:** adjust level of the individual tracks.

**friction:** adjust friction for the individual tracks.


## Download

https://github.com/tgk/rangl

or install from maiden:

```
;install https://github.com/tgk/rangl
```