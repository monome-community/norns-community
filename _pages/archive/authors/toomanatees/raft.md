---
title: raft
description: a scene-setting, softcut-based delay: three delay lines & noise generator & “froth” modulator!
published: true
date: 2022-05-24T17:25:53.674Z
tags: audio fx, delays + loopers
editor: markdown
dateCreated: 2022-05-24T17:25:50.909Z
---

# raft
## screenshots

![raft.png](/community/toomanatees/raft.png)

## description

raft is made up of:

- three delays lines (waves)
- global delay line modulator (froth)
- global filtered white noise generator (ocean)

Each wave has its own buffer, time, feedback, and output volume. The encoders control the parameters for the active delay.

**On startup only the first wave is active.** Press Key[3] `->` to move to the next wave; it will activate if it was previously inactive. Once multiple waves are active you can move between them using Key[2] `<-` and Key[3] `->`. 

**Key[3]'ing past Wave 3/3 will deactivate Waves 2+3 and return you to Wave 1.**

- on [Wave 1/3] pressing Key[2] will not do anything
- on [Wave 3/3] pressing Key[3] will reset all buffers, reset feedback to default value (0.5), and deactivate Waves 1 + 2. This way you can build up feedback and drones and Key[3] your way to safety.

Hold Key[1] and use the encoders to control the global settings:
- Key[1] + Enc[1] = froth rate
- Key[1] + Enc[2] = ocean amplitude
- Key[2] + Enc[3] = froth amount

Hold Key[1] and use the other keys to freeze the buffer of your active delay. Currently the only way to reactivate recording of a delay line is to Key[3] past Wave 3 (reset) as explained above.
- Key[1] + Key[2] = drone in reverse-playback
- Key[1] + Key[3] = drone in forward-playback

further parameters are available in the param menu including a global buffer rate.

## install

from maiden type
`;install https://github.com/timothy-taylor/raft`

## links

- [view on llllllll](https://l.llllllll.co/t/raft)
- [view on github](https://github.com/timothy-taylor/raft)
{.links-list}