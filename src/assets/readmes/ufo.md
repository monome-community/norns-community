# ufo

Ultra-low Frequency Oscillator, powered by the International Space Station

This is a script for the Monome Norns that uses the International Space Station (ISS) as a low-frequency oscillator, with a period of about 90 minutes. It grabs data from the [Where The ISS At? API](https://wheretheiss.at/), and maps the location of the ISS over the Earth to sound.

The ISS orbits Earth every 90 minutes or so, and so if you track its latitude and longitude then you'll get a sine wave for the former, and a ramp wave for the latter.

The script generates a internal supersaw (ISS) drone composed by [Jonathan Synder](https://llllllll.co/u/jaseknighter/). The latitude of the ISS is mapped to filter cutoff and modulation depth. The longitude is mapped to reverb absorption. Finally, the detune parameter of the supersaw is mapped to the distance between the ISS and the location specified in the `localLat` and `localLon` parameters at the top of the `ufo.lua` file, which you should replace with your own latitude and longitude coordinates to personalise the script.

Requires an internet connection.

## MIDI

The script plays a generative melody with a pre-set collection of notes, but you can change the note pool that it draws from by connecting a MIDI device and holding down some keys. You can set a root note and scale to quantize your note pool to in the parameters menu, as well as reset the original note pool.

## Crow

Additionally, the script generates a trio of voltages that it spits out through the Crow module, which connects to Norns over USB. You can then send those voltages wherever you want in your Eurorack system to modulate your patches with rocket science.

- out 1: latitude (-5-5V)
- out 2: longitude (0-10V)
- out 3: distance from your position to ISS (0-10V) - only if enabled in script

## Thanks

To Jonathan Snyder for endless sound design and code help
To Alanza for the emulation of erbeverb reverb
To Eric Skogen for the [Supercollider supersaw code](https://gist.github.com/audionerd/fe50790b7601cba65ddd855caffb05ad)
To Monome and the Norns community for everything <3

## Changelog

### v1.0

Initial release
