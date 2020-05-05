#!/usr/bin/env python3
#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = my_string.translate({ord(x): None for x in 'cC'})
    return (my_string)
