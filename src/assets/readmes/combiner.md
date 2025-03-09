# Combiner
Combine 2-127* Grids into a virtual grid available to all scripts

### What you can do with it
- Combine smaller Grids into a standard 128 or 256 size.
- Make non-standard layouts like 32x8 or a Grid with gaps.
- Mirror Grids so two can play at once.
- Set rotation (including 16x8 vertical) and LED 'intensity'.


### Requirements
- Norns 231114

### How to use it
1. Install from the Maiden project manager (or `;install https://github.com/dstroud/combiner`)
2. Enable the mod in SYSTEM>>MODS>>E3 (+ symbol) and restart.
3. Edit your layout in SYSTEM>>MODS>>COMBINER>>K3.
	- First, arrange your physical Grids however you want.
	- Press column 1, row 1 to place the first Grid. It will detect orientation.
	- Add new Grids by *holding* the corner of any placed Grid and tapping an adjacent corner of the new Grid.
	- To change additional settings, tap the center of a Grid to select it and use E2 (navigation) and E3 (change).
4. The virtual Grid will appear in appear to scripts on port 1 (default for most scripts).


### Notes
- Grids do not have to be added in SYSTEM>>DEVICES>>GRID. Only add them there if you want them to be available *in addition to* the virtual grid on port 1.
- Any Grid that you touch while in the mod menu is "enabled" as part of the virtual Grid's pool of devices. Use K3 to toggle this manually.
- K1+E3 enables fine editing of x/y offsets.
- LED intensity is not supported on all devices.
- If using a NeoTrellis, each device must have a unique name+serial in SYSTEM>>DEVICES>>GRID. This may require editing your .ino file and re-uploading the firmware.

### To script authors
- Sorry.
- Mirroring can result in repeat key down/up events (e.g. if the same key is held on two Devices). Feel free to not care.
- Combiner will call the `grid.add` callback when the virtual Grid changes so you can detect column/row changes with something like:

```lua
function grid.add(dev)
  cols = g.cols
  rows = g.rows
end
```


*Okay I've tested with 4 Grids. Prove me wrong.