#!/usr/bin/python3
def no_c(my_string):
    result_str = ""
    for x in range(len(my_string)):
        if my_string[x] != 'c' and my_string[x] != 'C':
            result_str += my_string[x]
    return (result_str)
