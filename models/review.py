#!/usr/bin/python3
"""
This module contains the Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def _init_(self, *args, **kwargs):
        """initializes Review"""
        super()._init_(*args, **kwargs)
