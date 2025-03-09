---
title: bitters
description: lo-fi FM-capable mono/poly
published: true
date: 2022-10-24T23:23:33.472Z
tags: synths, midi
editor: markdown
dateCreated: 2022-04-06T03:39:04.895Z
---

# bitters
Norns port of Max4Live projects bitters and onebit. I wanted to try my hand at learning a little SuperCollider, and this seemed like a great excuse. I implemented a “polynomial transition region” oscillator UGen; the pulse wave is essentially due to Peter McCulloch; I did the asymmetric triangle wave. Like the original, bitters is inspired by chiptune sounds, but doesn’t attempt to emulate anything out there. The architecture is as follows: each oscillator has an FM pair to modulate it a little like Just Friends or W/Synth. The oscillators are mixed and optionally degraded before reaching the filter, which is highpass-into-lowpass like the MS-20. The polyphony code is cribbed from @infinitedigits’s mx.synths, and I added @tehn’s halfsecond softcut delay from Awake.

## Documentation

Requires a SuperCollider restart after first running the script: the script checks to see whether my UGens, TrianglePTR and PulsePTR are installed and installs them if not. SuperCollider needs a restart in order to find these UGens.

E1, K2 and K3 scroll pages,
E2 scrolls page parameters
E3 edits parameter