#!/usr/bin/python3
"""
This module contains the City class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    state_id = ""
    name = ""

    def _init_(self, *args, **kwargs):
        """initializes City"""
        super()._init_(*args, **kwargs)
