import json
from Config import BASE_DIR

def build_data():
    with open(BASE_DIR +'/Data/read_data.json', encoding='utf-8') as f:
        test_data = json.load(f)
        return test_data

