#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first_char = None
        return first_char
    else:
        first_char = sentence[0]
        return (length, first_char)
