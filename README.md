# welcome to norns.community

[![norns community build & deploy](https://github.com/monome-community/norns-community/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/monome-community/norns-community/actions/workflows/build.yml)

[norns.community](https://norns.community) is a collection of open source software for the monome [norns](https://monome.org/docs/norns) sound computer.

this document serves as both the `README.md` for [this repository](https://github.com/monome-community/norns-community) and the 'about' page for [this website](https://norns.community/about).

---

## how do i get my script on norns.community?

first, take a fork of the [community catalog](https://github.com/monome/norns-community), update `community.json` with your script's details, and make a pull request. after your pull request is accepted and merged it will *automatically appear* on [norns.community](https://norns.community). the website refreshes nightly at 00:00 UTC, on every merge to its `main` branch, or on demand by admins. [this GitHub action](https://github.com/monome-community/norns-community/actions/workflows/build.yml) has all the details.

for script authors, this means:

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

## how do i get my README and cover image on norns.community?

these conventions were designed to "just work" with how most scripts are structured today.

READMEs are individually cached from each script's repository in the below cascading sequence. simply add a README to your project at either of the following locations:

```txt
1. ./doc/index.md
2. ./README.md
```

to ensure maximum resilience, please use [absolute URLs](https://en.wikipedia.org/wiki/HTTP_location) in your docs.

cover images (aka screenshots) are individually cached from each script's repository in the below cascading sequence. simply add a cover to your project at any of the following locations:

```txt
1. ./doc/cover.png
2. ./doc/<your_script_name>.png
3. ./doc/screenshot.png
4. ./cover.png
5. ./<your_script_name>.png
6. ./screenshot.png
```

if a cover image is not found in any of the above locations, we then try the local archive before finally using a default image:

```txt
7. ./archive/screenshots/<your_script_name>.png
8. dust.png
```

the local archive cache is from norns.community v1.0. it was archived in February, 2023.

---

## can i see an example?

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

## what if something is wrong?

[please open an issue on GitHub.](https://github.com/monome-community/norns-community/issues)

---

## how does this site work?

this site is built with [Zensical](https://zensical.org), a static site generator. the project is organized into three directories:

- **`src/`** — hand-maintained source files: static assets (CSS, JS, images, icons, favicons), [MiniJinja](https://github.com/mitsuhiko/minijinja) templates, and TypeScript source. this is what you edit.
- **`dist/`** — assembled content directory for Zensical. the [build script](https://github.com/monome-community/norns-community/blob/main/02-build.py) copies `src/` assets here, then generates markdown pages (project pages, tag pages, explore, index, etc.) from `community.json`. this directory is ephemeral and not committed.
- **`site/`** — final HTML output. Zensical compiles everything in `dist/` into static HTML here. this is what gets deployed to [GitHub Pages](https://pages.github.com).

the build pipeline:

1. `01-curl.sh` — fetches `community.json` from the [community catalog](https://github.com/monome/norns-community)
2. `02-build.py` — copies `src/` to `dist/`, fetches cover images and READMEs from GitHub, generates markdown pages in `dist/`
3. `03-zensical.sh` — runs `zensical build` to compile `dist/` into `site/`

additionally, these raw resources are available:

- [https://norns.community/community.json](https://norns.community/community.json)
- [https://norns.community/covers/dronecaster.png](https://norns.community/covers/dronecaster.png) (using `dronecaster` as example)

---

## how can i help maintain this website?

if you want to help maintain this website, you can run it locally and test your changes before submitting a [pull request](https://github.com/monome-community/norns-community/pulls).

### setup

1. clone repository to your computer
2. install [Python](https://www.python.org/) (3.10+)
3. create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
4. install dependencies: `pip install zensical aiohttp aiofiles`

### build & serve

1. fetch community data and build pages: `./01-curl.sh && ./02-build.py`
2. build the site: `./03-zensical.sh`
3. preview locally: `zensical serve`
4. visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

tip: see `package.json` for shortcuts. `npm run ncb` runs nuke + curl + build. `npm run dev` starts the dev server.

### TypeScript / JavaScript

there is a single TypeScript file (`src/javascripts/script.ts`) that is used to enable filtering on the "explore" page. it compiles to `src/javascripts/script.js` in the same directory.

install TypeScript and watch the file with:

1. `npm i`
2. `npm run tsc`

the build process assumes the transpiled JavaScript is already in `src/javascripts/` (it gets copied to `dist/` during the build). perform all the `npm` actions locally.

---

## philosophy

the architecture and technology of this site was inspired by [permacomputing](https://permacomputing.net/) concepts.

---

## links

- [monome](https://monome.org)
- [llllllll](https://llllllll.co)

---

## credits

- [tehn](https://github.com/tehn)
- [tyleretters](https://github.com/tyleretters)
- [p3r7](https://github.com/p3r7)
- [dndrks](https://github.com/dndrks)
