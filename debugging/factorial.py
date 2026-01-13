#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <non-negative integer>")
    sys.exit(1)

print(factorial(int(sys.argv[1])))
