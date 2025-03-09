# warmreload

a norns mod to automatically reload scripts during development.

when enabled, this mod will reload a script anytime there is a change in the `code` directory. this is useful for fast prototyping and development. 

## installation

```
;install https://github.com/schollz/warmreload
```



to activate, go to `SYSTEM > MODS` then select `warmreload` and turn `E2` until you  see a `+` sign. then restart your norns. now anytime you save a script it will reload it.

_note:_ the first time you run a script after enabling, the script will need an internet connection to download [a 4.5 MB binary](https://github.com/schollz/warmreload/releases/tag/v0.1.0) that enables the watch service.

_also note:_ if you are running this on not-a-norns (e.g. norns desktop) then you can still use this script, but it needs to be compiled for your system which is likely not `arm`. assuming you have Golang installed:

```
os.execute("cd /home/we/dust/code/warmreload && go build -v")
```

(any norns user doesn't need to do this, since the binary is already compiled for those norns shields and boxes).
## acknowledgements

I'd like to acknowledge all the mighty inspiring participants of the [habitus](https://llllllll.co/t/stockholm-norns-habitus-workshop-august-12-13-2023/62917) [workshops](https://llllllll.co/t/berlin-norns-habitus-workshop-august-3-4-5-6-2023/62286) - the topic of live reload came up often. I've had a solution for hot reloading while doing development but I've never shared it (mostly because it was sorta complicated), but all the discussions inspired me to push out a simple set-it-and-forget-it mod that accomplishes it.

