#!/bin/bash

set -e


## ------------------------------------------------------------------------
## DEPS - GENRIC

apt -qy install fakeroot git

# NB: to download latest release assets
# apt -qy install golang
# go install github.com/jreisinger/ghrel@latest


## ------------------------------------------------------------------------
## DEPS - NODE.JS

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR=$HOME/.nvm
. "$NVM_DIR/nvm.sh"

nvm install v19.6.1


## ------------------------------------------------------------------------
## MAIN

OLDPWD="$PWD"

mkdir /tmp/gallery-builder
cd /tmp/gallery-builder
# ghrel -p static-js-builder.tar.gz p3r7/norns-gallery
wget https://gitreleases.dev/gh/p3r7/norns-gallery/latest/static-js-builder.tar.gz
tar xzf static-js-builder.tar.gz

node main.js --mode file --source-html "$OLDPWD/_layouts/search.html" --dest-html "$OLDPWD/_layouts/search.html" --replace-tag "<p>search goes here...</p>"



printf ">> done."
