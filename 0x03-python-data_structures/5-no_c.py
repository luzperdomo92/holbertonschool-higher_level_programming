#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        my_string = my_string.translate({ord(i): None for i in "Cc"})
        return my_string
