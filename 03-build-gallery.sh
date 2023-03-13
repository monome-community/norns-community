#!/bin/bash

set -e


## ------------------------------------------------------------------------
## DEPS - GENRIC

sudo apt -qy install fakeroot git wget jq

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

LAST_RELEASE=$(wget -O - https://api.github.com/repos/p3r7/norns-gallery/releases/latest | jq -r .name)

mkdir /tmp/gallery-builder
cd /tmp/gallery-builder
# ghrel -p static-js-builder.tar.gz p3r7/norns-gallery
wget https://github.com/p3r7/norns-gallery/releases/download/$LAST_RELEASE/static-js-builder.tar.gz
tar xzvf static-js-builder.tar.gz

node target/cljsbuild/prerender/main.js --mode file --source-html "$OLDPWD/_layouts/search.html" --dest-html "$OLDPWD/_layouts/search.html" --replace-tag "<p>search goes here...</p>"



printf ">> done."
