---
title: pirate-radio
description: community radio for norns
published: true
date: 2022-01-12T08:59:46.696Z
tags: art, utilities, 16n
editor: markdown
dateCreated: 2022-01-09T23:19:58.362Z
---

![pirate-radio.png](/community/jaseknighter/pirate-radio.png)

# pirate radio

### background
pirate radio is a norns script running a pirate internet radio station that streams content, audio, weather and music that’s contributed from the lines community directly to your norns (uploader link below). 

it also adds some additional features such as an equalizer, visualiser, commenter, timewarper and effects.

this was initiated as an educational project that teamed up folks who had expertise in creating norns scripts with folks who were interested in learning about scripting. 

### requirements
a norns device connected to the internet

### download
download from the maiden library 

or run: `;install https://github.com/norns-study-group/pirate-radio`

### instructions 
#### first time starting

the first time you start the *pirate radio* it will take a minute. it will first install necessary linux tools if not already installed (`vorbis-tools`, `espeak`, `ffmpeg` and `lame`). afterwards, it will download available playlists for the different stations.

#### uploading your own music

goto [coffer.norns.online/](https://coffer.norns.online/) to upload your own tracks. simply select a station and choose the files. optionally, you can add some information about the artist and other info.

#### listening to the radio

once the radio is initiated, you'll see a dial. use **E3 to move the dial**. once you hit upon a station you should see the frequency get brighter and the 'magic eye' get smaller. some stations also have  graphics that will appear.

![image](https://user-images.githubusercontent.com/6550035/146977370-3edbabcc-19d9-4bdc-8f60-975a195ed582.png)

![image](https://user-images.githubusercontent.com/6550035/146977129-67f6be4a-2723-4859-baac-4028fd221a62.png)

once the radio station is dialed in you should stop hearing radio static and start hearing the radio. 

#### equalizer

use **E1 to change to the equalizer page**. on this page **K2 and K3 change equalizer preset** or you can use **E2 and E3 to customize the bands** of the equalizer.

![image](https://user-images.githubusercontent.com/6550035/146977701-71f3a645-10c0-4bc4-a71f-43dbfb585863.png)

#### visualizer

the visualizer shows the relative power of each band. use **E1 to change to the visualizer page**.

![image](https://user-images.githubusercontent.com/6550035/146977835-8c8f11d7-ee18-4af9-a423-ab20bde89016.png)

#### commenter

the commenter doesn't do anything yet. use **E1 to change to the commenter page**.

![image](https://user-images.githubusercontent.com/6550035/146977995-44e798f1-18d9-484b-a6f7-b7185691b64f.png)

#### timewarper

the timewarper lets you change, slow down, and reverse time, as well as loop time points. use **E1 to change to the time-warper**. 

![image](https://user-images.githubusercontent.com/6550035/146978108-1ebdf958-bafe-42b3-af1a-19defbe69ff5.png)

to make a loop, **press K2 twice to set start and end points**. once a loop is created, you **press K2 to deletel loop**. 

**press K3 once to get back to "live" audio**.

rotating **E2 will slow down and speed up time**. rotating **E3 will change position in time**. as of now, you cannot go into a time in the future.

use the norns TAPE to record your remixed audio.

#### effects

in addition to the normal compressor and reverb available on the norns, there are other effects available to add to the pirate radio. go into the parameters menu and you will see delay and granulator effects:

![image](https://user-images.githubusercontent.com/6550035/146978638-4cf5afc0-648b-4e48-b731-c3d1db2998bf.png)


### known issues
#### installing on fates
there have been reports of fates devices failing to play stations. the root cause is still under investigation, but people have resolved the issues by following these steps:

* install pirate-radio
* run the reinstall command for libraspberrypi0 as recommended on https://linuxaudiofoundation.org/troubleshooting-general/
* in maiden, delete the files in the directory `/dust/data/pirate-radio/metadata`
* put the device to sleep and power it back on

### reporting bugs
report bugs on the [lines forum thread](https://llllllll.co/t/pirate-radio/49013) or [discord channel](https://l.llllllll.co/pirate-radio)

please include the following details:

* device type: norns/shield/fates
* norns version number
* output from the matron tab (using the hiding feature)
`[details="matron output"]
*matron output goes here*
[/details]
* output from the supercollider tab (using the hiding feature)
`[details="supercollider output"]
*supercollider output goes here*
[/details]

