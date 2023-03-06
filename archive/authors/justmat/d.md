---
title: d
description: d is for distortion, decimation, and destruction... or whatever
published: true
date: 2022-07-02T20:45:11.950Z
tags: audio fx, midi
editor: markdown
dateCreated: 2022-06-26T13:59:09.557Z
---

<div style="padding:65% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/724190253?h=d9b7eeeafa&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="d"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


**d** is for distortion, decimation, and destruction... or whatever

## quick start
* put nice sound in
* twist encoders until it sounds awful, or awesome


## what's happening?

**d** is made up of two parts: an engine providing bit crushing and sample rate reduction as well as tape style distortion/saturation, and a randomized control matrix.

![d.png](/community/justmat/ddd/d.png)

the main screen is a lot to take in at first, but is pretty simple once you're in the know. size and brightness of screen elements reflect the state of the engine. the elements are:
* sr - sample rate
* bd - bit depth
* sat - saturation/distortion
* co - crossover freqency
* hb - highbias
* lb - lowbias
* hs - tape hiss

turn **encoders 1/2/3** to change the engine parameters in varying amounts, according to the control matrix.

### the matrix

![matrix-m.png](/community/justmat/ddd/matrix-m.png)

each time you launch **d** the control matrix is randomized, so **encoders 1/2/3** won't always react the same way. this adds lots of variation in the sounds produced and leads one to find **sweetspots**. learn how to save and recall **sweetspots** below.

in addition to the encoders and matrix, you can perform some special actions using the norns keys.

### nice numbers

![command-m.png](/community/justmat/ddd/command-m.png)

pressing and holding **key1** enters command mode. use **keys 2/3** to input numbers. releasing **key1** will input the command.

note, the first two numbers are the same for related commands:

(22 - reset)
* 2222 - reset decimator
* 2223 - reset distortion
* 2232 - reset/re-roll control matrix
* 2233 - reset/clear sweetspots

(23 - set sweetspots)
* 2322 - set sweetspot 1
* 2323 - set sweetspot 2
  * recall **sweetspots 1/2** with **key 2/3**

(33 - change screen view)
* 3322 - main/home screen
* 3323 - show engine parameter values
* 3332 - show the control matrix

