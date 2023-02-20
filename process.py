import json
import requests
import re

# print(">> fetch catalog")
# remote = requests.get('https://raw.githubusercontent.com/monome/norns-community/main/community.json')
# print(">> write catalog")
# open('community.json','wb').write(remote.content)
print(">> parse catalog")
cat = json.load(open('community.json','r'))
print("entries:", len(cat['entries']))

a = {}

print(">> generating index.md")
f = open('index.md','w')
for e in cat['entries']:
    # check for space (is collab if so)
    if not re.search(r"\s", e['author']):
        f.write('['+e['project_name']+'](/'+e['project_name']+') - ['
            +e['author']+'](/'+e['author']+') - '
            +e['description']+"  \n")
        # generate authors list
        a.setdefault(e['author'],[]).append(e)
        # TODO generate script page here
f.write('\n---\n\ncontributors\n\n')
for k,v in sorted(a.items()):
    # maybe don't include script count
    f.write(k+" ("+str(len(v))+") ")
f.write('\n---\n\ncollaborations\n\n')

f.close()

#print(json.dumps(a,indent=2))
