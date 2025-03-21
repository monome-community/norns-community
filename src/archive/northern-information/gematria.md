---
title: gematria
description: organized electricity with norns & crow
published: true
date: 2022-05-30T01:25:12.870Z
tags: sequencers, crow
editor: markdown
dateCreated: 2022-05-30T00:45:38.787Z
---

## screenshots

![gematria.png](/community/northern-information/gematria.png)

## docs

```
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A
E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G
M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E
A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M A T R I A G E M
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

## norns                                                 ## crow                   
- key 1:                     exit                       - in  1: clock in, parameters > clock
- key 2:                     gematria.lattice:toggle()  - in  2: unused
- key 3:                     randomize entire matrix    - out 1: organized electricity                     
- enc 1:                     "target"                   - out 2: organized electricity                     
- "clockwise" enc 2:         "wrap"                     - out 3: organized electricity                     
- "counter-clockwise" enc 2: "fall"                     - out 4: organized electricity  
- enc 3:                     "tune"

## maiden
- access everything via table "gematria"
- access lattice api via "gematria.lattice"
- access crow output 1 via "gematria.o1"
- this README uses "o1" as an example but the same commands work for o2, o3, and o4
- each output has an api for use with livecoding via maiden and/or extending the script:
  - gematria.o1.cipher
  - gematria.o1.now
  - gematria.o1.shape
  - gematria.o1.slew
  - gematria.o1.division
  - gematria.o1.enabled

### cipher
- table, eight steps in stringed hexadecimal
- set with "gematria.o1.cipher[1] = A"
- 0 maps to -5v, crow's min
- F maps to 10v, crow's max

### now
- integer, cipher step right now
- set like "gematria.o1.now = 4"

### shape                                     ### slew
- string, default linear                      - floating sequins in seconds, default 1.0
- set like "gematria.o1.shape = rebound"      - set like "gematria.o1.slew = sequins{.1,.2}"
- valid shapes:                               - the sequins are advanced each step
  - linear                                    
  - sine                                      ### divsion
  - logarithmic                               - float, default 1/4
  - exponential                               - the lattice pattern division
  - now                                       - set like "gematria.o1.division = 0.66"
  - wait                                      
  - over                                      
  - under                                     
  - rebound                                   

### enabled
- boolean, default true
- the lattice pattern state
- set like "gematria.o1.enabled = false"
- can also toggle with "gematria.o1.pattern:toggle()"

## troubleshooting
- if crow's tempo isn't working:
  - make sure you have pulses going into input 1
  - jiggle paramters > clock
  - disconnect and reconnect crow
```

## install

from maiden type
`;install https://github.com/northern-information/gematria`

## links

- [view on llllllll](https://l.llllllll.co/gematria)
- [view on github](https://github.com/northern-information/gematria)
{.links-list}