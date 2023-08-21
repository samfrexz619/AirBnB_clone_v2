#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        c_dict = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                part = key.replace('.', ' ')
                part = shlex.split(part)
                if (part[0] == cls.__name__):
                    c_dict[key] = self.__objects[key]
            return (c_dict)
        else:
            return self.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary
        Args:
            obj: object
        """
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dic = {obj: self.__objects[obj].to_dict()
                   for obj in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for obj in json.load(f).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete object from self objects"""
        if obj:
            key = f'{type(obj)}.__name__}.{obj.id}'
            del self.__objects[key]

    def close(self):
        """reload method."""
        self.reload()
