norns.community site generator

- fetches community catalog and parses into a static index, matrix tag search, and collected documentation

# TODO

- write up contribution guidelines
  - where docs go (/readme.md or /doc/index.md) (optional)
  - where screenshots go (/image.png or /doc/image.png) (optional)
- create fallback collection of images from norns.community for static hosting
- github actions setup
  - bash or python, generates static site from community.json (fetched)
- migrate tag filter (search) to use community.json (local copy, so that the site can be "downloaded" for offline viewing)

# navigation/content proposition:

## each page has the same header:
- short header: title, link to main norns docs navigation
- navigation: index, author, matrix

## index
- simple list of all scripts:
```
[name](local doc) - [author](author filter page) - description
```

## author
- simple list of scripts written by author:
```
[name](local doc) - description
```

## doc
- full meta-data from catalog.json
- screenshot
- scrape of doc

## matrix (filter? search?) @eigen 's choice locator
- i'd like to restyle this and put all the checkboxes at the top, in a big condensed list

