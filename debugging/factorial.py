#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

# Try to convert the argument to an integer and calculate the factorial
try:
    number = int(sys.argv[1])
    if number < 0:
        print("Please provide a non-negative integer.")
        sys.exit(1)
    f = factorial(number)
    print(f)
except ValueError:
    print("Please provide a valid integer argument.")
