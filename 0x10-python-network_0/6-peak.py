#!/usr/bin/python3


def find_peak(list_of_integers):
    """ function to finds a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    if size < 3:
        return None
    
    for i in range(1, size - 1):
        if (list_of_integers[i]>= list_of_integers[i - 1] and
            list_of_integers[i]>= list_of_integers[i + 1]):
            return list_of_integers[i]
