#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
    return best_key[0]
