# welcome to norns.community

[![norns community build & deploy](https://github.com/monome-community/norns-community/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/monome-community/norns-community/actions/workflows/build.yml)

[norns.community](https://norns.community) is a collection of open source software for the monome [norns](https://monome.org/docs/norns) sound computer.

This document serves as both the `README.md` for [this repository](https://github.com/monome-community/norns-community) and the 'about' page for [this website](https://norns.community/about).

---

## How do I get my script on norns.community?

First, take a fork of the [community catalog](https://github.com/monome/norns-community), update `community.json` with your script's details, and make a pull request. After your pull request is accepted and merged it will _automatically appear_ on [norns.community](https://norns.community). The website refreshes nightly at 00:00 UTC, on every merge to its `main` branch, or on demand by admins. [This GitHub action](https://github.com/monome-community/norns-community/actions/workflows/build.yml) has all the details.

For script authors, this means:

- your script will appear on the [index](https://norns.community) page
- your author name will appear on the [author](https://norns.community/author) page
- all of your community catalog scripts will appear under your author name
- your script will get its own page, [like this](https://norns.community/3d)
  - your script's README will be displayed on the page
  - your script's cover image will be displayed on the page
- your script will be available for discovery via any tags you added to its community catalog entry, like ["grid"](https://norns.community/tag/grid)
- your script and its tags will appear on the [explore](https://norns.community/explore) page
- if you update your README or cover image in your repository, it will automatically refresh on [norns.community](https://norns.community) within 24 hours

---

## How do I get my README and cover image on norns.community?

These conventions were designed to "just work" with how most scripts are structured today.

READMEs are individually cached from each script's repository in the below cascading sequence. Simply add a README to your project at either of the following locations:

```txt
1. ./doc/index.md
2. ./README.md
```

To ensure maximum resilience, please use [absolute URLs](https://en.wikipedia.org/wiki/HTTP_location) in your docs.

Cover images (aka screenshots) are individually cached from each script's repository in the below cascading sequence. Simply add a cover to your project at any of the following locations:

```txt
1. ./doc/cover.png
2. ./doc/<your_script_name>.png
3. ./doc/screenshot.png
4. ./cover.png
5. ./<your_script_name>.png
6. ./screenshot.png
```

If a cover image is not found in any of the above locations, we then try the local archive before finally using a default image:

```txt
7. ./archive/screenshot/<your_script_name>.png
8. ./assets/images/dust.png
```

The local archive cache is from norns.community v1.0. It was archived in February, 2023.

---

## Can I see an example?

[dronecaster](https://github.com/northern-information/dronecaster) is one of many possible examples of what a compatible script structure might look like:

```txt
./doc/dronecaster.png (this cover will be used)
./engine
./lib
./.gitignore
./LICENSE
./README.md (this README will be used)
./dronecaster.lua
```

---

## What if something is wrong?

[Please open an issue on GitHub.](https://github.com/monome-community/norns-community/issues)

---

## How does this site work?

A [curl](https://github.com/monome-community/norns-community/blob/main/01-curl.sh) script fetches our [community catalog](https://github.com/monome/norns-community). A [build](https://github.com/monome-community/norns-community/blob/main/02-build.py) script then uses that data to construct this [Eleventy](https://www.11ty.dev/) website. It is hosted with Cloudflare Pages on under Tyler Etters's account (todo: transfer to monome).

Additionally, these raw resources are available:

- [https://norns.community/community.json](https://norns.community/community.json)
- [https://norns.community/assets/covers/dronecaster.png](https://norns.community/assets/covers/dronecaster.png) (using `dronecaster` as example)
- [https://norns.community/assets/readmes/dronecaster.md](https://norns.community/assets/readmes/dronecaster.md) (using `dronecaster` as example)

---

## How can I help maintain this website?

If you want to help maintain this website, you can run it locally and test your changes before submitting a [pull request](https://github.com/monome-community/norns-community/pulls).

### Eleventy / HTML / CSS

1. clone repository to your computer
1. using a shell, navigate to the `norns-community` directory with `cd`
1. create a python virtual environment `python3 -m venv venv` & activate it with `source venv/bin/activate`
1. install python dependencies `pip install -r requirements.txt`
1. pull the latest community data and build with: `./00-nuke.sh && ./01-curl.sh && ./02-build.py`
1. install the javascript dependencies `npm i`
1. run the site `npm run dev`
1. tip: see scripts `package.json` for various shortcuts of the above.
1. you can now visit [todo](todo) in your browser

---

## Philosophy

The architecture and technology of this site was inspired by [permacomputing](https://permacomputing.net/) concepts.

---

## Links

- [monome](https://monome.org)
- [llllllll](https://llllllll.co)

---

## Credits

- [tehn](https://github.com/tehn)
- [tyleretters](https://github.com/tyleretters)
- [p3r7](https://github.com/p3r7)
- [dndrks](https://github.com/dndrks)
