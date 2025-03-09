---
title: strides
description: a set of pattern recorders and a sample player
published: true
date: 2021-08-20T17:41:17.373Z
tags: 
editor: markdown
dateCreated: 2021-08-20T17:07:45.597Z
---


# strides v1.4

---

strides is a collection of 16 pattern recorders.

8 are norns focused, expressed as encoder recorders sending midi cc's.

<iframe src="https://player.vimeo.com/video/589948831" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

8 are grid focused, allowing for finger drum style recording and looping (with optional midi note out).

<iframe src="https://player.vimeo.com/video/589948824" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>


---

## norns

load samples, set midi notes and cc destinations in the PARAMETERS menu.


there are two operating modes in strides, **grid** and **encoder**.
to switch modes, hold **key1** and press **key3**.


#### grid mode controls

- enc1 - volume
- enc2 - delay time
- enc3 - delay feedback
- key1 = hold to access secondary encoder/ key functions
	* enc1 = distortion amount
	* enc2 = delay level
	* enc3 = delay send
- key2 = half time
- key3 = double time

nb: delay send works on all samples and tracks. if you wish to send individual samples to delay, you can do so via the PARAMETERS menu.

#### encoder mode controls

- key2 = arm record
- key3 = start/ stop pattern
- enc1 = select active pattern
- enc2 = turn to begin recording (if armed) and/or set cc value

nb: set your cc destinations and midi output channels in the PARAMETERS menu.

---

## grid

![strides-grid1.png](/community/justmat/strides/strides-grid1.png)

hold alt to access secondary grid functions.

- a - track selection
- b - arm record
- c - start/stop selected track
- d - alt
	* a - track stop
	* b - clear all patterns
	* c - stop all tracks
- e - sample pads



nb: as of v1.2 a midi panic/ kill button was added just above alt. hold alt to expose.

as well as secondary controls, holding alt will bring up several controls for pattern and playback speed manipulation.

![strides-grid2.png](/community/justmat/strides/strides-grid2.png)

- f - toggle pattern linearization
- g - double sample playback speed
- h - half pattern speed
- i - double pattern speed
- j - half sample playback speed
- k - restore pattern speed to original or linearized if selected
- l - restore all sample playback speed to original
