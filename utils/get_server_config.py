import json

def get_server_config():
    with open('server.json') as f:
        CONFIG: dict = json.load(f) # Load config
    
    return CONFIG
