#!/bin/bash

# note this script is only needed to make local development easier
# github actions builds from scratch each time

printf ">> starting at %s\n" "$(date)"

TARGETS=(
  "./community.json"
  "./dist"
  "./.readmes"
  "./site"
  "./node_modules"
)

printf ">> deleting any files generated from a previous build..."
for TARGET in "${TARGETS[@]}"; do
  printf "%s\n" ">> - $TARGET"
  rm -rf "$TARGET"
done

printf ">> done."
