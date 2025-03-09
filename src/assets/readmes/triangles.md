# triangles

endless triangles

![screenshot of triangles](/img/triangles.png)

Each of the four voices consists of 2 triangle waves and some noise. Each voice is independently triggered by its own (tempo-sync'd) clock source. Adjust the amplitude envelope, filter cutoff, vibrato and bit rate of each voice to taste.

## Requirements

- norns
- MIDI controller (optional but recommended)

## Documentation

- K2: randomise parameters

Use the norns parameter menu `PARAMETERS > TRIANGLES` to change the parameters of each voice. Most parameters should be self-explanatory but there's a few less obvious ones:

- *detune* detunes one oscillator against the other in the voice
- *bellow* alters the mix between the two oscillators on the rise and fall of the envelope. `0.5` (default) plays both oscillators equally throughout the envelope, while `0` plays oscillator 1 on the rise, and 2 on the fall. `1` reverses this.
- *curve* adjusts the curvature of the [perc](https://doc.sccode.org/Classes/Env.html#*perc) amplitude envelope
- *trigger frequency* how often (in beats at the current system clock tempo) the envelope is triggered.

## Install

install from maiden using

```
;install https://github.com/chrislo/triangles
```

this script includes an Engine, so you will need to `SYSTEM > RESTART`.

## Acknowledgements

- @jayhaych for feedback and encouragement on my supercollider experiments during #jamuary. Some of those experiments became this script.
- @noiserock for beta testing
- @pfig, @tteejj, @imwaiting, @boboter, @21echoes for their encouragement and enthusiasm.
