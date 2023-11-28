#!/usr/bin/python3
def uppercase(str):
    capital = ""
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            capital += chr(ord(letter) - 32)
        else:
            capital += letter
    print(capital)
