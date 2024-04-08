#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """"inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def __str__(self):
        """returns str rep of user"""
        return "[user] ({}) {}".format(self.id, self.__dict__)
