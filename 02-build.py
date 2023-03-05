#!/usr/bin/env python3

'''
build the authors and entry/project pages.

this build script uses:
 - "entries" when operating directly on community.json.
 - "projects" when operating user-facing pages.

todo:
 - refactor project:
   - move authors to project['author']
   - add description to project['description']
   - sanitized and display names for project name and author name
 - index page:
   - sorted (requires project dict refactor)
 - search page
 - community tags -> jekyll tags
 - other things...
'''

import json
import re
import os
import subprocess

community_path = './community.json'
pages_path = '_pages'
authors_yml_path = '_data/authors.yml'
projects_path = pages_path + '/projects'
community = {} # the raw community.json, parsed to a dict
projects = {}  # santized entries dict with author assosciations
authors = []   # list of all authors

# log a message
def log(msg):
  print('>> ' + msg)

# only allow alphanumeric, dashes, and underscores
def sanitize(str):
  return re.sub('[^a-zA-Z0-9\-_]', '', str)




# PARSE
# PARSE
# PARSE
log('attempting to parse catalog at ' + community_path + '...')
if not os.path.exists(community_path):
  log('error. ' + community_path + ' not found. is there a problem with ./01-curl.sh?')
  log('aborting...')
  exit()
else:
  community = json.load(open(community_path, 'r'))
log('done.')

log('copying community.json to ./_data for jekyll...')
subprocess.Popen('cp ./community.json ./_data/community.json', shell=True)
log('done.')





# PRE-PROCESSING
# PRE-PROCESSING
# PRE-PROCESSING
log('pre-processing authors & projects...')
for entry in community['entries']:
  project_name = ''
  # defend against a missing project_name or author
  if not 'project_name' in entry.keys():
    log('error. entry is somehow missing a project_name, skipping...')
    continue
  elif not 'author' in entry.keys():
    log('error. entry is somehow missing an author, skipping...')
    continue
  else:
    project_name = sanitize(entry['project_name'])
    log('added project: ' + project_name)
    projects[project_name] = []

  # check for multiple authors
  if ' ' in entry['author']:
    # add each author
    split = entry['author'].split()
    # sanitize each
    split = list(map(sanitize, split))
    authors = authors + split
    projects[project_name] = split
  else:
    # add a lone author
    authors.append(sanitize(entry['author']))
    projects[project_name].append(entry['author'])
log('done.')

log('deduping & sorting authors...')
authors = list(set(authors))
authors.sort()
log(str(len(authors)) + ' authors found.')
log('done.')

log('sorting projects...')
projects = dict(sorted(projects.items()))
log(str(len(projects)) + ' authors found.')
log('done.')

log('raw output of authors & projects for debugging:')
print(authors, projects)
log('done.')

log('making projects directory...')
if not os.path.exists(projects_path):
  os.mkdir(projects_path)
log('done.')




# AUTHOR PAGE
# AUTHOR PAGE
# AUTHOR PAGE
log('building ' + authors_yml_path +'...')
fp = open(authors_yml_path, 'w')
for author in authors:
  log(author)
  fp.write('- author: ' + author + '\n\n')
   # get all projects that this author is associated with
  fp.write('  projects:\n\n')
  for project in projects:
    if author in projects[project]:
      fp.write('    - name: ' + project + '\n')
      fp.write('      url: ' + project + '\n\n')
fp.close()
log('done.')




# PROJECT PAGES
# PROJECT PAGES
# PROJECT PAGES
log('building project pages...')
for entry in community['entries']:
  project_name = entry['project_name']
  sanitized_project_name = sanitize(project_name)
  log('project: ' + project_name)
  # write the project front matter
  fp = open(projects_path + '/' + sanitized_project_name + '.md', 'w')
  fp.write('---\n')
  # layout, title, and permalink are needed by jekyll
  fp.write('layout: project\n')
  fp.write('title: ' + sanitized_project_name + '\n')
  fp.write('permalink: /projects/' + sanitized_project_name + '\n')
  # sanitized project name, raw project name is also available
  fp.write('sanitized_project_name: ' + sanitized_project_name + '\n')
  # authors list
  fp.write('authors:\n')
  for author in projects[sanitized_project_name]:
    fp.write(' - ' + author + '\n')
  # redirects list
  fp.write('redirect_from:\n')
  for author in projects[sanitized_project_name]:
    fp.write(' - /authors/' + author + '/' + sanitized_project_name + '\n')
  # raw data from community json
  if 'author' in entry:
    fp.write('raw_community_json_author: ' + entry['author'] + '\n')
  if 'project_name' in entry:
    fp.write('raw_community_project_name: ' + entry['project_name'] + '\n')
  if 'project_url' in entry:
    fp.write('raw_community_project_url: ' + entry['project_url'] + '\n')
  if 'description' in entry:
    fp.write('raw_community_description: ' + entry['description'] + '\n')
  if 'discussion_url' in entry:
    fp.write('raw_community_discussion_url: ' + entry['discussion_url'] + '\n')
  if 'documentation_url' in entry:
    fp.write('raw_community_documentation_url: ' + entry['documentation_url'] + '\n')
  if 'tags' in entry:
    fp.write('raw_community_tags:\n')
    for tag in entry['tags']:
      fp.write(' - ' + tag + '\n')
  fp.write('---\n')
  fp.close()
log('done.')




# INDEX PAGE
# INDEX PAGE
# INDEX PAGE
log('building the index page...')
fp = open('index.md', 'w')
fp.write('---\n')
fp.write('layout: index\n')
fp.write('---\n')
for entry in community['entries']:
  project_name = entry['project_name']
  sanitized_project_name = sanitize(project_name)
  # [name](local doc) - [author](author filter page) - description
  fragment_1 = '[' + project_name + '](/projects/' + sanitized_project_name + ')'
  fragment_2 = ''
  for author in projects[sanitized_project_name]:
    fragment_2 = fragment_2 + '[' + author + '](/author#' + author + ') '
  fragment_3 = entry['description']
  fp.write('- ' + fragment_1 + ' - ' + fragment_2 + ' - ' + fragment_3 + '\n')
fp.close()
log('done.')
