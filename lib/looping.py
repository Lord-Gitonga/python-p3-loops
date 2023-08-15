#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
    pass
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squares = [list **2 for list in int_list ]
    print(squares)
    pass
square_integers([1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5])

def fizzbuzz():
    # code goes here!
    number = 0
    while number <100:
        number +=1
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else: 
            print(number)
    pass
fizzbuzz()
