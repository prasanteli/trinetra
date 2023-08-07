import json

def read_json_data():
    with open(r'src\static\data\schemes.json', 'r', encoding="utf-8") as f:
        data = f.read()
        data = json.loads(data)
        return data


def filter_based_on_user(user,data):
    return data