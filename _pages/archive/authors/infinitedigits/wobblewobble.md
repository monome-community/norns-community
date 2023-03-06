---
title: wobblewobble
description: many lfos for crow outputs
published: true
date: 2021-12-04T10:03:05.632Z
tags: crow, utilities, midi
editor: markdown
dateCreated: 2021-05-16T14:03:09.360Z
---

# wobblewobble

slow oscillators for crow outputs.

![wobblewobble.png](/community/infinitedigits/wobblewobble.png)

assign each of the four crow outputs one of many different types of slowly oscillating modulation sources. oscillators are configured in SuperCollider making it easy to configure / design / add new oscillators, including complex ones from the [chaotic UGens](https://doc.sccode.org/Browse.html#UGens%3EGenerators%3EChaotic). current oscillators:

- sine
- triangle
- wobbly sine
- snek
- lorenzian
- henonian
- random walk

each output can also be configured to respond to midi input, either modulating the voltage level via pitch (any note, or top note), or modulating the voltage level from an envelope.

## Requirements

- norns
- crow

## Documentation

- hold K1 to switch crow
- K2/K3 switch modulator
- E1 changes frequency
- E2 changes lfo min
- E3 changes lfo max

via the parameters menu, "`WOBBLE`", you can also...

- clamp the minimum and maximum values of the lfo
- add midi input to control pitch (top note, any note) or add an envelope

## download

```
;install https://github.com/schollz/wobblewobble
```

## links

- [view on llllllll](https://llllllll.co/t/wobblewobble/45215)
- [view on github](https://github.com/schollz/wobblewobble)
{.links-list}

## demo

<iframe title="vimeo-player" src="https://player.vimeo.com/video/553165797?h=1cb093a4be" width="640" height="360" frameborder="0" allowfullscreen></iframe>

