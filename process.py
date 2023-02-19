import json
import requests

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
    if isinstance(e['author'],str):
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
f.close()

#print(json.dumps(a,indent=2))

# scripts are not sorted
print(">> generating author pages")
for k,v in sorted(a.items()):
    #f = open('authors.md','w')
    print(k,len(v))
    #for e in v:
        #f.write('['+e['author']+'](/'+e['author']+') - ['
            #+e['project_name']+'](/'+e['project_name']+') - '
            #+e['description']+"  \n")
    #f.close()
