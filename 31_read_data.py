import json

with open('data.json',encoding='utf-8') as f:
    result = json.load(f)
    print(result)
    print(result.get('name'))
    print(result.get('hobby')[1])
    print(result.get('address').get('city'))
    