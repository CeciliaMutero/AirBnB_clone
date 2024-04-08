#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines Review class"""
    def __init__(self, *args, **kwargs):
        """initializes the review class"""
        super().__init__(self, *args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

    def __str__(self):
        """returns the str rep of review instance"""
        return "[Review] ({}) {}".format(self.id, self.__dict__)
