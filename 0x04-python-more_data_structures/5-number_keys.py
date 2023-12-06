#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for key in range(len(a_dictionary)):
        count += key
    return count
