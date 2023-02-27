#!/bin/bash

# retreive the latest community.json file from the norns-community repo

echo ">> curling community.json..."
curl https://raw.githubusercontent.com/monome/norns-community/main/community.json > _data/community.json
echo ">> done."
