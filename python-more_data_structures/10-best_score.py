#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary) == 0:
        return None
    else:
        result = (max(a_dictionary, key=a_dictionary.get))
        if result == 0:
            return None
        else:
            return result
