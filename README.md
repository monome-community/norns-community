# TODO

- write up contribution guidelines
  - where docs go (/readme.md or /doc/index.md) (optional)
- migrate tag filter (search) to use community.json (local copy, so that the site can be "downloaded" for offline viewing)
- add `/tag/arc`, `/tag/sequencer`, etc. layout and pages for jekyll
- fallbacks for screenshots (presently only checks in ./assets/screenshots)

# norns.community site generator

fetches the [community catalog](https://github.com/monome/norns-community) and parses into a static site with matrix tag search and collected documentation.

# contributing your script

1. add screenshots to `./screenshots`. (note: screenshots were archived from the original [norns.community](https://norns.community) site on february 5, 2023.)


# development setup instructions

if you want to help maintain this site, you can run it locally and test your changes before submitting a pull request.

1. clone repository to your computer
2. install [ruby](https://www.ruby-lang.org/en/) and [bundle](https://bundler.io/)
3. using a shell, navigate to the `norns-community` directory with `cd`
4. in the directory execute: `bundle install`
5. then execute: `bundle exec jekyll serve --baseurl ''`
6. if you're going to be working on this alot, save the above command as an alias
7. pull the latest community data and build: `./00-nuke.sh && ./01-curl.sh && ./02-build.py`. this is also the main dev loop.
8. you can now visit [http://127.0.0.1:4000](http://127.0.0.1:4000) in your browser

(this site was built with `ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [arm64-darwin21]`)

# navigation/content proposition:

## each page has the same header:
- short header: title, link to main norns docs navigation
- navigation: index, author, matrix

## doc
- full meta-data from catalog.json
- screenshot
- scrape of doc

## matrix (filter? search?) @eigen 's choice locator
- i'd like to restyle this and put all the checkboxes at the top, in a big condensed list

