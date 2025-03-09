# clipper
slice and save samples for monome norns

## instructions

### key/encoder controls
access instructions for key/encoder controls within the script by pressing k1 + k3

* All screens
  * e2: next/prev control
* Screen 1: select/play sample 
  * k2: select sample to slice up
  * e3: incr/decr playhead
  * k3: start/stop playhead
* Screen 2: play mode
  * k2/k3: delete/add cutter
  * e3: change play mode
* Screen 3: adjust cut ends
  * k2/k3: delete/add cutter
  * k1 + e2: select cutter
  * k1 + e3: adjust cutter
  * k1 + e1: fine adjust cutter
  * e3: select cutter end
* Screen 4: move cutter
  * k2/k3: delete/add cutter
  * k1 + e2: select cutter
  * k1 + e3: adjust cutter
  * k1 + e1: fine adjust cutter
* Screen 5: adjust rate
  * k2/k3: delete/add cutter
  * k1 + e2: select rate
  * e3: adjust all cutter rates
  * k1 + e1: fine adjust rate
  * k1 + e3: adjust selected cutter rate
* Screen 6: adjust level
  * k2/k3: delete/add cutter
  * e3: adjust level
* Screen 7: autogenerate cutters
  * e3: autogenerate clips by level (up to 20)
  * k1 + e3: autogenerate clips with even spacing (up to 20)

### recording clips
clips may be recorded from the PARAMETERS>EDIT menu. what gets recorded depends on the `play mode` setting:
* *stop*: record the entire sample 
* *full loop*: record the entire sample 
* *all cuts*: record all sample areas set by cutters
* *sel cut*: record the sample area set by the selected cutter

*important note*: if *play mode* is set to `all cuts`, all *rate* settings must either be positive or negative. 

## requirements
norns

## credits
many thanks to @schollz and @catfact for their excellent coding advice.
