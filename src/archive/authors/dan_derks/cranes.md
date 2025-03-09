---
title: cranes
description: stereo varispeed looper / delay / timeline-smoosher
published: true
date: 2021-04-09T12:09:33.703Z
tags: grid, delays + loopers
editor: markdown
dateCreated: 2021-04-08T18:58:04.902Z
---

![cranes.png](/community/dan_derks/cranes.png)

stereo varispeed looper / delay / timeline-smoosher

this version of cranes builds on the "one buffer, two voices" approach of its predecessor in pursuit of a more flexible on-the-fly-sampling instrument. though the paper crane (initial record) allows original behavior, the pair of birds (overwrite) allows the artist to specify a buffer -- in combination with the 1/10th second adjustable loop points, this brings new performative options to the table.

## Requirements

- norns
- (128 vari-bright grid optional, but v fun)


## Documentation

### start

connect norns to a stereo signal + head over to the `parameters`
- when the buffer is completely cleared (at startup and after **KEY 3 + KEY 1** are held), cranes will record incoming audio at 1x speed into *both voices* and will immediately play back at the rates specified in the params page.
- left input will write to voice 1, right input will write to voice 2.
- for the most immediate fun, set `speed voice 1` to `0.5` and `speed voice 2` to `-1`

### record + loop
tap **KEY 2** to record into the buffers as you make some sounds
- to loop, tap **KEY 2** again. this sets the loop points (`s1/e1` and `s2/e2`) to the length of the recording.
- with the recommend settings, you should hear your material played at half-speed on the left and reversed on the right.
- with the recommended settings, you should see the `one / two` counters counting in the same direction and at the same speed as your audio.
  
### adjust loop points
hold **KEY 1** until you see `s1` and `e1` change to `s2` and `e2`. this switches which voice you want to control with the buttons and encoders
- use **ENC 2** and **ENC 3** to adjust the start and end points of the selected voice's loop points, with 0.1s resolution. you should see the counter for the voice lock to the new `s`tart and `e`nd points.
  
### overdub
tap **KEY 2** to toggle overdub / overwrite for the selected voice. you will see some friendly birds flying alongside your loop when overdub / overwrite is engaged.
- nb: to retain continuous audio, overdub / overwrite write to the selected voice at the rate specified in the params page.
- use **ENC 1** to crawl the spectrum of overdub / overwrite. `over: 0` is full overdub, adding incoming audio to the pre-existing audio in the selected voice. `over: 1` is full overwrite, replacing pre-existing audio in the selected buffer with incoming audio.

### fun things

- adjust `s`tart and `e`nd points past the existing audio and write into a new section of the selected voice, then slowly re-introduce the prior section.
- tap **KEY 3** to perform a speed bump on voice 1. hold **KEY 3** to produce a more dramatic change. **KEY 3**'s influence is selectable in the params, under `KEY3`. `~~` is a small pitch deviation, `0.5` is half-speed, etc.
- hold **KEY3 + KEY 1** to completely erase all audio content.
  - if you hit **KEY 2** again after this, you'll get back to the paper crane.

### grid

plug in a grid and re-boot cranes

use the following legend:

![](https://llllllll.co/uploads/default/original/3X/e/b/eb0fb77835e0a1fafc7afcaa85569408a03fcebf.jpeg)

- *speed + direction*: -4x to 4x, 0 in the middle (unlit) functions as 'pause'
- *sync playhead to other*: sync the voice's playhead to the location of the other's
- *re-size loop to other*: dynamically adjusts the voice's current loop points to the other's
- *reset playhead to start*: trigger voice to playback from currently defined start point
- *create snapshot*: collect speed + direction, playhead position, start and end points and assign it to a button on the far left (similar to `less concepts`)
- *erase all*: erase all of the voice's snapshots (similar to `less concepts`)
- *snapshot recall*: recall a saved snapshot's parameters
- *start point adjustment* + *end point adjustment*: add or subtract time from the voice's start and end points, in 0.01 second or 0.1 second increments
- *window adjustment*: adjust voice's loop window by 0.01 second increments or by the distance between the start and end points
{.grid-list}