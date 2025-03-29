# shfts
2-voice shift registers for norns &amp; grid

## details
~~~
-- shfts
-- 2 voice double binary shift register
-- + midi + dual quantizers
--
-- enc1: bpm
-- enc2: voice 1 pitch offset
-- enc3: voice 2 pitch offset
-- key2: start/stop voice 1
-- key3: start/stop voice 2
-- 
-- Midi device/channel output can be set per voice in params
-- Crow support - clock in on input 2
-- gate/pitch out on cv pairs 1/2, 3/4
-- 
-- GRID UI
-- 2 identical voices, 8 columns each
-- row 1 - pitch register bit display
-- row 2 - trigger register bit display
-- row 3 - clock division
-- row 4 - trigger bias (more triggers to the right)
-- row 5 - pitch rate of change (more change to the right)
-- row 6 - trigger rate of change (more change to the right)
-- row 7 - quantizer presets - hold a button and press keys from row 1-6; 
-- layout is perfect fourths vertical, chromatic scale horizontal
-- a nice pentatonic scale:
--    0 X 0 0 0 0 0 0
--    0 X 0 X 0 0 0 0
--    0 X 0 0 X 0 0 0
--    0 0 0 0 0 0 0 0
-- row 8 :
-- -- col 1: 1 start/stop clock
-- -- col 2: single-step register 
-- -- col 3: reduce loop length
-- -- col 4: increase loop length
-- -- col 5-8: pitch range (1-4 octaves)
-- all controls repeated on columns 9-16 for voice 2
-- this should work with a 8x8 grid I think?
~~~

## TODO (roughly in order)
- document grid layout (in the meantime the norns screen is pretty descriptive)
- test 2-channel quantizer
- save quantizer presets
- some subtle white-key/black-key display in the quantizer 

## license
CC Attribution-NonCommercial-NoDerivatives 4.0 for now, since I am rushing this out a bit ahead of schedule and haven't had a chance to think about rights much.  If you want to use this code, get in touch - if it's legit I'm happy to grant a more permissive license as needed.