#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_pos = number % 10
last_digit_neg = number % -10

if number > 0:

    if last_digit_pos > 5:
        print(f'Last digit of {number} is {last_digit_pos}'
              ' and is greater than 5')
    elif last_digit_pos == 0:
        print(f"Last digit of {number} is {last_digit_pos} and is 0")
    else:
        print(f'Last digit of {number} is {last_digit_pos}'
              ' and is less than 6 and not 0')
else:
    if last_digit_neg == 0:
        print(f"Last digit of {number} is {last_digit_neg} and is 0")
    else:
        print(f'Last digit of {number} is {last_digit_neg}'
              ' and is less than 6 and not 0')
