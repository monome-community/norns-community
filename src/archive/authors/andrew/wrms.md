---
title: wrms
description: dual asynchronous time-wigglers / echo loopers
published: true
date: 2022-06-28T18:11:08.087Z
tags: delays + loopers
editor: markdown
dateCreated: 2021-03-02T16:51:32.668Z
---

# ~ wrms ~~

dual stereo time-wigglers / echo loopers

two time-travel wrms for loops, delays, & everything in-between. a remix of cranes by [`@dan_derks`](/authors/dan_derks).

![screen recording](https://raw.githubusercontent.com/andr-ew/wrms/master/lib/img/wrm.gif)

<iframe width="560" height="315" src="https://www.youtube.com/embed/UTj8voI0-98" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/cNFIVs2eZI0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## requirements

- norns (update 210607 or later)
- audio input

## documentation

### video

(by peter bark)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZRi1mmXgXko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### written

[read here](https://github.com/andr-ew/wrms#documentation)

## changelog

## {.tabset}

### 2.1.0

a small update, mainly for compatibility with orgn v1.1 for use in orgnwrms

**IMPORTant:** users of the previous version will need to delete the script & reinstall in order for the update to function

- FIX: minor performance improvement
   - same deal as the recent orgn update, rewrote the main ui using nest v2. with this change I was able to increase the framerate for the screen, so things look & feel a little smoother compared to before.
   - apologies in advance if the rewrite introduced any new bugs (particularly in the norns UI). just let me know if you notice any differences from the last version & we shall sort it out
- FIX: round on-screen controls to reasonable amounts of decimals. sorry for being slow to fix this one!
- FIX: more reasonable range for the wgl param (easier midi mapping)
- NEW: input routing, left/right only options
- NEW: reset button param
- NEW: wgl dest param. set whether wrm 1, wrm 2, or both are affected by the wgl LFO (historically, wgl affected both wrms)


### 2.0.0

- various timing & click fixes
- **f** page for filter controls (previously available as a mod)
- start & endpoint adjustment for wrm 2 @DuellingAnts (**s** page alt)
- wrm 1 can be a pedal looper (hold **rec** to sleep)
- wrm 2 can be (more of a) delay (increase **e** from 0 when asleep)
- improved share mode (now wrm 2’s buffer control). 
    - wrm 1 now auto-adjusts to the length of wrm 2 when switching, which makes poly looping more accessible
- new share mode wrm 2 -> wrm 1
    - in this share mode wrm 2 loops back the delay material at a different pitch/direction in the style of alliterate
- small delay length abilities @claasp
    - length of wrm 1 can now be adjusted down to .1 milliseconds, just keep turning E2 to the left slowly
    - this is super super fun and there are tons of sweet spots down in the small lengths, especially when combined with ping-pong, feedback filters, octave shifting, and wiggle. you can get into all kinds of pseudo-reverb/chorus, phasor/pitch-shifter/mystery/horrible oscillator territories.
    - I’ve had a lot of fun with it while testing!
- K1-accessible alt page per-screen, with a gaggle of new controls
    - (from docs):
        - **sk:** skew the length of each loop channel in the stereo spectrum. great for stereofying mono sources.
        - **res:** trigger playhead from 0. this is most useful as a mapping destination for crow triggers, which allows for synced delays in a modular context
        - **ph:** set the phase separation of loop playback in the stereo spectrum.
        - **tap:** a tap tempo control for delay or loop lengths
        - **wgrt:** rate of the wgl LFO
        - **tp**: semitone pitch transposition, also useful as a wide-range pitch bend
        - **pan**: sets the _input_ pan for each wrm. K2 on this screen sets the overdub mode for wrm 1 - in the default ping-pong mode, panning a mono source will bring in the the stereo ping-pong effect.
        - **aliasing:** toggling on will disable anti-aliasing for both record heads. the effect is most noticible when recording at lower rates, especially when bent & wiggled.
- crow input mapping (via @21echo’s crowify)
    - I haven’t been able to test this yet, so lemme know how it goes ! !
- wrms/lite template
    - this is a simplified alt template for wrms based on how my partner uses it. might be a nice starting point for new travelers ! selectable from the SELECT menu

### 1.1.0

- fixes
    - visual lag (?)
    - softcut crashes
- reverse rate (k2+k3)
- persistence
- params
    - input mixer
    - param per control for midi mapping
    - file read
    - voice panning
- wrms mods / internal architecture restructure

### 1.0.1
+ auto-generated params from controls
+ session persistence
+ screen lag fixes