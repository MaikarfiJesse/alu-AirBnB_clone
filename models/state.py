#!/usr/bin/python3
"""
This module contains the State class
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """initializes State"""
        super()._init_(*args, **kwargs)
