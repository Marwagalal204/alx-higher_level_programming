#!/usr/bin/python3
def no_c(my_string):
    translation = str.maketrans('', '', 'cC')
    new_string = my_string.translate(translation)
    return new_string
