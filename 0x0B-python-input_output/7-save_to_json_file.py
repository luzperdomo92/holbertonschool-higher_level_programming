#!/usr/bin/python3
"""Defining  from_json_string Function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that  that writes an Object
     to a text file, using a JSON representation
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
