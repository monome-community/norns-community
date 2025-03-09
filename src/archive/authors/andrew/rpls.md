---
title: rpls
description: varispeed multitap echo
published: true
date: 2023-02-12T03:28:35.827Z
tags: delays + loopers
editor: markdown
dateCreated: 2023-02-12T03:26:36.174Z
---

# rpls

![cover](https://github.com/andr-ew/rpls/raw/main/lib/doc/img/rpls_cover.gif)

varispeed multitap echo. 3 taps (1 recording, 2 playing) cycle through 3 buffers. alter the rate of each playback tap independently from the record tap to create sliced rhythmic & harmonic counterpoint from the input signal in real-time, free from tape head collisions & audible clicks.

a spiritual successor to [alliterate](https://github.com/andr-ew/prosody#alliterate).

![rpls.png](/community/andrew/rpls.png)

## hardware

**required**

- [norns](https://github.com/p3r7/awesome-monome-norns) (210927 or later)
- audio input

## install

install from the maiden catalog

or

in the maiden REPL, type:

```
;install https://github.com/andr-ew/rpls/releases/download/latest/complete-source-code.zip
```
## patch notes

### watch

<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/AUcsdTWoAys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<br>

### read

[full patch notes](https://github.com/andr-ew/rpls/blob/main/lib/doc/patch-notes.md)


## documentation

[read here](https://github.com/andr-ew/rpls)

## thx

- @fourhexagons for making [selected public works vol. 5](https://lightbath.bandcamp.com/album/selected-public-works-vol-5) ! the excellent use of (I assume) strymon magneto's shift mode on that album inspired me to revisit the varispeed looping concept that I started on with alliterate, and make it click-free. not sure whether rpls uses the same effect as magneto, but I'm super happy with what I ended up with !
- ezra for softcut + norns core team for the clock system. really felt like I was pushing both systems to weird corners for this script, but they held up so well !


