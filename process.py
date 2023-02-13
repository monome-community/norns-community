import json
import requests

# print(">> fetch catalog")
# remote = requests.get('https://raw.githubusercontent.com/monome/norns-community/main/community.json')
# print(">> write catalog")
# open('community.json','wb').write(remote.content)
print(">> parse catalog")
cat = json.load(open('community.json','r'))
print("entries:", len(cat['entries']))

print(">> generating index.md")
f = open('index.md','w')
for e in cat['entries']:
    f.write('['+e['project_name']+'](/'+e['project_name']+') - ['
            +e['author']+'](/'+e['author']+') - '
            +e['description']+"  \n")
f.close()
