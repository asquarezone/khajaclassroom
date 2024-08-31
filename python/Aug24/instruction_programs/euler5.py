"""This program tries to solve project euler problem 5
"""

import math
largest_number = int(input("Enter the largest number: "))
maxiumum = math.factorial(largest_number)
count = 0
# Iterating from largest number 5 to 120 (in the case of 5)
# i.e. iterating from n to n! and incrementing by n
for number in range(largest_number,maxiumum+1,largest_number):
    count += 1
    is_divisible_by_all = True
    for index in range(1,largest_number+1):
        if number % index != 0:
            is_divisible_by_all = False
            break
    if is_divisible_by_all :
        print(f"Smallest number divisible by all numbers {number}")
        break

print(f"Iterations: {count}")
