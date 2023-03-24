#!/bin/bash

COMMUNITY_PATH="./community.json"

printf ">> retrieving the latest canonical community.json file..."
curl https://raw.githubusercontent.com/monome/norns-community/main/community.json > "$COMMUNITY_PATH"

printf ">> the sha526sum of community.json is: " 
sha256sum "$COMMUNITY_PATH" | awk '{print $1}'

printf ">> done."
