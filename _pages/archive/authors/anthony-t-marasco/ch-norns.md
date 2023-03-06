---
title: ch-norns
description: share control data and collaborate between norns, max, pure data, the web, and arduino 
published: true
date: 2022-06-29T18:39:35.974Z
tags: utilities, mods
editor: markdown
dateCreated: 2022-04-16T06:19:21.540Z
---


## screenshots
![ch-norns.png](/community/anthony-t-marasco/ch-norns.png)


## description

ch-norns is a mod and server package that allows your norns to share control data between software instruments built in max, pure data, and web pages, as well as hardware built using wifi-enabled microcontrollers. ch-norns brings the features of the [collab-hub](https://www.collab-hub.io/) framework to your norns, allowing you to design cross-platform, collaborative networked performances where data sent from your norns can modulate the parameters of any other connected instrument,and vice-versa. this opens the possibility for cross-platform jam sessions where users can modify each others software or hardware instruments from around the world. [click here](https://www.collab-hub.io/details/) to learn more details about collab-hub, download clients for other platforms, and to see examples of how it works.

## documentation
ch-norns (and collab-hub as a whole) works within a client-server architecture. when in use, ch-norns allows you to connect to the remotley-hosted collab-hub server as a 'client.' while connected, you can use the ch-norns mod menu to manage aspects of your connection (including who you can and cannot receive/send data from/to), create new indentifying headers to tag onto data you send, and get information on available users and groups of users available to collaborate with. you can check your connection to the collab-hub server and test sending/getting data by opening the [ch web interface](https://ch-server.herokuapp.com/) in any web browser on a computer or mobile device (scroll to the middle of the page to see a list of connected users and scroll back to the top to montior any data messages received by the server).

### how it works
as a mod, ch-norns runs in the background while you perform with other scripts. from the ch-norns menu, you can connect to the collab-hub remote server by setting your username and selecting the `CONNECT >` option. when the ch-norns graphic pops up in the lower right corner, you'll be online and able to send and receive data to any other currently-connected collab-hub users. from here, ch-norns uses the inherent ability to globally control the parameters of your currently loaded script through osc to allow your fellow collab-hub users to modify your instrument in a performance. 


## install

**ch-norns will soon be available for beta testing by the norns community at the end of july 2022. more information on downloading the package and submitting feedback will be posted here and on the [lines forum](https://llllllll.co/), so please check back then.**



## demos

**coming soon!**

<iframe width="560" height="315" src="" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>