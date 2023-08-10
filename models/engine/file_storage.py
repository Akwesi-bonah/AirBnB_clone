#!/usr/bin/python3
"""class file storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns object """
        return self.__objects

    def new(self, obj):
        """set object with key <obj_class_name> and id"""
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path)
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

