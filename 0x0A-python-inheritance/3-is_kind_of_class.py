#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        False
