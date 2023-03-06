---
title: blndr
description: a quantized delay with time bending effects
published: true
date: 2021-03-28T16:12:33.348Z
tags: audio fx
editor: markdown
dateCreated: 2021-03-28T16:12:30.550Z
---

## blndr

a quantized delay with time bending effects.

![blndr.png](/community/infinitedigits/blndr.png)

this is `blndr` - my first patch. `blndr` is a quantized delay with optional time bending effects in the stereo field. this would not have been possible without the stellar [softcut tutorial](https://monome.org/docs/norns/softcut/) and inspiration of randomizing speed shifts from [bounds](https://llllllll.co/t/bounds/23336). also i have a lot of inspiration and aspiration to recreate the drums from outkast's ms. jackson.

### Requirements

- audio input
- norns


### Documentation

the line-in audio is fed into a delay loop for a duration of one quarter note, so it automatically becomes quantized to the `bpm` (ENC1). the amount of delay can be dialed in with `level` (ENC2) and `feedback` (K1+ENC2).

the delay loop is randomly time shifted based on the probability from the `spin` parameter (ENC3). the audio from the delay loop is then fed into a second delay loop that is also time shifted and panned randomly.

the K2/K3 are used to quickly speed up/down the bpm to 1/3 intervals to get some cool polyrhythms (good for drums).

the K1+K2 to toggles muting incoming audio.

the K1+K3 will toggle *reverse mode* which is a delay that outputs notes in reverse.

### Download

```
;install https://github.com/schollz/blndr
```
