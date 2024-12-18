factors = []

number = 1000
start = 2
while start < number:
    if number % start == 0:
        factors.append(start)
    start += 1

print(factors)