from dataclasses import dataclass
from typing import Any, Dict, List, Union
from argon2 import PasswordHasher
from db import collabs


@dataclass
class BaseCollab:
    """Base class for representing collabs."""
    name: str
    server: str # hashed in argon2 by default
    host: int
    full_encrypt: bool = False
    users: Dict[int, str] = {}
    parts: Dict[int, List[str, str]] = []

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def find(filter: dict) -> Union[Any, None]:
        """Function for performing a database query on a collab."""
        return collabs.find(filter)
    
    @staticmethod
    def exists(doc: dict) -> bool:
        """Function for checking if a collab exists."""
        for i in ['users', 'parts', 'host']:
            del doc[i]
        
        return bool(collabs.find(doc))

    @staticmethod
    def delete(filter: dict) -> None:
        """Function for deleting a collab."""
        collabs.delete_one(filter)
    
    @staticmethod
    def delete_many(filter: dict) -> None:
        """Function for deleting multiple collabs."""
        collabs.delete_many(filter)

    @staticmethod
    def add_user(filter: dict, identifier: int, role: str) -> None:
        """Function for adding a user to a collab."""
        collabs.update_one(filter, {'$set': {f'users.{identifier}': role}})
    
    @staticmethod
    def add_part(filter: dict, identifier: int, start: str, end: str) -> None:
        """Function for adding a part to a collab."""
        collabs.update(filter, {'$push': {f'parts.{identifier}': [start, end]}})
    
    @staticmethod
    def save(doc: dict) -> None:
        ph = PasswordHasher()

        #unhashed = [i if (not i == 'server') else i for i in doc.keys()] if doc['full_encrypt'] else ['full_encrypt']


        for i in doc:
            if i in unhashed:
                continue

            key = doc[i]
            doc[i] = ph.hash(str(key))

        collabs.insert_one(doc)
        

class Collab(BaseCollab):
    """Schema class representing a collab."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        doc = self.__dict__

        if self.exists(doc):
            raise ValueError('Collab already exists.')

        collabs.insert_one(doc)

    def delete(self) -> None:
        """Function for deleting the current collab."""
        BaseCollab.delete(self.__dict__)
    
    def add_user(self, identifier: int, role: str) -> None:
        """Function for adding a user the current collab."""
        BaseCollab.add_user(self.__dict__, identifier, role)

    def add_part(self, identifier: int, start: str, end: str) -> None:
        """Function for adding a part to the current collab."""
        BaseCollab.add_user(self.__dict__, identifier, start, end)
