#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    first_element = True
    best_key = None

    for key, value in a_dictionary.items():
        if first_element or value > max_value:
            max_value = value
            best_key = key
            first_element = False

    return best_key
