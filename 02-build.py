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
import requests

# GLOBALS
# GLOBALS
# GLOBALS

community_json_src = 'community.json'
covers_src = 'archive/covers'
covers_dist = 'assets/covers'
readmes_src = 'assets/readmes'
authors_yml_dist = '_data/authors.yml'
projects_dist = '_pages/projects'
tags_dist = '_pages/tags'
explore_dist = '_pages/explore.md'
about_dist = '_pages/about.md'

# CLASSES
# CLASSES
# CLASSES

class Project():

  def __init__(self, entry):
    self.raw_name = entry['project_name']
    self.sanitized_name = sanitize(self.raw_name)
    self.screenshot = '/' + covers_dist + '/' + self.sanitized_name + '.png'
    self.permalink = '/' + self.sanitized_name
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
    # github strings are needed build the screenshot fallback urls
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
    self.permalink = '/author#' + self.sanitized_name

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

class Covers():

  def __init__(self, community_data: CommunityData):
    self.community_data = community_data
    self.remote_fallbacks = {
      1: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/cover.png',
      2: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/GITHUB_PROJECT.png',
      3: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/screenshot.png',
      4: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/cover.png',
      5: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/GITHUB_PROJECT.png',
      6: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/screenshot.png'
    }
    self.local_fallbacks = {
      1: './archive/screenshots/SANITIZED_NAME.png',
      2: './assets/images/dust.png'
    }


  def fetch(self):
    for project in self.community_data.get_projects_in_alphabetical_order():
      log('#### ' + project.raw_name + ' ####')
      remote_fallback_found = False
      # try remote covers first
      for fallback in sorted(self.remote_fallbacks.items()):
        url = fallback[1].replace('GITHUB_AUTHOR', project.github_author).replace('GITHUB_PROJECT', project.github_project)
        log('try ' + url)
        try:
          # test if exists (fast)
          response = requests.head(url)
          if response.status_code != 200:
            continue
          # download (slow)
          response = requests.get(url)
          if response.status_code == 200:
            log('image found!')
            destination = './' + covers_dist + '/' + project.sanitized_name + '.png'
            with open(destination, 'wb') as f:
              f.write(response.content)
              log('saved to ' + destination)
              remote_fallback_found = True
            break
        except requests.exceptions.RequestException as e:
          log('request failed.')
          log(e)
          continue
      # if remote fallbacks didn't work, try local
      if not remote_fallback_found:
        for fallback in sorted(self.local_fallbacks.items()):
          path = fallback[1].replace('SANITIZED_NAME', project.sanitized_name)
          log('try ' + path)
          if os.path.exists(path):
            log('image found!')
            command = 'cp ' + path + ' ./' + covers_dist + '/' + project.sanitized_name + '.png'
            log(command)
            subprocess.Popen(command, shell=True)
            break

class Readmes():

  def __init__(self, community_data: CommunityData):
    self.community_data = community_data
    self.remote_fallbacks = {
      1: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/README.md',
      2: 'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/index.md'
    }

  def fetch(self):
    for project in self.community_data.get_projects_in_alphabetical_order():
      log('#### ' + project.raw_name + ' ####')
      remote_fallback_found = False
      destination = './' + readmes_src + '/' + project.sanitized_name + '.md'
      # try remote covers first
      for fallback in sorted(self.remote_fallbacks.items()):
        url = fallback[1].replace('GITHUB_AUTHOR', project.github_author).replace('GITHUB_PROJECT', project.github_project)
        log('try ' + url)
        try:
          # test if exists (fast)
          response = requests.head(url)
          if response.status_code != 200:
            continue
          # download (slow)
          response = requests.get(url)
          if response.status_code == 200:
            log('README found!')
            with open(destination, 'wb') as f:
              f.write(response.content)
              log('saved to ' + destination)
              remote_fallback_found = True
            break
        except requests.exceptions.RequestException as e:
          log('request failed.')
          log(e)
          continue
      # if remote fallbacks didn't work, make an empty file
      if not remote_fallback_found:
        log('no README found, making empty file at ' + destination)
        with open(destination, 'w') as f:
          f.write('<< no README found >>')
          log('done.')

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

# only allow alphanumeric, dashes, and underscores
def sanitize(str):
  return re.sub('[^a-zA-Z0-9\-_]', '', str)

# project yml front matter for jekyll
def write_project_front_matter(fp, project):
  fp.write('screenshot: ' + project.sanitized_name + '.png' + '\n')
  fp.write('raw_name: ' + project.raw_name + '\n')
  fp.write('sanitized_name: ' + project.sanitized_name + '\n')
  fp.write('project_url: ' + project.project_url + '\n')
  fp.write('description: ' + project.description + '\n')
  fp.write('discussion_url: ' + project.discussion_url + '\n')
  fp.write('documentation_url: ' + project.documentation_url + '\n')
  fp.write('tags:\n')
  for tag in project.tags:
    fp.write(' - ' + tag + '\n')  
  fp.write('authors:\n')
  for author in project.authors:
    fp.write(' - ' + author + '\n')
  # redirects to mitigate against link rot from wiki.js (aka norns.community v1.0)
  fp.write('redirect_from:\n')
  for author in project.authors:
    fp.write(' - /authors/' + author + '/' + project.sanitized_name + '\n')

# explore yml front matter for jekyll
def write_explore_front_matter(fp, project):
  fp.write('\n') # newline for legibility only
  # these need to be indented 4 spaces for .yml:
  fp.write('  - raw_name: ' + project.raw_name + '\n')
  fp.write('    screenshot: ' + project.sanitized_name + '.png' + '\n')
  fp.write('    sanitized_name: ' + project.sanitized_name + '\n')
  fp.write('    url: ' + project.permalink + '\n')
  fp.write('    description: ' + project.description + '\n')
  fp.write('    tags:\n')
  for tag in project.tags:
    fp.write('     - ' + tag + '\n')  
  fp.write('    authors:\n')
  for author in project.authors:
    fp.write('     - ' + author + '\n')

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

# create directories
def build_setup():
  log('copying community.json to ./_data for jekyll...')
  subprocess.Popen('cp ./community.json ./_data/community.json', shell=True)
  log('done.')

  mkdir(projects_dist)
  mkdir(tags_dist)
  mkdir(covers_dist)
  mkdir(readmes_src)

def fetch_covers(community_data):
  log('fetching covers...')
  covers = Covers(community_data)
  covers.fetch()
  log('done.')

def fetch_readmes(community_data):
  log('fetching readmes...')
  readmes = Readmes(community_data)
  readmes.fetch()
  log('done.')

def build_index_page(community_data):
  log('building the index page...')
  fp = open('index.md', 'w')
  fp.write('---\n')
  fp.write('layout: index\n')
  fp.write('---\n')
  for project in community_data.get_projects_in_alphabetical_order():
    link = '[' + project.raw_name + '](' + project.permalink + ')'
    description = project.description
    fp.write('- ' + link + ' - ' + description + '\n')
  fp.close()
  log('done.')

def build_author_pages(community_data, authors_yml_dist):
  log('building ' + authors_yml_dist +'...')
  fp = open(authors_yml_dist, 'w')
  for author in community_data.get_authors_in_alphabetical_order():
    fp.write('- raw_name: ' + author.raw_name + '\n')
    fp.write('  sanitized_name: ' + author.sanitized_name + '\n')
    fp.write('  projects:\n\n')
    for project in community_data.get_projects_in_alphabetical_order():
      if author.raw_name in project.authors:
        fp.write('    - raw_name: ' + project.raw_name + '\n')
        fp.write('      url: ' + project.permalink + '\n\n')
  fp.close()
  log('done.')

def build_project_pages(community_data, projects_dist):
  log('building project pages...')
  for project in community_data.get_projects_in_alphabetical_order():
    # write the project front matter
    fp = open(projects_dist + '/' + project.sanitized_name + '.md', 'w')
    fp.write('---\n')
    # layout, title, and permalink are needed by jekyll
    fp.write('layout: project\n')
    fp.write('title: ' + project.raw_name + '\n')
    fp.write('permalink: ' + project.permalink + '\n')
    write_project_front_matter(fp, project)
    fp.write('---\n')
    # check if a readme exists in assets/readmes and pull it in
    readme_src = readmes_src + '/' + project.sanitized_name + '.md'
    if os.path.exists(readme_src):
      log('found readme for ' + project.raw_name + '...')
      fp.write(open(readme_src).read())
    fp.close()
  log('done.')

def build_tag_pages(community_data, tags_dist):
  log('building tag pages...')
  for tag in community_data.get_deduped_tags():
    log(tag + '...')
    fp = open(tags_dist + '/' + tag + '.md', 'w')
    fp.write('---\n')
    fp.write('layout: tag\n')
    fp.write('title: ' + tag + '\n')
    fp.write('permalink: /tag/' + tag + '\n')
    fp.write('projects:\n\n')
    for project in community_data.get_projects_in_alphabetical_order():
      if tag in project.tags:
        fp.write('  - raw_name: ' + project.raw_name + '\n')
        fp.write('    url: ' + project.permalink + '\n')
        fp.write('    description: ' + project.description + '\n\n')
    fp.write('---\n')
    fp.close()
  log('done.')

def build_explore_page(community_data, explore_dist):
  log('building explore page...')
  fp = open(explore_dist, 'w')
  fp.write('---\n')
  fp.write('layout: explore\n')
  fp.write('title: explore\n')
  fp.write('permalink: explore\n')
  fp.write('projects:\n')
  for project in community_data.get_projects_in_alphabetical_order():
    write_explore_front_matter(fp, project)
  fp.write('---\n')
  fp.close()
  log('done.')

def build_about_page(about_dist):
  log('building about page...')
  fp = open(about_dist, 'w')
  fp.write('---\n')
  fp.write('layout: page\n')
  fp.write('title: about\n')
  fp.write('permalink: about\n')
  fp.write('---\n')
  # copy contents of ./README.md to about.md
  with open('README.md', 'r') as readme:
    for line in readme:
      fp.write(line)
  fp.close()
  log('done.')

# MAIN
# MAIN
# MAIN

build_setup()
community_data = community_data_factory()
fetch_covers(community_data)
fetch_readmes(community_data)
build_index_page(community_data)
build_author_pages(community_data, authors_yml_dist)
build_project_pages(community_data, projects_dist)
build_tag_pages(community_data, tags_dist)
build_explore_page(community_data, explore_dist)
build_about_page(about_dist)
