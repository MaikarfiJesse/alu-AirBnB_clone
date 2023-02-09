#!/usr/bin/python3
"""
Modules containing filestorage class
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj: BaseModel):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                data = json.load(f)
                for key, value in data.items():
                    obj_class = eval(value["__class__"])
                    obj = obj_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
