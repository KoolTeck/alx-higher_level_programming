#!/usr/bin/python3
""" The base module """

import json


class Base:

    """ the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns str rep of a dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            saves list obj in json format to a file

            Args:
                list_objs(list): a list of objs who inherits of base

            Returns:
                   nothing

        """
        obj_lis = []
        json_str = ""
        if list_objs is None:
            json_str = '[]'
        else:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                obj_lis.append(dictionary)

            json_str = Base.to_json_string(obj_lis)

        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON str repr """
        if json_string is None or len(json_string) is 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ is 'Rectangle':
            instance = cls(4, 2)
        elif cls.__name__ is 'Square':
            instance = cls(3, 2)
        cls.update(instance, **dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        inst_list = []
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                json_string = f.read()
        except FileNotFoundError:
            return ([])
        list_output = cls.from_json_string(json_string)
        for dictionary in list_output:
            new_obj = cls.create(**dictionary)
            inst_list.append(new_obj)

        return (inst_list)
