#!/usr/bin/python3
"""Creating a new class"""
import json
import os.path


class Base:
    """ New Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor to define value to ID"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that  returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        new_data = json.dumps(list_dictionaries)
        return (new_data)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method  that writes the JSON
        string representation of list_objs to a file
        """
        file_name = cls.__name__ + '.json'

        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(file_name, "w", encoding='utf8') as fl:
            new_json = Base.to_json_string(new_list)
            fl.write(new_json)

    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns the list
        of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        new_data = json.loads(json_string)
        return (new_data)

    @classmethod
    def create(cls, **dictionary):
        """
        Method that returns an instance with
        all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        else:
            dummy = cls()
        return dummy

    @classmethod
    def load_from_file(cls):
        """ method that returns a list of instances"""
        file_name = cls.__name__ + '.json'
        new_list = []
        if not os.path.exists(file_name):
            return new_list

        with open(file_name, "r", encoding="utf8") as fl:
            json_string = fl.read()
            obj_in_list = Base.from_json_string(json_string)
            for obj_in_dict in obj_in_list:
                new_list.append(cls.create(**obj_in_dict))
        return (new_list)
