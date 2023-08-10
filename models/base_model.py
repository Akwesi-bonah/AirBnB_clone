#!/usr/bin/env python3
""" class BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel that defines all common
     attributes/methods for other classes
     """

    def __init__(self, *args, **kwargs):
        """

        :Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            t = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], t)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the class"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/
        values of __dict__ of the instance:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

