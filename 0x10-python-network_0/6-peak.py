#!/usr/bin/python3


def find_peak(list_of_integers):
    """ function to finds a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    if size < 1:
        return None
    elif size == 1 or (size == 2 and
                       list_of_integers[0] >= list_of_integers[0]):
        return list_of_integers[0]
    elif list_of_integers[size - 1] >= list_of_integers[size - 2] :
        return list_of_integers[size - 1]

    for i in range(1, size - 1):
        if (list_of_integers[i]>= list_of_integers[i - 1] and
            list_of_integers[i]>= list_of_integers[i + 1]):
            return list_of_integers[i]
