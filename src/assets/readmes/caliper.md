# caliper

Caliper is volt-per-octave calibration assistant for Norns + Crow.

![screenshot: tuning...](https://synthetiv.github.io/misc/caliper-out.png)

![screenshot: tuned](https://synthetiv.github.io/misc/caliper-in.png)

## how?

Plug in a Crow, patch output 1 to the 1v/oct input of the device you want to calibrate, and plug your test subject's output into Norns's audio input (probably through an attenuator).

If a fundamental frequency can be detected, it will be displayed on screen. 

Turn E2 clockwise to hear a reference tone. Turn E1 to change the reference tone pitch to match the input frequency. Hold K1 for fine control.

Press K2 or K3 to add/subtract octaves at Crow's output, or turn E3 to adjust output voltage to arbitrary values. Check the tuner display and cents offset. If subject's tracking is too wide or narrow, adjust its trimmers accordingly, turn E1 to match pitches again, and repeat.

Hold K2 and K3 to reset Crow output voltage to zero.

## how else?

Choose tracking standard (1v/oct or 1.2v/oct) from the params page.

Set input frequency smoothing (number of samples in running average) from the params page. Higher values will yield a steadier readout at the expense of slower response.

Caliper uses the [Tartini](http://doc.sccode.org/Classes/Tartini.html) UGen, which is more processor-intensive but (in my experience) way more accurate than the Pitch UGen used by Norns/Crone's built-in pitch polling.
