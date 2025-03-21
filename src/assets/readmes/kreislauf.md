[Kreislauf](https://norns.community/en/authors/frederickk/kreislauf)
---

v0.3.3

## Beat sequencing rund um den Kreis inspired very heavily by Pocket Operators and the work of [Ethan Hein](http://www.ethanhein.com/).

![Kreislauf UI](./.assets/kreislauf.gif)

## Requirements

[Norns](https://monome.org/norns) or [Fates](https://llllllll.co/t/fates-a-diy-norns-dac-board-for-raspberry-pi/22999).


## Install/Update

Kreislauf can be installed via [Maiden's](https://norns.local/maiden) project manager.


## Overview

#### Patterns

Each pattern consists of 4 concentric sequencer rings:

- channel 1 - kick (outermost),
- channel 2 - snare
- channel 3 - closed hi-hat
- channel 4 - open hi-hat (innermost).



#### Beat/Notes

When a beat is added to a ring, it fires off a Midi* note when active (`60` by default) to the corresponding channel. While, this script is design with intent to create drum patterns; each beat can have its note value adjusted allowing for melody/harmony constructs as well. Go wild...

*I've blindly implemented crow, but I have no idea if it works. Any crow users please let me know what bugs you find and I'll adjust.

#### Chaining

I also like the way Pocket Operators accommodate for chaining of beats so I incorporated the ability for multiple patterns with individual loop counts to be strung together. For single pattern beats be sure to keep loop count as `Inf.` if you want endless looping. If multiple patterns are create, the entire sequence will *always* loop.

#### Saving and Loading Sequences

Patterns can be saved and later recalled (along with accompanying `PSET`). A number of demo patterns of some staple beats is installed within `~/dust/data/kreislauf/patterns`. `LOAD` and `SAVE` patterns from the params menu.


<!-- WIP
## Demo

Here's a brief video showing a workflow with the OP-Z.

[ video ]
-->

## Controls and Params

| Controller          | Page   | Values      | Description                        |
| ------------------- | ------ | ----------- | ---------------------------------- |
| **E1**              | Global | 1 – 3       | Change page                        |
| **K2**              | Global | Play/stop   | Plays or stops sequence            |
|                     |        |             |                                    |

#### Page 1

![Kreislauf page 1 screenshot](./.assets/kreislauf-1.png)

| Controller          | Page   | Values      | Description                        |
| ------------------- | ------ | ----------- | ---------------------------------- |
| **E2**              | P1     | 1 – x       | Cycle through patterns             |
| **E3**              | P1     | 20 – 300    | Set BPM                            |
| **E3+K1** or **E4** | P1     | 1 – 16      | Step divider                       |
| **K3**              | P1     |             | Add pattern                        |
| **K3+K1**           | P1     |             | Remove pattern                     |

#### Page 2

![Kreislauf page 2 screenshot](./.assets/kreislauf-2.png)

| Controller          | Page   | Values      | Description                        |
| ------------------- | ------ | ----------- | ---------------------------------- |
| **E2**              | P2     | 1 – 4       | Cycle through rings                |
| **E3**              | P2     | 0 – 16      | Set channel for active ring        |
| **E3+K1** or **E4** | P2     | Inf, 1 – 32 | Loop count for active pattern      |
| **K3**              | P2     |             | Load pattern                       |

#### Page 3

![Kreislauf page 3 screenshot](./.assets/kreislauf-3.png)

| Controller          | Page   | Values      | Description                        |
| ------------------- | ------ | ----------- | ---------------------------------- |
| **E2**              | P3     | 1 – 16      | Cycle through steps                |
| **E3**              | P3     | 0 – 127     | Set note value for active step     |
| **E3+K1** or **E4** | P3     | 0 – 127     | Set velocity value for active step |
| **K3**              | P3     |             | Add beat/note to active step       |



## Development

[SSH](https://monome.org/docs/norns/maiden/#ssh) into your Norns/Fates, then enter the following commands in terminal.

```bash
$ cd ~/dust/code
$ git clone https://github.com/frederickk/kreislauf.git
```


## Changelog
- v0.3.x
    - Fixed/tidied UI
    - Fixed Midi note off
- v0.2.x
    - Added sequencing of multiple patterns
- v0.1.x Initial release