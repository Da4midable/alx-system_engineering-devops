#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        f = (num % 3 == 0)
        b = (num % 5 == 0)
        fb = (num % 15 == 0)
        if f and (not b) and (not fb):
            print("Fizz", end=" ")
        elif b and (not f) and (not fb):
            print("Buzz", end=" ")
        elif fb:
            print("FizzBuzz", end=" ")
        else:
            print(num, end=" ")
