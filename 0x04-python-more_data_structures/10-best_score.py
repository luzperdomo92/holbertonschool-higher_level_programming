#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key_big = max(a_dictionary, key=a_dictionary.get)
        return key_big
