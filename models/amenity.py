#!/usr/bin/python3
"""
This module contains the Amenity class
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """initializes Amenity"""
        super()._init_(*args, **kwargs)
