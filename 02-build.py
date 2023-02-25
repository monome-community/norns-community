#!/usr/bin/env python3
# build the authors and script pages

import json
import re
import os

print('>> parse catalog')
community = json.load(open('_data/community.json', 'r'))
entries = community['entries']
print('total entries:', len(entries))

print('>> get unqiue authors')
authors = []
for entry in community['entries']:
  # get unique authors
  if entry['author'] not in authors:
    # replace spaces with dashes
    kebob = re.sub(r'\s+', '-', entry['author'])
    authors.append(kebob)

print('>> make authors directory')
pages_path = '_pages'
authors_path = '_pages/authors'
if not os.path.exists(authors_path):
  os.mkdir(authors_path)

print('>> build author pages')
for author in authors: 
  fp = open(pages_path + '/authors/' + author + '.md', 'w')
  fp.write('---\n')
  fp.write('layout: author\n')
  fp.write('title: ' + author + '\n')
  fp.write('permalink: /authors/' + author + '\n')
  fp.write('---\n')
  fp.close()

print('>> build entry pages')
for entry in entries:
  # make sure we have the minimum required fields
  if not 'project_name' in entry or not 'author' in entry:
    continue
  author_path = pages_path + '/authors/' + entry['author']
  # make a directory for the author if it doesn't exist
  if not os.path.exists(author_path):
    os.mkdir(author_path)
  # write the entry front matter
  fp = open(author_path + '/' + entry['project_name'] + '.md', 'w')
  fp.write('---\n')
  fp.write('layout: entry\n')
  fp.write('title: ' + entry['project_name'] + '\n')
  if 'author' in entry and 'project_name' in entry:
    fp.write('permalink: /authors/' + entry['author'] + '/' + entry['project_name'] +'\n')
  if 'project_name' in entry:
    fp.write('project_name: ' + entry['project_name'] + '\n')
  if 'project_url' in entry:
    fp.write('project_url: ' + entry['project_url'] + '\n')
  if 'author' in entry:
    fp.write('author: ' + entry['author'] + '\n')
  if 'description' in entry:
    fp.write('description: ' + entry['description'] + '\n')
  if 'discussion_url' in entry:
    fp.write('discussion_url: ' + entry['discussion_url'] + '\n')
  if 'documentation_url' in entry:
    fp.write('documentation_url: ' + entry['documentation_url'] + '\n')
  fp.write('---\n')
  fp.close()

