#!/usr/bin/python3
def lookup(obj):
    """ 
    methot that returns the 
    list of available attributes 
    and methods of an object:
    """
    return(list(dir(obj)))
