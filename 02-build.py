#!/usr/bin/env python3

'''
build the authors and entry/project pages.

this build script uses:
 - "entries" when operating directly on community.json.
 - "projects" when operating user-facing pages.

screenshot fallback order is:
 1. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/cover.png
 2. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/GITHUB_PROJECT.png
 3. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/screenshot.png
 4. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/cover.png
 5. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/GITHUB_PROJECT.png
 6. https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/screenshot.png
 7. ./archive/screenshot/SANITIZED_NAME.png
 8. <nothing>

presently only projects hosted on github are supported.
'''

import json
import re
import os
import subprocess
import requests

community_json_src = 'community.json'
screenshots_dir_src = 'archive/screenshots'
screenshots_dir_dist = 'assets/screenshots'
authors_yml_dist = '_data/authors.yml'
projects_dir_dist = '_pages/projects'
tags_dir_dist = '_pages/tags'



# FUNCTIONS
# FUNCTIONS
# FUNCTIONS

def log(msg):
  print('>> ' + msg)

def sanitize(str):
  # only allow alphanumeric, dashes, and underscores
  return re.sub('[^a-zA-Z0-9\-_]', '', str)



# CLASSES
# CLASSES
# CLASSES

class Project():

  def __init__(self, entry):
    self.raw_name = entry['project_name']
    self.sanitized_name = sanitize(self.raw_name)
    self.screenshot = '/' + screenshots_dir_dist + '/' + self.sanitized_name + '.png'
    self.permalink = '/' + self.sanitized_name
    self.authors = []
    self.description = entry['description'] if 'description' in entry else ''
    self.project_url = entry['project_url'] if 'project_url' in entry else ''
    self.discussion_url = entry['discussion_url'] if 'discussion_url' in entry else ''
    self.documentation_url = entry['documentation_url'] if 'documentation_url' in entry else ''
    self.tags = entry['tags'] if 'tags' in entry else ''
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


class Screenshots():

  def __init__(self, community_data: CommunityData):
    self.community_data = community_data
    self.remote_fallbacks = {
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/cover.png',
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/GITHUB_PROJECT.png',
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/doc/screenshot.png',
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/cover.png',
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/GITHUB_PROJECT.png',
      'https://raw.githubusercontent.com/GITHUB_AUTHOR/GITHUB_PROJECT/main/screenshot.png',
    }
    self.local_fallbacks = {
      './archive/screenshots/SANITIZED_NAME.png',
      './assets/images/scriptname.png'
    }


  def fetch(self):
    for project in self.community_data.get_projects_in_alphabetical_order():
      log('#### ' + project.raw_name + ' ####')
      remote_fallback_found = False
      # try to fetch screenshots from the remote fallbacks first
      for fallback in self.remote_fallbacks:
        url = fallback.replace('GITHUB_AUTHOR', project.github_author).replace('GITHUB_PROJECT', project.github_project)
        log('try ' + url)
        try:
          response = requests.get(url)
          if response.status_code == 200:
            log('image found!')
            destination = './' + screenshots_dir_dist + '/' + project.sanitized_name + '.png'
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
        for fallback in self.local_fallbacks:
          path = fallback.replace('SANITIZED_NAME', project.sanitized_name)
          log('try ' + path)
          if os.path.exists(path):
            log('image found!')
            command = 'cp ' + path + ' ./' + screenshots_dir_dist + '/' + project.sanitized_name + '.png'
            log(command)
            subprocess.Popen(command, shell=True)
            break



# SETUP
# SETUP
# SETUP

log('attempting to parse catalog at ' + community_json_src + '...')
if not os.path.exists(community_json_src):
  log('error. ' + community_json_src + ' not found. is there a problem with ./01-curl.sh?')
  log('aborting...')
  exit()

community_data = CommunityData(community_json_src)
community_data.build()
log('done.')

log('copying community.json to ./_data for jekyll...')
subprocess.Popen('cp ./community.json ./_data/community.json', shell=True)
log('done.')

log('making projects directory...')
if not os.path.exists(projects_dir_dist):
  os.mkdir(projects_dir_dist)
log('done.')

log('making tags directory...')
if not os.path.exists(tags_dir_dist):
  os.mkdir(tags_dir_dist)
log('done.')



# SCREENSHOTS
# SCREENSHOTS
# SCREENSHOTS

log('making screenshots directory...')
if not os.path.exists(screenshots_dir_dist):
  os.mkdir(screenshots_dir_dist)
log('done.')

log('fetching screenshots...')
screenshots = Screenshots(community_data)
screenshots.fetch()
log('done.')



# INDEX PAGE
# INDEX PAGE
# INDEX PAGE

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



# AUTHOR PAGE
# AUTHOR PAGE
# AUTHOR PAGE

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



# PROJECT PAGES
# PROJECT PAGES
# PROJECT PAGES

log('building project pages...')
for project in community_data.get_projects_in_alphabetical_order():
  # write the project front matter
  fp = open(projects_dir_dist + '/' + project.sanitized_name + '.md', 'w')
  fp.write('---\n')
  # layout, title, and permalink are needed by jekyll
  fp.write('layout: project\n')
  fp.write('title: ' + project.raw_name + '\n')
  fp.write('screenshot: ' + project.sanitized_name + '.png' + '\n')
  fp.write('sanitized_name: ' + project.sanitized_name + '\n')
  fp.write('permalink: ' + project.permalink + '\n')
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
  # redirects to mitigate against link rot from wiki.js (norns.community v1.0)
  fp.write('redirect_from:\n')
  for author in project.authors:
    fp.write(' - /authors/' + author + '/' + project.sanitized_name + '\n')
  fp.write('---\n')
  fp.close()
log('done.')



# TAG PAGES
# TAG PAGES
# TAG PAGES

log('building tag pages...')
for tag in community_data.get_deduped_tags():
  fp = open(tags_dir_dist + '/' + tag + '.md', 'w')
  fp.write('---\n')
  fp.write('layout: tag\n')
  fp.write('title: ' + tag + '\n')
  fp.write('permalink: /tag/' + tag + '\n')
  fp.write('projects:\n')
  for project in community_data.get_projects_in_alphabetical_order():
    if tag in project.tags:
      fp.write('  - raw_name: ' + project.raw_name + '\n')
      fp.write('    url: ' + project.permalink + '\n')
      fp.write('    description: ' + project.description + '\n')
  fp.write('---\n')
  fp.close()
log('done.')



# dev zone
# project
# ygg = community_data.projects['yggdrasil']
# log(ygg.raw_name)
# log(ygg.sanitized_name)
# log(ygg.permalink)
# log(ygg.description)
# log(ygg.project_url)
# log(ygg.discussion_url)
# log(ygg.documentation_url)
# print(sorted(ygg.tags))
# print(sorted(ygg.authors))

# author
# ty = community_data.authors['tyleretters']
# log(ty.raw_name)
# log(ty.sanitized_name)
# log(ty.permalink)
# print(sorted(ty.projects))

# for a in community_data.get_authors_in_alphabetical_order():
#   log(a.raw_name)
#   log(a.sanitized_name)
#   log(a.permalink)
