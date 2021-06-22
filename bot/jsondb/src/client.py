from typing import Union, Any
from pathlib import Path
from .json_obj import Json
import os
import json
from .database import Database
import asyncio
import sys

class Client: # Define client

    @staticmethod
    def run(coro):
        if sys.version_info >= (3, 7):
            return asyncio.run(coro)

        # Emulate asyncio.run() on older versions

        # asyncio.run() requires a coroutine, so require it here as well
        if not isinstance(coro, types.CoroutineType):
            raise TypeError("run() requires a coroutine object")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()
            asyncio.set_event_loop(None)


    @staticmethod
    async def database(directory: Union[str, Path] = '') -> Database: # Define database property
        return Database(directory) # Return the database object





