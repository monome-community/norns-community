# welcome to norns.community

[norns.community](https://norns.community) is a collection of open source software for the monome [norns](https://monome.org/docs/norns) sound computer.

this document serves as both the README.md for [this repository](https://github.com/monome-community/norns-community) and the about page for [this website](https://norns.community/about).

---

## how do i get my script on norns.community?

after your PR is merged to the [community catalog](https://github.com/monome/norns-community) it will *automatically appear* on the website. the website refreshes nightly at 00:00 UTC. alternatively, an admin can run [this github action](https://github.com/monome-community/norns-community/actions/workflows/build.yml) for on-demand builds.

for script authors this means:

- your name will appear on the [index](https://norns.community) page
- any of your scripts will appear under your name
- your script will get its own page, [like this](https://norns.community/3d)
  - your script's README will be displayed on the page
  - your script's cover image will be displayed on the page
- your script will be available for discovery via any tags, like [grid](https://norns.community/tag/grid)
- your script will appear on the [explore](https://norns.community/explore) page
- if you update your README or cover image, it will automatically refresh on the website within 24 hours

---

## how do i get my README and cover image on norns.community?

these conventions was designed to "just work" with how most scripts are structured today.

READMEs are individually cached from your repository in the below cascading sequence. simply add a README to your project at any of the following locations:

```txt
1. ./README.md
2. ./doc/index.md
```

to ensure maximum resilience, please use [absolute urls](https://en.wikipedia.org/wiki/HTTP_location) in your docs.

covers (aka screenshots) are individually cached from your repository in the below cascading sequence. simply add a screenshot to your project at any of the following locations:

```txt
1. ./doc/cover.png
2. ./doc/<your_script_name>.png
3. ./doc/screenshot.png
4. ./cover.png
5. ./<your_script_name>.png
6. ./screenshot.png
```

if a cover image is not found in any of the above locations, we try the local archive before finally using a default image:

```txt
7. ./archive/screenshot/<your_script_name>.png
8. ./assets/images/dust.png
```

the local archive cache is from norns.community v1.0. it was archived in february, 2023.

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

[please open an issue on github.](https://github.com/monome-community/norns-community/issues)

---

## how does this site work?

a [curl](https://github.com/monome-community/norns-community/blob/main/01-curl.sh) script fetches our [community catalog](https://github.com/monome/norns-community). then a [build](https://github.com/monome-community/norns-community/blob/main/02-build.py) script uses that data to construct this [jekyll](https://jekyllrb.com) website. it is hosted with [github pages](https://pages.github.com).

additionally, these raw resources are available:

- [https://norns.community/community.json](https://norns.community/community.json)
- [https://norns.community/assets/covers/dronecaster.png](https://norns.community/assets/covers/dronecaster.png)
- [https://norns.community/assets/readmes/dronecaster.md](https://norns.community/assets/readmes/dronecaster.md)

---

## how can i help maintain this website?

if you want to help maintain this website, you can run it locally and test your changes before submitting a [pull request](https://github.com/monome-community/norns-community/pulls).

### jekyll (ruby) / html / css

1. clone repository to your computer
2. install [ruby](https://www.ruby-lang.org/en/) and [bundle](https://bundler.io/)
3. using a shell, navigate to the `norns-community` directory with `cd`
4. in the directory execute: `bundle install`
5. then execute: `bundle exec jekyll serve --baseurl ''`
6. tip: if you're going to be working on this alot, save the above command as an alias. this is also available as `npm run dev`.
7. pull the latest community data and build with: `./00-nuke.sh && ./01-curl.sh && ./02-build.py`
8. you can now visit [http://127.0.0.1:4000](http://127.0.0.1:4000) in your browser

this site was built with `ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [arm64-darwin21]`

### typescript / javascript

there is a single typescript file that is used to enable filtering on the "explore" page.

install typescript and watch the file with:

1. `npm i`
2. `npm run tsc`

the build process assumes the transpiled javascript is already there. do all the npm stuff locally.

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
- [dndkrs](https://github.com/dndkrs)
- [p3r7](https://github.com/p3r7)
- [tyleretters](https://github.com/tyleretters)
