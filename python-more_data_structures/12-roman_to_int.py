#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_values = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
    total = 0

    for i in range(len(roman_string) - 1):
        actuel = roman_values[roman_string[i]]
        suivant = roman_values[roman_string[i+1]]
        if actuel < suivant:
            total -= actuel
        else:
            total += actuel

    total += roman_values[roman_string[-1]]

    return total
