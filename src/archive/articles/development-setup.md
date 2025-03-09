---
title: development setup
description: 
published: true
date: 2022-12-11T20:52:08.380Z
tags: 
editor: markdown
dateCreated: 2021-05-13T10:43:10.910Z
---

## maiden

Using maiden in the web browser is the most straightforward way.

just access norns via http://norns.local

it provides both a [file brower + editor](https://monome.org/docs/norns/maiden/#file-viewer) and a [REPL](https://monome.org/docs/norns/maiden/#repl) (shell) allowing you create and edit scripts, launch them an see their output.


## remote access via command line

### basics

One can directly hop onto norns via [SSH / USB serial](https://monome.org/docs/norns/wifi-files/#advanced-access).

Then, script can be edited directly with prefered editors (such an `nano` or `vi`).

The maiden REPL can also be spawned [from the command line](https://monome.org/docs/norns/maiden/#advanced-access).

Here is a walkthrough of the process:

<iframe width="560" height="315" src="https://www.youtube.com/embed/1A5-bqgYPyQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### sshfs - mount source files locally

sshfs allow to locally mount remote norns filesystem as if it was local, allowing you to use any prefered local editor.

```shell
mkdir /home/Documents/norns_mount
cd /home/Documents/norns_mount
sshfs we@norns:/home/we/dust dust
```

Depending on your editor of choice, some more optimal options might be available (see bellow).


### maiden-run - automatic reload

[maiden-run](https://github.com/ngwese/maiden-run) allows to automatically reload  a script when saving its source code. 


## editor integration

All those setup allow interacting with norns at the confort of your familiar editor runing on you main computer.

### atom

This [comment](https://github.com/monome/norns/issues/1067#issuecomment-611732427) describes a working setup for remote integration with atom.

### emacs

to enable Lua and supercolider support:

```elisp
;; lua

(use-package lua-mode
  :init
  (setq lua-indent-level 2))
  
;; sclang

(defvar my-supercolider-scel-path "~/.local/share/SuperCollider/Emacs/scel")

(let ((sclang-dir (concat my-supercolider-scel-path "/el")))
  (when (file-directory-p sclang-dir)
    (normal-top-level-add-to-load-path (list sclang-dir))))

(when (and (locate-library "sclang")
           (locate-library "sclang-vars"))
  (use-package sclang
    :ensure nil
    :demand))
```

Emacs can access norns filesystem as if local using [TRAMP](https://www.gnu.org/software/tramp/).

```shell
	M-x find-file
  /ssh:we@norns.local:/home/we/dust/
```

to prevent having to re-type the password each time, put this line in your `~/.authinfo`:

```conf
machine norns.local login we port ssh password sleep
```

TO launch the REPL, you can spawn follow [cli isntructions](https://monome.org/docs/norns/maiden/#advanced-access) after spawning a remote shell using either:
 - `tramp-term` (built-in `term` + [tramp-term](https://github.com/randymorris/tramp-term.el))
 - `vterm-toggle-cd` ([vterm](https://github.com/akermu/emacs-libvterm) + [vterm-toggle](https://github.com/jixiuf/vterm-toggle))

### VSCode

COde on norns can be accessed as if locally using [Remote - SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh).

[@midouest](https://norns.community/en/authors/midouest) made a [vscode extension](https://llllllll.co/t/norns-repl-vscode-extension/41382) to spawn and interact with a remote maiden repl session from vscode.

### vim / neovim

[vim-norns](https://github.com/madskjeldgaard/vim-norns) provides various commands to spawn and interract with a maiden REPL.

[scvim](https://github.com/supercollider/scvim) for supercollider syntax.


## supercollider

### installing extension classes (ugens...)

Simply drop them into `/home/we/.local/share/SuperCollider/Extensions/`.

Subfolders are allowed.

see [sc doc](https://doc.sccode.org/Guides/UsingExtensions.html) for more info.

### norns engines on desktop

first, you'll need to copy both your engine code & [norns' supercollider sources](https://github.com/monome/norns/tree/main/sc/core) into your supercollider extensions folder (or any subfolder). in scide, you can find the extensions path by running `Platform.userExtensionDir;`. recompile your class library & you should hear a familiar tone on boot.

using this strategey, you can use your engine `.sc` class code as-is and test out commands in a seperate `.scd` file using `CroneTester`. first, set the engine - `CroneTester.engine('myengine');` - then send a command `CroneTester.cmd('mycommand', [array, of, arguments]);`. for midi-like code you can use a snippet like this:

```sclang

MIDIdef.noteOn(\keybOn, {
    arg vel, nn, chan, src;
    CroneTester.cmd('noteOn', [nn, nn.midicps, vel]);
})
MIDIdef.noteOff(\keybOff, {
	  arg vel, nn;
    CroneTester.cmd('noteOff', [nn]);
});
```

See also: [Mac OS specific instructions](https://gist.github.com/mimetaur/18346a71f1444ec8bea98a0c3c6fa365)

### controlling local supercollider with norns

patch value of `ext_addr` / `ext_port` in function `o_init` in `/home/we/norns/matron/src/oracle.c` to point to your desktop IP.

[original comment](https://discord.com/channels/765746584582750248/789941892812242954/835437953781202954).