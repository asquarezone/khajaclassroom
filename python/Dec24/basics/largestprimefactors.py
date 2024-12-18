"""_summary_
"""
NUMBER = 13195
for factor in range(NUMBER-1,1,-1):
    # from 13194 to 2 find factors
    if NUMBER % factor == 0:
        # check if this factor is prime or not
        is_prime = True
        for index in range(2,factor):
            if factor % index == 0:
                is_prime = False
                break
        # if it is prime print and exit
        if is_prime:
            print(factor)
            break