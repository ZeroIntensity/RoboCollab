import json
from typing import Union, Any
from pathlib import Path

class Json: # Define abstract class
    def __init__(self, path: Union[str, Path], db) -> None: # Define init method
        self._path = path
        self._db = db

    @property
    async def database(self): # Define property
        return self._db

    async def remove(self, key: Any) -> "self":
        with open(self._path, 'r') as f:
            load = json.load(f) # Load the json
        
        del load[key]

        with open(self._path, 'w') as f:
            json.dump(load, f, indent = indent) # Dump the json
                
        return self

    async def empty(self) -> "self":
        with open(self._path, 'w') as f:
            f.write('{}')
        
        return self
    async def rename(self, key: Any, new_key: Any, indent: int = 4) -> "self": # Define rename method
        with open(self._path, 'r') as f:
            load = json.load(f) # Load the json

        load[new_key] = load.pop(key) # Rename the key

        with open(self._path, 'w') as f:
            json.dump(load, f, indent = indent) # Dump the json
        
        return self
    async def dump(self, key: Any, value: Any, indent: int = 4) -> "self": # Define dump method

        with open(self._path, 'r') as f:
            load = json.load(f) # Load the json

        load[key] = value # Set the key to the value
        with open(self._path, 'w') as f:
            json.dump(load, f, indent = indent) # Dump the json
        return self

    def __str__(self) -> str: # Define str method
        return self._path

    def __repr__(self) -> dict: # Define repr method
        return json.load(open(self._file))

    def __getitem__(self, item: Any) -> Any: # Define read method
        with open(self._path, 'r') as f:
            load = json.load(f)

        return load[item]

    async def read(self) -> str: # Define read method
        with open(self._path, 'r') as f:
            return f.read()



