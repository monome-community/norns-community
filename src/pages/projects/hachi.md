---
layout: project
title: hachi
permalink: /hachi
cover: hachi.png
raw_name: hachi
sanitized_name: hachi
project_url: https://github.com/pangrus/hachi
description: euclidean drum machine emulating the TR-808 sound
discussion_url: https://llllllll.co/t/35947
documentation_url: https://norns.community/authors/pangrus/hachi
tags:
 - drum
authors:
 - pangrus
redirect_from:
 - /en/authors/pangrus/hachi
 - /authors/pangrus/hachi
---
# hachi

Euclidean drum machine emulating the TR-808 sound.  
I’ve written this script to learn Lua, SuperCollider and the norns environment.  
The sound engine is based on the SC808 by [Yoshinosuke Horiuchi](https://www.patreon.com/4H).  
I have implemented only my favorite sounds, to keep the GUI in a single norns page.
The sequencer borrows some techniques from *playfair* euclidean drummer written by [@tehn](https://github.com/tehn) with new features (randomizer, real time recording).

![hachi](https://raw.githubusercontent.com/pangrus/hachi/HEAD/hachi.png)

## how to use hachi
k1 shift  
k1+k3 clear all (if stopped)  
k1+k3 randomize (if started)  
k2 start/stop  
k3 insert step (if started)  
k3 randomize all (if stopped)  
e1 instrument select  
e2 drum parameter 1  
e3 drum parameter 2  
e1+k1 rotate pattern  
e2+k1 number of pulses  
e3+k1 number of steps  




