#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit:
    print(f"The last digit of {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"The last digit of {number:d} is {digit:d} and is zero")
else:
    print(f"The last digit of {number:d} is {digit:d} and is less than 6 and not 0")
