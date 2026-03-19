#!/usr/bin/env python3

'''
build the website.

this script is designed to be run via github actions.

presently only projects hosted on github are supported.

to match domain terminology, this build script uses:
 - "entry/entries" when operating directly on community.json.
 - "project(s)" when operating user-facing pages.
 - "cover(s)" when operating on cover images, which are typically (but not always) screenshots.

see README.md for more information.
'''

import json
import re
import os
import subprocess
import datetime

import aiohttp
import asyncio
import aiofiles

# GLOBALS
# GLOBALS
# GLOBALS

community_json_src = 'community.json'
covers_src = 'archive/covers'
covers_dist = 'docs/covers'
readmes_src = '.readmes'
projects_dist = 'docs'
tags_dist = 'docs/tag'
explore_dist = 'docs/explore.md'
about_dist = 'docs/about.md'
index_dist = 'docs/index.md'
github_raw_url_template = 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/HEAD'
remote_cover_count = 0
local_cover_count = 0
missing_cover_count = 0
remote_readme_count = 0
missing_readme_count = 0


# CLASSES
# CLASSES
# CLASSES

class Project():

  def __init__(self, entry):
    self.raw_name = entry['project_name']
    self.sanitized_name = sanitize(self.raw_name)
    self.cover = self.sanitized_name + '.png'
    self.permalink = '/' + self.sanitized_name + '/'
    self.authors = []
    self.description = entry['description'] if 'description' in entry else ''
    self.project_url = entry['project_url'] if 'project_url' in entry else ''
    self.discussion_url = entry['discussion_url'] if 'discussion_url' in entry else ''
    self.documentation_url = entry['documentation_url'] if 'documentation_url' in entry else ''
    # sanitize each tag
    unsanitized_tags = entry['tags'] if 'tags' in entry else ''
    self.tags = []
    for tag in unsanitized_tags:
      self.tags.append(sanitize(tag))
    # github strings are needed build the cover fallback urls
    github_strings = entry['project_url'].replace('https://github.com/', '').split('/')
    self.github_author = github_strings[0] # sometimes author names differ from github usernames
    self.github_project = github_strings[1]

  def associate_author(self, author_raw_name):
    self.authors.append(sanitize(author_raw_name))

  def get_authors_in_alphabetical_order(self):
    return sorted(self.authors, key=lambda author: author.casefold())

class Author():

  def __init__(self, raw_name):
    self.raw_name = raw_name
    self.sanitized_name = sanitize(raw_name)
    self.permalink = '/#' + self.sanitized_name

class CommunityData():

  def __init__(self, community_json_src):
    self.community = json.load(open(community_json_src, 'r'))
    self.authors = {}
    self.projects = {}

  def build(self):
    for entry in self.community['entries']:
      # defend against a missing project_name or author
      if not 'project_name' in entry.keys():
        log('error. entry is somehow missing a project_name, skipping...')
        continue
      elif not 'author' in entry.keys():
        log('error. entry is somehow missing an author, skipping...')
        continue
      else:
        self.add_project(entry)

  # note: projects and authors have a many-to-many relationship
  def add_project(self, entry):
    if not entry['project_name'] in self.projects.keys():
      log('adding ' + entry['project_name'])
      project = Project(entry)
      self.projects[project.raw_name] = project
      # multiple authors are separated by a space
      author_raw_name = entry['author']
      if ' ' in author_raw_name:
        script_authors = author_raw_name.split()
        for author_raw_name in script_authors:
          project.associate_author(author_raw_name)
          self.add_author(author_raw_name)
      else:
        project.associate_author(author_raw_name)
        self.add_author(author_raw_name)

  # add a new author if they don't already exist
  def add_author(self, author_raw_name):
    if not author_raw_name in self.authors.keys():
      self.authors[author_raw_name] = Author(author_raw_name)

  # return a list of authors in alphabetical order
  def get_authors_in_alphabetical_order(self):
    return sorted(self.authors.values(), key=lambda author: author.raw_name.casefold())

  # return a list of projects in alphabetical order
  def get_projects_in_alphabetical_order(self):
    return sorted(self.projects.values(), key=lambda project: project.raw_name.casefold())

  def get_deduped_tags(self):
    tags = []
    for project in self.projects.values():
      for tag in project.tags:
        if not tag in tags:
          tags.append(tag)
    return sorted(tags, key=lambda tag: tag.casefold())


## ------------------------------------------------------------------------
## COVERS

URL_TMPLT_COVER = [
  github_raw_url_template + '/doc/cover.png',
  github_raw_url_template + '/doc/GITHUB_PROJECT.png',
  github_raw_url_template + '/doc/screenshot.png',
  github_raw_url_template + '/cover.png',
  github_raw_url_template + '/GITHUB_PROJECT.png',
  github_raw_url_template + '/screenshot.png'
]

async def afetch_cover(session, project, idx):
  global remote_cover_count
  global local_cover_count
  global missing_cover_count

  filename = project.sanitized_name + '.png'
  destination = './' + covers_dist + '/' + filename

  for url_tmplt in URL_TMPLT_COVER:
    url = url_tmplt.replace('GITHUB_AUTHOR', project.github_author).replace('GITHUB_PROJECT', project.github_project)
    async with session.get(url) as response:
      if response.status == 200:
        log(project.sanitized_name + ' - remote cover found at ' + url)
        remote_cover_count += 1
        content = await response.read()
        async with aiofiles.open(destination, 'wb') as f:
          await f.write(content)
        return

  archive_path = './archive/screenshots/' + filename
  if os.path.exists(archive_path):
    log(project.sanitized_name + ' - local cover found in archive.')
    local_cover_count += 1
    command = 'cp ' + archive_path + ' ' + destination
    subprocess.Popen(command, shell=True)
  else:
    log(project.sanitized_name + ' - no cover found. using dust.')
    missing_cover_count += 1
    command = 'cp ./docs/images/dust.png' + ' ' + destination
    subprocess.Popen(command, shell=True)

async def afetch_covers(projects):
  async with aiohttp.ClientSession() as session:
    tasks = [afetch_cover(session, project, idx) for idx, project in enumerate(projects)]
    await asyncio.gather(*tasks)


## ------------------------------------------------------------------------
## READMES

URL_TMPLT_README = [
  github_raw_url_template + '/doc/index.md',
  github_raw_url_template + '/README.md'
]

async def afetch_readme(session, project, idx):
  global remote_readme_count
  global missing_readme_count

  filename = project.sanitized_name + '.md'
  destination = './' + readmes_src + '/' + filename

  for url_tmplt in URL_TMPLT_README:
    url = url_tmplt.replace('GITHUB_AUTHOR', project.github_author).replace('GITHUB_PROJECT', project.github_project)
    async with session.get(url) as response:
      if response.status == 200:
        log(project.sanitized_name + ' - remote readme found at ' + url)
        remote_readme_count += 1
        content = await response.read()
        async with aiofiles.open(destination, 'wb') as f:
          await f.write(content)
        return

  log(project.sanitized_name + ' - no readme found.')
  missing_readme_count += 1

async def afetch_readmes(projects):
  async with aiohttp.ClientSession() as session:
    tasks = [afetch_readme(session, project, idx) for idx, project in enumerate(projects)]
    await asyncio.gather(*tasks)


## ------------------------------------------------------------------------
# FUNCTIONS
# FUNCTIONS
# FUNCTIONS

def log(msg):
  print('>> ' + msg)

def mkdir(path):
  log('making directory at ' + path)
  if not os.path.exists(path):
    os.makedirs(path)
  log('done.')

# replace both local and relative markdown image paths with raw.githubusercontent.com paths
# works for:
# ![alt](./image.png)
# ![alt](/image.png)
# ![alt](image.png)
# ![alt](https://github.com/toneburst/bline/blob/main/screenshots/bLINE_Logo_GIF_02.gif)
def replace_image_paths(string, absolute_url):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    replaced_string = re.sub(pattern, lambda match: process_image_path(match, absolute_url), string)
    return replaced_string

def process_image_path(match, absolute_url):
    alt_text = match.group(1)
    image_path = match.group(2)

    # github image paths need to be served from raw.githubusercontent.com, not the github.com
    if image_path.startswith("https://github.com"):
      image_path = image_path.replace("https://github.com", "https://raw.githubusercontent.com")
      image_path = image_path.replace('/blob/', '/')
      return "![{}]({})".format(alt_text, image_path)

    # Skip processing if the image link already starts with "http" or "https" (maybe they're linking to their personal website)
    if image_path.startswith("http"):
        return match.group(0)

    return "![{}]({}/{})".format(alt_text, absolute_url.rstrip("/"), image_path.lstrip("./"))

# only allow alphanumeric, dashes, and underscores
def sanitize(str):
  return re.sub('[^a-zA-Z0-9\-_]', '', str)

# escape a string for safe YAML output
def yaml_escape(s):
  if not s:
    return '""'
  # wrap in double quotes if it contains special yaml characters
  if any(c in s for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
  return s

# write build metadata into front matter
def write_build_metadata(fp, build_meta):
  fp.write('build_time: "' + build_meta['build_time'] + '"\n')
  fp.write('build_year: "' + build_meta['build_year'] + '"\n')
  fp.write('git_hash_full: ' + build_meta['git_hash_full'] + '\n')
  fp.write('git_hash_short: ' + build_meta['git_hash_short'] + '\n')

# project yml front matter for zensical
def write_project_front_matter(fp, project, build_meta):
  fp.write('template: project.html\n')
  fp.write('cover: ' + project.sanitized_name + '.png' + '\n')
  fp.write('raw_name: ' + yaml_escape(project.raw_name) + '\n')
  fp.write('sanitized_name: ' + project.sanitized_name + '\n')
  fp.write('project_url: ' + project.project_url + '\n')
  fp.write('description: ' + yaml_escape(project.description) + '\n')
  fp.write('discussion_url: ' + yaml_escape(project.discussion_url) + '\n')
  fp.write('documentation_url: ' + yaml_escape(project.documentation_url) + '\n')
  if project.tags:
    fp.write('tags:\n')
    for tag in project.tags:
      fp.write(' - ' + tag + '\n')
  else:
    fp.write('tags: []\n')
  if project.authors:
    fp.write('authors:\n')
    for author in project.authors:
      fp.write(' - ' + author + '\n')
  else:
    fp.write('authors: []\n')
  write_build_metadata(fp, build_meta)

# explore yml front matter for zensical
def write_explore_front_matter(fp, project):
  fp.write('\n') # newline for legibility only
  # these need to be indented 4 spaces for .yml:
  fp.write('  - raw_name: ' + yaml_escape(project.raw_name) + '\n')
  fp.write('    cover: ' + project.cover + '\n')
  fp.write('    sanitized_name: ' + project.sanitized_name + '\n')
  fp.write('    url: ' + project.permalink + '\n')
  fp.write('    description: ' + yaml_escape(project.description) + '\n')
  if project.tags:
    fp.write('    tags:\n')
    for tag in project.tags:
      fp.write('     - ' + tag + '\n')
  else:
    fp.write('    tags: []\n')
  if project.authors:
    fp.write('    authors:\n')
    for author in project.authors:
      fp.write('     - ' + author + '\n')
  else:
    fp.write('    authors: []\n')

# prepare the raw community.json data
def community_data_factory():
  log('attempting to parse catalog at ' + community_json_src + '...')
  if not os.path.exists(community_json_src):
    log('error. ' + community_json_src + ' not found. is there a problem with ./01-curl.sh?')
    log('aborting...')
    exit()

  community_data = CommunityData(community_json_src)
  community_data.build()
  log('done.')
  return community_data

# compute build metadata (git hash, timestamps)
def get_build_metadata():
  log('computing build metadata...')
  git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
  now = datetime.datetime.now()
  meta = {
    'git_hash_full': git_hash,
    'git_hash_short': git_hash[:7],
    'build_time': now.strftime("%a %b %d %H:%M:%S %Z %Y"),
    'build_year': now.strftime("%Y"),
  }
  log('done.')
  return meta

# create directories
def build_setup():
  mkdir(projects_dist)
  mkdir(tags_dist)
  mkdir(covers_dist)
  mkdir(readmes_src)
  # serve community.json as a static file
  log('copying community.json to docs/...')
  subprocess.Popen('cp ./community.json ./docs/community.json', shell=True)
  log('done.')

def fetch_covers(community_data):
  log('fetching covers...')
  asyncio.run(afetch_covers(community_data.get_projects_in_alphabetical_order()))
  log('done.')

def fetch_readmes(community_data):
  log('fetching readmes...')
  asyncio.run(afetch_readmes(community_data.get_projects_in_alphabetical_order()))
  log('done.')

def build_index_page(community_data, build_meta):
  log('building the index page...')
  fp = open(index_dist, 'w')
  fp.write('---\n')
  fp.write('title: index\n')
  fp.write('template: index.html\n')
  write_build_metadata(fp, build_meta)
  fp.write('projects:\n')
  for project in community_data.get_projects_in_alphabetical_order():
    fp.write('  - raw_name: ' + yaml_escape(project.raw_name) + '\n')
    fp.write('    url: ' + project.permalink + '\n')
    fp.write('    description: ' + yaml_escape(project.description) + '\n')
    if project.authors:
      fp.write('    authors:\n')
      for author in project.get_authors_in_alphabetical_order():
        fp.write('      - ' + author + '\n')
    else:
      fp.write('    authors: []\n')
  fp.write('---\n')
  fp.close()
  log('done.')

def build_author_redirects(community_data):
  log('building author redirects...')
  author_dir = 'docs/author'
  mkdir(author_dir)
  # /author/ -> /
  fp = open(author_dir + '/index.html', 'w')
  fp.write('<!DOCTYPE html><html><head>')
  fp.write('<meta http-equiv="refresh" content="0; url=/">')
  fp.write('</head><body>')
  fp.write('Redirecting to <a href="/">index</a>')
  fp.write('</body></html>')
  fp.close()
  # /author/name/ -> /#name
  for author in community_data.get_authors_in_alphabetical_order():
    this_author_dir = author_dir + '/' + author.raw_name
    mkdir(this_author_dir)
    fp = open(this_author_dir + '/index.html', 'w')
    fp.write('<!DOCTYPE html><html><head>')
    fp.write('<meta http-equiv="refresh" content="0; url=/#' + author.raw_name + '">')
    fp.write('</head><body>')
    fp.write('Redirecting to <a href="/#' + author.raw_name + '">' + author.raw_name + '</a>')
    fp.write('</body></html>')
    fp.close()
  log('done.')

def build_project_pages(community_data, build_meta):
  log('building project pages...')
  for project in community_data.get_projects_in_alphabetical_order():
    # write the project front matter
    fp = open(projects_dist + '/' + project.sanitized_name + '.md', 'w')
    fp.write('---\n')
    fp.write('title: ' + yaml_escape(project.raw_name) + '\n')
    write_project_front_matter(fp, project, build_meta)
    fp.write('---\n')
    # check if a readme exists and pull it in
    readme_path = readmes_src + '/' + project.sanitized_name + '.md'
    if os.path.exists(readme_path):
      log('found readme for ' + project.raw_name + '...')
      # attempt to update relative links to raw github links
      # this should leave us with something like northern-information/dronecaster
      # note: we can't just look at the project.authors because we don't know who publishes the repo
      github_author_and_project = project.project_url.replace('https://github.com/', '')
      # remove trailing slash, if one exists:
      github_author_and_project = github_author_and_project.rstrip('/')
      this_github_raw_url_template = github_raw_url_template.replace('GITHUB_AUTHOR/GITHUB_PROJECT', github_author_and_project)
      readme = open(readme_path).read()
      readme = replace_image_paths(readme, this_github_raw_url_template)
      fp.write(readme)
    fp.close()
  log('done.')

def build_tag_pages(community_data, build_meta):
  log('building tag pages...')
  for tag in community_data.get_deduped_tags():
    log(tag + '...')
    fp = open(tags_dist + '/' + tag + '.md', 'w')
    fp.write('---\n')
    fp.write('title: ' + tag + '\n')
    fp.write('template: tag.html\n')
    write_build_metadata(fp, build_meta)
    fp.write('projects:\n')
    for project in community_data.get_projects_in_alphabetical_order():
      if tag in project.tags:
        fp.write('  - raw_name: ' + yaml_escape(project.raw_name) + '\n')
        fp.write('    url: ' + project.permalink + '\n')
        fp.write('    description: ' + yaml_escape(project.description) + '\n')
    fp.write('---\n')
    fp.close()
  log('done.')

def build_explore_page(community_data, build_meta):
  log('building explore page...')
  fp = open(explore_dist, 'w')
  fp.write('---\n')
  fp.write('title: explore\n')
  fp.write('template: explore.html\n')
  write_build_metadata(fp, build_meta)
  fp.write('tags:\n')
  for tag in community_data.get_deduped_tags():
    fp.write('  - ' + tag + '\n')
  fp.write('\n')
  fp.write('projects:\n')
  for project in community_data.get_projects_in_alphabetical_order():
    write_explore_front_matter(fp, project)
  fp.write('---\n')
  fp.close()
  log('done.')

def build_about_page(build_meta):
  log('building about page...')
  fp = open(about_dist, 'w')
  fp.write('---\n')
  fp.write('title: about\n')
  fp.write('template: page.html\n')
  write_build_metadata(fp, build_meta)
  fp.write('---\n')
  # copy contents of ./README.md to about.md
  with open('README.md', 'r') as readme:
    for line in readme:
      fp.write(line)
  fp.close()
  log('done.')

def build_404_page(build_meta):
  log('building 404 page...')
  fp = open('docs/404.md', 'w')
  fp.write('---\n')
  fp.write('title: "404"\n')
  fp.write('template: page.html\n')
  write_build_metadata(fp, build_meta)
  fp.write('---\n')
  fp.write('<h1>404</h1>\n')
  fp.write('<p>The requested page could not be found.</p>\n')
  fp.close()
  log('done.')

def build_redirects(community_data):
  log('building redirects...')
  for project in community_data.get_projects_in_alphabetical_order():
    for author in project.authors:
      for prefix in ['en/authors', 'authors']:
        redirect_dir = 'docs/' + prefix + '/' + author + '/' + project.sanitized_name
        mkdir(redirect_dir)
        redirect_path = redirect_dir + '/index.html'
        fp = open(redirect_path, 'w')
        fp.write('<!DOCTYPE html><html><head>')
        fp.write('<meta http-equiv="refresh" content="0; url=' + project.permalink + '">')
        fp.write('</head><body>')
        fp.write('Redirecting to <a href="' + project.permalink + '">' + project.raw_name + '</a>')
        fp.write('</body></html>')
        fp.close()
  log('done.')

def log_stats(community_data):
  log('################################')
  log('norns.community stats')
  log('authors: ' + str(len(community_data.authors)))
  log('projects: ' + str(len(community_data.projects)))
  log('remote covers: ' + str(remote_cover_count))
  log('local covers: ' + str(local_cover_count))
  log('missing covers: ' + str(missing_cover_count))
  log('remote readmes: ' + str(remote_readme_count))
  log('missing readmes: ' + str(missing_readme_count))

# MAIN
# MAIN
# MAIN

time_start = datetime.datetime.now()
log('starting at ' + time_start.strftime("%a %b %d %H:%M:%S %Z %Y"))
build_meta = get_build_metadata()
build_setup()
community_data = community_data_factory()
fetch_covers(community_data)
fetch_readmes(community_data)
build_index_page(community_data, build_meta)
build_author_redirects(community_data)
build_project_pages(community_data, build_meta)
build_tag_pages(community_data, build_meta)
build_explore_page(community_data, build_meta)
build_about_page(build_meta)
build_404_page(build_meta)
build_redirects(community_data)
log_stats(community_data)
runtime = datetime.datetime.now() - time_start
log('finishing at ' + datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y"))
log('02-build.py runtime ' + runtime.__str__())
