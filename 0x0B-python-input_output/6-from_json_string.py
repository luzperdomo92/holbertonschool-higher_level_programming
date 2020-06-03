#!/usr/bin/python3
"""Defining  from_json_string Function"""
import json


def from_json_string(my_str):
    """
    Function that returns an object
    (Python data structure) represented
    by a JSON string:
    """
    new_data = json.loads(my_str)
    return (new_data)
