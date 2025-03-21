---
title: breakthrough
description: 
published: true
date: 2021-04-11T12:23:50.492Z
tags: midi, generative
editor: markdown
dateCreated: 2021-04-11T12:23:46.366Z
---

## screenshots

![breakthrough.png](/community/tomw/breakthrough.png)

![breakthrough2.png](/community/tomw/breakthrough2.png)

## description

breakthrough turns the rebound norns script into the breakout/arkanoid video game. blocks are assigned notes and when they get hit by a ball, those notes play. notes play through the polyperc engine and on midi channel 1.

## install

from maiden type
`;install https://github.com/tomwaters/breakthrough`

## documentation

### controls

#### normal mode
in normal mode, blocks get hit 4 times before the are removed. the root note is also played when a ball hits the top or bottom of the screen (depending on settings).

k2 - add ball
k3 - change current ball
e2 - change current ball direction
e3 - change current ball speed
k1 + k2 - remove current ball
k1 + k3 - toggle game mode

#### game mode
in game mode you move the paddle to try to keep the ball hitting blocks without letting it hit the bottom of the screen. blocks are removed after a single hit and there is only one ball in play. after clearing the screen it resets, the ball gets a little faster and the paddle a little smaller.

e3 - move paddle

### parameters
most of the parameters should be self-explanatory but some might not be....

**octaves**
the number of octaves to spread the blocks over

**wall note orbs**
whether all, none or just the selected ball plays when they hit the top or bottom
brick density: how many blocks are in the wall when it resets

**super orb**
possibility of a ball being a super orb and breaking through all bricks for one pass up and down the screen


## links

- [view on llllllll](https://llllllll.co/t/breakthrough/)
- [view on github](https://github.com/tomwaters/breakthrough)
{.links-list}

