import json, os

#Read json(config.json)
JSON_PATH = str(os.getcwd()) + '\config.json'
def read_json():
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)
        result = [data['config']['guild_id'], data['config']['token']]
    return result

    