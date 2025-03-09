Stjörnuíþrótt<sup>[1](#_1)</sup>
---

Drone synth for [Norns](https://monome.org/norns)/[Fates](https://llllllll.co/t/fates-a-diy-norns-dac-board-for-raspberry-pi/22999) heavily inspired Moffeenzeef [Stargazer](https://www.moffenzeefmodular.com/stargazer). Much appreciation goes to [Moffeenzeef](https://www.moffenzeefmodular.com/) for creating the Stargazer and [kergener](https://sccode.org/kergener) for their [SCgazer](https://sccode.org/1-5db) Supercollider engine which serves as the backbone for this Norns version.

Follow development progress at [https://llllllll.co/t/33889](https://llllllll.co/t/stjornuithrott-stargazer-inspired-drone-synth/33889).

![Stjörnuíþrótt UI](.assets/stjoernuithrott.gif)

The hardware Stargazer has some impressive drone capabilities, which are emulated here:

- dual wavetable oscillator with 90 arbitrary waveforms
- sub-octave, detune, volume for second oscillator 
- 2 resonant filters
- sample rate reduction
- bit rate reduction
- 3 wavetable LFOs
- CMOS distortion with 100x gain 


## Demo

Here’s brief (albeit limited exposé of all the sonic possibilities available) [demo](https://www.youtube.com/watch?v=iaO3x2EGuU0) highlighting how it can be used with and without an external controller.


## Requirements

[Norns](https://monome.org/norns) or [Fates](https://llllllll.co/t/fates-a-diy-norns-dac-board-for-raspberry-pi/22999) or device. For Fates owners, the pitch value can be persistently controlled using the 4th encoder, for Norns owners it's `E2` the first page `P0`


## Install/Update

Stjörnuíþrótt can be installed via [Maiden's](https://norns.local/maiden) project manager.

**After install or update `RESET` or `SLEEP` is required, because Stjörnuíþrótt installs a new engine.**


## Params

The params for Stjörnuíþrótt are vast. As with the original Stargazer knob twiddling and experimentation are encouraged. However, here's a table of all the controls and their values (also listed within the params menu).

| Page    | Controller                    | Description                               | Values                         |
| ------- | ----------------------------- | ----------------------------------------- | ------------------------------ |
| All     | E1                            | Change page                               |                                | 
| All     | K2                            | Toogle sub-octave 2nd oscillator          | On or Off                      |
| All     | K3                            | Randomize parameters                      |                                |
| **0**   | **E2** or **E4**<br />**Midi Note**     | **Pitch**                       | **16.35 – 1046.5 Hz**          |
| 0       | E3                            | Detune parameter of the 2nd oscillator    | 0 – 100% (relative to pitch)   |
| **1**   | **E2**<br />**Midi Velocity** | **Volume**                                | **0.0 - 1.0**                  |
| 1       | E3                            | Gain stage for CMOS distortion            | -1 is clean, 1 is dirty        |
| 2       | E2                            | Waveform selector                         | 0 – 89                         |
| 2       | E3                            | Mix for 2nd oscillator.                   | Only osc. 1, both osc., Only osc. 2 |
| 3       | E2                            | Cutoff frequency for the 1st filter       | 1 – 1320 Hz                    |
| 3       | E3                            | Cutoff frequency for the 2nd filter       | 1 – 1320 Hz                    |
| 4       | E2                            | LFO of 1st filter                         | Sine, Tri(angle), Saw, Pulse   |
| 4       | E3                            | Rate of 1st LFO                           | 0.05 – 100.0                   |
| *5*     | *E2*                          | *LFO of 1st filter*                       | *Sine, Tri(angle), Saw, Pulse* |
| 5       | E3                            | Res of 1st LFO                            | 0.0 – 1.0                      |
| *6*     | *E2*                          | *LFO of 1st filter*                       | *Sine, Tri(angle), Saw, Pulse* |
| 6       | E3                            | Depth of 1st LFO                          | 1 none, 0 max                  | 
| 7       | E2                            | LFO of 2nd filter                         | Sine, Tri(angle), Saw, Pulse   |
| 7       | E3                            | Rate of 2nd LFO                           | 0.05 – 100.0                   |
| *8*     | *E2*                          | *LFO of 2nd filter*                       | *Sine, Tri(angle), Saw, Pulse* |
| 8       | E3                            | Res of 2nd LFO                            | 0.0 – 1.0                      |
| *9*     | *E2*                          | *LFO of 2nd filter*                       | *Sine, Tri(angle), Saw, Pulse* |
| 9       | E3                            | Depth of 2nd LFO                          | 1 none, 0 max                  | 
| 10      | E2                            | LFO of 3rd filter                         | Sine, Tri(angle), Saw, Pulse   |
| 10      | E3                            | Rate of 3rd LFO                           | 0.05 – 100.0                   |
| *11*    | *E2*                          | *LFO of 3rd filter*                       | *Sine, Tri(angle), Saw, Pulse* |
| 11      | E3                            | Depth of 3rd LFO                          | 1 none, 0 max                  |
| 12      | E2                            | Sample rate reduction                     | 100 – 48000 Hz                 |
| 12      | E3                            | Bit rate reduction                        | 0 – 24 bits                    |


## Midi

Bolded params above are controllable via the Midi commands listed. All other commands can be mapped to CC values within the Norns menu `parameters > map > ...`

![Stjörnuíþrótt UI](.assets/stjoernuithrott_midi-map.gif)


## Development

[SSH](https://monome.org/docs/norns/maiden/#ssh) into your Norns/Fates, then enter the following commands in terminal.

```bash
$ cd dust/code
$ git clone https://github.com/frederickk/stjoernuithrott.git
```

If you want to get the latest version run these commands:

```bash
$ cd dust/code/stjoernuithrott
$ git fetch origin
$ git checkout primary
$ git merge origin/primary
```


## Changelog

- v1.1.0
  - Fixed sub-octave and wave selector bugs
  - Fixed order of UI elements
  - Added LFO res 
  - Added Midi [passthrough](https://github.com/nattog/passthrough)
  - Added parameter randomization
- v1.0.0 Initial release


---

<sup id="_1">1</sup> Stjörnuíþrótt is a crazy name huh? It's old Norse for Astronomy.
