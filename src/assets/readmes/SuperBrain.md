# SuperBrain
SuperBrain is a midi sequencer script for the norns music computer environment, originally developed for the LanchpadX controller.
The goal of the script is to allow parallel sequencing of multiple instruments with different sequencer styles.

## Main Architecture
SuperBrain consists of five individual sequencer tracks synchronized to a master clock.
The following attributes can be selected per track:
- sequencer Engine
- destination ("midi", "sound_engine")
- usb device
- midi mode ("polyphonic", "fork")
- midi channels

<img src="https://user-images.githubusercontent.com/39985617/116898861-322e3580-ac37-11eb-8cbc-58efb38c1664.png" width="50%">


The grid interface is devided in two main areas. First, a 9x4 area for the sequencer engines and a 9*4 area for note input via an isomorphic keyboard layout.

The configuration of the whole system with the stored note information can be saved as up to 64 presets.

Internally a button handler is extracting button events based on the grid input actions and sends theses events to the main brain object with then distributes these to the isomorphic keyboard and the active track.
The used event types are:
- press / release
- click / double click
- hold / double hold (click followed with hold)

## Engines
One sequencer engine can be used per track. Currently the following three engines are implemented:

### Graph^Theory
Is a graph sequencer with four individual playheads. The vertices of the graph can contain multiple edges and note values. The playheads can have different speeds and starting points. Based on this open principle, common sequencer types such as regular step sequencers, random walk sequencers and others can be created.

### Quantum#Physics
Is a polyrhythm sequencer with four rows, the idea is strongly based on the meadowphysics script. Due to space limitations it is not as sophisticated as the original.

### Time~Waver
Is a four track quantized midi looper, with the ability to filter notes by order of occurrence. This can enable creative ways of overdubbing and performative manipulation of former static midi loops.

## Presets
All presets are stored as txt files (lua tables) in the norns dust data folder.

## Future Work
- more engines
- Graph^Theory: add velocity to steps
- Time~Waver: unquantized looping (loop length and notes); loop mute and unmute 
- monome grid compatibility
- flexible width for efficient use of the 128 buttons (global variables for width and height)
- enable other time signatures
- global parameters: matrix width, velocity, ...
