# graintopia

![six grains](https://repository-images.githubusercontent.com/638070059/b32be6c4-aa7e-43ad-aeed-ed96aa0daa22)

three lands. each land has six grains. each grain moves with physics modeled by 1d kinematics of interlocked elastic beads of random masses. the width of the grain corresponds to the size of the sample. the speed, volume, pan, and direction of the sample is controlled through internalized random oscillations. these oscillations have a macro control, or micro control [if you want to venture into editing the heavily commented code](https://github.com/schollz/graintopia/blob/main/lib/Engine_Graintopia.sc#L66-L78) (encouraged!!).

this script was born out of creating [a sampling demo for the ceti workshop series](https://github.com/schollz/workshops/blob/main/2023-03-ceti-supercollider/lush-sound-baths/workshop.scd#L468-L586). it has [a standalone SuperCollider implementation called Ube](https://schollz.com/tinker/ube/) (though Ube is missing the organic physics controls). its origin is also in [barcode](https://llllllll.co/t/barcode/35297) which has its provenance [in the softcut norns study #3](https://monome.org/docs/norns/softcut/#3-cut-and-poll).

## Requirements

- norns

## Documentation

- e2/e3 changes boundaries
- k2/k3 navigates lands
- e1 changes timescale
- hold k1+k2 to load audio
- hold k1+k3 to record audio
- press k1 to toggle "favorites"
- when in favorites mode: 
-   e1 changes number of grains
-   e2 scrubs favorite
-   e3 creates favorites

check the options to tune things even further. there is an incredible reverb ([a stereo variant from Jon Dattorro implemented by jpcima](https://github.com/jpcima/fverb)) and you can control the "velocity" when switching between favorites for some great performable gestures. 



## Install

install with

```
;install https://github.com/schollz/graintopia
```

after installing and you run, you may be prompted to install additional SuperCollider libraries. 
this has been tested and seems to work on most devices, but let me know if you run into trouble.
