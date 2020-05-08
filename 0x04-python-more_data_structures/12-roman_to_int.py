#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        value = 0
        roman_numb = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman_string = list(roman_string)
        result = [roman_numb.get(item, item) for item in roman_string]
        for x in range(0, len(result) - 1):
            if result[x] < result[x + 1]:
                value -= result[x]
            else:
                value += result[x]
        value = value + result[-1]
        return value
    else:
        return 0
