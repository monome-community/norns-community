<img src="https://raw.githubusercontent.com/jaseknighter/parrot/main/images/birdies.png" width="400">

# parrot

a cv recorder and player for norns+crow 

*parrot* allows crow inputs 1 and 2 to record cv which may then be replayed out of crow outputs 1-4.

## instructions

### installation
`;install https://github.com/jaseknighter/parrot`

### key/encoder controls
* e2: select previous/next control
* k2/k3: select previous/next sub-control
* k1+e2: display instructions

### features
the *parrot* script's features are accessable from the script's main screen and from the `PARAMETERS` menu

* `bucket zoom` (bz): scale the norns display of cv recorded from crow inputs 1 and 2
* `bucket record` (br): turn the cv recording from crow inputs 1 & 2  on and off
* `bucket loop length` (bl): set the amount cv to play that has been recorded from crow inputs 1 & 2 (up to ~15 seconds)
* `tap assignment` (ta): routes the cv recorded to crow inputs 1 & 2 to the 4 crow outputs. there are six assignment options:
  * `in1`: outputs crow input 1
  * `in2`: outputs crow input 2
  * `or12`: compares the voltages of inputs 1 and 2, outputing the higher voltage 
  * `&12`: compares the voltages of inputs 1 and 2, outputing the lower voltage 
  * `rec1`: outputs crow input 1, turning any negative voltages positive
  * `rec2`: outputs crow input 2, turning any negative voltages positive
* `tap delay` (td): delay the recorded cv sent to crow outputs 1-4
* `quantize taps` (tq): quantize the cv sent to crow outputs 1-4 

### todo
* tbd

## requirements
* norns
* crow

## credits
*parrot* is based on the *cvdelay* script built into @whimsicalraps [bowering](https://github.com/whimsicalraps/bowering) crow script collection following a suggestion by @lijnenspel.

many, many thank to @p3r7 for creating a lovely parrot image for this script and to @justmat for the crow image i am borrowing from his [crow_talk](https://llllllll.co/t/crow-talk/41560) script.
