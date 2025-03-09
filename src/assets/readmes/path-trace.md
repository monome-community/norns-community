### Path Trace

A movement recorder for Norns and Crow. 

Record encoder rotations to four looping, independent buffers — one for each Crow output — and optionally set voltage output range, sample and hold trigger, and quantization.

![Path Trace Cover Image](https://github.com/brokyo/path-trace/blob/main/cover.png?raw=true)

### Requirements
- Norns
- Crow

### Documentation
#### Select
- `E1` selects one of four buffers. Each buffer corresponds with the Crow output of the same number.
#### Record
- `K2` toggles recording. Press once to begin recording, and press again to end it. 'R' appears in lower right when recording is active.
- `E2` is monitored during recording. The encoder's position is captured every 30ms.
#### Play
- `K3` toggles playback. Press once to begin playing, and press again to end it. 'P' appears in lower right when playback is active.
#### Configure
- Settings can be changed through the `Params` menu, get there by pressing `K1` and turning `E1` until you see the fourth screen.

*Global Configuration*
- `Key` and `Mode` apply to all quantized buffers 

*Individual Buffer Configuration*
- `Voltage Range` adjusts the minimum and maximum voltage values. Select from common Eurorack standards.
- `S&H Input` designates which crow input will trigger a sample and hold event. Once selected `C[#]` will appear in lower right and will flash when a pulse comes in.
- `Quantization` adjusts the buffer's output to match the scale set by the global `Key` and `Mode`.
- `Octave Base` and `Octave Range` set the octaves to which the quantized notes will be mapped.

#### Other Things To Know
-  Each buffer can hold up to five minutes of recording, with samples taken every 30ms. 
- Recording will immediately end if `E1` is turned.
- Using `K2` to stop recording resets the buffer to the start.
- Changing the `Voltage Range` does not retroactively adjust existing values.

#### Future Ideas
- Tune playback speed on scope 
- Connect tempo to internal clock
- TXO support
- One shots