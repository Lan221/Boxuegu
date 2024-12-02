import json

with open('info.json',encoding = 'utf-8') as f:
    info = json.load(f)


    for d in info:
        sex = 'Women' if d.get('iswomen') else "Men"
        print(f"Name:{d.get('name')} Age:{d.get('age')} Sex:{sex} \t "
                f"Hobby:{d.get('hobby')[2]}  City:{d.get('address').get('city')}")

