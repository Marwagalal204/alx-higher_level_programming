#!/usr/bin/python3
"""divide a function by ?:. parameter"""


def text_indentation(text):
    """a funtion to divide a given a string using ?.: delimeter"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    res = ""
    for char in text:
        res += char
        if char == "." or char == "?" or char == ":":
            res += "\n\n"
    for i in res.split('\n'):
        print(i.strip())
