## synthy

a synthesizer critter and chord sequencer.

![image](https://user-images.githubusercontent.com/6550035/131072123-00275007-b08a-470a-85d5-a0cee8179c21.gif)

https://vimeo.com/593330469

synthy is a polyphonic synth composed of two saw-wave oscillators per note which are mildly chorused plus a pulse-wave sub-oscillator that responds with low-note priority as a monophonic bass. 

synthy's mind is its own and obeys an internal stochastic rhythm. synthy may decide to shrink or grow and when it does, it causes a global filter to close (when shrinking) or open (when growing). you can use E3 to manually take control, but after you stop turning E3 the synthy will revert to its own behavior after a certain time (available to change as a setting). 

synthy's body is modeled as six revolute joints which are kinematically re-positioned when moving with E2 or E3. the x- and y- flucuations from the kinematics of the body movement do detuning and tremelo respectively. the degree of modulation is available to change in parameters ("squishy detuning" or "squishy tremelo"). 

plug in a midi keyboard to play synthy. if you don't play any notes, synthy will try to help you out. synthy knows 1,000 chord progressions which can be recalled randomly with K2 and start/stopped with K3.

### Todo

- midi/jf/crow output from chord sequencer
- what does E1 do?
- fix :bug: 

### Requirements

- norns
- any midi controller (optional)

### Documentation

- E2 modulates flanger
- E3 modulates lpf
- K2 generates chords
- K3 stops/starts chord sequencer

see `PARAMS` menu for more.

### Install

install with 

```
;install https://github.com/schollz/synthy
```