---
title: tweaks
description: small tweaks for your norns
published: true
date: 2021-09-20T02:06:02.394Z
tags: 
editor: markdown
dateCreated: 2021-05-19T15:14:28.273Z
---

This section lists advanced patches and tweaks that could get applied to norns.

Use at your own risk, and be aware that those could get reverted by updates.


## additional audio ports via USB

[connect-opz](https://github.com/xmacex/connect-opz) ([lines thread](https://llllllll.co/t/connect-opz-using-usb-audio-with-norns/37819)) is the most advanced attempt at this, doing most of the heavy work by modifying the `jackd` routing.

Made to work with a Teenage engineering OP-Z, but may be adaptable to other USB audio interfaces.


## decrease encoders sensitivity globally

depending on encoder knob diameter, encoders may feel a bit too sensitive or not enough.

[nmEncoderTest](https://github.com/TuesdayNightMachines/nmEncoderTest) allows you to interactively test sensitivity settings.

Patching allows us to tweak their values `/home/we/norns/lua/core/encoders.lua` ([original source](https://github.com/monome/norns/blob/main/lua/core/encoders.lua)).

global menu sensitivity of each encoder can be tweaked with var `encoders.sens`.

default script sensitivity of each encoder can be tweaked with var `sens`.

Values go from 1 (high sensitivity) to 16 (low).

We can prevent scripts from setting their knob sensitivity by overriding function `norns.enc.sens`:

```lua
norns.enc.sens = function(n,s)
    if(_menu.mode == false) then norns.encoders.set_sens(n,s) end
end
```

Please note that some scripts may use threshold on the delta values of encoders turns to tweak their sensitivity, which is less patchable globally.


## make arc act as encoders

globally, patch function `_norns.arc.delta` in `core/lua/arc.lua`:

```lua
_norns.arc.delta = function(id, n, delta)
  if n == 3 or n == 4 then -- only arcs 3 & 4
    _norns.enc(n - 1, delta/16) -- acting as e2 / e3
    return
  end
  -- [rest of function ...]
end
```  

[original message](https://discord.com/channels/765746584582750248/825387870873190410/841843403620614165)

for a single script, use [arcify](https://llllllll.co/t/arcify/22133).