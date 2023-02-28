#!/bin/bash

TARGETS=(
  "./_data/community.json"
  "./community.json"
  "./index.md"
  "./_pages/projects"
  "./_pages/authors"
)

printf ">> deleting any files generated from a previous build..."
for TARGET in "${TARGETS[@]}"; do
  printf "%s\n" ">> - $TARGET"
  rm -rf "$TARGET"
done

printf ">> done."
