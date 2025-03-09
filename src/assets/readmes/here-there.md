# HERE/THERE
norns listens to sound input for the first ~30 seconds and then plays back the following:    
 (a) up to 32 sine waves with random parameters, randomly spaced in the stereo field, in [currently] two modes: "chords" and "drones"     
 (b) two separate softcut buffers (l/r, based on inputs), at random positions [currently] in time with the sine actions   
 (c) granular buffer with random parameters   
   
## Controls   
k2: change sine mode  
k1(hold) + k2: reset softcut buffer   
k3: clear/freeze sines and begin polling again  
k1(hold) + k3: randomize granular parameters  
e1: sines volume      
e2: softcut volume  
e3: granular volume/speed    

TODO:   
- Grid controls (sines)  
- UI/screen integration   
- selectable polling time/frequency
- more control over durations
