#!/usr/bin/python3
"""
FizzBuzz implementation
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function that prints numbers from 1 to n
    - For multiples of 3: print "Fizz"
    - For multiples of 5: print "Buzz"  
    - For multiples of 15: print "FizzBuzz"
    - For all other numbers: print the number
    """
    result = []
    for i in range(1, n + 1):
        # FIXED: Check divisible by 15 first, then 3, then 5
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n <= 0:
            print("Please provide a positive number")
            sys.exit(1)
        
        result = fizzbuzz(n)
        print(" ".join(result))
    except ValueError:
        print("Please provide a valid number")
        sys.exit(1)