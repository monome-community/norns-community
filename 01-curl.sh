#!/bin/bash

printf ">> starting at %s\n" "$(date)"

COMMUNITY_PATH="./community.json"
UPSTREAM_PATH="./.upstream"

printf ">> retrieving the latest canonical community.json file..."
curl https://raw.githubusercontent.com/monome/norns-community/main/community.json > "$COMMUNITY_PATH"

printf ">> the sha526sum of community.json is: " 
sha256sum "$COMMUNITY_PATH" | awk '{print $1}'

# get a clone of monome/norns-community so we can read the
# git log of community.json. This gives us the date each entry 1st
# appeared on the index, for the "new" feed.
printf ">> syncing upstream repo for git history...\n"
if [ -d "$UPSTREAM_PATH/.git" ]; then
  git -C "$UPSTREAM_PATH" fetch --quiet origin main
  git -C "$UPSTREAM_PATH" reset --quiet --hard origin/main
else
  git clone --quiet --filter=blob:none https://github.com/monome/norns-community.git "$UPSTREAM_PATH"
fi

printf ">> done."
