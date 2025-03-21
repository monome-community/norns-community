# giro

Giro is a performance oriented (a)sync looper.

## Requirements

- norns
- audio input

## Documentation

### Install
;install https://github.com/juhavaaraniemi/giro

### General

- Loops are mono. Input is read from left input of norns.
- Master loops are cut to lenght when pressing play or stop after recording.
- Slave loops are multiples (1-8) of master loops.
- Loops are synced to master loops when playing is started.
- There can be multiple master loops within a loop group which are then asynchronous.
- Rate can be adjusted for loops and they will get async but will be synced again when stopped and started.
- There is a one step undo so it's possible to revert to previous loop state and cancel current recording.

### Screen

<img src="giro.png" alt="screen" width="300"/>

- *white dot* - selected loop
- *number* - loop number, suffixed by c when there is content in the loop
- *status* - status of loop (rec/ovr/play/stop)
- *arc* - loop progress bar
- *vertical bar* - loop level
- *horizontal bar* - loop pan
- *m(number)* - number of master loop e.g. m1
- *x(number)* - number of loop multiples
- *g(number)* - number of loop group
- *G* - group play enabled when visible

### Buttons

- *E1 select loop* - Selects active loop.
- *K2 rec/ovr/play* - 1st press will start rec for empty master loops and overdub for slave loops. 2nd press will play loop. Next press will again overdub.
- *E3 stop* - Stops selected loop.
- *K1+K2 enable group play* - Group play will toggle group play on/off when on there is a "G" in upper right hand corner visible. In group play mode all loops within group start when one loop is started.
- *K1+K3 clear loop* - Clears loop contents.
- *E2 loop level* - Adjusts loop level.
- *K1+E2 loop pan* - Adjusts loop pan.
- *E3 loop group rate* - Adjusts rate for the whole loop group at once.
- *K1+E3 loop rate* - Adjusts rate for selected loop.

### Parameters

- *master loop* - it's possible to slave loop to another loop by selecting corresponding loop number
- *loop group* - loops can be grouped to loop/choke groups so that starting a loop from another group will stop currently playing group
- *loop multiple* - loop can be a multiple of 1-8 to it's master loop. Note: if master loop length * multiples > maximum loop length - multiples will be reduced accordingly
- *level* - loop level
- *pan* - loop pan
- *rate* - loop rate (-2x,-1x,-0.5x,0.5x,1x,2x)

There are toggles for all the buttons so that they can be mapped to e.g. midi foot controller.
- *record/ovr/play*
- *play*
- *stop*
- *stop all*
- *clear*
- *undo*
- *next loop*
- *previous loop*
- *group play*

- *save loops to disk* - contents of the loops will be save to disk from buffer pre of any level,pan,rate adjustments. Loops are saved to folder /audio/giro/ in format giro_sessionidxxxxxx_saveid_yyyyyy_loopz where xxxxxx is a random number for giro session, yyyyyy is a random number for saving time and z is the number of loop - e.g. giro_sessionid489027_saveid118714_loop2.wav.


### Stuff to do next

- Test & fix bugs
- Maybe grid UI for more hands on performance and less menu tweaking

## Thanks

- Norns studies and all who have participated in building those
- Softcut and all who have participated in building it
- @schollz for oooooo and rc505 scripts I have been reading thru and trying to learn something
- @kbra for a couple of useful suggestions for a looper

## license 

mit 
