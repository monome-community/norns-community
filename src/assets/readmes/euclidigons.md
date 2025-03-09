# euclidigons

Sequencer for monome norns, imagined by and realized in collaboration with @setfield

![screenshot](https://synthetiv.github.io/euclidigons/screenshot.png)

## installation

- Download [the latest version](https://github.com/synthetiv/euclidigons/archive/main.zip) from GitHub
- Unzip into Norns' `/home/we/dust/code/` directory
- Reset or sleep yr norns (there's a custom engine)

## introduction

At startup, there will be two shapes visible on the screen. Think of the polygons' sides as strings: when a side is crossed by one of the other shapes' vertices, the string is plucked or struck.* The faster the side-string and vertex-plectrum are traveling relative to one another, the louder and brighter the note will be; and different harmonics will be emphasized depending on where along its length the string is struck.

**E1** chooses a shape to edit.\
**E2** moves it along the X axis.\
**E3** changes its size.\
**K1+E2** sets the note to which its sides are tuned.\
**K1+E3** transposes the note in octaves.\
**K2+E2** sets rotation rate.\
**K2+E3** sets the number of sides (1-9).\
**K3** mutes or unmutes the selected shape.†\
**K1+K2** deletes the selected shape.\
**K1+K3** inserts a new shape.

Arc encoders are also supported and edit the currently active shape:

**ARC 1** sets the note.\
**ARC 2** transposes the note in octaves.\
**ARC 3** sets the rotation rate.\
**ARC 4** sets the number of sides (1-9).

<em>* by default, notes are only sounded when one shape's vertex crosses _into_ another shape, but this  can be changed using the 'trigger style' param.</em>\
<em>† set the 'mute style' param to 'own note only' to allow a muted shape's vertices to pluck the strings of another shape.</em>

## about the engine

`PrimitiveString` "models" a plucked string in the style of Kazimir Malevich. A blend of two basic tone generators -- a "nulse" pulse wave with added AM'd white noise, and a "caw" comb-filtered sawtooth wave -- is fed through a low pass filter and multiplier. Overall amplitude, LPF cutoff, noise amount, and comb filter feedback are all controlled by a single attack-release envelope.

Settings exposed in Norns params:

`amp`: this one is simple: volume\
`waveform (pulse/saw)`: blend between the two waveforms/generators described above; 0.0 = pure pulse, 1.0 = pure saw\
`pulse noise`: the amount of noise present in the pulse waveform\
`saw comb`: the decay (in seconds) of the comb filter fed by the saw waveform\
`brightness`: sets maximum filter cutoff\
`attack`: AR envelope attack time in seconds\
`release`: AR envelope release time in seconds

