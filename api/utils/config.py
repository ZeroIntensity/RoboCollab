import json

with open('./config.json') as f: # will break if "api" isn't the top level directory
    tmp: dict = json.load(f)
    state: str = 'dev'

    if tmp['production']:
        state: str = 'prod'

    StateConfig: dict = tmp[state]
    Config: dict = tmp
