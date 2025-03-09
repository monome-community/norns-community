# Skylines

Monome grid-based sequencer take on the M185 sequencer by [RYK modular](https://rykmodular.bigcartel.com/products), also inspired by the [m18s script by jlmitch5](https://github.com/jlmitch5/m18s).

* Two voices of up to 8 steps, each step having up to 8 stages. 
* Clock from crow input 1 or norns global clock. V/oct and gate outs from crow. 
* Notes are quantized to a scale of choice, and glide can be set per step. 
* The sequencer can play forward, in reverse, ping-pong or random. 
* Several play-modes for the stages of each step: all, none, first, every second, every third, every fourth, random.
* Random note and step generator.
* Preset saving/recalling.

## Requirements

* Norns
* Grid (128 varibright)
* Crow

## Documentation

Place the grid vertically, with the USB port on top. Change pages with E1.

### Page 1: Sequencer

<img src="https://github.com/unit-cell/skylines/blob/main/docs/sequence_screen.png" width="500" />

The sequencer will be displayed on the grid while norns is on page 1. Use K3 to start the internal clock, and K2 to reset the sequencer to the first step. Alternatively, send a clock signal into crow input 1 to start the sequencer. A 2V pulse into crow input 2 will reset the sequencer.

<img src="https://github.com/unit-cell/skylines/blob/main/docs/sequencer_grid.png" width="1500" />

### Page 2: Presets & scales

The top block of lit LEDs represents memory slots for presets, which store all the information of a patch (except for the internal clock tempo).

* Press K3 to enter saving mode, and then press a pad in this block to store the preset there. The pad will light up.

* Use E3 to change the function of K3 between saving and deleting. K3 will then delete presets instead of saving them.

* Press K2 to enter loading mode, and then press a preset pad to load the corresponding preset.

<img src="https://github.com/unit-cell/skylines/blob/main/docs/preset_screen.png" width="500" />

The second block of LEDs represents an octave on a piano, black keys on the top row and white keys on the bottom row. Press any of these keys to change the root of the current scale to the corresponding note.

The last block of LEDs represent different scales form the MusicUtil library. Press any of these to change the selected scale to the corresponding one. You can see the selected scale represented on the root note LEDs with brighter pads.

<img src="https://github.com/unit-cell/skylines/blob/main/docs/memory_root_scales_grid.png" width="1500" />

