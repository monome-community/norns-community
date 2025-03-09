# sampswap

swap samples within loops to make new loops.

![sampswap-01](https://user-images.githubusercontent.com/6550035/157546058-96e5c62b-410a-4426-80b6-90976b9d70c4.jpg)


this script is forked from [makebreakbeat](https://github.com/schollz/makebreakbeat). *makebreakbeat* worked by building the audio one piece at a time while *sampswap* copies and pastes to edit audio in-place. *sampswap* first repeats the original audio and then copies random regions, adds effects to that copy, and then pastes the effected copy to a random position along the loop (editing the file in-place essentially).

this script works best with loops (see notes below for reasons why). it can be used to generate material (especially "breakbeat" type things) but since it automatically tempolocks and syncs up to four tracks it can be nicely performed. 

some may also find this script might be a framework to borrow from or extend (which I happily encourage!). in addition to the normal norns engine, it has [a 'non-realtime' engine](https://github.com/schollz/sampswap/blob/main/lib/Engine_Sampswap.sc#L24-L78) which effectively can be used to resample audio processed by any SuperCollider SynthDef. also there is a embedded [lua library that wraps sox](https://github.com/schollz/sampswap/blob/main/lib/sampswap.lua#L410-L430) for easily creating effects+splices (more info about this on [my blog](https://schollz.com/blog/sampswap/)). sox splicing works easily because sox can join with crossfades using wave similarity to find best locations. basically sox+scnrt = daw in a primordial form. this script is not trying to reinvent the daw, though. if anything I want this script to be a "raw" ("random audio workstation") where all the operations are random and you only can define their probabilities.


# Requirements

- norns

# Documentation

- E1 selects a track
- E2 selects a parameter
- E3 modifies parameter
- K2 generates track
- K3 toggles playing

see the parameters menu for all the parameters. most of the parameters are available on the front UI for quick navigation.

## rundown of the screen

the title bar. this shows the current track loaded, and the current index of the generated track (in parentheses).

right below the title bar on the left is "Xqn Y" where X is the guessed number of quarter notes in the beat and Y is the guessed bpm. you can change the guessed bpm in the parameters menu.

the third line on the left shows also "Xqn Y" but here it is showing that it will generate X beats at tempo Y.

the fourth line that says "off: X" shows X beats from the down be to sync the current track.

the fifth line that says "repitch/stretch/none" is indicating how the re-tempoing will occur. repitch will simply speed it up/down. stretch will perform a timestretch. none will do nothing.

the seven bars specify the probabilities for adding any of the specified effects to the generated track (except the last bar 
which controls amplitude in realtime).

each effect is applied in order and can affect effects further down. basically all the editing happens "in place" in the file, so you end up with something along these lines:

![howitworks](https://user-images.githubusercontent.com/6550035/157556885-5b99578c-b68e-4253-8dfb-6e95278e2b58.jpg)

happy to answer questions and if time permits I can make a little tutorial video.


## notes

- track bpms are "guessed" assuming they are *loops* of even number beats. if you are not using loops then do not expect the input bpm to be correct (and probably the syncing won't work). 
- input tracks are trimmed before processing, so if your loop has purposeful silence at the end, it probably not be guessed correctly for the right bpm.
- if your track name contains "bpmX" then it will skip guessing the beat and assume the source bpm is X
- this script generates beats *slowly*. to get around this I suggest generating short beats (16 beats) continuously (beats continue to play when generating).
- when the script starts it needs another 3 seconds to start the non-realtime server so K2 will not function until then (in case you see K2 not doing anything).

# Install

install with

```
;install https://github.com/schollz/sampswap
```

once you start the script for the first time it will install `sox`, and `sendosc` (~8 MB total).
