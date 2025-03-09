# lemniscate
an 8-track-cassette-inspired looper for norns

![lemniscate screenshot](./assets/lemniscate.png)

## In a few words
It's a stereo looper (softcut-based) with an adjustable length between four seconds and five minutes, forty-eight seconds. From there, it's conceptually based on the operation of an 8-track cassette, such that a four minute loop is one minute of tape with four "programs" running in parallel. One can hop the play/record head from program to program, maintaining the relative position.

That's it. Simple looper with a little trick. Control for playback amplitude, overdub iteration amplitude, and LPF are in params. There's also a param for mixing in 8-track player noises for authentic, if cloying, nostalgia and feedback.

- ENC 3 adjusts loop length (non-destructive)
- K2 plays and pauses
- K1 + K2 records and halts recording
- K3 selects the next program
- K1 + K3 stops playback and recording, jumping the counter to the start
- K1 + K2 + K3 clears the buffer without affecting playback/record status

That's all, folks.
