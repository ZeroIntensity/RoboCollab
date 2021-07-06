import os

def check_collab_exists(id, name):
    json_path = f'./private/database/json/{name}_{id}.json'

    if os.path.exists(json_path):
        return True
    
    return False

