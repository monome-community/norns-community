#!/bin/bash

TARGETS=(
  "./_data/community.json"
  "./_data/authors.yml"
  "./community.json"
  "./index.md"
  "./_pages/projects"
)

printf ">> deleting any files generated from a previous build..."
for TARGET in "${TARGETS[@]}"; do
  printf "%s\n" ">> - $TARGET"
  rm -rf "$TARGET"
done

printf ">> done."
