"""This program is solution for Hacker Rank
Problem of conditionals
"""

n = int(input().strip())
# checking if the input is valid
is_valid = 1 <= n <= 100
if not is_valid:
    exit(1)

# if the n is valid
is_even = n%2 == 0
if not is_even :
    print('Weird')
else:
    if 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print ('Weird')
    else:
        print('Not Weird')
