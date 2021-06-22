import os
import functools
import json
from .json_obj import Json
from typing import Union, Any, Optional
from pathlib import Path
import os


class Database: # Define database object
    def __init__(self, directory: Union[str, Path]) -> None: # Define init method
        self._directory = directory
        if not os.path.exists(directory):
            raise FileNotFoundError('Directory not found.')
        
        if os.path.isfile(directory):
            raise NotADirectoryError('Path must be a directory.')
        
        self._connection = None

    @property
    async def directory(self) -> str:  # Define property
        return self._directory

    def change_directory(self, directory: Union[str, Path]):
        self._directory = directory


    @property
    async def full_connection(self) -> str:  # Define property
        return os.path.join(
            self._directory,
            self._connection
        )  # Return connection
    @property
    async def files(self) -> list: # Define property
        files = [i for i in os.listdir(self._directory)] # Iterate through directory
        return files

    @property
    async def connection(self) -> str: # Define property
        return self._connection

    @staticmethod
    async def create(file: Union[str, Path]) -> None: # Define create method

        f = open(file, 'w')
        f.write('{}')
        f.close()

    async def remove(self, file: Union[str, Path]) -> "self": # Define remove method
        os.remove(os.path.join( # Remove the file
            await self.directory,
            file
        ))

        return self # Return the client

    async def connect(self, file: Union[str, Path], create: bool = True) -> Json: # Define connect method
        if not create:
            if not os.path.exists(
                os.path.join( # Access create method
                await self.directory,
                file
            )):
                raise FileNotFoundError('File not found.')
            
        
        if create: # If argument "create" is true
            # Handle file build
            await self.create(os.path.join( # Access create method
                await self.directory,
                file
            ))

        self._connection = file # Set the connection
        return Json(  # Return json object instance
            os.path.join(  # Get path
                self._directory,
                file
            ),
            self  # Pass in the database object
        )




    async def clear_connection(self) -> "self": # Define clear_connection method
        self._connection = None
        return self # Return the client

    async def get_json(self, file: Union[str, Path] = None) -> Json: # Define get_json method
        if not file:
            file = self._connection
        return Json( # Return json object instance
            os.path.join( # Get path
                self._directory,
                file
            ),
            self # Pass in the database object
        )




