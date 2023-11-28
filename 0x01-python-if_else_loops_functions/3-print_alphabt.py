#!/usr/bin/pyton3
for letter in range(97, 123):
    letter = chr(letter)
    if letter == 'e' or letter == 'q':
        continue
    else:
        print(letter, end="")
