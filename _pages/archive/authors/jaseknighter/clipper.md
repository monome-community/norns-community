---
title: clipper
description: slice and save samples for monome norns
published: true
date: 2021-12-05T18:53:37.960Z
tags: samplers
editor: markdown
dateCreated: 2021-07-27T00:59:20.395Z
---

slice and save samples for monome norns

![clipper.png](/community/jaseknighter/clipper.png)


this is a utility library, similar to @Justmat's [sam](https://llllllll.co/t/sam/23943) with some performative features. it was built to help me learn softcut and also make it easier to cut up samples for scripts that utilize samples (cheatcodes, goldeneye, etc.) 


### Requirements

norns


### key/encoder controls
access instructions for key/encoder controls within the script by pressing k1+e3

* All screens
  * e2: next/prev control
* Screen 1: select/play sample 
  * k2: select sample to slice up
  * e3: incr/decr playhead
  * k3: start/stop playhead
* Screen 2: play mode
  * k2/k3: delete/add cutter
  * e3: change play mode
* Screen 3: adjust cut ends
  * k2/k3: delete/add cutter
  * k1 + e2: select cutter
  * k1 + e3: adjust cutter
  * k1 + e1: fine adjust cutter
  * e3: select cutter end
* Screen 4: move cutter
  * k2/k3: delete/add cutter
  * k1 + e2: select cutter
  * k1 + e3: adjust cutter
  * k1 + e1: fine adjust cutter
* Screen 5: adjust rate
  * k2/k3: delete/add cutter
  * k1 + e2: select rate
  * e3: adjust all cutter rates
  * k1 + e1: fine adjust rate
  * k1 + e3: adjust selected cutter rate
* Screen 6: adjust level
  * k2/k3: delete/add cutter
  * e3: adjust level
* Screen 7: autogenerate cutters
  * e3: set # of clips to autogenerate (up to 20)

### recording clips
clips may be recorded from the PARAMETERS>EDIT menu. what gets recorded depends on the `play mode` setting:
* *stop*: record the entire sample 
* *full loop*: record the entire sample 
* *all cuts*: record all sample areas set by cutters
* *sel cut*: record the sample area set by the selected cutter

*important note*: if *play mode* is set to `all cuts`, all *rate* settings must either be positive or negative. 

### Installation from maiden

`;install https://github.com/jaseknighter/clipper`

[GitHub  link](https://github.com/jaseknighter/clipper)

### todo
fix bugs and improve usability (e.g. when cutting up a sample into > 15 pieces)

### credits
many thanks to @infinitedigits and @zebra for coding advice!
