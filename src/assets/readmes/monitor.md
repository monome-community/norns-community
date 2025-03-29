# Monitor

A **small MIDI utility** to transpose and route midi messages through the Norns. I have this [AKAI midi keyboard](http://akai-pro.jp/lpk25/) that cannot connect directly into my [Elta Polivoks](https://www.eltamusic.com/polivoks-mini), I usually run it through my laptop, but I figured it might be more fun to simply go through the Norns instead. 

The issue was that the Поливокс only listens to one channel, I needed to give my keyboard the power to target a specific channel, and also down-transpose `-24` so it aligns with that weird russian specs. I hope this comes in handy to someone else. :)

Enjoy!

<img src='https://raw.githubusercontent.com/neauoire/monitor/master/PREVIEW.png?raw=true' width='450'/>

### Monitor Controls

- `Knob 2`, change output channel.
- `Knob 3`, transpose outgoing note.

### Sequencer Controls

- `turn knob1`, change length.
- `turn knob2`, change position.
- `turn knob3`, change value.
- `hold key2`, change BPM.
- `hold key3`, change division.
- `press midi key`, change root note.