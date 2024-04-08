#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """initializes state instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        """returns str rep of state instance"""
        return "[State] ({}) {}".format(self.id, self.name)
