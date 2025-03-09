![ONG screen](ong-screen.png)

ONG is an ocean noise generator for Monome Norns.

[lines community thread](https://llllllll.co/t/ong-ocean-noise-generator-for-monome-norns/50364)

Even by the standards in the Norns ecosystem this script might be considered a bit more experimental than some others.
A little bit akin to the [Showers](https://norns.community/authors/justmat/showers) script by mat.

## install
from maiden type

```
;install https://github.com/dst78/ong
```

## dreamers

ONG creates a soundscape that simulates ocean waves rolling in. I sincerely hope the soundscape brings you inner calm and relaxation.

Record it with tape, play other things on top of it. Enjoy, exhale and deflate and let your thoughts get lost.

## realists
There are a few controls to alter the sound, but ultimately it is several noise generators running through filters, being modulated by LFOs.

**Norns controls are:**

* K1 display help
* E1 overall amplitude
* E2 near waves amplitude
* K2+E2 near waves speed
* K3+E2 foam amplitude
* E3 far waves amplitude
* K2+E3 far waves speed
* K3+E3 ambience amplitude

There are a bunch of other parameters that are available through the parameter page, but not mapped to encoders.

## historians
ONG is my first own script in the Norns universe. I'm dipping my toes into all this, learning Lua and SuperCollider as I go along.

I'm sure when I look at this in a couple of years or months I would structure many things differently, although having debugged the fabulous [Arcologies](https://github.com/northern-information/arcologies) script by [@tyleretters](https://www.instagram.com/tyleretters/) I believe I've already learned a thing or two.

## lawyers
ONG is deeply inspired by the Ocean Noise Generator "guitar" pedal built by [Syntherjack](https://syntherjack.net/ocean-noise-generator/). I'm releasing this software version with permission from them.

## releases
v1.1.0 viscosity
* re-coupled the wave graphics to the sound engine parameters for a more pleasant
tweaking experience. the graphic generation has been optimized and should be lag-free now
* improved the ambience tweak-ability in the parameter menu
* cleaned up sound engine to allow for total silence through the various volume controls
* general code cleanup

v1.0.1 ocean cleanup
* decoupled the graphics from engine wave speed to prevent UI slowdown / hangs
* converted all engine LFOs to audio rate to have cleaner sound when using very high frequencies
* automatically deactivate compressor if it is on and restore original setting on exit (thanks @eigen for the hint)

v1.0.0 first waves
* initial release

