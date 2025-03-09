## Samsara

Samsara is a minimalist looper that, given enough time, reaches nirvana.

![board](screenshots/samsara.png)

Inspired by [Dakim](https://www.youtube.com/watch?v=AmQ7AMnooj0), Samsara invites you to slowly layer in new material as old material fades away. Toggle recording on and off easily while the loop plays, or use one-shot record mode to precisely record a single phrase. The loop duration is set in terms of tempo & beats, making it simple to integrate into other musical contexts (it uses norns' clock system, so you can use MIDI clock & transport messages, Ableton Link, or Crow). Tap tempo is also available via K2+K3.

You can also easily extend the loop. Say you have an awesome 1-bar drum pattern, and now you want to add harmonic content. Your harmonic phrase is probably longer than that one bar, so just hold K1 and tap K2 to double to two bars, and then again to double to four bars. Now you can layer a 4-bar harmonic phrase on top of that original 1-bar drum loop and keep everything moving.

### Requirements
* norns (update to software version 200424 or later)
* Audio in (stereo preferred, mono mode available in params)

### Documentation
* E1: Number of beats
* Hold K2+turn E1: Tempo
* E2: Loop preserve rate
* E3: Rec. mode (loop/one-shot)
* K2: Start/pause playback
* K3: Arm/disarm recording
* Hold K2+tap K3: Tap tempo
* Hold K1+tap K2: Double buffer
* Hold K1+tap K3: Clear buffer

### Roadmap
* Beta release & bug fixing
* Multi-mode filter
* Click tracks
* Param-ify recording and playing (so they can be MIDI-mapped)
* "Extend mode"
  * while recording, keep extending the loop by (original loop length), until "stop recording" is hit (stops recording at next multiple-of-original). Like "double buffer", but if you don't know how long your new phrase is gonna be
* Varispeed
* Loop window slide & endpoint move (with wav viewer?)

### Download
Available as a [direct download](https://github.com/21echoes/samsara/archive/master.zip). Unzip, rename to `samsara` (instead of `samsara-master`), and put into the `code` folder on your norns.
