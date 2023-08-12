#!/usr/bin/env python3

""" JSON file """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

cls_dic = {'BaseModel': BaseModel,
           'User': User,
           'Place': Place,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Review': Review
           }


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    def __init__(self):

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Return an object dictionary """
        return self.__objects

    def new(self, obj):
        """set object with key <obj_class_name> and id"""

        name = obj.__class__.__name__
        self.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file
         (path: __file_path)
        """""
        odict = self.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    self.new(cls_dic[class_name](**value))
        except FileNotFoundError:
            pass
