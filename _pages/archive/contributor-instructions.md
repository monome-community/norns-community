---
title: contributor instructions
description: how to get your scripts added to the site
published: true
date: 2021-08-22T15:46:58.713Z
tags: 
editor: markdown
dateCreated: 2021-03-20T14:48:57.526Z
---

# step 0: 👍 learn the conventions
> **look for info in these green boxes to understand the conventions that _must_ be followed for the [gallery](https://norns.community/en/gallery) to function properly.**
{.is-success}


# step 1: 🗝️ login

welcome! to edit or add new pages to the norns.community wiki, you'll need to log in here: https://norns.community/login

there are two separate login tracks, depending on how you wish to contribute:

- script authors: for those who wish to add documentation for their scripts
- non-scripting editors: for those who wish to modify or create waypoints for catalog exploration. this includes the individual category pages, but can also expand to lists like *scripts which support monobright 8x8 grids*.

this guide is focused on script authors, but the mechanics are similar for editors. the main difference is where you're able to add or edit content.

### author role
- you'll use GitHub to sso into this wiki
- authors can create and edit any page or asset under the `/authors` filetree
- authors can edit (but not create) any page under the `/script-categories` filetree
- authors cannot edit `faq` or `home`

### editor role
- you'll use discord to sso into this wiki (if you haven't already, please join the [norns study server](https://discord.gg/Y2fmdZBAfp) to access this role)
- editors can create and edit any pages under `/script-categories` (and we can add more sections!)
- editors cannot edit `faq`, `home`, or `/authors` pages

# step 2: 🤸 create your author page

from any page click the "new page" icon in the upper menu.

![new-page.png](/meta/new-page.png)

select the `authors` folder and replace `new-page` with your name.

> **if your author name has spaces, replace them with hyphens or underscores.**
>
> so "northern information" becomes "northern-information"
{.is-success}

![enter-your-name.png](/meta/enter-your-name.png)

this creates a "landing page" for your author profile, where people can learn more about your work. use this Markdown template to fill yours out:

```
## bio

if you wanna!

## scripts

<iframe src="https://p3r7.github.io/norns-gallery-render/?author=northern-information"id="gallery-iframe"></iframe>

## links

- [personal site](url)
- [bandcamp](url)
- [GitHub](url)
```

be sure to replace the `author` string in the `iframe` with yours to automatically pull in all your scripts.

> **a small piece of crucial context**
this site features a loosely-coupled integration with a [small clojurescript application](https://github.com/p3r7/norns-gallery) developed by `@eigen` and `@tyleretters`. the application leverages the [wiki.js `GQL` ](https://docs.requarks.io/dev/api) to render collections of scripts in iframes across the site. any reference to `iframes` are talking about this piece of tech.
{.is-info}


# Step 3: 📟 create your script page

> **if your script name has spaces, replace them with hyphens.**
>
> so "molly the poly" becomes "molly-the-poly"
{.is-success}

follow the same steps above for your script page. try to name the page exactly as you've named your script elsewhere (maiden, github, lines, etc.)

> **please nest your scripts under your author page, eg. `authors/justmat/otis`**
your author page doubles as an author *folder* once you add another page under it!
{.is-success}

here is a suggested script template. you can see how this renders, [here](https://norns.community/en/authors/northern-information/dronecaster).

feel free to add or remove whatever sections make sense for your script.

```
## screenshots

![dronecaster.png](/community/northern-information/dronecaster.png)

![dronecaster-controls.png](/community/northern-information/dronecaster-controls.png)

## description

dronecaster is a simple synth to help the community learn [supercollider](https://supercollider.github.io/), the audio synthesis engine of norns.

## install

from maiden type
`;install https://github.com/northern-information/dronecaster`

## links

- [view on llllllll](https://l.llllllll.co/dronecaster)
- [view on github](https://github.com/northern-information/dronecaster)
{.links-list}

## demos

<iframe width="560" height="315" src="https://www.youtube.com/embed/sYnHYDg3rhg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


we recommend using the wiki.js "markdown" editor. if you're new to markdown, you can click the green question mark to get a handy guide:
![markdown.png](/meta/markdown.png)

## adding tags

tags are used to organize data on this site.

> **at least one tag must be added for your script for the iframe galleries to pick it up.**
{.is-success}

![add-tags.png](/meta/add-tags.png)

current tags are:

- `art`
- `audio fx`
- `delays + loopers`
- `drums`
- `generative`
- `granulators`
- `samplers`
- `sequencers`
- `synths`
- `utilities`

> **non-sanctioned tags will be deleted!** if you think a new tag ought to be added let us know. adding new tags requires a small amount of admin work as well as a [pull request](https://github.com/p3r7/norns-gallery/pull/1).
{.is-danger}

## adding i/o icons

additionally, there are six i/o icons available. apply any of these tags to your script and the icons will appear in the iframe galleries:

- `arc`
- `crow`
- `grid`
- `keyboard`
- `midi`
- `mouse`

## adding images

> **at least one `.png` on your script page _must_ be named exactly the same as the script for the homepage gallery to pick it up.**
>
> **additionally**, the image must be hosted here on https://norns.community. this is because our [custom gallery](https://github.com/p3r7/norns-gallery) builds the URL with the following logic:
>
> `"https://norns.community/community/" + <authorname> + "/" + <scriptname> + ".png"`
>
> for example, dronecaster's script page is: `https://norns.community/northern-information/dronecaster`
> 
> so our image _must_ be found at `https://norns.community/northern-information/dronecaster.png`
{.is-success}

> here's how to take a screenshot: https://monome.org/docs/norns/help/#png
{.is-info}

from the editor window click "insert assets"

![insert-assets.png](/meta/insert-assets.png)

> **before moving on, please confirm you are in the `/community/` folder and not in `/root`!**
{.is-success}

under `/community/`, create a folder for yourself using your author name

![create-an-author-directory.png](/meta/create-an-author-directory.png)

> **after your asset folder is created, you'll need to select it in the UI**
{.is-warning}

drag an asset onto the grey box on the right side, then Click "upload"

![upload-assets.png](/meta/upload-assets.png)

after your asset is uploaded, you can select it in the filepicker and click "insert". to delete an asset, click the three dots `...` under *actions*

> fyi, wiki.js can't delete folders yet: https://feedback.js.wiki/wiki/p/delete-folders-in-the-image-file-manager
{.is-danger}

# Step 4: ♨️ get in the index

last step is to add yourself to the [authors index](/authors/index). if you have any trouble, just DM one of the admins. current admins are:

- `@dan_derks`
- `@eigen`
- `@tehn`
- `@tyleretters`