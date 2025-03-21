<h1 align="center">EELS</h1>

![eels screen animated gif. two pixelated eels flop up & down in sync as 'time a' is modified. yellow backround with some random text around the sides](/lib/doc/img/eels_cover.gif)

dual delay / comb filter with a variety of i/o modes and modulation options.

an undersea cousin of [wrms](https://github.com/andr-ew/wrms).

**NOTE:** to view images, please read at [github.com](https://github.com/andr-ew/eels) not [norns.community](https://norns.community/eels)

## hardware

**required**

- [norns](https://github.com/p3r7/awesome-monome-norns) (220321 or later)

**also supported**

- [crow](https://monome.org/docs/crow/)
- arc

## install

install from the maiden catalog

or

in the maiden REPL, type: 
```
;install https://github.com/andr-ew/eels/releases/download/latest/complete-source-code.zip
```

## patch notes

[watch the video](https://www.youtube.com/watch?v=NxpqsLtH880)

[read the complete patch notes](/lib/doc/patch-notes.md)

## norns UI

### intro

![page B of rpls, E1-3 & K2-3 are labelled](/lib/doc/img/eels-02.png)

- **K2:** increment page
- **K1 (hold):** set modulation source

eels is split into three pages – one page for eels **A** & **B**, respectively, and an `M` page for setting the **i/o mode** & some internal modulation settings. on pages `A` & `B`, holding **K1** allows you to set the modulation source for each parameter with the encoders. 

available modulation sources:
- **lfo 1**: internal LFO.
- **lfo 2**: internal LFO.
- **crow in 1** & **crow in 2**: control voltage from crow. **time** tracks v/oct, levels expect 0-5v.
- **midi**: midi note value, converted to volt/octave.
- **clock**: an offset that will sync **time = 0** with the global clock tempo in delay mode. positive whole number voltages will be multiples of the clock, negative whole number voltages will be divisions of the clock.


note that many params use eurorack-native voltage units for pairity with crow input modulation, though eels is still designed to work well as standalone effect.

### page `M`

![page M of rpls, E1-3 & K2-3 are labelled](/lib/doc/img/eels-03.png)

- **E1:** i/o mode
- **E2:** internal lfo period
- **E3:** internal lfo depth
- **K3:** lfo focus 1/2

there are 5 **i/o modes** to choose from, which affect the routing of inputs & outputs, as well as the relationship between both eels.
- **coupled**: all **B** controls are coupled with **A**, but **time b** is the sum of the **A** & **B** voltage values.
- **decoupled**: separate **A** & **B** controls.
- **series**: decoupled controls, **A** delay routed into **B**.
- **ping-pong**: all **B** controls coupled with **A**, ping-pong feedback between delays.
- **send/return**: **A** delay only (left channel), external feedback loop (right channel). 
    - input L: dry signal, patch from input or mixer send
    - output L: wet signal, patch to mixer
    - output R: patch to the input of external effect (such as a filter)
    - input R: patch in from the output of external effect
    - **for best results, be sure to silence the system monitor level.**
    
eels has two internal LFOs, which can be set as modulation sources for parameters on the `A` & `B` pages. additional settings for each LFO are available in the params menu.

### pages `A` & `B`

![page A of rpls, E1-3 & K2-3 are labelled](/lib/doc/img/eels-01.png)

- **E1:** delay time (v/oct)
- **E2:** delay time slew/lag (volts, 0 to +5)
- **E3:** delay feedback (volts, -5 to +5)
- **K3:** delay range

on page `B`, some parameters may appear greyed-out – this means that those parameters are mapped to the value of eel **A** in accordance to the current **i/o mode**.

there are two ranges for **time**, which detirmines the audio effect that the eel will be set up to behave like:
- **delay**: 4.65s - 0.07s
- **comb**: 110hz - 7040hz

the **delay** range can be useful for several types of effects:
| range of time                     | use case                         |
| ---                               | ---                              |
| low values, -2 to 0               | looper, with feedback set high   |
| mid values, -1 to 3               | conventional delay               |
| high values, 3 to 4               | resonator, phasor, or chorus, depending on modulation & feedback settings |

the **comb** range turns eels into a spiky resonant filter. 
- **time** now sets the resonant frequency of the filter
- **feedback** sets the resonance/decay time of the spectral spikes

the most common use for comb filters is [Karplus–Strong synthesis](https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis) (though eels is missing the damping lowpass filter). feed bursts of noise into the input of eels to turn it into pitched, string-like plucks. use midi or crow modulation to sequence the resonant frequency & create melodies. it can also be rewarding to feed eels a mixture of noise & musical tones, using the comb filter as a weird resonant EQ.

**time** is measured in volts/octave. reference the table below for the actual value of each volt (assuming **fine = A** and **root = 440hz**).

| volt   | **range = delay**   | **range = comb** |
| ------ | ------------------- | -----------      |
| -2     | 4.65 seconds        | 110 hz           |
| -1     | 2.32 seconds        | 220 hz           |
| 0      | 1.16 seconds        | 440 hz           |
| 1      | 0.58 seconds        | 880 hz           |
| 2      | 0.29 seconds        | 1760 hz          |
| 3      | 0.14 seconds        | 3520 hz          |
| 4      | 0.07 seconds        | 7040 hz          |

- **NOTE:** the range is quite wide - when mapping to a midi controller, you may want to reduce the output range of the mapping for more sensitive control.
- **NOTE:** in comb range, **ping-pong** & **send/return** modes do not track v/oct correctly
    
**lag** sets the lag/slew value for **time**. set to 0 for instantaneous changes (clicky), set > 0 for smoothed encoder movements or portamento when sequencing comb filter pitch.

**feedback** sets the feedback level of the delay, or the decay time of the comb filter.
    
## arc UI

arc offers high-sensitivity control of key parameters. highly reccomended!

- time a
- feedback a
- time b
- feedback b

## additional params

a few more params can be accessed exclusively in the params menu:

### modes

- **input**: mono or stereo audio input. only effects **coupled**, **decoupled**, and **series** modes.

### time

- **time a quant** & **time b quant**
    - **free**: continuous control over **time**.
    - **oct**: **time** is quantized to whole numbers. this has different use cases in each range.
      - comb range: **time** becomes an octave control 
      - delay range w/ clock modulation: **time** becomes a clock multiplier/divider. reference the table for multiple/division at each volt:
        | volt   | time in beats       |
        | ------ | ------------------- |
        | -2     | 4                   |
        | -1     | 2                   |
        | 0      | 1                   |
        | 1      | 1/2                 |
        | 2      | 1/4                 |
        | 3      | 1/8                 |
        | 4      | 1/16                |

      
- **fine**: fine tune the **time** value in semitones. adjusts the musical key when sequencing the comb filter pitch via crow. no need to adjust when sequencing over midi.
- **root**: set the concert pitch frequency for **time**.

### levels

- **input a** & **input b**: audio input level
- **output a** & **output b**: audio output level
- **stereo width**: set the output stereo separation between **A** & **B**.

### modulation

set the modulation source for each modulatable param

### lfo 1 + 2

the parameters of the internal lfos. see [`lib/lfo`](https://monome.org/docs/norns/reference/lib/lfo#lfo-attributes--defaults) for further info.

### pset

- **reset all params**: resets all params to default values
- **overwrite default pset**: when **autosave** is disabled, sets the current state as the default state when starting the script.
- **autosave pset**: disables saving the pset to the default slot when exiting the script. when enabled, settings will persist between sessions.
