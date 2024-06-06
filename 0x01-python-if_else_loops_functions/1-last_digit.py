#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigit = abs(number) % 10
if lastDigit > 5:
    print("Last digit of {} and is greater than 5".format(number))
elif lastDigit > 0:
    print("Last digit of {} and is 0".format(number))
elif (lastDigit < 6) and lastDigit > 0:
    print("Last digit of {} and is less than 6 and not 0".format(number))
