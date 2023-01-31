#!/usr/bin/python3
"""Creating th e class BaseModel"""
import datetime
import uuid
import json
import models


class BaseModel:
    def __str__(self):
        """creates formatted string
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates public instance attribute
        updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary containing all keys/values of
            __dict__ of the instance
        Returns:
            dictionary containing all key/values of __dict__ of instance
        """
        a_dict = dict(self.__dict__)
#        a_dict = self.__dict__
#        a_dict = {}
#        a_dict.update(self.__dict__)
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "created_at":
                a_dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                a_dict[key] = self.updated_at.isoformat()
        a_dict["__class__"] = type(self).__name__
        return a_dict
