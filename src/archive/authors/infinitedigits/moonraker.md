---
title: moonraker
description: explore a galaxy of rhythm.
published: true
date: 2022-01-12T21:23:47.177Z
tags: grid, drums
editor: markdown
dateCreated: 2022-01-12T21:23:44.613Z
---

# MOONRAKER

explore a galaxy of rhythm.

![moonraker.png](/community/infinitedigits/moonraker.png)


this is a deviation/fork/sequel/derivation of [goldeneye](https://llllllll.co/t/46556) (thank you @tyleretters for your illustrious goldeneye script and providing the most perfect of names for this script!). 

rhythms are generated using random selections of drum samples with stochastic patterns that emerge from modulo math and also continually evolve through periodic mutations.



## Requirements

- norns
- grid (optional)
- at least 200 MB of disk space (for downloaded samples)

## Documentation


***quick start***

press K3 to start. press K2 to regenerate beat. 

save beats with K1+K3 and return to them with K1+K2.



https://vimeo.com/665254703

***the user manual***

- E1 removes/adds instruments
- E2 changes filter
- E3 mutes banks
- **K2 regenerates samples** (the only one you really need)
- K3 starts/stops
- K1+E1 changes slot
- K1+K2 loads in slot
- K1+K3 saves in slot

turn the `PARAMS > mutation rate` to `0` if you want to completely freeze the pattern. otherwise patterns will continuously change...forever.


***the technical manual***

moonraker has eight banks (kick, snare, rim, hat, ride, shaker, perc, risers) each containing 112 samples, for 896 samples in total. each sample is initiated with random characteristics (lpf cutoff, hpf cutoff, attack, decay, sample start, pan, amplitude, delay send, reverb send). upon regeneration, samples are randomly activated (or activated with E1).

during playback, each beat is counted and a modulus is computed against each active sample. each sample contains modulus numbers and inverse modulus numbers. an active sample is *played* when any modulus number computed against the current beat has no remainder. however, the inverse modulus do the opposite - whenever their computed modulus has no remainder then the playing of the current active sample is reversed. the randomly assigned modulo numbers are all prime numbers (with exception for two numbers: *1* and *4*). modulo numbers are randomly changed at a rate corresponding to the `PARAMS > mutation rate`.

## todo

- explain the grid interface (its heavily complicated unfortunately). I will make a video tutorial. in the meantime just use K2 :boom: 

## Install

install using with

```
;install https://github.com/schollz/moonraker
```

after installing, make sure you install the samples with this command in maiden:

```
os.execute("cd ~/dust/audio && echo 'downloading...' && wget -q https://github.com/schollz/moonraker/releases/download/samplepack1/moonraker.zip && unzip moonraker.zip && rm moonraker.zip; echo 'ready (make sure to restart)'")
```