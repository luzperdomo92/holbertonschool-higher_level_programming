#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    methot to check if the object 
    is an instance of a class that 
    inherited (directly or indirectly) 
    from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
