#!/bin/bash

# note this script is only needed to make local development easier
# github actions builds from scratch each time

TARGETS=(
  "./_data/community.json"
  "./_data/authors.yml"
  "./community.json"
  "./index.md"
  "./_pages/projects"
  "./_pages/tags"
  "./assets/screenshots"
  "./node_modules"
)

printf ">> deleting any files generated from a previous build..."
for TARGET in "${TARGETS[@]}"; do
  printf "%s\n" ">> - $TARGET"
  rm -rf "$TARGET"
done

printf ">> done."
