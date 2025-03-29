---
layout: project
title: nc03-ds
permalink: /nc03-ds
cover: nc03-ds.png
raw_name: nc03-ds
sanitized_name: nc03-ds
project_url: https://github.com/monome-community/nc03-ds
description: norns/circle/03 dressed in sequins
discussion_url: https://llllllll.co/t/norns-circle-03-dressed-in-sequins/57649
documentation_url: 
tags:
 - art
authors:
 - norns-community
redirect_from:
 - /en/authors/norns-community/nc03-ds
 - /authors/norns-community/nc03-ds
---
# (norns/circle/03) dressed in sequins

> a gathering— a group study where participants each create a script according to a prompt. scripts are submitted by an established deadline. discussion and help will be provided to facilitate completion of scripts.
>
> this series will focus on softcut. for an introduction, see [softcut studies](https://monome.org/docs/norns/softcut/). for general norns scripting, see [norns studies](https://monome.org/docs/norns/studies/). this edition will also extensively use [sequins](https://monome.org/docs/norns/reference/lib/sequins).
>
> upon completion we will release the pack of scripts as a collection along a bandcamp compilation of captures from each script. see [the collected past gatherings](https://llllllll.co/t/norns-circle-collected/30411).
>
> we’ll be here throughout the process to assist everyone in getting scripts working. please ask questions -- this is an ideal time to learn.
>
> future prompts will have different parameters. don’t go overboard building out your script with extra functionality -- try to stay close to the prompt.

### norns/circle/03 dressed in sequins

(nb. requires [norns: update 220802](https://llllllll.co/t/norns-update-220802/57563))

construct an evolving expression of rhythmic time using provided synth drum samples, the new [lfo library](https://monome.org/docs/norns/reference/lib/lfo), and [sequins](https://monome.org/docs/norns/reference/lib/sequins).

- 7 sample groups with 9 variations are provided
- no USB controllers, no audio input, no engines
- map
	- E1 volume
	- E2 cadence
	- E3 horizon
	- K1 stability
	- K2 relax
	- K3 bind
- visualization of data

parameters are subject to interpretation. "stability" could mean timbral parameter randomization, but perhaps something else. "horizon" could mean the navigation of changes to rhythmic balance, but perhaps something else. "relax" and "bind" could mean a stop/play mechanism, but perhaps something else.

see the [lfo docs](https://monome.org/docs/norns/reference/lib/lfo) for additional details on the lfo library.  
see the [sequins docs](https://monome.org/docs/norns/reference/lib/sequins) for additional details on the sequins library.  
see the [softcut helper readme](https://github.com/monome-community/nc03-ds/blob/main/softcut_helper-readme.md) for additional details on the optional softcut helpers including in the `lib` file.

---

deadline: **oct 1**

submit your script by submitting a PR to github: https://github.com/monome-community/nc03-ds (we will help with instructions when the time comes, or feel free to submit early)

record 2-3 minutes of the output of your script using TAPE. feel free to use the built-in reverb and compessor. upload to google drive, dropbox, etc. post link on thread.

---

to get started, go to maiden’s project manager, refresh the collection, and install `nc03-ds`. note, this will take some time to download as it includes some audio files.

if you need a place to start from, check out [`scarlet.lua`](https://github.com/monome-community/nc03-ds/blob/main/scarlet.lua)
