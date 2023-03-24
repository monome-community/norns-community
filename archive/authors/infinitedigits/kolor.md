---
title: kolor
description: drum sample sequencer
published: true
date: 2021-04-08T19:19:24.612Z
tags: sequencers, grid, drums
editor: markdown
dateCreated: 2021-03-28T18:17:31.602Z
---

## כל אור
every light sequences samples.

![kolor.png](/community/infinitedigits/kolor.png)

the words "כל אור" translate from Hebrew to English as "every light" and is pronounced "kol-or". its meant to portray my attempt of using every light to sequence samples with [the grid](https://monome.org/docs/grid/).


this script is born out an exploration of sampler sequencers. i drew inspiration from the op-z and model:samples (though i don't own these i was inspired by how i think they are supposed to work). i had five goals making this sample sequencer:

1. kolor will work as a standalone script *and* import as a library into most non-grid norns script, meaning **you can use kolor from within another script (if you have a grid)**. i've made [a](https://github.com/schollz/oooooo) [lot](https://github.com/schollz/downtown) [of](https://github.com/schollz/barcode) [scripts](https://github.com/schollz/glitchlets) and i want to plug in a grid and use it immediately as a "groove box" in addition to the original host script. to meet this goal, the norns screen actually doesn't provide any information for kolor (except for providing the save/load screen in the parameters). currently [you can get this branch of *oooooo*](https://github.com/schollz/oooooo/tree/kolor) to use with kolor. i plan to add to other scripts as well
2. **step-specific parameter locks with lots of *mods*** - volume, pitch, filters, sample positions, probability, etc. each *mod* has its own lfo. and an lfo for the lfo's, because why not.
3. **easy pattern chaining and probabilistic chaining** for automatically adding variation (markov chaining).
4. **as little menu-diving as possible**, with very few "hold" buttons or "mode" screens. (have to do my best given 128 white lights...)
5. **stereo samples**! because uncorrelated noise in both ears sounds awesome.

at the end i had to make compromises to reach these goals. the compromises mean that there is a list of things that *kolor* does not do (...yet, but maybe not at all):

1. all the steps in one track must have the same sound. (this is not a technical limitation, but a menu-diving limitation as it would be hard to determine which step has which sound).
2. mod parameters are limited to 4-bit resolution, because there are only 15 keys devoted to the selection scale. however, *if you use a lfo* the values will oscillate with supercollider's bit-depth (32-bit resolution i believe). there may be ways of getting around the 4-bit with some menu diving or more button pushing.

i'm totally open to ideas to remove these limitations or improve in general.

## demos

all drums in these samples provided by kolor. (these demos show the kolor script behavior, since i don't have grid to actually use the grid part...yet).

demo1 (using grid, and sequencing the plinky synth with tmi at the same time):

https://vimeo.com/510535132

demo2 (5/4 tempo cover of weird fishes, no grid here but kolor still works fine):

https://vimeo.com/500923599

## requirements

- norns
- grid (optional, but recommended). [64-grid is supported](https://schollz.github.io/kolor/#25)

## documentation

please see [schollz.github.io/kolor](https://schollz.github.io/kolor/).

### download

get from maiden or from the latest norns image just do

```bash
;install https://github.com/schollz/kolor
```

https://github.com/schollz/kolor