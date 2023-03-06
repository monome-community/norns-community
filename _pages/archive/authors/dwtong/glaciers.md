---
title: glaciers
description: Extreme sound stretcher and harmoniser.
published: true
date: 2022-04-17T20:19:08.083Z
tags: audio fx
editor: markdown
dateCreated: 2021-05-29T02:57:41.060Z
---

## description

glaciers is a four voice extreme audio stretcher, based on paulstretch. Take an audio sample or live recording, and stretch it until time almost ceases to exist.

https://vimeo.com/551661371

## Features
* Stretch audio samples to the extreme, until they are almost frozen in time
* Four separate audio buffers that can be manipulated
* Add multi-octave harmonisation
* Create movement and space with panning LFO
* live recording for immediate stretching
* bandpass filter for mixing
* Based on Paulstretch algorithm 


## Requirements

norns

## install

Install through the community catalogue on Maiden (don’t forget to refresh).
Be sure to restart to make sure Glacial Engine is loaded.

## documentation

### navigation
**K1** (hold down) bring up the buffer (contextual) menu
**k2** (press) previous page/buffer action
**k3** (press) next page/buffer action

**e1** change voice
**e2** select parameter
**e3** change parameter value

### buffer - stopped state

![buffer1.png](/community/dwtong/buffer1.png)

**k2** load a file from the norns audio directory
**k3** immediately start recording live input

### buffer - playing state

![buffer2.png](/community/dwtong/buffer2.png)

**k2** clear buffer. stops currently playing file
**k3** immediately start recording live input

### buffer - recording state

![buffer3.png](/community/dwtong/buffer3.png)

**k2** clear buffer. current recording will not be saved
**k3** save recording. new recording will then be stretched. 

*recording is saved in glaciers audio directory.*
*when recording, buffer screen will stay open without having to hold k1.*

### sound

![sound.png](/community/dwtong/sound.png)

*general sound parameters*

**volume** sets the level for the voice.
**stretch** is based on the playback rate. 1x stretch is 1x playback rate.
**harmonic oct** sets the octive for the harmonics. 1 will be one octave above.
**harmonic mix** controls how much of the harmonics vs original sound plays. 0 is all original, 1 is all harmonics.


### pan

![pan.png](/community/dwtong/pan.png)

*move the sound through the stereo field*

**position** sets where the sound is in the stereo field.
**lfo spread** sets how far the sound will be moved by the lfo.
**lfo rate** controls how long it takes the pan lfo to complete a cycle.

### filter

![filter.png](/community/dwtong/filter.png)

*a basic bandpass filter*

**freq** sets the centre frequency.
**width** sets the width of the filter from the centre freq, in octaves.

### global parameters
**gain offset** - offset the gain of all voices by up to +/-12db.

## links

- [view on llllllll](https://llllllll.co/t/glaciers/45117)
- [view on github](https://github.com/dwtong/glaciers)
{.links-list}