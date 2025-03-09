![blndr4](https://user-images.githubusercontent.com/6550035/89736309-58fb6a80-da1d-11ea-8cf7-e8072b76ba2a.png)

this is `blndr` - my first patch for [norns](https://monome.org/docs/norns/). `blndr` is a quantized delay with optional time bending effects in the stereo field.

## demo

<p align="center"><a href="https://www.instagram.com/p/CDfppIbBFnF/?utm_source=ig_web_button_share_sheet"><img src="https://user-images.githubusercontent.com/6550035/89372587-6621fd80-d69b-11ea-98e2-c013fac69565.png" alt="Demo of playing" width=80%></a></p>

## requirements

- norns
- line-in

## documentation

the line-in audio is fed into a delay loop for a duration of one quarter note, so it automatically becomes quantized to the `bpm` (ENC1). the amount of delay can be dialed in with `level` (ENC2) and `feedback` (K1+ENC2).


![blndr6](https://user-images.githubusercontent.com/6550035/89736311-5d278800-da1d-11ea-8638-53a8013f36b7.png)


the delay loop is randomly time shifted based on the probability from the `spin` parameter (ENC3). the audio from the delay loop is then fed into a second delay loop that is also time shifted and panned randomly.

the K2/3 are used to quickly speed up/down the bpm to 1/3 intervals to get some cool polyrhythms (good for drums).

you can use K1+K2 to mute incoming audio.

you can use K1+K3 to switch to reverse mode.

## my other patches

- [barcode](https://github.com/schollz/barcode): replays a buffer six times, at different levels & pans & rates & positions, modulated by lfos on every parameter.

## thanks

this would not have been possible without the stellar [softcut tutorial](https://monome.org/docs/norns/softcut/) and inspiration of randomizing speed shifts from [bounds](https://llllllll.co/t/bounds/23336). 

## license

MIT


