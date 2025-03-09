# Forge
A playable oscilloscope for [norns](https://monome.org/docs/norns/) and [crow](https://monome.org/docs/crow/) that works just as well without crow if you prefer.

![animated demonstration](./assets/images/forge.gif)

## What it does
In a nutshell it's a note making machine, drawing the low frequency cycles it receives from an attached crow's inputs or a pair of internal LFOs or a combination of the two, and spawning notes at a regular (configurable) cadence where the lines intersect.

From there the newly formed notes are conveyed through optional step and scale quantization and eventually played into a dealer's choice of outputs of the engine, i2c, and/or MIDI varieties.

Transport is controlled by K3, and K1 + K3 lets you stop and flush the player roll. Speaking of K1 combos, there are some immediate controls for fine-tuning the oscilloscope. K1 + ENC1 adjusts the sample frequency. K1 + ENC2/3 trims the legroom and headroom respectively. Most everything else can be controlled by parameters. 

A note on the crow outputs: they're disabled initially, but should you use them, 2 and 4 are gates. 1 is a frequency derived from the MIDI note created by the generator (quantized or unquantized per param). 3 is the raw frequency of the graph intersection, optionally offset to be unipolar.

That's it. The rest is for exploration. I hope it's all smooth sailing, but bug reports and feature requests are welcome.

# Install
Run `;install https://github.com/cachilders/forge.git` from maiden at `<your-norns>.local`.

## Acknowledgements
The code draws heavily from the efforts of the norns community. The gif was made using [norns.online](https://github.com/schollz/norns.online). The name comes from the blacksmith guild's headquarters in Loom.
