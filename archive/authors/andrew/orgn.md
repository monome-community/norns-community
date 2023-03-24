---
title: orgn
description:  3-operator FM synth + fx for norns 
published: true
date: 2022-06-28T18:10:20.153Z
tags: audio fx, synths, grid
editor: markdown
dateCreated: 2021-12-01T02:13:19.511Z
---

![orgn logo](https://github.com/andr-ew/orgn/blob/master/lib/doc/logo-01.png?raw=true) 

<p align="center">
  <img src="https://github.com/andr-ew/orgn/blob/master/lib/doc/screen_cap.gif?raw=true" alt="orgn screen animated gif"/>
</p>
<br>

# orgn

a 3-operator FM synth with fx. inspired by yamaha portasound keyboards

## requirements

- norns (210927 or later)
- grid (any size) or midi keyboard
- audio input (optional)
- midi mapping encouraged


## documentation

### video overview

<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ug39z2mZhsQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>

### written

[read here](https://github.com/andr-ew/orgn#documentation)

## changelog

## {.tabset}

### 1.1.0

this update is focused on performance + maintainability. no new features, but there are a few bug fixes sprinkled in.

**IMPORTant:** users of the previous version will need to delete the script & reinstall in order for the update to function

**IMPORTant:** includes engine changes. please SYSTEM > RESET after updating

- FIX: performance issues
    - a lot of people brought up timing issues with note input & pattern playback on the grid. there was some similar lag going on with the encoders + on-screen UI. this update fixes all of that! things are butter-smooth as they should be
    - the deets: I narrowed down all these issues to one file: the core code that runs my UI library, nest_. the current version is kind of a mess & I’m not surprised that it’s slowing things down. luckily, I have a rewrite/redesign in the works, & so far it’s running great !
- engine rewrite
    - I didn’t test things super in-depth so it’s hard to say whether the engine code was contributing to performance issues. but I knew that my solution to multi-phonic voice architecture was creating more resources than necessary, and I wasn’t using those features in this app (my plans for using this feature kinda got cancelled as soon as I bought a crow). so, for posterity + future maintainability I decided to simplify the engine code, using PolySub as a mold
- FIX: voices being freed prematurely with certain span settings. much much better percussive sounds now (!)
- FIX: clamp crinkle to a logical, not crashing range
- FIX: add polyphony limit (16 voices) + voice stealing
- FIX: encoder pattern recording drift
- FIX: lack of ascii art
- DIFFERENT: envelopes are non-retriggering in mono mode
- DIFFERENT: hold K1 to enter scale editor (holding a scale key to enter this screen no longer works)


