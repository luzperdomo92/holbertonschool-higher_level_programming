#!/usr/bin/python3
"""Defining  to_json_string Function"""
import json


def to_json_string(my_obj):
    """
    Function that returns
    the JSON representation of an object (string)
    """
    new_data = json.dumps(my_obj)
    return (new_data)
