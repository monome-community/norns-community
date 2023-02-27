#!/bin/bash

# nuke the authors & projects directories

echo ">> nuking ./_pages/authors..."
rm -rf _pages/authors
echo ">> done."

echo ">> nuking ./_pages/projects..."
rm -rf _pages/projects
echo ">> done."

echo ">> nuking ./index.md..."
rm -rf index.md
echo ">> done."