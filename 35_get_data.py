import json

with open('info.json',encoding='utf-8') as data:
    info = json.load(data)
    new_list=[]
    for i in info:
        i.pop('error')
        new_list.append(tuple(i.values()))
    print(new_list)