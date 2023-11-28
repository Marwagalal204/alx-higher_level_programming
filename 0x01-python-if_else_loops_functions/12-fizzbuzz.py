#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        if (number % 3 == 0):
            print("Fizz")
        elif (number % 5 == 0):
            print("Bizz")
        elif (number % 15 == 0):
            print("FizzBuzz")
        else:
            print(number)
