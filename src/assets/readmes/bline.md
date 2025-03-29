![bline](https://github.com/toneburst/bline/blob/main/screenshots/bLINE_Logo_GIF_02.gif)

A parametric acid bassline explorer for Monome Norns.

## Prerequisites:

#### Required

- Original Norns, Norns Shield or Fates

#### Recommended

- MIDI controller with multiple sliders, knobs or encoders for parameter-mapping (optimised for Novation Launch Control XL)
- Hardware or software tb-303 emulator
- MIDI interface or USB cable to connect to the above

tb-303 emulator should apply accent to received MIDI notes with a high velocity value (accent threshold adjustable) and slide to overlapping notes ("mono-legato" mode).

Other synths that have a mono-legato mode and allow velocity to modulate note volume and filter envelope modulation amount and/or cutoff may also produce interesting results. 

## Installation

Install from Maiden

`;install https://github.com/toneburst/bline`

Restart Norns to enable engine.

## Quick-Start:

- E1 : Change parameter page
- E2 : Param 1
- E3 : Param 2
- K2 : Toggle parameter group
- K3 : Currently unassigned

Not all parameters are exposed in the UI display. Mapping Params to MIDI controller recommended!

If you have a [Novation Launch Control XL](https://novationmusic.com/en/launch/launch-control-xl), plug it in, assign it to Norns MIDI device slot 16 and load factory patch 1 on the controller. You'll find all the key parameters mapped for you.

If you have another MIDI controller, I recommend starting by mapping the following parameters:

* X
* Y
* Accent Density
* Accent Length
* Accent Offset
* Slide Density
* Slide Length
* Slide Offset
* Rest Density
* Rest Length
* Rest Offset

See [wiki](https://github.com/toneburst/bline/wiki) for more information.

[![GitHub forks](https://img.shields.io/github/forks/toneburst/bline)](https://github.com/toneburst/bline/network)
[![GitHub issues](https://img.shields.io/github/issues/toneburst/bline)](https://github.com/toneburst/bline/issues)
[![GitHub stars](https://img.shields.io/github/stars/toneburst/bline)](https://github.com/toneburst/bline/stargazers)
[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Ftoneburst%2Fbline)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Ftoneburst%2Fbline)

```txt
                         H
                         |
                   H  H  C--H
                    `.|,'|
                      C  H  H
                      |     |
                 O    N  H  C
                 \\ ,' `.|,'|`.
                   C     C  H  H
                   |     |
                H--C     H
                 ,' `.
          H  H--C  H--C--H
          |     ||    |
    H     C     C     N  H  H
     `. ,' `. ,' `. ,' `.|,'
       C  _  C  H  C     C
       | (_) |   `.|     |
       C     C     C     H
     ,' `. ,' `. ,' `.
    H     C     C     H
          |    ||
          N-----C
          |     |
          H     H

```
