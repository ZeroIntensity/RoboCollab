import json
from .types import StateConfig, Config

with open('./config.json') as f: # will break if "api" isn't the top level directory
    tmp: Config = json.load(f)
    state: str = 'dev' if not tmp['production'] else 'prod'

    STATE_CONFIG: StateConfig = tmp[state]
    CONFIG: Config = tmp
