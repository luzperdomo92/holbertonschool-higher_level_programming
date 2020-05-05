#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        new_str = my_string
        new_str = new_str.translate({ord(letter): None for letter in "Cc"})
        return new_str
    new_str = my_string
    return new_str
