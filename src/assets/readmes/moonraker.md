# MOONRAKER

explore a galaxy of rhythm.


![moonraker](https://user-images.githubusercontent.com/6550035/149183571-4a89882f-17ba-4d0a-8b20-dfed75a740d1.png)



this is a deviation/fork/sequel/derivation of [goldeneye](https://llllllll.co/t/46556) (thank you @tyleretters for your illustrious goldeneye script and providing the most perfect of names for this script!). 

rhythms are generated using random selections of drum samples with stochastic patterns that emerge from modulo math and also continually evolve through periodic mutations.



## Requirements

- norns
- grid (optional)
- at least 200 MB of disk space (for downloaded samples)

## Documentation


***quick start***

press K3 to start. press K2 to regenerate beat. 

save beats with K1+K3 and return to them with K1+K2.



https://vimeo.com/665254703

***the user manual***

- E1 removes/adds instruments
- E2 changes filter
- E3 mutes banks
- **K2 regenerates samples** (the only one you really need)
- K3 starts/stops
- K1+E1 changes slot
- K1+K2 loads in slot
- K1+K3 saves in slot

turn the `PARAMS > mutation rate` to `0` if you want to completely freeze the pattern. otherwise patterns will continuously change...forever.


***the technical manual***

moonraker has eight banks (kick, snare, rim, hat, ride, shaker, perc, risers) each containing 112 samples, for 896 samples in total. each sample is initiated with random characteristics (lpf cutoff, hpf cutoff, attack, decay, sample start, pan, amplitude, delay send, reverb send). upon regeneration, samples are randomly activated (or activated with E1).

during playback, each beat is counted and a modulus is computed against each active sample. each sample contains modulus numbers and inverse modulus numbers. an active sample is *played* when any modulus number computed against the current beat has no remainder. however, the inverse modulus do the opposite - whenever their computed modulus has no remainder then the playing of the current active sample is reversed. the randomly assigned modulo numbers are all prime numbers (with exception for two numbers: *1* and *4*). modulo numbers are randomly changed at a rate corresponding to the `PARAMS > mutation rate`.

***using the grid***

the grid is optional. using it will allow you to edit the parameters of specific samples. here is a short tutorial on how to use the grid.

https://vimeo.com/665856265


![m1](https://user-images.githubusercontent.com/6550035/150999017-de8bddfd-02ad-4f1d-9738-e3d75aac856f.png)

![m2](https://user-images.githubusercontent.com/6550035/150999013-56a3f6e9-afda-4abd-966e-6e7238a19560.png)

thank you @rebuspop for the amazing Grid layout tutorial!

## Install

install using with

```
;install https://github.com/schollz/moonraker
```

after installing, make sure you install the 100 MB of samples with this command in maiden:

```
os.execute("cd ~/dust/audio && echo 'downloading...' && wget -q https://github.com/schollz/moonraker/releases/download/samplepack1/moonraker.zip && unzip moonraker.zip && rm moonraker.zip; echo 'ready (make sure to restart)'")
```
