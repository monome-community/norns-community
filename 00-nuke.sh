#!/bin/bash

# note this script is only needed to make local development easier
# github actions builds from scratch each time

printf ">> starting at %s\n" "$(date)"

TARGETS=(
  "./community.json"
  "./docs/index.md"
  "./docs/author.md"
  "./docs/explore.md"
  "./docs/about.md"
  "./docs/404.md"
  "./docs/covers"
  "./.readmes"
  "./docs/tag"
  "./docs/community.json"
  "./docs/en"
  "./docs/authors"
  "./site"
  "./node_modules"
)

printf ">> deleting any files generated from a previous build..."
for TARGET in "${TARGETS[@]}"; do
  printf "%s\n" ">> - $TARGET"
  rm -rf "$TARGET"
done

# all .md files in docs/ root are generated (project pages)
# static assets (css, js, images, icons, favicons) are not .md
if [ -d "./docs" ]; then
  printf ">> removing generated .md files from docs/...\n"
  find ./docs -maxdepth 1 -name "*.md" -delete
fi

printf ">> done."
