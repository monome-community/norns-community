# nice-tapes
A norns mod for more descriptive tape names.

![nice-tapes004](https://user-images.githubusercontent.com/85847646/164801933-05495de2-029d-48ea-a0bf-877de06e149a.png)


## installation

```
;install https://github.com/MentalSandal/nice-tapes
``` 
`nice-tapes` will also be available from maiden's catalog soon.    

More info about mods in general can be found in the [docs](https://monome.org/docs/norns/community-scripts/).


## setup
Head to `SYSTEM > MODS` then select `nice-tapes` and turn `E2` until you  
see a + sign.  
Restart your norns and you're ready to configure your  naming convention.


## configuration
Access the menu by going back to the mods page, selecting `nice-tapes` and  
 pressing `K3`.

You can choose different descriptors that will be added to your tape file names,  
next time you save a tape.

The different options are: 
- *date*     (an internet connection is required to get an accurate date)
- *tempo*     (based on your current clock bpm)
- *script name*     (will be left blank if no script is running)
- *prefix*     a user-defined name/tag. ie. `norns`, `shield`, `sketch`, etc...

If a prefix isn't required, setting it to an empty string will disable it.  
You can recreate the standard naming convention by setting all the options to  `no` and  
the prefix to an empty string. This will result in `####.wav`.

The preview field at the bottom will update automatically as you change options.  
If the name is too long to fit on the display, select the preview and use `K3` to scroll.

## saving 
Setting a prefix or simply validating an existing one by pressing ok in the text entry  
menu will save all the options into a txt file in `dust/data/nice-tapes` so that options  
are recalled after a reboot.
