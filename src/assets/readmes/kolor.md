# כל אור

every light sequences samples.

![Image](https://user-images.githubusercontent.com/6550035/104591857-284ddb80-5622-11eb-8c7a-cb1aaff0894b.png)


the words "כל אור" translate from Hebrew to English as "every light" and is pronounced "kol-or". its meant to portray my attempt of using every light to sequence samples with [the grid](https://monome.org/docs/grid/).

this script is born out an exploration of sampler sequencers. i drew inspiration from the op-z and model:samples (though i don't own these i was inspired by how i think they are supposed to work). i had five goals making this sample sequencer:

1. works easily with any non-grid norns script. i've made [a](https://github.com/schollz/oooooo) [lot](https://github.com/schollz/downtown) [of](https://github.com/schollz/barcode) [scripts](https://github.com/schollz/glitchlets) and i want to plug in a grid and use it immediately as a "groove box" in addition to the original host script. to meet this goal, the norns screen actually doesn't provide any information (except for providing the save/load screen).
2. trigger-specific parameter locks with lots of *mods* - volume, pitch, filters, sample positions, probability, etc. each *mod* has its own lfo. and an lfo for the lfo's, because why not.
3. easy pattern chaining and probabilistic chaining for automatically adding variation (markov chaining).
4. as little menu-diving as possible, with very few "hold" buttons or "mode" screens. (have to do my best given 128 white lights...)
5. stereo samples! because uncorrelated noise in both ears sounds awesome.

at the end i had to make compromises to reach these goals. the compromises mean that there is a list of things that *kolor* does not do (...yet, but maybe not at all):

1. all the steps in one track must have the same sound. (this is not a technical limitation, but a menu-diving limitation as it would be hard to determine which step has which sound).
2. mod parameters are limited to 4-bit resolution, because there are only 15 keys devoted to the selection scale. however, *if you use a lfo* the values will oscillate with supercollider's bit-depth (16-bit or 32-bit resolution??). there may be ways of getting around the 4-bit with some menu diving or more button pushing.

i'm totally open to ideas to remove these limitations or improve in general.

## requirements

- norns
- 128- or 64-grid (grid is optional, but recommended)

## documentation

the usage documentation lives at [schollz.github.io/kolor](https://schollz.github.io/kolor/).

## license

mit
