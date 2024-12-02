import json

info = {'name': 'yuhan','age':18, 'hobby':'football'}
with open('info.json','a',encoding = 'utf-8') as f:
    json.dump(info, f, indent = 4)