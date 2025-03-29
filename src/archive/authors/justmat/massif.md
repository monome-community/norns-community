---
title: massif
description: 8 band resonator
published: true
date: 2021-04-04T22:22:56.310Z
tags: audio fx
editor: markdown
dateCreated: 2021-04-03T14:12:34.182Z
---

a resonator with 8 peaks

![massif.png](/community/justmat/massif.png)

![massif-dict.png](/community/justmat/massif-dict.png)

----------

massif is a simple wrapper around the [dynklank](https://doc.sccode.org/Classes/DynKlank.html) supercollider ugen. massif works best when utilizing an external controller, though it is not required.

## control

* key 1 = alt

### play

* key 2 = tunes all peaks to random notes of your selected scale, based on the pitch at the left input

*nb: set your scale selection in the parameters menu*

----------

hold alt and press key 3 to enter **edit** mode. 

### edit

* key 2 = tune current peak to the pitch at the left input
* key 3 = hold and play a midi note to tune current peak to the midi note

* alt + encoder 1 = peak select 1 - 8
* encoder 1 = frequency
* encoder 2 = amplitude (be careful with this one, it can get loud)
* encoder 3 = ring time/decay time

## demo

<iframe src="https://player.vimeo.com/video/532952102?title=0&amp;byline=0&amp;portrait=0&amp;speed=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="720" height="406" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="massif"></iframe>

## installation
available in maiden via the ``install`` command.
``;install https://github.com/justmat/massif``
