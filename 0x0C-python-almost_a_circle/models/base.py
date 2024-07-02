#!/usr/bin/python3
"""
This module for Base class,
This class will be the base of all other classes.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs).
"""
import json


class Base:
    """This a Base calss"""
    __nb_objects = 0

    def __init__(self, id=None):
        '''This the initializion method with id attribute'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is None or len(list_objs) == 0:
            with open(f'{cls.__name__}.json', 'w') as jsnFile:
                json.dump([], jsnFile)
        else:
            # list_dicts = []
            # for lst in list_objs:
            #     list_dicts.append(lst.to_dictionary())
            list_dicts = [lst.to_dictionary() for lst in list_objs]
            jsnStr = cls.to_json_string(list_dicts)
            with open(f'{cls.__name__}.json', 'w') as jsnFile:
                jsnFile.write(jsnStr)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        # Dummy instance that we will update it at next step
        dummy = cls(2, 3)
        dummy.update(**dictionary)
        # **dictionary must be used as **kwargs of the method update
        return dummy
