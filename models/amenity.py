#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines class Amenity"""
    def __init__(self, *args, **kwargs):
        """initializes amenity instance"""
        super().__init__(self, *args, **kwargs)
        self.name = kwargs.get('name', '')

    def __str__(self):
        """returns str rep of amenity instance"""
        return "[Amenity] ({}) {}".format(self.id, self.name)
