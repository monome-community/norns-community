# CLAUDE.md

## Project Overview

norns.community is a script index for the monome norns sound computer. It is a data-driven static site where all content is generated from `community.json` (fetched from https://github.com/monome/norns-community).

## Architecture

**Static site generator:** [Zensical](https://zensical.org) (Python/Rust)

**Build pipeline:**
1. `00-nuke.sh` - cleans generated files (local dev only)
2. `01-curl.sh` - fetches `community.json` from GitHub
3. `02-build.py` - copies static assets from `src/` to `dist/`, parses JSON, async-fetches cover images & READMEs from GitHub, generates markdown pages with YAML front matter in `dist/`
4. `03-zensical.sh` - compiles markdown pages into static HTML in `site/`

**Key directories:**
- `src/` - Hand-maintained source files: static assets (CSS, JS, images, icons, favicons) and MiniJinja templates
  - `overrides/` - MiniJinja templates. Standalone HTML documents (not extending Zensical's base theme)
  - `overrides/partials/` - Shared template partials (prefixed `nc_` to avoid collisions with Zensical's default theme partials)
  - `javascripts/` - TypeScript source (`script.ts`) and compiled JS (`script.js`)
- `dist/` - Assembled Zensical content directory (not committed). Built by `02-build.py` from `src/` static assets + generated markdown pages
- `.readmes/` - Temp cache for fetched README files (not served, not committed)
- `site/` - Build output (not committed)
- `archive/` - Legacy v1.0 screenshot cache (cover image fallback)

**Templates (MiniJinja):**
- `page.html` - generic pages (index, about, 404)
- `project.html` - individual project pages with metadata table + README content
- `explore.html` - project grid with client-side tag filtering
- `author.html` - author listing with nested project links
- `tag.html` - projects filtered by tag

**Front matter conventions:**
- `template:` selects the MiniJinja template (not `layout:`)
- Custom properties are accessed via `page.meta.*` in templates
- Build metadata (`build_time`, `build_year`, `git_hash_full`, `git_hash_short`) is injected into every page
- Empty lists must use `[]` not bare `key:` (Zensical's parser treats bare keys as null)

## Common Commands

```bash
# Full rebuild from scratch
./00-nuke.sh && ./01-curl.sh && ./02-build.py && ./03-zensical.sh

# Quick rebuild (skip fetch, reuse cached data)
./02-build.py && ./03-zensical.sh

# Dev server with live reload
zensical serve

# npm shortcuts
npm run ncb    # nuke + curl + build + zensical
npm run dev    # zensical serve
npm run tsc    # typescript watch
```

## Dependencies

- Python 3.10+ with: `zensical`, `aiohttp`, `aiofiles`
- Node.js (dev only, for TypeScript compilation)

## Deployment

GitHub Actions (`.github/workflows/build.yml`). Triggers on push to main, nightly at 00:00 UTC, repository dispatch from monome/norns-community merges, or manual dispatch. Deploys to GitHub Pages.

## Important Notes

- `src/` contains only hand-maintained static assets (stylesheets, javascripts, images, icons, favicons, robots.txt, site.webmanifest) and templates
- `dist/` is entirely generated — `02-build.py` copies `src/` assets there, then generates all `.md` files, covers, tags, and redirects
- The `yaml_escape()` function in `02-build.py` handles YAML-unsafe characters in descriptions
- Redirects from old wiki.js URLs (`/en/authors/...`, `/authors/...`) are generated as static HTML files with meta-refresh
- Cover image fallback sequence: 6 remote GitHub paths -> local archive -> dust.png default
