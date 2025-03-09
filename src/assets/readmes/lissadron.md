# lissadron

*seeding fields forever*

![](media/lissadron-cover2.jpg)

A software synth for the [norns](https://monome.org/docs/norns/) platform. 


The undelying synthesis engine has four voices, each playing in a harmonic relation to the base frequency determined by the `note`.
Each voice has a plentytude of parameters that are controlled by the two meta-parameters `x0` and `x1`. Influence of the two meta-parameters on the sound as well as the harmonic structure of the voices are chosen at random. The powerful part of the system lies in the possibility to retrigger the randomisation by providing a different [random seed](https://en.wikipedia.org/wiki/Random_seed). This also makes it possible to save and recall the (seemingly random) state of the system.
The integrated sequencer allows to step through random seedsm, based either on the intenal clock, or an externally provided one. By an integrated euclidean trigger-pattern distributor, a broad variety of rythms can be created.

The norns-native interface is

```sh
K2 seed--   -- increase random seed by one
K3 seed++   -- decrease random seed
<shift>-K2 seed - 131
<shift>-K3 seed + 131
E1 amp      -- legato
E2 x0       -- meta parameter, different for each seed
E3 x1       -- meta parameter, different for each seed
<shift>-E1 note 
<shift>-E2 seq_steps
<shift>-E3 seq_freq

K1 <shift>
```

Parameters (controlled e.g. via MIDI mapping) are 

+ `amp` — if 0dB, plays a continuous sound, otherwise the synth can betriggered either by (MIDI-)notes (first MIDI device) or seed changes
+ `note` — midi-note
+ `seed` — 14bit value determining the current random seed
+ `x0` — meta-parameter (see above)
+ `x1` — meta-parameter (see above)
+ `lazy` — determines speed of parameter adaptation to a new seed 
+ `attack` — envelope attack
+ `decay` — envelope decay
+ `seq_freq` — frequency relative to clock
+ `seq_steps` — number of sequencer steps, if 1, then sequencer is turned off
+ `seq_fill` — relative density of the euclidean pattern
+ `seq_shift` — relative value determining shifting of the euclidean pattern
+ `trigOnSeed` — weather or not to trigger the envelope on seed change


-----

Sound engine by [LFSaw](http://lfsaw.de) ([Till Bovermann](http://tai-studio.org)). 

Changelog on [release-page](https://github.com/tai-studio/lissadron/releases)
Discussion at [lines](https://llllllll.co/t/lissadron/)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S72858T)

![](media/lissadron-cover2.jpg)
