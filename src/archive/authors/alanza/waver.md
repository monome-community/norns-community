---
title: waver
description: 
published: true
date: 2021-10-06T03:03:10.061Z
tags: utilities
editor: markdown
dateCreated: 2021-10-06T02:44:23.619Z
---

# waver

assemble a song from TAPE

![waver.png](/community/alanza/waver.png)

The purpose of waver is to give Norns the capability of a basic DAW, inspired by the OP-1’s tape and powered by softcut. There are four mono tracks which can be panned individually. The tape has a length of 5 minutes. There are two views: song and track. In song view, all four tracks are visible and audible. This view is for previewing, navigating and planning. In track view, a preselected track and a “scratch work” track are visible and audible, allowing you to stage changes to the given track. More about track and song view in the documentation below.

## Requirements

- norns

## Documentation

In waver's `song` and `track` views, a small 'minimap' appears at the top of the screen, showing the portion of the tape currently in the window, the loop markers, and the playhead. Below this are barline markers, which are numbered, and (provided sufficient zoom), beats, which are unnumbered. **These are only a visual aid:** waver currently has no warping or repitching, so changing the tempo in PARAMS will not affect the position or pitch of audio currently on the tape. Below this are the relevant tracks for the mode, in `song` view, all four tracks are visible. In `track` view only the currently active track and the "scratch work" track are visible. Depending on your settings, this part of the screen will contain one or more of the loop markers and possibly the playhead.

The following apply to both `song` and `track` views.
#### View
- E1 scrolls the portion of the window in view.
- E2  zooms in and out
- E3 chooses the active track
#### Settings
- K1 + E1 moves the playhead
- K1 + E2 moves the loop start marker
- K1 + E3  moves the loop end marker
- K2 toggles playback
- K3 toggles looping
#### Song View
- long K1 saves track
- K1 + K3 enters track view
- K1 + K2 is "undo": it returns to track view of the last active track with the last set of changes offloaded to the "scratch work" track. **NB:** there is only one level of undo, no undo history, and entering track view with K1 + K3 will destroy it.
#### Track View
- long K1 loads sample into scratch track
- long K2 cuts loaded sample between the loop markers, discarding the rest
- long K3 pastes what was cut earlier at the playhead
- K2 + E2 adjusts the level of the currently selected track (use E3 to switch between the tape's track and the "scratch work" track)
- K2 + E3 adjusts the panning of both tracks
- K1 + K3 commits the current changes, mixing the "scratch work" track together with the tape's track and exits to `song` view.
- K1 + K2 discards the current changes and exits to `song` view

## download

```
;install https://github.com/ryleelyman/waver
```


