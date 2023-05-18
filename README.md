# welcome to norns.community

[![norns community build & deploy](https://github.com/monome-community/norns-community/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/monome-community/norns-community/actions/workflows/build.yml)

[norns.community](https://norns.community) is a collection of open source software for the monome [norns](https://monome.org/docs/norns) sound computer.

This document serves as both the `README.md` for [this repository](https://github.com/monome-community/norns-community) and the 'about' page for [this website](https://norns.community/about).

---

## How do I get my script on norns.community?

After your pull request is merged to the [community catalog](https://github.com/monome/norns-community) it will *automatically appear* on [norns.community](https://norns.community), provided the default branch of your script's repository is named `main`. The website refreshes nightly at 00:00 UTC, on every merge to its `main` branch, or on demand by admins. [This GitHub action](https://github.com/monome-community/norns-community/actions/workflows/build.yml) has all the details.

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

READMEs are individually cached from each script's repository in the below cascading sequence. Simply add a README to your project's `main` branch at any of the following locations:

```txt
1. ./README.md
2. ./doc/index.md
```

To ensure maximum resilience, please use [absolute URLs](https://en.wikipedia.org/wiki/HTTP_location) in your docs.

Cover images (aka screenshots) are individually cached from each script's repository in the below cascading sequence. Simply add a screenshot to your project at any of the following locations:

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

If you do not see your README populate on your script's page, please check to make sure that your script's default branch is named `main`, as this is the only naming scheme norns.community supports.

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

A [curl](https://github.com/monome-community/norns-community/blob/main/01-curl.sh) script fetches our [community catalog](https://github.com/monome/norns-community). A [build](https://github.com/monome-community/norns-community/blob/main/02-build.py) script then uses that data to construct this [Jekyll](https://jekyllrb.com) website. It is hosted with [GitHub pages](https://pages.github.com).

Additionally, these raw resources are available:

- [https://norns.community/community.json](https://norns.community/community.json)
- [https://norns.community/assets/covers/dronecaster.png](https://norns.community/assets/covers/dronecaster.png) (using `dronecaster` as example)
- [https://norns.community/assets/readmes/dronecaster.md](https://norns.community/assets/readmes/dronecaster.md) (using `dronecaster` as example)

---

## How can I help maintain this website?

If you want to help maintain this website, you can run it locally and test your changes before submitting a [pull request](https://github.com/monome-community/norns-community/pulls).

### Jekyll (Ruby) / HTML / CSS

1. clone repository to your computer
2. install [Ruby](https://www.ruby-lang.org/en/) and [bundle](https://bundler.io/)
3. using a shell, navigate to the `norns-community` directory with `cd`
4. in the directory execute: `bundle install`
5. then execute: `bundle exec jekyll serve --baseurl ''`
6. tip: if you're going to be working on this a lot, save the above command as an alias. this is also available as `npm run dev`.
7. pull the latest community data and build with: `./00-nuke.sh && ./01-curl.sh && ./02-build.py`
8. you can now visit [http://127.0.0.1:4000](http://127.0.0.1:4000) in your browser

This site was built with `ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [arm64-darwin21]`

### TypeScript / JavaScript

There is a single TypeScript file that is used to enable filtering on the "explore" page.

Install TypeScript and watch the file with:

1. `npm i`
2. `npm run tsc`

The build process assumes the transpiled JavaScript is already there. Perform all the `npm` actions locally.

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
