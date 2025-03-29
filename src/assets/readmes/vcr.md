# vcr

a simple Voltage Collection Recall script for norns + grid + crow


## norns

![](assets/vcr-1.png)

#### keys
  * **key 1** - alt
  * **key 2** - navigate to previous voltage set
  * **key 3** - navigate to next voltage set
  * **alt + key 3** - send current voltage set to crow

#### encoders
  * **enc 1** - set voltage 1 for the current voltage set
  * **enc 2** - set voltage 2 for the current voltage set
  * **enc 3** - set voltage 3 for the current voltage set

holding alt will shift focus to a second set of parameters:

![](assets/vcr-2.png)

  * **alt + enc 1** - set slew shape/style for the current voltage set
  * **alt + enc 2** - set voltage 4 for the current voltage set
  * **alt + enc 3** - set slew time for the current voltage set

## grid

![](assets/grid.png)

* **record/play/stop** - multi-function button
  * while dimly lit - press to arm pattern recorder
  * while flashing - press to play pattern
  * while brightly lit - press to stop pattern playback
* **clear** - press to clear your recorded pattern
* **grid alt** - a modifier

* **voltage set buttons** - pressing one of these buttons will select a voltage set, and send it to crow. if the pattern recorder is armed, your presses here, and the time between presses, will be recorded. pressing rec/play/stop again will playback your recorded pattern, allowing you to set up sequences of voltages like lfos
* **grid alt + voltage set** - select current voltage set, but don't send it to crow

the **voltage scope** area represents the four crow outputs, arranged vertically 1-4, and their voltages. the far left of the grid represents -5 volts, the constant dimly lit collumn represents 0 volts, and the far right represents 10 volts. outside of the 0 volt collumn, a dimly lit button represents the destination voltage, while a brightly lit button shows the actual current voltage at crows outputs. your slew time determines how long it will take for the actual voltage to reach the destination voltage.

* **voltage scope** - pressing a button here will set a single coarse voltage (use norns encoders to fine tune)
* **grid alt + voltage scope** - set a single coarse voltage and send it to crow

## crow

crow outputs 1-4 will carry voltages 1-4 from your voltage sets.

-----------
# notes

## pattern recording quick start: 
* press the r/p/s (record/play/stop) button to arm the pattern recorder
* press some of the voltage set buttons
* press r/p/s again to playback your pattern
* press r/p/s yet again to stop playback
* press clear to clear your pattern

_n.b. the pattern recorder only records presses in the voltage set area._

## slew shapes/styles

* 'linear'
* 'sine'
* 'logarithmic'
* 'exponential'
* 'now': ignore slew time, go instantly to the destination then wait
* 'wait': wait at the current level, then go to the destination
* 'over': move toward the destination and overshoot, before landing
* 'under': move away from the destination, then smoothly ramp up
* 'rebound': emulate a bouncing ball toward the destination

