#!/usr/bin/env python3
def no_c(my_string):
    string = ""
    for letter in my_string:
        if (letter is not 'c' and letter is not 'C'):
            string = string + letter
    return(string)
