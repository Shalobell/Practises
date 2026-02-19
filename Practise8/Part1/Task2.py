import json

filenames = ['50kb.json', '100kb.json', '200kb.json']

for fname in filenames:
    with open('json/'+fname, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        obj = json.loads(content)