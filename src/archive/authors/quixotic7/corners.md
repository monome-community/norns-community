---
title: corners
description: a grid controlled physics instrument
published: true
date: 2021-06-23T09:38:15.851Z
tags: synths, grid, midi, generative
editor: markdown
dateCreated: 2021-06-22T07:44:51.373Z
---

**corners** is a grid controlled physics instrument.

![corners.png](/community/quixotic7/corners.png)

using the grid the musician can add gravity wells to the space to manipulate the "puck". velocities, positions, and border crossings are mapped to sound parameters and events.

this script is ported from tehn's original m4l script https://github.com/monome-community/corners

molly the polly is used as an internal synth source and it can also send midi out to use with external gear. 

internal synth params and external cc's can be mapped to the puck's position and velocity. 

https://www.instagram.com/p/CQVIlcOBQRD/

https://www.instagram.com/p/CQY2rOaKitS/

## requirements

* **norns**
* **any sized grid**
* **molly the polly**

## optional

* **external synths** 

## doc

* **key 2** random lead
* **key 3** random perc
* **enc 2** friction
* **enc 3** gravity

* **grid** press and hold a key to create a gravity well to manipulate the puck. notes are triggered while holding keys
* **double click grid edge** toggle a boundary's reflection between bounce or warp

* **params menu** here you can change which notes are played per boundary and map physics properties to control midi cc's or internal synth parameters

## installation

**on maiden:**

```lua
;install https://github.com/Quixotic7/corners.git
;install https://github.com/markwheeler/molly_the_poly.git
```

**on norns:**
system > reset then launch corners

## version notes
**v1.1.4**
- Added the ability to generate random notes within a scale and octave range. Key shortcuts added to quickly generate new notes. Can also generate random notes every boundary crossing. 
- Fixed bug with the key forces being uneven. 

**v1.1.3**
- added separate physics update that is synced to the clock. you can change the sync rate in the params menu. 
- walls now light up when the puck reflects

**v1.1.2**

- updated params to make it easier to change sound sources for boundary events and key events. 
- added fix to prevent stuck notes if changing sound settings. 

**v1.1.1**
- initial release

## links
- [view on llllllll](https://llllllll.co/t/46227)
- [view on github](https://github.com/Quixotic7/corners)
{.links-list}