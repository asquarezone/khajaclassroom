"""
factors.py

This module has the code to find the factors of the number
"""

# This is a comment
number = 1000
start = 2
while start < number:
    if number % start == 0:
        print(start)
    start += 1
