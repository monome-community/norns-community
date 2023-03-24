---
title: lissadron
description: seeding fields forever
published: true
date: 2021-04-14T14:06:19.572Z
tags: synths, midi, generative
editor: markdown
dateCreated: 2021-04-13T08:28:51.444Z
---

## screenshots

![lissadron.png](/community/lfsaw/lissadron/lissadron.png)

<!--![haven_teaser.jpg](/community/lfsaw/haven/haven_teaser.jpg)-->

## description

A software synth for the norns platform making extensive use of seeded randomness.

Concept, sound engine and implementation by [LFSaw](http://lfsaw.de/).  
You might also like [haven](https://llllllll.co/t/haven/21285).

If you like what I do, please also have a look at my [bandcamp page](http://lfsaw.bandcamp.com/).

![lissadron-cover1.jpg](/community/lfsaw/lissadron/lissadron-cover1.jpg)

## install

from maiden type
`;install https://github.com/tai-studio/lissadron`

`Lissadron` contains a dedicated sound engine, so a `reset` might be required. If the reset results in a `supercollider fail`, just reboot the norns and it should be fine. The engine is quite heavy and takes some time for loading. Lissadron uses global clock, which requires [200424](https://llllllll.co/t/norns-update-200424/31644) to run.

## links

- [view on llllllll](https://llllllll.co/t/lissadron)
- [view on github](https://github.com/tai-studio/lissadron)

{.links-list}

## demos

<iframe width="560" height="315" src="https://www.youtube.com/embed/CuHfXGIOZOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Documentation

The underlying synthesis engine is monophonic and consists of four _voices_, each playing in harmonic relation to the base frequency determined by the `note` parameter.

Each voice has a plentytude of parameters that are controlled by the two meta-parameters `x0` and `x1`. Influence of the two meta-parameters on the sound as well as the harmonic structure of the voices are chosen at random. The powerful part of the system lies in the possibility to retrigger the randomisation by providing a different [random seed](https://en.wikipedia.org/wiki/Random_seed). This also makes it possible to save and recall the (seemingly random) state of the system.

The integrated sequencer allows to step through random seedsm, based either on the intenal clock, or an externally provided one. By an integrated euclidean trigger-pattern distributor, a broad variety of rythms can be created.

The norns-native interface is:

```
K2 seed--	-- increase random seed by one
K3 seed++	-- decrease random seed
<shift>-K2 seed - 131
<shift>-K3 seed + 131
E1 amp 		-- legato
E2 x0  		-- meta parameter, different for each seed
E3 x1  		-- meta parameter, different for each seed
<shift>-E1 note 
<shift>-E2 seq_steps
<shift>-E3 seq_freq

K1 <shift>
```

Parameters (controlled e.g. via MIDI mapping) are

- `amp` — if 0dB, plays a continuous sound, otherwise the synth can betriggered either by (MIDI-)notes (first MIDI device) or seed changes
- `note` — midi-note
- `seed` — 14bit value determining the current random seed
- `x0` — meta-parameter (see above)
- `x1` — meta-parameter (see above)
- `lazy` — determines speed of parameter adaptation to a new seed
- `grit` — overall resonance
- `attack` — envelope attack
- `decay` — envelope decay
- `seq_freq` — frequency relative to clock
- `seq_steps` — number of sequencer steps, if 1, then sequencer is turned off
- `seq_fill` — relative density of the euclidean pattern
- `seq_shift` — relative value determining shifting of the euclidean pattern
- `trigOnSeed` — weather or not to trigger the envelope on seed change


## Releases and issues

Here is the [current release](https://github.com/tai-studio/lissadron/tree/master). The dust project manager always points to the git head of the master branch, so you should be save.

For a changelog, see [release page](https://github.com/tai-studio/lissadron/releases). Please file issues in the corresponding github issue tracker (and possibly provide a pull request to fix the issue).
