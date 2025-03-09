---
layout: project
title: rangl
permalink: /rangl
cover: rangl.png
raw_name: rangl
sanitized_name: rangl
project_url: https://github.com/tgk/rangl
description: arc based granular four track sampler with live recording and friction.
discussion_url: https://llllllll.co/t/rangl/44673
documentation_url: 
tags:
 - sampler
 - granulator
 - arc
authors:
 - tgk
redirect_from:
 - /en/authors/tgk/rangl
 - /authors/tgk/rangl
---
## rangl

https://vimeo.com/545457820

rangl is based on [angl](https://github.com/tehn/ash) but adds

- instant recording functionality heavily inspired by
  [granchild](https://llllllll.co/t/granchild/41894), and
- the concept of friction.

### Requirements

- norns
- arc
- the Glut engine (comes with [ash](https://github.com/tehn/ash))

### Documentation

Press K3 to switch modes. The modes are

**speed:** adjust the speed on the four tracks. Hold K2 and touch arc
to set speed to zero.

**pitch:** adjust pitch on the four tracks. Hold K2 for fine control.

**record:** touch arc to select track. Hold K2 and press K3 to start
recording. Touch another track to end recording or hold K2 and press
K3.

**level:** adjust level of the individual tracks.

**friction:** adjust friction for the individual tracks.

### Install

https://github.com/tgk/rangl

from maiden:

```
;install https://github.com/tgk/rangl
```
