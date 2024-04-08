#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines class city"""
    def __init__(self, *args, **kwargs):
        """initializes city instance"""
        super().__init__(self, *args, **kwargs)
        self.state_id = kwargs.get('state.id', '')
        self.name = kwargs.get('name', '')

    def __str__(self):
        return "[City] ({}) {} {}".format(self.id, self.name, self.state_id)
