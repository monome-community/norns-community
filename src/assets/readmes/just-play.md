# just-play

Play Just Friends in synth mode with MIDI (6-voice polyphony)

## requirements

- [norns](https://monome.org/docs/norns/)
- [crow](https://monome.org/docs/crow/)
- [just friends](https://www.whimsicalraps.com/products/just-friends?variant=5586981781533) connected to crow via i2c
- a MIDI controller
- [grid](https://monome.org/docs/grid/) (optional)

## documentation

Just Friends

- switch to sound/transient or sound/sustain
- synth mode can be disabled in the params menu

Crow

- output 1 is a 10V trigger pulse (5ms) on each note
- output 2 is v/oct CV of the most recent note (0-10V or +/-5V)
- output 3 is the velocity of the most recent note (0-10V or +/-5V)
- output 4 is a MIDI CC value (0-10V or +/-5V, defaults to CC1)

voltage range, midi CC and pitch bend range are configurable in the params menu

## roadmap

- Advanced crow output configuration
- UI improvements
- Do something with the crow inputs?

## known bugs

- Crow trigger output cycles on latest RC firmware
