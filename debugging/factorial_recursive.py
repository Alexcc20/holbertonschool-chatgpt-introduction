#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer.

    Parameters:
    - n: An integer for which the factorial needs to be calculated.

    Returns:
    - The factorial of the input integer 'n'.
      If 'n' is negative, returns a string indicating that factorial is not defined for negative numbers.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer argument.")
