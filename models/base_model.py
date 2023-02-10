#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
   In order to create, update, and convert objects to dictionaries, BaseModel,
   a fundamental model class, offers common functionality.

    id (str): A distinctive identifier for each class instance
        produced automatically using the uuid library.
    created at (datetime): Timestamp indicating the creation time of the object.
    updated at (datetime): Timestamp for the most recent update to the object.
    """
    def _init_(self, *args, **kwargs):
        """
       creates a base model object. The associated characteristics are set
           if keyword arguments are provided.
       The 'id', 'created at', and 'updated at' properties are automatically
       set if no keyword parameters are given.

        Args:
            *args: Variable length argument list. Not used in this method.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '_class_':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def _str_(self):
        """
        Returns a string representation of the object in the following format:
        [<class_name>] (<self.id>) <self._dict_>

        Returns:
            str: String representation of the object.
        """
        return "[{}] ({}) {}".format(type(self)._name, self.id, self.dict_)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary. The dictionary keys are the object
        attributes, and the values are the attribute values. Additionally,
        the 'created_at' and 'updated_at' values are converted to ISO format.

        Returns:
            dict: Dictionary representation of the object.
        """
        obj_dict = self._dict_.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['_class'] = type(self).name_
        return obj_dict
