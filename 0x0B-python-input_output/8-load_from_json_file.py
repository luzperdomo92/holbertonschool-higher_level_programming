#!/usr/bin/python3
"""Defining  load_from_json_file Function"""
import json


def load_from_json_file(filename):
    """
    Function function that creates
    an Object from a “JSON file”
    """
    with open(filename) as fl:
        new_obj = json.load(fl)
        return (new_obj)
