# torii

*torii - a traditional Japanese gate which symbolically marks the transition from the mundane to the sacred*

__Gated audio sequencer for norns__

v0.5.6 @okyeron

Send audio in, each step gates the audio.


__Requirements:__
  * norns version 200424 (for global clock)
  * audio in
  * R library - https://github.com/antonhornquist/r

__Optional:__
  * Grid


__Controls:__  

K2 : randomize sequence  
K3 : bypass gates  

E1 : change BPM  
K1 HOLD + E1 : change seq length  
E2 : change edit step  
E3 : change filter amt per step  

See Params menu for clock divider, envelope values, filter envelopes, delays, etc.  (and Mapping those to MIDI)

MIDI Start/Stop/Continue are supported

Sequence length is 1 to 32.  

__Grid controls:__

Row 8 buttons are the sequence steps

Rows 1-7 are a level amount for filter per step
Row 7 will clear the env amount if hit while selected

For sequences longer than 16, scroll the grid side to side with E2

