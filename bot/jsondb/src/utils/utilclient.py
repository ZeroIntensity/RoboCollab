import os
from typing import Union
from pathlib import Path
from ..database import Database
class UtilClient: # Define UtilClient class
    def __init__(self, file: Union[str, Path] = None): # Define init method
        self._file = file

    async def get_current_dir(self, file: Union[str, Path] = None) -> str: # Define get_current_dir method
        if file is None:
            file = self._file
        return os.path.abspath(
            os.path.dirname(
                file
            )
        ) # Get the current dir


    async def get_dirs(self, amount = 1, file: Union[str, Path] = None) -> str: # Define get_dirs method
        if file is None:
            file = self._file
        path = file
        for i in range(amount):
            path = os.path.abspath(
                os.path.dirname(
                    path
                )
            ) # Get the parent dir over and over again

        return path # Return the path

    @staticmethod
    async def create_db_tree(database: Database) -> dict:
        path = await database.directory
        tree = {
            'dirs': {},
            'files':[]
                }
        for root, dirs, files in os.walk(path):
            for name in files:
                f = open(os.path.join(root, name))
                tree['files'][os.path.join(root, name)] = f.read()
                f.close()
            for name in dirs:
                tree['files'].append(os.path.join(root, name))

        return tree

    @staticmethod
    async def download_db_tree(tree: dict, directory: Union[str, Path]) -> None:
        for i in tree['dirs']:
            os.mkdir(
                os.path.join(
                    directory,
                    i
                )
            )
        for i in tree['files']:
            f = open(
                os.path.join(
                    directory,
                    i
                )
            ,
            'w'
            )
            f.write(tree['files'].get(i))
            f.close()
