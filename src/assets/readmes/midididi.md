# midididi mod

a norns mod to record and playback midi cc loops.

best friends with your faderfox or midi fighter twister, and should work with any midi controller that can send ccs and note on/off.

## demo

[![midididi demo](https://img.youtube.com/vi/_Mm79ezd1Oc/0.jpg)](https://www.youtube.com/watch?v=_Mm79ezd1Oc)

this is playing awake, but this mod can be used with any norns script (in theory, i haven't tested them all lol)

## instructions

- install the mod, enable it, and restart norns
- choose your device in the SYSTEM > MODS > MIDIDIDI menu
    - this setting is global across scripts
- ensure that your device can send midi cc and note values simultaneously:
    - if you have a faderfox EC4 (like i do) then you'll need to [update to firmware v2.0](http://www.faderfox.de/ec4.html)
    - if you have a midi fighter twister, you'll need to configure it to send note on/off as the push event (the default is cc)
- configure your midi device note and cc values:
    - the note id must match the cc id for the given param
    - the midi channels must be the same

## current shortcomings/future features
- note on/off must be mapped to the same midi channel and cc id as the cc to be recorded. ideally this would be configurable
- only supports a single device. if you would like multi device support, let me know
- does not support relative midi values
- cannot map new parameters while loops are playing (not sure why you'd want to do this but i tried)

## acknowledgements

- thanks @mmckegg for the idea, which i stole from [loopdrop](https://github.com/mmckegg/rust-loop-drop)
- also thanks @alanza @dan_derks @sonoCircuit for [reflection lib](https://monome.org/docs/norns/reference/lib/reflection) which made developing this super buttery
