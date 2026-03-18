#!/bin/bash

printf ">> starting at %s\n" "$(date)"
printf ">> building site with zensical...\n"
zensical build --clean
printf ">> done.\n"
