# rachim

raw reflections in the rifts.

rachim lets you conduct a 5-piece orchestra, where each piece can play different notes at different times at different volumes. how they play is up to you. 

# requirements

- norns ([version 240221+](https://llllllll.co/t/norns-update-240221))
- crow (optional)

# documentation

- E1: select pattern
- E2: select parameter
- E3: change parameter
- K3: toggle play
- K1+K3: toggle play all

notes are from a scale (change scale in `PARAMS -> scale`), with `1-7` denoting the note and `0` denoting a rest.

the sustain/release is a global control that can be changed (`PARAMS -> fill`).

for crow, the first four pieces are output as v/oct.

## install

install with

```
;install https://github.com/schollz/rachim
```

after installing and you run, you may be prompted to install additional SuperCollider libraries. 
this has been tested and seems to work on most devices, but let me know if you run into trouble.
