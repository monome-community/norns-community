# norns.community

this repository fetches our [community catalog](https://github.com/monome/norns-community) and parses into a static website.

[this github action](https://github.com/monome-community/norns-community/actions/workflows/jekyll.yml) runs the build and then deploys via github pages.

screenshots are individually cached from their respective repos in the following priority order:

```txt
1. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/cover.png
2. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/GITHUB_PROJECT.png
3. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/screenshot.png
4. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/cover.png
5. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/GITHUB_PROJECT.png
6. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/screenshot.png
7. ./archive/screenshot/SANITIZED_NAME.png
8. ./assets/images/dust.png
```

[archived screenshots](https://github.com/monome-community/norns-community/tree/main/archive/screenshots) were archived from the original https://norns.community wiki.js site on february 5, 2023. one of our goals is to completely retire this step and push the responsibility of hosting script cover images to the authors.

in practice, this means script can simply add a screenshot their repos at any of the following locations:

```txt
./doc/cover.png
./doc/your-script-name.png
./doc/screenshot.png
./cover.png
./your-script-name.png
```

## development setup instructions

if you want to help maintain this site, you can run it locally and test your changes before submitting a pull request.

1. clone repository to your computer
2. install [ruby](https://www.ruby-lang.org/en/) and [bundle](https://bundler.io/)
3. using a shell, navigate to the `norns-community` directory with `cd`
4. in the directory execute: `bundle install`
5. then execute: `bundle exec jekyll serve --baseurl ''`
6. tip: if you're going to be working on this alot, save the above command as an alias
7. pull the latest community data and build with: `./00-nuke.sh && ./01-curl.sh && ./02-build.py`
8. you can now visit [http://127.0.0.1:4000](http://127.0.0.1:4000) in your browser

this site was built with `ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [arm64-darwin21]`

## todo

- about page
  - write up contribution guidelines
  - where docs go (/readme.md or /doc/index.md)
  - where cover image can go (list)
