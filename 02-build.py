#!/usr/bin/env python3

'''
build the authors and entry/project pages.

this build script uses:
 - "entries" when operating directly on community.json.
 - "projects" when operating user-facing pages.
'''

import json
import re
import os
import subprocess

community_json_src = 'community.json'
screenshots_dir_src = 'screenshots'
screenshots_dir_dist = 'assets/screenshots'
authors_yml_dist = '_data/authors.yml'
projects_dir_dist = '_pages/projects'




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

log('making screenshots directory...')
if not os.path.exists(screenshots_dir_dist):
  os.mkdir(screenshots_dir_dist)
log('done.')

log('copying ./screenshots to ./assets/screenshots for jekyll...')
subprocess.Popen('cp -r ' + screenshots_dir_src + '/* ' + screenshots_dir_dist, shell=True)
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
  fp.write('screenshot: ' + project.screenshot + '\n')
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
  # recirects to mitigate against link rot from wiki.js (norns.community v1.0)
  fp.write('redirect_from:\n')
  for author in project.authors:
    fp.write(' - /authors/' + author + '/' + project.sanitized_name + '\n')
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
