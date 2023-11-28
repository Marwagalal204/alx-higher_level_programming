#!/usr/bin/python3
def print_last_digit(number):
    last_digit_pos = number % 10
    last_digit_neg = number % -10

    if number > 0:
        print(last_digit_pos, end="")
        return last_digit_pos
    elif number == 0:
        print(0, end="")
    else:
        last_digit_neg = -(last_digit_neg)
        print(last_digit_neg, end="")
        return last_digit_neg
