#!/usr/bin/python3


def find_peak(list_of_integers):
    """ function to finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size_of_list = len(list_of_integers)
    if size_of_list == 1:
        return list_of_integers[0]
    elif size_of_list == 2:
        return max(list_of_integers)

    middle = int(size_of_list / 2)
    peck_number = list_of_integers[middle]

    if (peck_number > list_of_integers[middle - 1]
       and peck_number > list_of_integers[middle + 1]):
        return peck_number
    elif peck_number < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
