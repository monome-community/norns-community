# Stack

A stack of 8 fixed-frequency resonant bandpass filters, for Monome Norns. Each filter is one octave apart.

- Use `ENC1` to choose which filter is active

Filter selection can be recorded and played back as a pattern.

- Press `KEY2` to begin recording
- Play with `ENC1` to select active filter
- Press `KEY3` to finish recording and play back pattern
- Play around with your input audio!
- Press `KEY2` then `KEY3` to clear pattern (record empty pattern)

Stack operates on a stereo input signal.
 
## Installation

[Download latest release](https://github.com/cfdrake/stack/archive/master.zip) and copy files into `~/dust/code/stack`.

Or use Git:

```
<ssh into your Norns>
$ cd ~/dust/code
$ git clone https://github.com/cfdrake/stack.git
```

Note that after installing you must `SYSTEM => RESET` your Norns before running this script, as it includes a new SuperCollider engine.

## SuperCollider Engine

This script makes a new SuperCollider engine available, `Stack`. Please see `lib/Engine_Stack.sc` for the latest parameter definitions.