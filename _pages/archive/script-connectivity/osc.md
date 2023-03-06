---
title: OSC
description: open sound control
published: true
date: 2021-10-09T13:45:04.449Z
tags: 
editor: markdown
dateCreated: 2021-10-09T07:44:53.526Z
---

osc is a powerfull way to interract with norns.

you can see it as midi, except that:
- controls are explicitely named instead of relying on `CC` numbers
- works over Wi-Fi, no cables needed!

all parameters present in the param menu at a given time are controllable remotely via OSC.

additionally, scripts can be made to listen to OSC events ([code snippet](https://llllllll.co/t/norns-receive-osc-notes-from-ableton/33772/2)).

For more details, read the [norns osc documenation](https://monome.org/docs/norns/control-clock/#osc).


## touchosc

[touchosc](https://hexler.net/touchosc) is an android/ios/ipados app that allows using your phone/tablet to build OSC control surfaces.

[felart/Norns-TouchOSC](https://github.com/felart/Norns-TouchOSC) templates allow controlling global params.

[toga](/authors/wangpy/toga) and [oscgrid](https://github.com/okyeron/oscgrid) ([lines thread](https://llllllll.co/t/touchosc-templates-for-grid-and-arc/25005)) expend this further by providing a virtual *grid* and *arc*.

## ableton (m4l)

a m4l device was made to allow controlling norns global params quickly from ableton.

[lines thread](https://llllllll.co/t/norns-osc-control-m4l-device/45011)

![screenshot_unfolded](https://llllllll.co/uploads/default/original/3X/6/c/6c0af7b6bf4411afda39ab11b87fae40cd68ad7d.png)

some script also have accompagnying m4l devices:
- [cheat_codes_2](/authors/dan_derks/cheat_codes_2).